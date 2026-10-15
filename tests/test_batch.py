import json

import pytest

from app import pipeline
from app.core.config import Settings
from app.extraction.schemas import ContractExtraction


def test_batch_continues_and_summarizes(tmp_path, monkeypatch):
    folder = tmp_path / "contracts"
    folder.mkdir()
    for name in ("good.txt", "missing.txt", "bad.txt", "unknown.txt"):
        (folder / name).write_text(name, encoding="utf-8")
    (folder / "ignored.pdf").write_text("ignored", encoding="utf-8")
    reference = tmp_path / "reference.csv"
    reference.write_text(
        "Filename,Parties-Answer,Agreement Date-Answer,Governing Law-Answer\n"
        "good.pdf,Alpha,5/8/14,Nevada\n"
        "missing.pdf,,unrecognized date,\n"
        "bad.pdf,,,\n",
        encoding="utf-8",
    )
    settings = Settings("secret", "test-model", reference, tmp_path / "reports")

    def extract(text, settings):
        if text == "bad.txt":
            raise ValueError("Invalid extraction")
        if text == "missing.txt":
            return ContractExtraction(
                parties=[], agreement_date=None, governing_law=None
            ), dict.fromkeys(
                ("input_tokens", "output_tokens", "thinking_tokens", "total_tokens")
            )
        return ContractExtraction.model_validate(
            {
                "parties": [{"value": "Alpha", "evidence": "Alpha"}],
                "agreement_date": {
                    "basis": "explicit",
                    "value": "2014-05-08",
                    "evidence": "May 8, 2014",
                },
                "governing_law": {"value": "California", "evidence": "California"},
            }
        ), {
            "input_tokens": 100,
            "output_tokens": 20,
            "thinking_tokens": 5,
            "total_tokens": 125,
        }

    monkeypatch.setattr(pipeline, "extract_contract", extract)
    summary, path = pipeline.process_batch(folder, settings)
    assert (summary["total"], summary["succeeded"], summary["failed"]) == (4, 2, 2)
    assert summary["fields"]["parties"]["populated"]["match_rate"] == 1
    assert summary["fields"]["parties"]["missing"]["match_rate"] == 1
    assert summary["fields"]["governing_law"]["populated"]["match_rate"] == 0
    assert summary["fields"]["agreement_date"]["needs_review"] == 1
    assert summary["token_usage"]["total_tokens"] == {
        "recorded_total": 125,
        "unavailable_contracts": 3,
    }
    assert json.loads(path.read_text()) == summary
    assert len(list(settings.output_dir.glob("*.json"))) == 3
    success = next(
        item for item in summary["contracts"] if item["filename"] == "good.txt"
    )
    assert success["evaluation"]["governing_law"]["extracted"] == "California"
    assert success["evaluation"]["governing_law"]["reference"] == "Nevada"
    assert success["review_reasons"]
    assert summary["contracts_with_evidence_issues"] == 1
    assert all(
        "report_path" not in item
        for item in summary["contracts"]
        if item["status"] == "failed"
    )


def test_empty_folder_creates_no_report(tmp_path):
    settings = Settings("secret", "test-model", output_dir=tmp_path / "reports")
    with pytest.raises(ValueError, match="No TXT contracts"):
        pipeline.process_batch(tmp_path, settings)
    assert not settings.output_dir.exists()
