# Lecture 27.02: Project Architecture, Pipeline Engineering aur Dataset Ingestion

## 📌 Executive Summary (Hinglish)
CreditWise loan system ka complete end-to-end machine learning pipeline architecture, dataset loading, schema audit, aur memory profiling.

---

### 📋 Is Topic/Section Mein Hum Kya Cover Kar Rahe Hain?
1. CreditWise end-to-end ML pipeline ke distinct stages ka architectural blueprint.
2. `loan_approval_data.csv` ka automated ingestion aur schema validation (1,000 rows, 20 features).
3. Continuous numerical features vs discrete categorical attributes ka taxonomy classification.
4. Target column `Loan_Approved` ka class distribution aur baseline imbalance check.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**Pipeline Architecture**: Ingestion -> Imputation -> EDA -> Encoding -> Train/Test Split -> Scaling -> Multi-Model Benchmarking -> Feature Engineering -> Post-Transformation Optimization.

**Data Ingestion**: Dataset mein 1,000 applicants ke 20 attributes hain. Hum Pandas ke `read_csv` se ingest karke dtype inspection aur missingness check execute karte hain.

**Feature Taxonomy**: Numerical attributes (Applicant_Income, Coapplicant_Income, Age, Dependents, Credit_Score, Existing_Loans, DTI_Ratio, Savings, Collateral_Value, Loan_Amount, Loan_Term) aur Categorical attributes (Employment_Status, Marital_Status, Loan_Purpose, Property_Area, Education_Level, Gender, Employer_Category).

**Class Imbalance**: Total 1,000 samples mein se 50 missing target values hain. Cleaned 950 samples mein 68.6% No (Rejected) aur 31.4% Yes (Approved) hain.

---

## 🏛️ Mathematical Architecture & Detailed Theory

### 🏗️ CreditWise Machine Learning Pipeline Architecture

To engineer an enterprise-grade automated underwriting solution, the software and statistical pipeline is decoupled into strictly isolated, reproducible stages:

```mermaid
flowchart LR
    A["Raw Data Ingestion<br/>(loan_approval_data.csv)"] --> B["Data Sanitization<br/>& SimpleImputer"]
    B --> C["Exploratory Data Analysis<br/>(Distributions & Outliers)"]
    C --> D["Feature Encoding<br/>(OHE & LabelEncoder)"]
    D --> E["Leakage-Free Partition<br/>(Train-Test Split 80/20)"]
    E --> F["Feature Standardization<br/>(StandardScaler)"]
    F --> G["Multi-Model Benchmark<br/>(LogReg, KNN, Naive Bayes)"]
    G --> H["Non-Linear Feature Eng.<br/>(Polynomials & Ratios)"]
    H --> I["Decision Threshold Tuning<br/>(Optimal Tau Cutoff)"]
```

---

### 📋 Feature Attribute Dictionary

The dataset `loan_approval_data.csv` contains 20 columns across 1,000 applicant records:

| Column Name | Mathematical Type | Domain Description | Invariant Constraint |
| :--- | :--- | :--- | :--- |
| `Applicant_ID` | Discrete Identifier | Unique database primary key | Dropped during preprocessing |
| `Applicant_Income` | Continuous ($\mathbb{R}^+$) | Primary monthly salary or business income (INR) | Non-negative, positive skew |
| `Coapplicant_Income` | Continuous ($\mathbb{R}^+$) | Co-borrower monthly income (INR) | Can be 0.0 (single applicant) |
| `Employment_Status` | Categorical Nominal | `Salaried`, `Self-Employed`, `Business` | Mutually exclusive |
| `Age` | Discrete ($\mathbb{Z}^+$) | Age in completed years | Typically $[21, 65]$ |
| `Marital_Status` | Categorical Binary | `Married`, `Single` | Binary demographic factor |
| `Dependents` | Discrete ($\mathbb{Z}^+$) | Number of financially dependent family members | $[0, 5+]$ |
| `Credit_Score` | Continuous / Ordinal | CIBIL / Experian bureau credit score | Standard range $[300, 900]$ |
| `Existing_Loans` | Discrete ($\mathbb{Z}^+$) | Count of active ongoing EMI credit facilities | Operational leverage indicator |
| `DTI_Ratio` | Continuous ($\mathbb{R}^+$) | Debt-to-Income ratio ($rac{	ext{Monthly Debt}}{	ext{Monthly Income}}$) | Crucial risk driver $[0.0, 1.0+]$ |
| `Savings` | Continuous ($\mathbb{R}^+$) | Liquid savings and liquid deposit reserves (INR) | Liquidity cushion |
| `Collateral_Value` | Continuous ($\mathbb{R}^+$) | Pledged property or asset appraisal value (INR) | Security backstop |
| `Loan_Amount` | Continuous ($\mathbb{R}^+$) | Requested loan principal amount (INR) | Exposure at Default |
| `Loan_Term` | Discrete ($\mathbb{Z}^+$) | Loan tenure in months (e.g., 36, 60, 84, 120, 240) | Duration risk |
| `Loan_Purpose` | Categorical Nominal | `Home`, `Education`, `Personal`, `Car`, `Business` | Risk classification bucket |
| `Property_Area` | Categorical Nominal | `Urban`, `Semiurban`, `Rural` | Geographic location factor |
| `Education_Level` | Categorical Ordinal | `Graduate`, `Postgraduate`, `Not Graduate` | Earning potential proxy |
| `Gender` | Categorical Nominal | `Male`, `Female` | Demographic feature |
| `Employer_Category` | Categorical Nominal | `Govt`, `Private`, `Self` | Income stability metric |
| `Loan_Approved` | Binary Target | `1` (Approved), `0` (Rejected) | Ground truth supervisory label |

---

## 💻 Python Implementation & Code Example

```python
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("loan_approval_data.csv")
print("Dataset Dimensions:", df.shape)

# Memory and schema verification
assert df.shape == (1000, 20), f"Expected shape (1000, 20), got {df.shape}"
num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()

print(f"Numerical Features ({len(num_cols)}):", num_cols)
print(f"Categorical Features ({len(cat_cols)}):", cat_cols)

```

---

## 🎯 Quick Revision Points (Interview Notes)
- **Objective**: Credit risk modeling mein precision hamesha accuracy se zyada important hoti hai.
- **Data Invariant**: SimpleImputer aur StandardScaler ko hamesha training data par `fit` karke test set par sirf `transform` kiya jaata hai.
- **Decision Boundary**: Non-linear feature transformations ($DTI^2$, $Credit^2$) linear models ko non-linear patterns capture karne ki capability provide karte hain.
