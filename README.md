## Setup

1. Copy `.env.example` to `.env` and fill in your Kaggle credentials:
   ```bash
   cp .env.example .env
   ```
2. Install dependencies from `uv.lock` and enable local pre-commit hooks (auto-strips notebook outputs and runs `ruff` on commit):
   ```bash
   uv sync
   uvx pre-commit install
   ```
3. Fetch and verify the dataset into `data/raw/`:
   ```bash
   uv run python scripts/fetch_data.py
   ```

## File Architecture

```
.
├── .github/
│   ├── ISSUE_TEMPLATE/hypothesis.md   # Template for proposing new hypotheses
│   ├── pull_request_template.md       # PR checklist (takeaway, README update)
│   └── workflows/ci.yml               # Runs gitleaks, >5MB guard, ruff, and nbstripout
├── data/                              # Git-ignored local data
│   ├── raw/                           # Downloaded Kaggle files
│   └── processed/                     # Cleaned/intermediate outputs
├── docs/
│   └── data_dictionary.md             # Column definitions, quirks, and edge cases
├── notebooks/
│   ├── 01-eda/                        # Exploratory data analysis
│   ├── 02-hypotheses/                 # Hypothesis tests (h01-..., h02-...)
│   └── 03-modeling/                   # Occasional prediction experiments
├── reports/
│   ├── figures/                       # Exported charts for slides/docs
│   └── findings/                      # Short markdown takeaways & exported HTML/PDFs
├── scripts/
│   └── fetch_data.py                  # One-command Kaggle downloader & checksum verifier
├── src/project_name/
│   ├── config.py                      # Shared dataset slugs, date cutoffs, & thresholds
│   ├── loaders.py                     # Kaggle download (.env) & shared cleaning helpers
│   └── stats.py                       # Shared hypothesis test helpers
├── .env.example                       # KAGGLE_USERNAME and KAGGLE_KEY placeholders
├── .gitignore                         # Ignores .env, data/, .ipynb_checkpoints/
├── .pre-commit-config.yaml            # Local nbstripout + ruff hooks
├── pyproject.toml                     # Dependencies + ruff & nbstripout settings
└── uv.lock                            # Locked environment for reproducible runs
```

## Creating Notebooks ("One Person, One Notebook")

To prevent Git merge conflicts on `.ipynb` files, scope each notebook to a single owner and topic using:

```
<prefix>-<owner>-<topic>.ipynb
```

Examples in `notebooks/02-hypotheses/`:
- `h01-alex-pricing-impact.ipynb`
- `h02-sam-retention-cohorts.ipynb`

Workflow:
1. Create a new notebook with your name and the next hypothesis number (`h03-<you>-<topic>.ipynb`).
2. To build on a teammate's work, copy their notebook to a new file (`h03-...`) or move shared cleaning/test logic into `src/project_name/`.
3. Keep `notebooks/` clean—commit with `pre-commit` active so outputs are stripped. To share rendered charts with stakeholders, export to `reports/findings/` via `jupyter nbconvert --to html`.

## Hypothesis Status

| ID | Hypothesis | Owner | Notebook | Status | Key Takeaway |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `h01` | *Example: Pricing tier X increases 30-day retention* | `alex` | `notebooks/02-hypotheses/h01-alex-pricing-impact.ipynb` | Planned | — |
