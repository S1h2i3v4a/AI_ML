"""
SmartCredit — Loan Risk Scoring System
Main Streamlit application: Home / Prediction Portal
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import matplotlib.pyplot as plt

# ── Page configuration ──────────────────────────────────────────────────────
st.set_page_config(
    page_title="SmartCredit",
    page_icon="🏦",
    layout="wide",
)

# ── Paths (relative to project root) ────────────────────────────────────────
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best_model.joblib")
FEATURE_COLS_PATH = os.path.join(BASE_DIR, "models", "feature_columns.joblib")


import sys

# ── Helper: build feature DataFrame from raw user inputs ────────────────────
def prepare_input_features(
    age: int,
    gender: str,
    marital_status: str,
    dependents: int,
    education: str,
    employment: str,
    employer: str,
    income: float,
    coapplicant_income: float,
    credit_score: int,
    existing_loans: int,
    savings: float,
    collateral: float,
    loan_amount: float,
    loan_term: int,
    loan_purpose: str,
    property_area: str,
    feature_columns: list,
) -> pd.DataFrame:
    """
    Construct a single-row DataFrame using the exact feature engineering
    pipeline from src/feature_engineering.py.
    """
    total_income = income + coapplicant_income
    dti_est = (loan_amount / max(loan_term, 1)) / max(total_income, 1)

    raw_df = pd.DataFrame([{
        "Applicant_Income": float(income),
        "Coapplicant_Income": float(coapplicant_income),
        "Age": float(age),
        "Dependents": float(dependents),
        "Credit_Score": float(credit_score),
        "Existing_Loans": float(existing_loans),
        "DTI_Ratio": float(min(dti_est, 1.0)),
        "Savings": float(savings),
        "Collateral_Value": float(collateral),
        "Loan_Amount": float(loan_amount),
        "Loan_Term": float(loan_term),
        "Employment_Status": employment,
        "Marital_Status": marital_status,
        "Loan_Purpose": loan_purpose,
        "Property_Area": property_area,
        "Education_Level": education,
        "Gender": gender,
        "Employer_Category": employer,
    }])

    # Import feature engineering module
    src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
    if src_path not in sys.path:
        sys.path.insert(0, src_path)
    from feature_engineering import engineer_all_features

    df_feat = engineer_all_features(raw_df)

    # Ensure all training feature columns exist
    for col in feature_columns:
        if col not in df_feat.columns:
            df_feat[col] = 0

    return df_feat[feature_columns]


# ── Sidebar: Applicant Details ──────────────────────────────────────────────
with st.sidebar:
    st.header("📋 Applicant Details")

    st.subheader("Personal Information")
    age = st.slider("Age", 18, 70, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    marital_status = st.selectbox("Marital Status", ["Single", "Married"])
    dependents = st.slider("Dependents", 0, 5, 0)
    education = st.selectbox("Education Level", ["Graduate", "Not Graduate"])

    st.subheader("Employment & Income")
    employment = st.selectbox("Employment Status", ["Salaried", "Self-employed", "Contract", "Unemployed"])
    employer = st.selectbox("Employer Category", ["Private", "Government", "MNC", "Business", "Unemployed"])
    income = st.number_input("Applicant Income (₹)", min_value=1000, max_value=200000, value=25000)
    coapplicant_income = st.number_input("Co-applicant Income (₹)", min_value=0, max_value=100000, value=0)

    st.subheader("Credit & Assets")
    credit_score = st.slider("Credit Score", 300, 900, 650)
    existing_loans = st.slider("Existing Loans", 0, 10, 1)
    savings = st.number_input("Savings (₹)", min_value=0, value=10000)
    collateral = st.number_input("Collateral Value (₹)", min_value=0, value=50000)

    st.subheader("Loan Details")
    loan_amount = st.number_input("Loan Amount (₹)", min_value=10000, max_value=500000, value=100000)
    loan_term = st.selectbox("Loan Term (months)", [12, 24, 36, 48, 60, 72, 84, 120, 180, 240, 360])
    loan_purpose = st.selectbox("Loan Purpose", ["Personal", "Car", "Business", "Home", "Education"])
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

    st.divider()
    predict_btn = st.button("🚀 Predict Risk", width="stretch", type="primary")


# ── Main area ───────────────────────────────────────────────────────────────
st.title("🏦 SmartCredit — Loan Risk Scoring System")

if predict_btn:
    # --- Check that model artefacts exist ---------------------------------
    if not os.path.exists(MODEL_PATH) or not os.path.exists(FEATURE_COLS_PATH):
        st.warning(
            "⚠️ **Model not found!**  \n"
            "Please run the training pipeline first:  \n"
            "```bash\n"
            "python SmartCredit/src/train.py\n"
            "```"
        )
        st.stop()

    # --- Load model & feature columns -------------------------------------
    model = joblib.load(MODEL_PATH)
    feature_columns = joblib.load(FEATURE_COLS_PATH)

    # --- Prepare input features -------------------------------------------
    X_input = prepare_input_features(
        age=age,
        gender=gender,
        marital_status=marital_status,
        dependents=dependents,
        education=education,
        employment=employment,
        employer=employer,
        income=income,
        coapplicant_income=coapplicant_income,
        credit_score=credit_score,
        existing_loans=existing_loans,
        savings=savings,
        collateral=collateral,
        loan_amount=loan_amount,
        loan_term=loan_term,
        loan_purpose=loan_purpose,
        property_area=property_area,
        feature_columns=feature_columns,
    )

    # --- Prediction -------------------------------------------------------
    prediction = model.predict(X_input)[0]
    proba = model.predict_proba(X_input)[0]
    default_prob = proba[0]  # probability of "No" (not approved / default)
    approval_prob = proba[1]  # probability of "Yes" (approved)

    # Use default_prob for risk assessment
    risk_prob = default_prob

    # Risk tier
    if risk_prob < 0.3:
        risk_tier = "🟢 Low Risk"
        tier_color = "green"
        income_factor = 5
    elif risk_prob < 0.6:
        risk_tier = "🟡 Medium Risk"
        tier_color = "orange"
        income_factor = 3
    else:
        risk_tier = "🔴 High Risk"
        tier_color = "red"
        income_factor = 1.5

    total_income = income + coapplicant_income
    recommended_loan = int(total_income * income_factor)

    # --- Display results --------------------------------------------------
    st.subheader("📊 Prediction Results")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Risk Tier", risk_tier)
    with col2:
        st.metric("Default Probability", f"{risk_prob * 100:.1f}%")
    with col3:
        st.metric("Recommended Max Loan", f"₹{recommended_loan:,}")

    # Risk gauge (progress bar)
    st.subheader("Risk Gauge")
    st.progress(min(risk_prob, 1.0))

    if risk_prob < 0.3:
        st.success(f"✅ **Low Risk** — Default probability is {risk_prob*100:.1f}%. This applicant looks creditworthy.")
    elif risk_prob < 0.6:
        st.warning(f"⚠️ **Medium Risk** — Default probability is {risk_prob*100:.1f}%. Manual review recommended.")
    else:
        st.error(f"🚨 **High Risk** — Default probability is {risk_prob*100:.1f}%. Loan approval not recommended.")

    # Decision
    st.divider()
    decision = "✅ **APPROVED**" if prediction == 1 else "❌ **REJECTED**"
    st.subheader(f"Model Decision: {decision}")

    # Feature importance (if Random Forest)
    model_name = type(model).__name__
    if hasattr(model, "feature_importances_"):
        st.subheader(f"📈 Feature Importance ({model_name})")
        importances = model.feature_importances_
        feat_imp = pd.Series(importances, index=feature_columns).sort_values(ascending=True).tail(15)

        fig, ax = plt.subplots(figsize=(8, 5))
        feat_imp.plot(kind="barh", ax=ax, color="#4c72b0")
        ax.set_xlabel("Importance")
        ax.set_title("Top 15 Feature Importances")
        plt.tight_layout()
        st.pyplot(fig)

    # Show input summary
    with st.expander("📝 View Input Summary"):
        st.dataframe(X_input.T.rename(columns={0: "Value"}), width="stretch")

else:
    # ── Welcome / landing page ───────────────────────────────────────────
    st.markdown(
        """
        Welcome to **SmartCredit**, an intelligent loan risk scoring system powered
        by machine learning.

        ### 🔍 How it works
        1. **Fill in** the applicant details in the sidebar
        2. **Click** the **🚀 Predict Risk** button
        3. **Review** the risk assessment, default probability, and recommended
           loan amount

        ### 🧠 Under the hood
        - Multiple ML models (Logistic Regression, Random Forest, Gradient Boosting,
          SVM) are trained and compared
        - The best model is selected automatically during training
        - Feature engineering creates derived risk indicators for better accuracy

        ### 📂 Project Pages
        | Page | Description |
        |------|-------------|
        | **📊 EDA** | Explore the training data with interactive charts |
        | **🤖 Model Comparison** | Compare model performance metrics side-by-side |

        ---
        > **First time?** Run `python SmartCredit/src/train.py` to train the
        > models before using the prediction portal.
        """
    )
