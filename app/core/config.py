import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Settings:
    gemini_api_key: str
    gemini_model: str
    reference_path: Path = PROJECT_ROOT / "data/raw/master_clauses.csv"
    output_dir: Path = PROJECT_ROOT / "data/processed"


def load_settings() -> Settings:
    load_dotenv(PROJECT_ROOT / ".env")
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    model = os.getenv("GEMINI_MODEL", "").strip()
    if not api_key or not model:
        raise ValueError(
            "Set GEMINI_API_KEY and GEMINI_MODEL in .env or the environment."
        )
    return Settings(gemini_api_key=api_key, gemini_model=model)
