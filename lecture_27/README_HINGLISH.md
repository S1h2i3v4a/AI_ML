# 💳 Lecture 27: CreditWise Loan Approval System (Minor Project)
## Automated Credit Underwriting ke liye Production Machine Learning Pipeline

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.9.1-orange.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#)

🌐 **Language Navigation:** [English](README.md) | **हिंदी / Hinglish**

**Lecture 27: CreditWise Loan Approval System** mein aapka swagat hai! Yeh ek production-grade supervised machine learning minor project hai jisme hum **SecureTrust Bank** ke retail loan underwriting process ko automate karte hain. Is module mein raw observational CSV data ingestion, statistical imputation, exploratory data analysis (EDA), dummy variable trap-free encoding, leak-free feature scaling, multi-model benchmarking (Logistic Regression, KNN, Gaussian Naive Bayes), non-linear feature engineering ($DTI^2$, $Credit^2$), aur asymmetric profit-maximizing threshold optimization ko end-to-end cover kiya gaya hai.

---

### 📂 Course Assets aur Reference Files

| Asset Name | Description | Direct Link |
| :--- | :--- | :--- |
| **Loan Approval Dataset** | 1,000 retail loan applicants ka 20-feature database | [`loan_approval_data.csv`](loan_approval_data.csv) |
| **Original Reference Notebook** | Official lecture Jupyter Notebook implementation | [`credit_wise_original.ipynb`](credit_wise_original.ipynb) |
| **Problem Statement (Part 1)** | Official business context aur challenges ka screenshot | [`Problem_Statement_Part1.png`](assets/Problem_Statement_Part1.png) |
| **Dataset Feature Dictionary** | Attributes aur schema definition ka official screenshot | [`Problem_Statement_Dataset_Description.png`](assets/Problem_Statement_Dataset_Description.png) |

---

### 🗺️ Submodules aur Topics ka Index

| Submodule | Topic Title | Core Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **27.01** | Problem Statement aur Credit Risk Underwriting | SecureTrust Bank ka case study, default economics, Type I vs Type II errors, asymmetric loss matrix | [Notes](Notes_27.01/README_HINGLISH.md) \| [PDF](Notes_27.01/notes.pdf) \| [Notebook](Notes_27.01/lecture_27_01.ipynb) |
| **27.02** | Project Architecture aur Dataset Ingestion | loan_approval_data.csv ka schema audit (1000x20), numerical vs categorical features, ML pipeline | [Notes](Notes_27.02/README_HINGLISH.md) \| [PDF](Notes_27.02/notes.pdf) \| [Notebook](Notes_27.02/lecture_27_02.ipynb) |
| **27.03** | Missing Values ko Handle Karna — Mean aur Mode Imputation | MCAR vs MAR missingness, SimpleImputer se numerical (mean) aur categorical (mode) imputation | [Notes](Notes_27.03/README_HINGLISH.md) \| [PDF](Notes_27.03/notes.pdf) \| [Notebook](Notes_27.03/lecture_27_03.ipynb) |
| **27.04** | Exploratory Data Analysis (EDA) — Skewness aur Outliers | Target class imbalance (68.6% vs 31.4%), right-skewed income histograms, Tukey IQR outlier fences | [Notes](Notes_27.04/README_HINGLISH.md) \| [PDF](Notes_27.04/notes.pdf) \| [Notebook](Notes_27.04/lecture_27_04.ipynb) |
| **27.05** | Feature Encoding — Dummy Variable Traps | LabelEncoder target/ordinal ke liye, OneHotEncoder(drop='first') multicollinearity rokne ke liye | [Notes](Notes_27.05/README_HINGLISH.md) \| [PDF](Notes_27.05/notes.pdf) \| [Notebook](Notes_27.05/lecture_27_05.ipynb) |
| **27.06** | Correlation Analysis aur Multicollinearity Diagnostics | Pearson correlation matrix, target Loan_Approved ke sath ranking, primary risk predictors | [Notes](Notes_27.06/README_HINGLISH.md) \| [PDF](Notes_27.06/notes.pdf) \| [Notebook](Notes_27.06/lecture_27_06.ipynb) |
| **27.07** | Feature Scaling aur Data Leakage Prevention | StandardScaler Z-score scaling, 80/20 train-test partition, fit vs transform software invariant | [Notes](Notes_27.07/README_HINGLISH.md) \| [PDF](Notes_27.07/notes.pdf) \| [Notebook](Notes_27.07/lecture_27_07.ipynb) |
| **27.08** | Multi-Model Training aur Baseline Classification | Logistic Regression, KNN (k=5), Gaussian Naive Bayes, Confusion Matrix, Precision comparison | [Notes](Notes_27.08/README_HINGLISH.md) \| [PDF](Notes_27.08/notes.pdf) \| [Notebook](Notes_27.08/lecture_27_08.ipynb) |
| **27.09** | Advanced Feature Engineering — Non-Linear Transformations | Polynomial square features (DTI^2, Credit^2), total household income, collateral coverage ratios | [Notes](Notes_27.09/README_HINGLISH.md) \| [PDF](Notes_27.09/notes.pdf) \| [Notebook](Notes_27.09/lecture_27_09.ipynb) |
| **27.10** | Productionizing Credit Risk Systems aur Guardrails | Optimal decision threshold tau tuning, 3-tiered automated underwriting policy, model governance | [Notes](Notes_27.10/README_HINGLISH.md) \| [PDF](Notes_27.10/notes.pdf) \| [Notebook](Notes_27.10/lecture_27_10.ipynb) |

---

### 🧪 Practice Problems aur Systems Engineering Suite

Banking credit risk modeling ke core algorithmic mechanics par based full practice problem set:
- **Questions Folder**: [`Practice_Problems/Questions/README_HINGLISH.md`](Practice_Problems/Questions/README_HINGLISH.md) \| [`questions.pdf`](Practice_Problems/Questions/questions.pdf) \| [`questions.ipynb`](Practice_Problems/Questions/questions.ipynb)
- **Solutions Folder**: [`Practice_Problems/Solutions/README_HINGLISH.md`](Practice_Problems/Solutions/README_HINGLISH.md) \| [`solutions.pdf`](Practice_Problems/Solutions/solutions.pdf) \| [`solutions.ipynb`](Practice_Problems/Solutions/solutions.ipynb)

#### 8 Core Algorithmic Problems:
1. `CreditRiskDataAuditor`: Automated schema validation aur numerical (mean) / categorical (mode) imputation.
2. `FinancialFeatureEncoder`: Dummy Variable Trap se mukt robust categorical encoder.
3. `OutlierCappingTransformer`: Tukey IQR fence capping transformer.
4. `FinancialRatioGenerator`: Non-linear quadratic polynomials ($DTI^2$, $Credit^2$) aur leverage coverage ratios.
5. `CostSensitiveLogisticRegression`: False Positives par heavy loss penalty ($w_0 \gg w_1$) lagane wala underwriter.
6. `KNNUnderwritingEngine`: Inverse-distance weighted metric matching aur nearest peers explainability.
7. `GaussianNBRiskAssessor`: Generative class-conditional densities se maximum Precision achieve karna.
8. `OptimalDecisionThresholdTuner`: Decision cutoff $\tau \in [0.05, 0.95]$ par net bank profit maximize karna.

#### 🔬 Systems Engineering Case Studies (300 DPI Graphics):
- **Case Study 1**: Asymmetric Financial Risk aur Optimal Decision Threshold Curve ([Diagram](Practice_Problems/Solutions/case1_threshold_profit_utility_curve.png))
- **Case Study 2**: Core Risk Features Correlation Matrix aur Multicollinearity ([Diagram](Practice_Problems/Solutions/case2_correlation_heatmap_risk_features.png))
- **Case Study 3**: Imbalanced Loan Portfolio par Classifiers ka ROC aur PR Benchmark ([Diagram](Practice_Problems/Solutions/case3_model_roc_pr_frontier_comparison.png))
