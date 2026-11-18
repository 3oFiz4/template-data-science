"""One-command Kaggle data fetcher: reads slug from config.py and credentials from .env."""

from project_name.config import KAGGLE_DATASET_SLUG, RAW_DATA_DIR
from project_name.loaders import download_kaggle_dataset


def main() -> None:
    dest = download_kaggle_dataset(KAGGLE_DATASET_SLUG, RAW_DATA_DIR)
    print(f"Downloaded and verified '{KAGGLE_DATASET_SLUG}' into {dest}")


if __name__ == "__main__":
    main()
