from pathlib import Path

import pytest

from app.evaluation.cuad import (
    evaluate_contract,
    load_reference,
    normalize_law,
    reference_date,
    reference_parties,
)
from app.extraction.schemas import ContractExtraction


def test_normalized_matches():
    extraction = ContractExtraction.model_validate(
        {
            "parties": [
                {"value": "Beta Inc.", "evidence": "Beta Inc."},
                {"value": "ALPHA CORP.", "evidence": "ALPHA CORP."},
            ],
            "agreement_date": {
                "basis": "explicit",
                "value": "2014-05-08",
                "evidence": "May 8, 2014",
            },
            "governing_law": {"value": " State of NEW YORK ", "evidence": "New York"},
        }
    )
    reference = {
        "Parties-Answer": 'Alpha Corp. ("Company"); Beta Inc. ("Affiliate", "MA")',
        "Agreement Date-Answer": "5/8/14",
        "Governing Law-Answer": "New York",
    }
    result = evaluate_contract(extraction, reference)
    assert all(field["match"] for field in result.values())


def test_missing_values_and_invalid_reference_date():
    extraction = ContractExtraction(parties=[], agreement_date=None, governing_law=None)
    reference = {
        "Parties-Answer": "",
        "Agreement Date-Answer": "",
        "Governing Law-Answer": "",
    }
    assert all(
        field["match"] for field in evaluate_contract(extraction, reference).values()
    )
    reference["Agreement Date-Answer"] = "unrecognized date"
    assert evaluate_contract(extraction, reference)["agreement_date"]["match"] is None
    reference["Governing Law-Answer"] = "Nevada"
    assert evaluate_contract(extraction, reference)["governing_law"]["match"] is False


def test_reference_lookup(tmp_path):
    path = tmp_path / "reference.csv"
    path.write_text("Filename,Parties-Answer\ncontract.pdf,Alpha\n", encoding="utf-8")
    assert load_reference(path, Path("contract.txt"))["Parties-Answer"] == "Alpha"
    with pytest.raises(ValueError, match="found 0"):
        load_reference(path, Path("missing.txt"))
    path.write_text("Filename\ncontract.pdf\ncontract.pdf\n", encoding="utf-8")
    with pytest.raises(ValueError, match="found 2"):
        load_reference(path, Path("contract.txt"))


def test_annotation_typo_remains_a_mismatch():
    extraction = ContractExtraction.model_validate(
        {
            "parties": [
                {
                    "value": "Mount Knowledge Holdings Inc.",
                    "evidence": "Mount Knowledge Holdings Inc.",
                }
            ],
            "agreement_date": None,
            "governing_law": None,
        }
    )
    reference = {
        "Parties-Answer": "Mount Kowledge Holdings Inc.",
        "Agreement Date-Answer": "",
        "Governing Law-Answer": "",
    }
    assert evaluate_contract(extraction, reference)["parties"]["match"] is False


@pytest.mark.parametrize("extension", ["pdf", "PDF", "Pdf"])
def test_reference_lookup_normalizes_extension(tmp_path, extension):
    path = tmp_path / "reference.csv"
    path.write_text(
        f"Filename,Parties-Answer\ncontract.{extension},Alpha\n", encoding="utf-8"
    )
    assert load_reference(path, Path("contract.txt"))["Parties-Answer"] == "Alpha"


def test_reference_lookup_rejects_duplicate_extension_variants(tmp_path):
    path = tmp_path / "reference.csv"
    path.write_text("Filename\ncontract.pdf\ncontract.PDF\n", encoding="utf-8")
    with pytest.raises(ValueError, match="found 2"):
        load_reference(path, Path("contract.txt"))


@pytest.mark.parametrize(
    ("name", "annotation"),
    [
        ("Bunker One (USA) Inc.", '("Bunker One")'),
        ("Dialog Semiconductor (UK) Ltd.", "(“DIALOG”)"),
        ("TOM Online (BVI) limited", '("Online BVI")'),
        ("China Online Housing (Hong Kong) Co., Ltd.", '("Party B")'),
    ],
)
def test_party_legal_name_parentheses_are_preserved(name, annotation):
    extraction = ContractExtraction.model_validate(
        {
            "parties": [{"value": name, "evidence": name}],
            "agreement_date": None,
            "governing_law": None,
        }
    )
    reference = {
        "Parties-Answer": f"{name}{annotation}",
        "Agreement Date-Answer": "",
        "Governing Law-Answer": "",
    }
    result = evaluate_contract(extraction, reference)["parties"]
    assert result["reference"] == [name]
    assert result["match"] is True
    extraction.parties[0].value = name.replace(
        name[name.index("(") : name.index(")") + 1], ""
    )
    assert evaluate_contract(extraction, reference)["parties"]["match"] is False


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("the State of Ohio", "ohio"),
        ("Province of British Columbia", "british columbia"),
        ("State of California, USA", "california usa"),
        (
            "State of California and the United States",
            "california and the united states",
        ),
    ],
)
def test_law_normalization_preserves_scope(raw, expected):
    assert normalize_law(raw) == expected


def test_collective_descriptions_and_aliases():
    names, ignored = reference_parties(
        'Alpha Inc. ("A"); Beta (UK) Ltd. "B"; '
        'Alpha and Beta collectively referred to as the "Parties"'
    )
    assert names == ["Alpha Inc.", "Beta (UK) Ltd."]
    assert len(ignored) == 1


def test_collective_alias_does_not_remove_named_party():
    names, ignored = reference_parties(
        'Veoneer US, Inc. (“Veoneer US", and together with Veoneer AB, the “Veoneer Parties”); '
        "Allison Transmission Holdings, Inc. (the “Company”)"
    )
    assert names == ["Veoneer US, Inc.", "Allison Transmission Holdings, Inc."]
    assert ignored == []


def test_legal_suffixes_and_affiliate_scope_are_not_erased():
    extraction = ContractExtraction.model_validate(
        {
            "parties": [
                {"value": "Ingram Micro Inc.", "evidence": "Ingram Micro Inc."}
            ],
            "agreement_date": None,
            "governing_law": None,
        }
    )
    reference = {
        "Parties-Answer": "Ingram Micro",
        "Agreement Date-Answer": "",
        "Governing Law-Answer": "",
    }
    assert evaluate_contract(extraction, reference)["parties"]["match"] is False
    names, _ = reference_parties("Alpha and all its subsidiaries and Affiliates")
    assert names == ["Alpha and all its subsidiaries and Affiliates"]


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("07/31/2000; 07/[]/2000", "2000-07-31"),
        ("2020-01-27", "2020-01-27"),
        ("1/27/20; 01/27/2020", "2020-01-27"),
    ],
)
def test_reference_date_formats(raw, expected):
    assert reference_date(raw) == (expected, None)


@pytest.mark.parametrize("raw", ["[]/[]/2020", "1/1/20; 2/1/20", "not a date"])
def test_ambiguous_reference_dates_require_review(raw):
    value, note = reference_date(raw)
    assert value is None and note
