import argparse
import json
from pathlib import Path

from app.core.config import load_settings
from app.pipeline import process_batch, process_contract


def main():
    parser = argparse.ArgumentParser(
        description="Extract fields from a TXT contract or folder of TXT contracts."
    )
    parser.add_argument("contract", type=Path, help="Path to a TXT file or folder")
    args = parser.parse_args()

    if not args.contract.exists():
        parser.error("The contract path does not exist.")
    if not args.contract.is_dir() and args.contract.suffix.lower() != ".txt":
        parser.error("The contract must be a TXT file or folder.")

    settings = load_settings()
    runner = process_batch if args.contract.is_dir() else process_contract
    report, output_path = runner(args.contract, settings)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
