"""
preprocessing.py — Data cleaning and preprocessing for SmartCredit.

Handles missing values, outlier removal, target encoding, and provides a
single-call pipeline that orchestrates the full preprocessing workflow.
"""

import numpy as np
import pandas as pd

try:
    from .data_loader import load_raw_data
except (ImportError, ValueError):
    from data_loader import load_raw_data


# ---------------------------------------------------------------------------
# Missing-value handling
# ---------------------------------------------------------------------------

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values in the dataset.

    Strategy
    --------
    1. Drop rows where target `Loan_Approved` is NaN (cannot train on unlabeled data).
    2. For remaining missing values:
       - Numeric columns  → fill with column **median**.
       - Categorical columns → fill with column **mode**.
    """
    df = df.copy()

    # Step 1: Drop rows where target is missing
    if "Loan_Approved" in df.columns:
        rows_before = len(df)
        df = df.dropna(subset=["Loan_Approved"])
        print(f"Dropped {rows_before - len(df)} rows with missing target 'Loan_Approved'.")

    # Step 2: impute remaining missing values
    numeric_cols = df.select_dtypes(include="number").columns
    categorical_cols = df.select_dtypes(exclude="number").columns

    for col in numeric_cols:
        if df[col].isnull().any():
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
            print(f"  Filled '{col}' NaNs with median ({median_val:.2f})")

    for col in categorical_cols:
        if df[col].isnull().any():
            mode_val = df[col].mode()[0]
            df[col] = df[col].fillna(mode_val)
            print(f"  Filled '{col}' NaNs with mode ('{mode_val}')")

    print(f"Remaining missing values: {df.isnull().sum().sum()}")
    return df


# ---------------------------------------------------------------------------
# Outlier removal
# ---------------------------------------------------------------------------

def remove_outliers(df: pd.DataFrame, columns: list, method: str = "iqr") -> pd.DataFrame:
    """
    Remove outliers from specified numeric columns using the IQR method.

    A data point is considered an outlier if it falls below Q1 − 1.5·IQR
    or above Q3 + 1.5·IQR.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    columns : list
        List of numeric column names to check for outliers.
    method : str, optional
        Outlier detection method (currently only 'iqr' is supported).

    Returns
    -------
    pd.DataFrame
        DataFrame with outlier rows removed.
    """
    if method != "iqr":
        raise ValueError(f"Unsupported outlier method: '{method}'. Use 'iqr'.")

    df = df.copy()
    rows_before = len(df)

    for col in columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        df = df[(df[col] >= lower) & (df[col] <= upper)]

    rows_removed = rows_before - len(df)
    print(f"Outlier removal ({method.upper()}): removed {rows_removed} rows "
          f"across columns {columns}.")
    return df


# ---------------------------------------------------------------------------
# Target encoding
# ---------------------------------------------------------------------------

def encode_target(df: pd.DataFrame, col: str = "Loan_Approved") -> pd.DataFrame:
    """
    Encode the binary target column (Yes / No) → (1 / 0).
    """
    df = df.copy()
    if col in df.columns:
        df[col] = df[col].map({"Yes": 1, "No": 0, 1: 1, 0: 0}).astype(int)
        print(f"Target '{col}' encoded: Yes→1, No→0")
        print(f"  Class distribution:\n{df[col].value_counts().to_string()}")
    return df


# ---------------------------------------------------------------------------
# Full preprocessing pipeline
# ---------------------------------------------------------------------------

def preprocess_pipeline(filepath: str) -> pd.DataFrame:
    """
    End-to-end preprocessing pipeline.

    Steps
    -----
    1. Load raw CSV data.
    2. Handle missing values (drop all-NaN rows, impute rest).
    3. Remove outliers from key numeric columns via IQR.
    4. Encode the target variable.

    Parameters
    ----------
    filepath : str
        Path to the raw CSV file.

    Returns
    -------
    pd.DataFrame
        Cleaned and preprocessed DataFrame ready for feature engineering.
    """
    print("=" * 60)
    print("PREPROCESSING PIPELINE")
    print("=" * 60)

    # 1. Load
    print("\n[1/4] Loading data...")
    df = load_raw_data(filepath)

    # 2. Missing values
    print("\n[2/4] Handling missing values...")
    df = handle_missing_values(df)

    # 3. Outlier removal on key numeric columns
    print("\n[3/4] Removing outliers (IQR)...")
    numeric_outlier_cols = [
        "Applicant_Income",
        "Coapplicant_Income",
        "Loan_Amount",
        "DTI_Ratio",
    ]
    # Only use columns that actually exist in the DataFrame
    numeric_outlier_cols = [c for c in numeric_outlier_cols if c in df.columns]
    df = remove_outliers(df, columns=numeric_outlier_cols)

    # 4. Encode target
    print("\n[4/4] Encoding target variable...")
    df = encode_target(df)

    print("\n" + "=" * 60)
    print(f"Preprocessing complete. Final shape: {df.shape}")
    print("=" * 60)
    return df
