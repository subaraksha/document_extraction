import json
from unittest.mock import MagicMock

import pytest
from google.genai import types

import main
from app.core.config import Settings
from app.extraction import gemini_client


@pytest.mark.parametrize("has_usage", [True, False])
def test_pipeline_saves_report(tmp_path, monkeypatch, has_usage):
    contract = tmp_path / "contract.txt"
    contract.write_text("A contract with no extractable fields.", encoding="utf-8")
    reference = tmp_path / "reference.csv"
    reference.write_text(
        "Filename,Parties-Answer,Agreement Date-Answer,Governing Law-Answer\n"
        "contract.pdf,,,\n",
        encoding="utf-8",
    )
    settings = Settings("test-key", "test-model", reference, tmp_path / "reports")
    monkeypatch.setattr(main, "load_settings", lambda: settings)
    monkeypatch.setattr("sys.argv", ["main.py", str(contract)])
    client = MagicMock()
    monkeypatch.setattr(gemini_client.genai, "Client", client)
    client.return_value.__enter__.return_value.models.generate_content.return_value = types.GenerateContentResponse(
        candidates=[
            types.Candidate(
                content=types.Content(
                    parts=[
                        types.Part(
                            text='{"parties": [], "agreement_date": null, "governing_law": null}'
                        )
                    ]
                )
            )
        ],
        usage_metadata=types.GenerateContentResponseUsageMetadata(
            prompt_token_count=100,
            candidates_token_count=20,
            thoughts_token_count=10,
            total_token_count=130,
        )
        if has_usage
        else None,
    )
    main.main()
    main.main()
    reports = list(settings.output_dir.glob("*.json"))
    assert len(reports) == 2
    report = json.loads(reports[0].read_text(encoding="utf-8"))
    assert report["source_filename"] == "contract.txt"
    assert report["model"] == "test-model"
    assert report["processing_seconds"] >= 0
    assert report["token_usage"] == {
        "input_tokens": 100 if has_usage else None,
        "output_tokens": 20 if has_usage else None,
        "thinking_tokens": 10 if has_usage else None,
        "total_tokens": 130 if has_usage else None,
    }
    assert all(field["match"] for field in report["evaluation"].values())
    assert "test-key" not in reports[0].read_text(encoding="utf-8")
