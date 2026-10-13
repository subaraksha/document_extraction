import csv
import re
from datetime import datetime
from pathlib import Path

from app.extraction.schemas import ContractExtraction


def load_reference(reference_path: Path, contract_path: Path) -> dict[str, str]:
    filename = contract_path.with_suffix(".pdf").name
    with reference_path.open(encoding="utf-8", newline="") as file:
        matches = [
            row
            for row in csv.DictReader(file)
            if Path(row["Filename"]).with_suffix(".pdf").name == filename
        ]
    if len(matches) != 1:
        raise ValueError(
            f"Expected one CUAD reference row for {filename}; found {len(matches)}."
        )
    return matches[0]


def normalize_text(value: str) -> str:
    return " ".join(re.sub(r"[^\w\s]", "", value.casefold()).split())


def normalize_law(value: str | None) -> str:
    return re.sub(r"^state of ", "", normalize_text(value or ""))


def evaluate_contract(
    extraction: ContractExtraction, reference: dict[str, str]
) -> dict:
    expected_parties = [
        re.sub(
            r'\(\s*(?:["“]|formerly known as\b)[^)]*\)',
            "",
            party,
            flags=re.IGNORECASE,
        ).strip()
        for party in reference["Parties-Answer"].split(";")
        if party.strip()
    ]
    actual_parties = [party.value for party in extraction.parties]
    raw_date = reference["Agreement Date-Answer"].strip()
    expected_date = None
    date_note = None
    if raw_date:
        try:
            expected_date = datetime.strptime(raw_date, "%m/%d/%y").date().isoformat()
        except ValueError:
            date_note = "Reference date format needs manual review."
    actual_date = (
        extraction.agreement_date.value.isoformat()
        if extraction.agreement_date
        else None
    )
    expected_law = reference["Governing Law-Answer"].strip() or None
    actual_law = extraction.governing_law.value if extraction.governing_law else None

    return {
        "parties": {
            "extracted": actual_parties,
            "reference": expected_parties,
            "match": {normalize_text(p) for p in actual_parties}
            == {normalize_text(p) for p in expected_parties},
        },
        "agreement_date": {
            "extracted": actual_date,
            "reference": raw_date or None,
            "match": actual_date == expected_date if date_note is None else None,
            "note": date_note,
        },
        "governing_law": {
            "extracted": actual_law,
            "reference": expected_law,
            "match": normalize_law(actual_law) == normalize_law(expected_law),
        },
    }
