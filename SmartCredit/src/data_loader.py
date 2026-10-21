"""
data_loader.py — Data loading and summary utilities for SmartCredit.

Provides functions to load the raw loan dataset from CSV and generate
descriptive summaries (shape, dtypes, missing values, numeric statistics).
"""

import pandas as pd


def load_raw_data(filepath: str) -> pd.DataFrame:
    """
    Load raw loan data from a CSV file.

    Parameters
    ----------
    filepath : str
        Absolute or relative path to the CSV file.

    Returns
    -------
    pd.DataFrame
        The loaded DataFrame.
    """
    df = pd.read_csv(filepath)

    # Quick overview printed to console
    print(f"Dataset loaded: {filepath}")
    print(f"  Shape : {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"  Memory: {df.memory_usage(deep=True).sum() / 1024:.1f} KB")
    print()
    print("Column types:")
    print(df.dtypes.value_counts().to_string())
    print()
    print("Missing values per column:")
    missing = df.isnull().sum()
    print(missing[missing > 0].to_string() if missing.any() else "  None")

    return df


def get_data_summary(df: pd.DataFrame) -> dict:
    """
    Generate a comprehensive summary dictionary for a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.

    Returns
    -------
    dict
        Dictionary with keys:
        - 'shape'         : (rows, cols) tuple
        - 'dtypes'        : Series of column dtypes
        - 'missing_counts': Series of missing-value counts per column
        - 'numeric_stats' : DataFrame from df.describe() for numeric columns
    """
    summary = {
        "shape": df.shape,
        "dtypes": df.dtypes,
        "missing_counts": df.isnull().sum(),
        "numeric_stats": df.describe(),
    }
    return summary
