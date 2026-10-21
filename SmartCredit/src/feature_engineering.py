"""
feature_engineering.py — Feature creation and encoding for SmartCredit.

Creates derived features (income ratios, credit tiers, risk flags),
one-hot encodes categoricals, and drops identifiers to produce the
final modelling-ready DataFrame.
"""

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Income features
# ---------------------------------------------------------------------------

def create_income_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create income-related features.

    New columns
    -----------
    - ``total_income``      : Applicant_Income + Coapplicant_Income
    - ``income_loan_ratio`` : total_income / Loan_Amount

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """
    df = df.copy()
    df["total_income"] = df["Applicant_Income"] + df["Coapplicant_Income"]
    df["income_loan_ratio"] = df["total_income"] / df["Loan_Amount"]

    # Guard against division-by-zero / infinities
    df["income_loan_ratio"] = df["income_loan_ratio"].replace([np.inf, -np.inf], np.nan).fillna(0)

    print("Created income features: total_income, income_loan_ratio")
    return df


# ---------------------------------------------------------------------------
# Credit-score tiers
# ---------------------------------------------------------------------------

def create_credit_tiers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Bin Credit_Score into categorical tiers.

    Tiers
    -----
    - Poor      : < 580
    - Fair       : 580 – 669
    - Good       : 670 – 739
    - Excellent  : 740 +

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
        With new ``credit_tier`` column.
    """
    df = df.copy()
    bins = [-np.inf, 580, 670, 740, np.inf]
    labels = ["Poor", "Fair", "Good", "Excellent"]
    df["credit_tier"] = pd.cut(
        df["Credit_Score"], bins=bins, labels=labels, right=False
    )
    print("Created credit_tier feature:", df["credit_tier"].value_counts().to_dict())
    return df


# ---------------------------------------------------------------------------
# Risk flags
# ---------------------------------------------------------------------------

def create_risk_flags(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create binary risk-flag features.

    Flags
    -----
    - ``high_dti``        : 1 if DTI_Ratio > 0.5
    - ``low_savings``     : 1 if Savings < 5 000
    - ``high_loan_ratio`` : 1 if Loan_Amount / total_income > 5

    Parameters
    ----------
    df : pd.DataFrame
        Must contain ``total_income`` (call ``create_income_features`` first).

    Returns
    -------
    pd.DataFrame
    """
    df = df.copy()
    df["high_dti"] = (df["DTI_Ratio"] > 0.5).astype(int)
    df["low_savings"] = (df["Savings"] < 5000).astype(int)

    # Safely compute loan-to-income ratio
    loan_to_income = (df["Loan_Amount"] / df["total_income"]).replace([np.inf, -np.inf], np.nan).fillna(0)
    df["high_loan_ratio"] = (loan_to_income > 5).astype(int)

    print("Created risk flags: high_dti, low_savings, high_loan_ratio")
    return df


# ---------------------------------------------------------------------------
# Categorical encoding
# ---------------------------------------------------------------------------

def encode_categoricals(df: pd.DataFrame) -> pd.DataFrame:
    """
    One-hot encode categorical columns using ``pd.get_dummies`` with
    ``drop_first=True`` to avoid multicollinearity.

    Columns encoded
    ----------------
    Employment_Status, Marital_Status, Loan_Purpose, Property_Area,
    Education_Level, Gender, Employer_Category

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
        With original categorical columns replaced by dummy variables.
    """
    cat_cols = [
        "Employment_Status",
        "Marital_Status",
        "Loan_Purpose",
        "Property_Area",
        "Education_Level",
        "Gender",
        "Employer_Category",
    ]

    # Also encode credit_tier if it exists
    if "credit_tier" in df.columns:
        cat_cols.append("credit_tier")

    # Only encode columns that are present
    cat_cols = [c for c in cat_cols if c in df.columns]

    df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

    # Ensure all dummy columns are integers (0/1)
    bool_cols = df.select_dtypes(include="bool").columns
    df[bool_cols] = df[bool_cols].astype(int)

    print(f"One-hot encoded {len(cat_cols)} categorical columns. "
          f"DataFrame now has {df.shape[1]} columns.")
    return df


# ---------------------------------------------------------------------------
# Master feature-engineering function
# ---------------------------------------------------------------------------

def engineer_all_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Run the full feature-engineering pipeline.

    Steps
    -----
    1. Create income features (total_income, income_loan_ratio).
    2. Create credit-score tiers.
    3. Create binary risk flags.
    4. One-hot encode all categorical columns.
    5. Drop ``Applicant_ID`` (non-informative identifier).

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned / preprocessed DataFrame.

    Returns
    -------
    pd.DataFrame
        Final modelling-ready DataFrame.
    """
    print("=" * 60)
    print("FEATURE ENGINEERING PIPELINE")
    print("=" * 60)

    df = create_income_features(df)
    df = create_credit_tiers(df)
    df = create_risk_flags(df)
    df = encode_categoricals(df)

    # Drop the identifier column
    if "Applicant_ID" in df.columns:
        df.drop(columns=["Applicant_ID"], inplace=True)
        print("Dropped 'Applicant_ID' column.")

    print(f"\nFinal feature-engineered shape: {df.shape}")
    print("=" * 60)
    return df
