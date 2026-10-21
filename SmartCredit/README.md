# 🏦 SmartCredit — Intelligent Loan Default & Risk Scoring System
### Production-Grade Machine Learning & FinTech Credit Risk Engine (Lectures 01 – 28 Integration)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3%2B-orange.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#)

---

## 📌 1. Problem Statement & Business Context

In consumer banking and Non-Banking Financial Companies (NBFCs), loan approval workflows face two major challenges:
1. **Manual Underwriting Inefficiency:** Evaluating credit applications manually is slow, costly, and subject to cognitive bias.
2. **Non-Performing Asset (NPA) Exposure:** Unsound loan sanctions lead to loan defaults, degrading bank solvency and regulatory capital ratios.

**SmartCredit** is an end-to-end Machine Learning intelligence engine that:
- Accurately classifies credit applicants into **Approved** or **High-Risk Default** states.
- Quantifies risk into granular tiers: `🟢 Low Risk (< 30% default probability)`, `🟡 Medium Risk (30% - 60%)`, and `🔴 High Risk (> 60%)`.
- Computes optimal **Safe Recommended Loan Limits** based on household earning capacity and existing leverage.
- Provides a **Streamlit Web Application** enabling loan officers to run real-time credit checks, inspect interactive Exploratory Data Analysis (EDA), and evaluate multi-model benchmarks.

---

## 🏛️ 2. Repository Architecture & File Index

```plaintext
SmartCredit/
├── .gitignore                    # Python, Jupyter & model checkpoints exclusions
├── LICENSE                       # MIT Open Source License
├── requirements.txt              # Production dependency specifications
├── run_pipeline.py               # Master end-to-end execution pipeline
├── README.md                     # Comprehensive documentation & presentation guide
│
├── data/
│   ├── raw/
│   │   └── loan_data.csv         # Benchmark historical dataset (1,000 applicants × 20 attributes)
│   └── processed/
│       └── loan_cleaned.csv      # Engineered modelling matrix (950 rows × 36 features)
│
├── notebooks/
│   └── SmartCredit_Master.ipynb  # Self-contained presentation & analysis notebook
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py            # Robust CSV ingestion & metadata introspection
│   ├── preprocessing.py          # Missing-value imputation & outlier filtering
│   ├── feature_engineering.py    # DTI ratios, credit tiers & one-hot encoding
│   ├── model_training.py         # Logistic, Pruned Decision Tree & Random Forest
│   └── evaluation.py             # ROC curves, confusion matrices & feature importance
│
├── models/
│   ├── logistic_regression.pkl   # Fitted baseline Logistic Regression
│   ├── decision_tree.pkl         # Fitted Decision Tree with Cost-Complexity Pruning
│   ├── random_forest.pkl         # Fitted Random Forest Classifier
│   ├── best_model.joblib         # Champion model for web deployment
│   ├── best_model_name.joblib    # Champion model designation string
│   └── feature_columns.joblib    # Aligned feature schema for zero-error inference
│
├── app/
│   ├── app.py                    # Main Streamlit web application & risk simulator
│   └── pages/
│       ├── 1_EDA.py              # Interactive Exploratory Data Analysis dashboard
│       └── 2_Model_Comparison.py # Side-by-side performance & visualization portal
│
├── reports/
│   ├── model_comparison.csv      # Tidy classification metrics summary
│   ├── model_metrics.csv         # Streamlit-formatted metrics ledger
│   └── figures/
│       ├── confusion_matrices.png # 300 DPI high-definition confusion matrices
│       ├── roc_curves.png         # 300 DPI multi-model ROC benchmark curves
│       └── feature_importance.png # 300 DPI Gini impurity driving factor rankings
│
└── tests/
    └── test_pipeline.py          # 6 automated unit & integration test suites
```

---

## 📊 3. Model Benchmark & Empirical Results

The pipeline evaluates three architectures on a held-out stratified test set (20% split, 190 applicants):

| Model Architecture | Test Accuracy | Precision | Recall (Default Detection) | F1 Score | ROC-AUC Benchmark |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression (Baseline)** | 78.42% | 61.45% | 85.00% | 0.7133 | 0.8565 |
| **Decision Tree (Pruned `ccp_alpha=0.00357`)** | 94.21% | 86.57% | 96.67% | 0.9134 | 0.9536 |
| **🏆 Random Forest Classifier (Champion)** | **95.79%** | **88.24%** | **100.00%** | **0.9375** | **0.9771** |

> [!IMPORTANT]
> **Why Recall is King in Credit Risk:** In banking, a **False Negative** (classifying a defaulter as creditworthy) causes direct capital write-offs (NPA). The Random Forest achieves **100% recall** on approved borrowers while minimizing false approvals.

---

## 🗺️ 4. Lectures 01 to 28 Curriculum Integration

| Lecture Topic | Course Lectures | SmartCredit Implementation Component |
| :--- | :--- | :--- |
| **Python OOP & Modularity** | Lectures 01 – 05 | Clean modular package design (`src/`), decoupled pipelines, and exception guards |
| **NumPy Matrix Operations** | Lectures 06 – 09 | Array transformations, vector clipping, and numerical bounds |
| **Pandas Data Manipulation** | Lectures 10 – 17 | `dropna`, median/mode imputation, `pd.cut` tiering, and `get_dummies` |
| **Data Visualization & Styling** | Lectures 18 – 19 | Matplotlib object-oriented subplots, Seaborn KDEs, boxplots, 300 DPI export |
| **Probability Theory & Bayes** | Lecture 20 | Risk probabilities $P(\text{Default} \mid \text{Low CIBIL})$, threshold calibration |
| **Calculus & Gradient Descent** | Lecture 22 | Logistic loss minimization $\min_{\mathbf{w}} -\sum [y \ln \hat{y} + (1-y)\ln(1-\hat{y})]$ |
| **Logistic Regression** | Lecture 24 | Odds ratio calculation, Sigmoid link $\sigma(z) = \frac{1}{1+e^{-z}}$ |
| **Decision Trees & Pruning** | Lecture 28 | CART algorithm, Gini Impurity, Minimal Cost-Complexity Pruning ($ccp\_\alpha$) |
| **Ensemble Bagging** | Lectures 29+ preview | 200-tree de-correlated Random Forest with out-of-bag variance reduction |

---

## 🚀 5. Quickstart & Execution Guide

### Step 1: Clone & Install Dependencies
```bash
cd SmartCredit
pip install -r requirements.txt
```

### Step 2: Execute the Automated Pipeline
Runs preprocessing, feature engineering, cross-validation tuning, model fitting, and generates evaluation graphics:
```bash
python run_pipeline.py
```

### Step 3: Run the Automated Test Suite
```bash
python -m unittest tests/test_pipeline.py
```

### Step 4: Launch the Interactive Streamlit Web App
```bash
streamlit run app/app.py
```

---

## 🎤 6. Viva & Presentation Cheat Sheet

1. **Q: Why was Cost-Complexity Pruning (`ccp_alpha`) applied to the Decision Tree?**  
   *Answer:* Unpruned decision trees recursively split until leaves reach purity ($N=1$), memorizing training noise and causing extreme variance. By minimizing $R_\alpha(T) = R(T) + \alpha |T|$, we penalized tree size $|T|$, boosting generalization accuracy from 88% to 94.2%.

2. **Q: How does the system prevent Data Leakage?**  
   *Answer:* Missing-value medians and IQR boundary parameters are computed strictly from training distributions and saved for inference. Categorical encodings are aligned to fixed saved schemas (`feature_columns.joblib`).

3. **Q: How is the Safe Recommended Loan Amount calculated?**  
   *Answer:* Based on the applicant's risk probability, an income multiplier factor is applied: Low-risk applicants receive up to $5\times$ household income, medium-risk $3\times$, and high-risk applicants are limited to $1.5\times$ with mandatory collateral checks.

---

## 👤 Author
**Shivam Keshari**  
*AI & Machine Learning Masterclass Project*
