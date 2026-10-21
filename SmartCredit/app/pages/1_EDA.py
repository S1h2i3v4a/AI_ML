"""
SmartCredit — Exploratory Data Analysis Dashboard
Streamlit page: interactive EDA on the raw loan dataset.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="SmartCredit · EDA", page_icon="📊", layout="wide")
st.title("📊 Exploratory Data Analysis")

# ── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "loan_data.csv")

# ── Plotting style ───────────────────────────────────────────────────────────
plt.style.use("seaborn-v0_8-whitegrid")


# ── Data loading (cached) ───────────────────────────────────────────────────
@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    """Load the raw loan dataset."""
    return pd.read_csv(path)


if not os.path.exists(DATA_PATH):
    st.error(
        f"Dataset not found at `{DATA_PATH}`.  \n"
        "Please make sure `loan_data.csv` is placed in `data/raw/`."
    )
    st.stop()

df = load_data(DATA_PATH)

# ── Tabs ─────────────────────────────────────────────────────────────────────
tab_overview, tab_dist, tab_corr, tab_cat = st.tabs(
    ["Overview", "Distributions", "Correlations", "Categorical Analysis"]
)

# ─────────────────────────────────────────────────────────────────────────────
# TAB 1 — Overview
# ─────────────────────────────────────────────────────────────────────────────
with tab_overview:
    st.subheader("Dataset Shape")
    col1, col2 = st.columns(2)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])

    st.subheader("Column Data Types")
    dtype_df = pd.DataFrame({"Column": df.columns, "Type": df.dtypes.astype(str).values})
    st.dataframe(dtype_df, width="stretch", hide_index=True)

    st.subheader("Missing Values")
    missing = df.isnull().sum()
    missing = missing[missing > 0].sort_values(ascending=False)
    if len(missing) > 0:
        fig, ax = plt.subplots(figsize=(10, 4))
        missing.plot(kind="bar", ax=ax, color="#e07b54")
        ax.set_ylabel("Count of Missing Values")
        ax.set_title("Missing Values per Column")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.success("No missing values in the dataset! 🎉")

    st.subheader("First 10 Rows")
    st.dataframe(df.head(10), width="stretch", hide_index=True)

# ─────────────────────────────────────────────────────────────────────────────
# TAB 2 — Distributions
# ─────────────────────────────────────────────────────────────────────────────
with tab_dist:
    st.subheader("Numeric Feature Distributions")

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # Income distribution (KDE)
    if "Applicant_Income" in df.columns:
        sns.kdeplot(df["Applicant_Income"].dropna(), ax=axes[0, 0], fill=True, color="#4c72b0")
        axes[0, 0].set_title("Applicant Income — KDE")
        axes[0, 0].set_xlabel("Income (₹)")

    # Credit Score histogram
    if "Credit_Score" in df.columns:
        axes[0, 1].hist(df["Credit_Score"].dropna(), bins=30, color="#55a868", edgecolor="white")
        axes[0, 1].set_title("Credit Score — Histogram")
        axes[0, 1].set_xlabel("Credit Score")

    # Loan Amount distribution
    if "Loan_Amount" in df.columns:
        sns.kdeplot(df["Loan_Amount"].dropna(), ax=axes[1, 0], fill=True, color="#c44e52")
        axes[1, 0].set_title("Loan Amount — Distribution")
        axes[1, 0].set_xlabel("Loan Amount (₹)")

    # Age distribution
    if "Age" in df.columns:
        axes[1, 1].hist(df["Age"].dropna(), bins=25, color="#8172b3", edgecolor="white")
        axes[1, 1].set_title("Age — Distribution")
        axes[1, 1].set_xlabel("Age")

    plt.tight_layout()
    st.pyplot(fig)

# ─────────────────────────────────────────────────────────────────────────────
# TAB 3 — Correlations
# ─────────────────────────────────────────────────────────────────────────────
with tab_corr:
    st.subheader("Correlation Heatmap (Numeric Features)")

    numeric_df = df.select_dtypes(include=[np.number])
    if numeric_df.shape[1] > 1:
        corr = numeric_df.corr()
        fig, ax = plt.subplots(figsize=(12, 9))
        sns.heatmap(
            corr,
            annot=True,
            fmt=".2f",
            cmap="coolwarm",
            center=0,
            ax=ax,
            linewidths=0.5,
            square=True,
        )
        ax.set_title("Pearson Correlation Matrix")
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.info("Not enough numeric columns to compute correlations.")

# ─────────────────────────────────────────────────────────────────────────────
# TAB 4 — Categorical Analysis
# ─────────────────────────────────────────────────────────────────────────────
with tab_cat:
    st.subheader("Default Rate by Categorical Features")

    # Encode target for grouping
    target_col = "Loan_Approved"
    if target_col in df.columns:
        df_temp = df.copy()
        df_temp["_approved"] = (df_temp[target_col] == "Yes").astype(int)
        df_temp["_default"] = 1 - df_temp["_approved"]

        cat_features = [
            ("Education_Level", "Default Rate by Education Level"),
            ("Property_Area", "Default Rate by Property Area"),
            ("Employment_Status", "Default Rate by Employment Status"),
        ]

        cols = st.columns(len(cat_features))
        for idx, (col_name, title) in enumerate(cat_features):
            if col_name in df_temp.columns:
                rate = df_temp.groupby(col_name)["_default"].mean().sort_values(ascending=False)
                fig, ax = plt.subplots(figsize=(5, 4))
                rate.plot(kind="bar", ax=ax, color="#dd8452", edgecolor="white")
                ax.set_title(title)
                ax.set_ylabel("Default Rate")
                ax.set_ylim(0, 1)
                plt.xticks(rotation=45, ha="right")
                plt.tight_layout()
                cols[idx].pyplot(fig)
            else:
                cols[idx].warning(f"Column `{col_name}` not found.")
    else:
        st.warning(f"Target column `{target_col}` not found in the dataset.")
