# 💳 Lecture 27: CreditWise Loan Approval System (Minor Project)
## Production Machine Learning Pipeline for Automated Credit Underwriting

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.9.1-orange.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#)

🌐 **Language Navigation:** **English** | [हिंदी / Hinglish](README_HINGLISH.md)

Welcome to **Lecture 27: CreditWise Loan Approval System**, an enterprise-grade supervised machine learning minor project simulating retail loan underwriting for **SecureTrust Bank**. This module implements the complete real-world machine learning lifecycle—from raw observational data ingestion, missing value imputation, and exploratory data analysis to feature encoding, leak-free standardization, multi-model benchmarking (Logistic Regression, KNN, Gaussian Naive Bayes), non-linear financial feature engineering, and cost-utility threshold optimization.

---

### 📂 Course Assets & Reference Materials

| Asset Name | Description | Resource Link |
| :--- | :--- | :--- |
| **Loan Approval Dataset** | Historical database of 1,000 retail loan applicants across 20 features | [`loan_approval_data.csv`](loan_approval_data.csv) |
| **Original Reference Notebook** | Official lecture Jupyter Notebook implementation | [`credit_wise_original.ipynb`](credit_wise_original.ipynb) |
| **Problem Statement (Part 1)** | Official business context & operational challenges screenshot | [`Problem_Statement_Part1.png`](assets/Problem_Statement_Part1.png) |
| **Dataset Feature Dictionary** | Official attributes & data schema description screenshot | [`Problem_Statement_Dataset_Description.png`](assets/Problem_Statement_Dataset_Description.png) |

---

### 🗺️ Module Subtopics & Curriculum Index

| Submodule | Topic Title | Core Engineering Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **27.01** | Problem Statement & Credit Risk Fundamentals | SecureTrust Bank case, financial default economics, Type I vs Type II errors, asymmetric loss matrix | [Notes](Notes_27.01/README.md) \| [PDF](Notes_27.01/notes.pdf) \| [Notebook](Notes_27.01/lecture_27_01.ipynb) |
| **27.02** | Project Architecture, Pipeline Engineering & Ingestion | Schema audit of loan_approval_data.csv (1000x20), feature taxonomy, pipeline blueprint | [Notes](Notes_27.02/README.md) \| [PDF](Notes_27.02/notes.pdf) \| [Notebook](Notes_27.02/lecture_27_02.ipynb) |
| **27.03** | Handling Missing Values — Statistical Imputation | MCAR/MAR missingness mechanisms, SimpleImputer (Mean for numerical, Mode for categorical) | [Notes](Notes_27.03/README.md) \| [PDF](Notes_27.03/notes.pdf) \| [Notebook](Notes_27.03/lecture_27_03.ipynb) |
| **27.04** | Exploratory Data Analysis (EDA) — Skewness & Outliers | Class imbalance (68.6% vs 31.4%), log-normal income distributions, Tukey IQR outlier fences | [Notes](Notes_27.04/README.md) \| [PDF](Notes_27.04/notes.pdf) \| [Notebook](Notes_27.04/lecture_27_04.ipynb) |
| **27.05** | Feature Encoding — Nominal, Ordinal & Dummy Traps | LabelEncoder for binary/ordinal, OneHotEncoder(drop='first') to avoid matrix singularity | [Notes](Notes_27.05/README.md) \| [PDF](Notes_27.05/notes.pdf) \| [Notebook](Notes_27.05/lecture_27_05.ipynb) |
| **27.06** | Correlation Analysis & Multicollinearity Diagnostics | Pearson correlation matrix r_xy, ranking top positive (Credit_Score) and negative (DTI) risk drivers | [Notes](Notes_27.06/README.md) \| [PDF](Notes_27.06/notes.pdf) \| [Notebook](Notes_27.06/lecture_27_06.ipynb) |
| **27.07** | Feature Scaling & Splitting — Data Leakage Prevention | Z-score standardization (StandardScaler), 80/20 partition, fit_transform vs transform contract | [Notes](Notes_27.07/README.md) \| [PDF](Notes_27.07/notes.pdf) \| [Notebook](Notes_27.07/lecture_27_07.ipynb) |
| **27.08** | Multi-Model Training & Baseline Classification | Logistic Regression, KNN (k=5), Gaussian Naive Bayes, Confusion Matrix, Precision benchmarking | [Notes](Notes_27.08/README.md) \| [PDF](Notes_27.08/notes.pdf) \| [Notebook](Notes_27.08/lecture_27_08.ipynb) |
| **27.09** | Advanced Feature Engineering — Non-Linear Transformations | Quadratic terms (DTI^2, Credit^2), household total income, loan leverage and collateral coverage | [Notes](Notes_27.09/README.md) \| [PDF](Notes_27.09/notes.pdf) \| [Notebook](Notes_27.09/lecture_27_09.ipynb) |
| **27.10** | Productionizing Credit Risk Systems & Guardrails | Optimal decision threshold tau tuning, 3-tiered auto-underwriting routing, model governance | [Notes](Notes_27.10/README.md) \| [PDF](Notes_27.10/notes.pdf) \| [Notebook](Notes_27.10/lecture_27_10.ipynb) |

---

### 🧪 Practice Problems & Systems Engineering Suite

A comprehensive industrial problem set designed to test first-principles financial systems engineering:
- **Questions Directory**: [`Practice_Problems/Questions/README.md`](Practice_Problems/Questions/README.md) \| [`questions.pdf`](Practice_Problems/Questions/questions.pdf) \| [`questions.ipynb`](Practice_Problems/Questions/questions.ipynb)
- **Solutions Directory**: [`Practice_Problems/Solutions/README.md`](Practice_Problems/Solutions/README.md) \| [`solutions.pdf`](Practice_Problems/Solutions/solutions.pdf) \| [`solutions.ipynb`](Practice_Problems/Solutions/solutions.ipynb)

#### Core Problems:
1. `CreditRiskDataAuditor`: Automated schema validation and missing data imputation pipeline.
2. `FinancialFeatureEncoder`: Robust categorical encoder avoiding the Dummy Variable Trap.
3. `OutlierCappingTransformer`: Tukey IQR fence capping preserving extreme wealth signals.
4. `FinancialRatioGenerator`: Non-linear quadratic polynomials ($DTI^2$, $Credit^2$) and leverage coverage ratios.
5. `CostSensitiveLogisticRegression`: Weighted loss matrix penalizing False Positives ($w_0 \gg w_1$).
6. `KNNUnderwritingEngine`: Distance-weighted metric matching with local neighborhood audit.
7. `GaussianNBRiskAssessor`: Generative class-conditional densities delivering high Precision.
8. `OptimalDecisionThresholdTuner`: Portfolio profit maximization across decision cutoff $\tau \in [0.05, 0.95]$.

#### 🔬 Systems Engineering Case Studies (300 DPI Visualizations):
- **Case Study 1**: Asymmetric Financial Risk & Threshold Optimization Curve ([Figure](Practice_Problems/Solutions/case1_threshold_profit_utility_curve.png))
- **Case Study 2**: Core Risk Features Correlation Matrix & Target Linkage ([Figure](Practice_Problems/Solutions/case2_correlation_heatmap_risk_features.png))
- **Case Study 3**: Classifier Benchmark Frontier on Imbalanced Loan Approval Portfolio ([Figure](Practice_Problems/Solutions/case3_model_roc_pr_frontier_comparison.png))
