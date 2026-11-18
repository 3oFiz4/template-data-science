"""Data fetching (Kaggle API via .env) and shared cleaning helpers."""

import hashlib
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

from project_name.config import EXPECTED_CHECKSUMS, RAW_DATA_DIR


def verify_checksums(data_dir: Path = RAW_DATA_DIR) -> None:
    """Verify SHA-256 checksums for files listed in EXPECTED_CHECKSUMS."""
    for filename, expected_hash in EXPECTED_CHECKSUMS.items():
        file_path = data_dir / filename
        if not file_path.exists():
            raise FileNotFoundError(f"Expected data file not found: {file_path}")
        actual_hash = hashlib.sha256(file_path.read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            raise ValueError(
                f"Checksum mismatch for {filename}: expected {expected_hash}, got {actual_hash}"
            )


def download_kaggle_dataset(dataset_slug: str, dest_dir: Path = RAW_DATA_DIR) -> Path:
    """Authenticate via .env and download/unzip a Kaggle dataset into dest_dir."""
    load_dotenv()
    from kaggle.api.kaggle_api_extended import KaggleApi

    dest_dir.mkdir(parents=True, exist_ok=True)
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset_slug, path=str(dest_dir), unzip=True)
    verify_checksums(dest_dir)
    return dest_dir


def load_csv(filename: str, data_dir: Path = RAW_DATA_DIR) -> pd.DataFrame:
    """Load a CSV from data_dir with basic whitespace/column normalization."""
    df = pd.read_csv(data_dir / filename)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df
