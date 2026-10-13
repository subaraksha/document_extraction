import argparse
import json
from datetime import UTC, datetime
from pathlib import Path
from time import perf_counter

from app.core.config import load_settings
from app.evaluation.cuad import evaluate_contract, load_reference
from app.extraction.gemini_client import extract_contract


def main():
    parser = argparse.ArgumentParser(
        description="Extract fields from a contract TXT file."
    )
    parser.add_argument("contract", type=Path, help="Path to the contract TXT file")
    args = parser.parse_args()

    if args.contract.suffix.lower() != ".txt":
        parser.error("The contract must be a TXT file.")

    started_at = datetime.now(UTC)
    start = perf_counter()
    text = args.contract.read_text(encoding="utf-8")
    settings = load_settings()
    reference = load_reference(settings.reference_path, args.contract)
    result, usage = extract_contract(text, settings)
    evaluation = evaluate_contract(result, reference)
    report = {
        "source_filename": args.contract.name,
        "model": settings.gemini_model,
        "started_at": started_at.isoformat(),
        "processing_seconds": round(perf_counter() - start, 3),
        "token_usage": usage,
        "extraction": result.model_dump(mode="json"),
        "evaluation": evaluation,
    }
    settings.output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = started_at.strftime("%Y%m%dT%H%M%S%fZ")
    output_path = settings.output_dir / f"{args.contract.stem}_{timestamp}.json"
    output = json.dumps(report, indent=2, ensure_ascii=False)
    output_path.write_text(output + "\n", encoding="utf-8")
    print(output)
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
