import json
from unittest.mock import MagicMock

import pytest
from google.genai import types

import main
from app.core.config import Settings
from app.extraction import gemini_client
from app.extraction.schemas import ContractExtraction


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


def test_separate_evidence_quotes_and_source_check():
    source = "Entered into as of the Effective Date.\nEffective Date means May 8, 2014."
    extraction = ContractExtraction.model_validate(
        {
            "parties": [],
            "agreement_date": {
                "value": "2014-05-08",
                "basis": "defined_date",
                "evidence": [
                    "Entered into as of the Effective Date.",
                    "Effective Date means May 8, 2014.",
                ],
            },
            "governing_law": {"value": "Nevada", "evidence": "Laws of Nevada."},
        }
    )
    checks = extraction.check_evidence(source)
    assert all(c["found_in_source"] for c in checks["agreement_date"])
    assert checks["governing_law"][0]["found_in_source"] is False
    extraction.agreement_date.evidence = "Entered into ... May 8, 2014."
    assert (
        extraction.check_evidence(source)["agreement_date"][0]["found_in_source"]
        is False
    )


@pytest.mark.parametrize("evidence", ["", [], [""]])
def test_empty_evidence_is_invalid(evidence):
    from pydantic import ValidationError

    with pytest.raises(ValidationError):
        ContractExtraction.model_validate(
            {
                "parties": [{"value": "Alpha", "evidence": evidence}],
                "agreement_date": None,
                "governing_law": None,
            }
        )
