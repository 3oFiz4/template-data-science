"""Shared hypothesis testing helpers."""

from dataclasses import dataclass

import pandas as pd
from scipy import stats

from project_name.config import ALPHA


@dataclass(frozen=True)
class TestResult:
    """Structured summary of a two-group hypothesis test."""

    test_name: str
    statistic: float
    p_value: float
    significant: bool
    n_a: int
    n_b: int


def compare_two_groups(
    group_a: pd.Series,
    group_b: pd.Series,
    *,
    parametric: bool = True,
    alpha: float = ALPHA,
) -> TestResult:
    """Run Welch's t-test (parametric) or Mann-Whitney U test (non-parametric)."""
    a = group_a.dropna()
    b = group_b.dropna()

    if parametric:
        stat, p_val = stats.ttest_ind(a, b, equal_var=False)
        test_name = "Welch's t-test"
    else:
        stat, p_val = stats.mannwhitneyu(a, b, alternative="two-sided")
        test_name = "Mann-Whitney U"

    return TestResult(
        test_name=test_name,
        statistic=float(stat),
        p_value=float(p_val),
        significant=bool(p_val < alpha),
        n_a=len(a),
        n_b=len(b),
    )
