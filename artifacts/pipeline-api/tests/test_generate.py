"""Tests for the generate module - specifically API key validation."""
from __future__ import annotations
import os
import pytest
from pathlib import Path
from unittest.mock import patch

from backend.modules import generate as generate_module
from backend.modules.generate import _get_client, run_generate, generate_for_chunk
from backend.schemas import Chunk, GenerationConfig, DatasetRecord, DatasetRecordScores


class TestGetClient:
    """Tests for _get_client() function."""

    def test_raises_error_when_api_key_not_set(self):
        """Should raise ValueError when AI_INTEGRATIONS_OPENAI_API_KEY is not set."""
        env = {"AI_INTEGRATIONS_OPENAI_API_KEY": ""}
        with patch.dict(os.environ, env, clear=True):
            with pytest.raises(ValueError) as exc_info:
                _get_client()
            assert "not set" in str(exc_info.value)
            assert "AI_INTEGRATIONS_OPENAI_API_KEY" in str(exc_info.value)

    def test_raises_error_when_api_key_is_none(self):
        """Should raise ValueError when AI_INTEGRATIONS_OPENAI_API_KEY is None."""
        env = {"AI_INTEGRATIONS_OPENAI_API_KEY": ""}
        with patch.dict(os.environ, env, clear=True):
            with pytest.raises(ValueError) as exc_info:
                _get_client()
            assert "not set" in str(exc_info.value)

    def test_creates_client_when_api_key_is_set(self):
        """Should create OpenAI client when API key is set."""
        env = {"AI_INTEGRATIONS_OPENAI_API_KEY": "test-key-123"}
        with patch.dict(os.environ, env, clear=True):
            client = _get_client()
            assert client is not None
            assert client.api_key == "test-key-123"


class TestRunGenerate:
    """Tests for run_generate() function."""

    def test_returns_empty_when_api_key_not_configured(self, tmp_path: Path):
        """Should return empty list and write empty file when API key not configured."""
        chunks = [
            Chunk(
                chunk_id="chk_123",
                source_id="src_123",
                idx=0,
                text="Test chunk content for testing purposes.",
                tokens=8,
                overlap=10,
                section="",
                hash="abc123",
            )
        ]
        config = GenerationConfig(mode="qa", max_records_per_chunk=1)
        out_dir = tmp_path / "output"
        out_dir.mkdir()

        env = {"AI_INTEGRATIONS_OPENAI_API_KEY": ""}
        with patch.dict(os.environ, env, clear=True):
            records = run_generate(chunks, config, out_dir, max_records=100)

        assert records == []
        
        # Verify empty file was written
        records_file = out_dir / "records.jsonl"
        assert records_file.exists()
        assert records_file.read_text() == ""

    def test_generate_for_chunk_uses_configured_teacher_model(self):
        """Should use configured teacher_model for non-distillation generation."""
        chunk = Chunk(
            chunk_id="chk_model",
            source_id="src_model",
            idx=0,
            text="Transformers are neural networks that use attention.",
            tokens=9,
            overlap=10,
            section="",
            hash="model123",
        )
        config = GenerationConfig(mode="qa", max_records_per_chunk=1, teacher_model="gpt-custom-model")
        existing_hashes: set[str] = set()
        captured_model = None

        def fake_llm_call(client, model, prompt, max_tokens=2048):
            nonlocal captured_model
            captured_model = model
            return '[{"instruction":"What are transformers?","input":"","output":"They are attention-based neural networks."}]'

        with patch.object(generate_module, "_get_client", return_value=object()):
            with patch.object(generate_module, "_llm_call", side_effect=fake_llm_call):
                records = generate_for_chunk(chunk, config, existing_hashes)

        assert captured_model == "gpt-custom-model"
        assert len(records) == 1

    def test_respects_max_records_limit_when_chunk_returns_more(self, tmp_path: Path):
        """Should cap final output to max_records even if a chunk over-produces."""
        chunks = [
            Chunk(
                chunk_id="chk_limit_1",
                source_id="src_limit",
                idx=0,
                text="First chunk text",
                tokens=3,
                overlap=10,
                section="",
                hash="limit1",
            ),
            Chunk(
                chunk_id="chk_limit_2",
                source_id="src_limit",
                idx=1,
                text="Second chunk text",
                tokens=3,
                overlap=10,
                section="",
                hash="limit2",
            ),
        ]
        config = GenerationConfig(mode="qa", max_records_per_chunk=3)
        out_dir = tmp_path / "output_cap"
        out_dir.mkdir()

        generated_per_chunk = [
            DatasetRecord(
                id=f"ds_{i}",
                type="qa",
                instruction=f"inst {i}",
                input="",
                output=f"out {i}",
                provenance={"source_id": "src_limit", "chunk_id": "chk_limit_1"},
                scores=DatasetRecordScores(),
                meta={},
            )
            for i in range(3)
        ]

        with patch.object(generate_module, "_get_client", return_value=object()):
            with patch.object(generate_module, "generate_for_chunk", return_value=generated_per_chunk):
                records = run_generate(chunks, config, out_dir, max_records=4)

        assert len(records) == 4

    def test_processes_chunks_when_api_key_configured(self, tmp_path: Path):
        """Should attempt to process chunks when API key is configured."""
        chunks = [
            Chunk(
                chunk_id="chk_456",
                source_id="src_456",
                idx=0,
                text="Machine learning is a subset of artificial intelligence.",
                tokens=10,
                overlap=10,
                section="",
                hash="def456",
            )
        ]
        config = GenerationConfig(mode="qa", max_records_per_chunk=1)
        out_dir = tmp_path / "output"
        out_dir.mkdir()

        # Use a mock API key but it will fail on actual LLM call
        env = {"AI_INTEGRATIONS_OPENAI_API_KEY": "sk-mock-key"}
        with patch.dict(os.environ, env, clear=True):
            records = run_generate(chunks, config, out_dir, max_records=100)

        # With a mock key, the API call will fail but the function should complete
        assert isinstance(records, list)
        
        records_file = out_dir / "records.jsonl"
        assert records_file.exists()
