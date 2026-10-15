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
    return re.sub(r"^(?:the )?(?:state|province) of ", "", normalize_text(value or ""))


def reference_parties(answer: str) -> tuple[list[str], list[str]]:
    """Remove explicit aliases and collective descriptions, never legal suffixes."""
    names = []
    ignored = []
    for party in answer.split(";"):
        if not party.strip():
            continue
        name = re.sub(
            r'\(\s*(?:(?:the|a|an)\s+)?(?:["“]|formerly known as\b)[^)]*\)',
            "",
            party,
            flags=re.IGNORECASE,
        )
        if re.search(
            r"\b(?:collectively|individually|together|jointly)\b.*\bpart(?:y|ies)\b",
            name,
            re.IGNORECASE,
        ):
            ignored.append(party.strip())
            continue
        name = re.sub(r'["“][^"”]*["”]', "", name).strip()
        if name:
            names.append(name)
    return names, ignored


def reference_date(answer: str) -> tuple[str | None, str | None]:
    if not answer.strip():
        return None, None
    dates = set()
    for part in answer.split(";"):
        part = part.strip()
        # Incomplete template dates are not fabricated into full dates.
        if "[" in part or "_" in part:
            continue
        for fmt in ("%m/%d/%y", "%m/%d/%Y", "%Y-%m-%d"):
            try:
                dates.add(datetime.strptime(part, fmt).date().isoformat())
                break
            except ValueError:
                continue
        else:
            return None, "Unsupported reference date format; manual review required."
    if len(dates) != 1:
        return (
            None,
            "Incomplete or conflicting reference dates; manual review required.",
        )
    return dates.pop(), None


def evaluate_contract(
    extraction: ContractExtraction, reference: dict[str, str]
) -> dict:
    expected_parties, ignored_parties = reference_parties(reference["Parties-Answer"])
    actual_parties = [party.value for party in extraction.parties]
    raw_date = reference["Agreement Date-Answer"].strip()
    expected_date, date_note = reference_date(raw_date)
    actual_date = (
        extraction.agreement_date.value.isoformat()
        if extraction.agreement_date
        else None
    )
    expected_law = reference["Governing Law-Answer"].strip() or None
    actual_law = extraction.governing_law.value if extraction.governing_law else None
    party_match = {normalize_text(p) for p in actual_parties} == {
        normalize_text(p) for p in expected_parties
    }
    party_note = None
    if ignored_parties:
        party_note = "Collective party descriptions excluded; see original reference."
    if not party_match:
        party_note = "Party names or scope differ; review source and reference. No fuzzy matching or legal-suffix removal applied."
    if ignored_parties and not expected_parties:
        party_match = None
        party_note = (
            "Reference contains only collective descriptions; manual review required."
        )
    law_match = normalize_law(actual_law) == normalize_law(expected_law)

    return {
        "parties": {
            "extracted": actual_parties,
            "reference": expected_parties,
            "original_reference": reference["Parties-Answer"],
            "ignored_collective_descriptions": ignored_parties,
            "match": party_match,
            "note": party_note,
        },
        "agreement_date": {
            "extracted": actual_date,
            "reference": raw_date or None,
            "match": actual_date == expected_date if date_note is None else None,
            "note": date_note
            or (
                "Agreement dates differ; review date selection and evidence."
                if actual_date != expected_date
                else None
            ),
        },
        "governing_law": {
            "extracted": actual_law,
            "reference": expected_law,
            "match": law_match,
            "note": None
            if law_match
            else "Jurisdiction wording or scope differs; manual review required. Country and federal-law detail retained.",
        },
    }
