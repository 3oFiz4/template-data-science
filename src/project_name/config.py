"""Shared dataset slugs, paths, date cutoffs, and statistical thresholds."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

KAGGLE_DATASET_SLUG = "owner/dataset-slug"

# Optional SHA-256 checksums for downloaded raw files: {"filename.csv": "hex_digest"}
EXPECTED_CHECKSUMS: dict[str, str] = {}

# Shared analysis cutoffs & thresholds
DATE_CUTOFF_START = "2024-01-01"
ALPHA = 0.05
MIN_SAMPLE_SIZE = 30
