import json
from datetime import UTC, datetime
from pathlib import Path
from time import perf_counter

from app.core.config import Settings
from app.evaluation.cuad import evaluate_contract, load_reference
from app.extraction.gemini_client import extract_contract


def save_report(report: dict, stem: str, settings: Settings) -> Path:
    settings.output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%S%fZ")
    path = settings.output_dir / f"{stem}_{timestamp}.json"
    path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return path


def process_contract(path: Path, settings: Settings) -> tuple[dict, Path]:
    start = perf_counter()
    started_at = datetime.now(UTC).isoformat()
    text = path.read_text(encoding="utf-8")
    reference = load_reference(settings.reference_path, path)
    extraction, usage = extract_contract(text, settings)
    evaluation = evaluate_contract(extraction, reference)
    evidence_checks = extraction.check_evidence(text)
    review_reasons = [
        f"{field}: {result['note'] or 'Reference mismatch.'}"
        for field, result in evaluation.items()
        if result["match"] is not True
    ]
    for field, checks in evidence_checks.items():
        if any(not check["found_in_source"] for check in checks):
            review_reasons.append(
                f"{field}: Evidence quote not found verbatim after whitespace normalization."
            )
    report = {
        "source_filename": path.name,
        "model": settings.gemini_model,
        "started_at": started_at,
        "processing_seconds": round(perf_counter() - start, 3),
        "token_usage": usage,
        "extraction": extraction.model_dump(mode="json"),
        "evaluation": evaluation,
        "evidence_checks": evidence_checks,
        "review_reasons": review_reasons,
    }
    return report, save_report(report, path.stem, settings)


def process_batch(folder: Path, settings: Settings) -> tuple[dict, Path]:
    paths = sorted(
        p for p in folder.iterdir() if p.is_file() and p.suffix.lower() == ".txt"
    )
    if not paths:
        raise ValueError(f"No TXT contracts found in {folder}.")
    start = perf_counter()
    summary = {
        "model": settings.gemini_model,
        "started_at": datetime.now(UTC).isoformat(),
        "total": len(paths),
        "succeeded": 0,
        "failed": 0,
        "contracts_needing_review": 0,
        "contracts_with_evidence_issues": 0,
        "fields": {},
        "token_usage": {},
        "contracts": [],
    }
    for field in ("parties", "agreement_date", "governing_law"):
        summary["fields"][field] = {
            "populated": {"evaluated": 0, "matched": 0},
            "missing": {"evaluated": 0, "matched": 0},
            "needs_review": 0,
        }
    for token in ("input_tokens", "output_tokens", "thinking_tokens", "total_tokens"):
        summary["token_usage"][token] = {
            "recorded_total": 0,
            "unavailable_contracts": 0,
        }
    for path in paths:
        try:
            report, report_path = process_contract(path, settings)
        except Exception as error:  # noqa: BLE001 — isolate failures at the batch boundary
            summary["failed"] += 1
            summary["contracts"].append(
                {
                    "filename": path.name,
                    "status": "failed",
                    "error": f"{type(error).__name__}: {error}",
                }
            )
            for usage in summary["token_usage"].values():
                usage["unavailable_contracts"] += 1
            continue
        summary["succeeded"] += 1
        summary["contracts_needing_review"] += bool(report["review_reasons"])
        summary["contracts_with_evidence_issues"] += any(
            not check["found_in_source"]
            for checks in report["evidence_checks"].values()
            for check in checks
        )
        summary["contracts"].append(
            {
                "filename": path.name,
                "status": "succeeded",
                "report_path": str(report_path),
                "processing_seconds": report["processing_seconds"],
                "extraction": report["extraction"],
                "evaluation": report["evaluation"],
                "evidence_checks": report["evidence_checks"],
                "review_reasons": report["review_reasons"],
            }
        )
        for field, result in report["evaluation"].items():
            counts = summary["fields"][field]
            if result["match"] is None:
                counts["needs_review"] += 1
                continue
            group = counts["populated" if result["reference"] else "missing"]
            group["evaluated"] += 1
            group["matched"] += int(result["match"])
        for token, count in report["token_usage"].items():
            usage = summary["token_usage"][token]
            if count is None:
                usage["unavailable_contracts"] += 1
            else:
                usage["recorded_total"] += count
    for counts in summary["fields"].values():
        for group_name in ("populated", "missing"):
            group = counts[group_name]
            group["match_rate"] = (
                round(group["matched"] / group["evaluated"], 3)
                if group["evaluated"]
                else None
            )
    summary["processing_seconds"] = round(perf_counter() - start, 3)
    return summary, save_report(summary, "batch_summary", settings)
