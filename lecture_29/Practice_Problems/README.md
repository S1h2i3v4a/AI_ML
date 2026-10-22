# ⚔️ Lecture 29: Practice Problems & Systems Engineering Suite
## Supervised Machine Learning (Part 5) — Support Vector Machines & Ensemble Learning

Welcome to the **Practice Problems & Systems Engineering Suite** for **Lecture 29**! This laboratory suite is strictly derived from the curriculum taught in Lecture 29: maximum margin separation, soft-margin duality, slack variables $\xi_i$, Mercer kernels (Linear, Polynomial, Gaussian RBF, Sigmoid), Support Vector Regression (SVR) with $\epsilon$-insensitive tubes, mandatory dual feature scaling, coordinate descent scaling (`LinearSVR` via Liblinear vs `SVR` via Libsvm), Condorcet's Jury Theorem, Bootstrap Aggregation (Bagging), Out-Of-Bag (OOB) first-principles convergence derivation ($\lim_{N \to \infty} (1 - 1/N)^N = 1/e \approx 36.79\%$), Random Forest double randomness, and production meta-estimators (`BaggingClassifier`).

---

## 🌐 Language Navigation
- **English Master Documentation**: [`README.md`](README.md)
- **हिंदी / Hinglish Master Documentation**: [`README_HINGLISH.md`](README_HINGLISH.md)

---

## 📂 Suite Architecture

```plaintext
lecture_29/Practice_Problems/
├── README.md                           # Master English Suite Overview
├── README_HINGLISH.md                  # Master Hinglish Suite Overview
├── Questions/
│   ├── README.md                       # Complete Case-Based Problem Statements (English)
│   ├── README_HINGLISH.md              # Case-Based Problem Statements (Hinglish)
│   └── questions.ipynb                 # Interactive Starter Jupyter Notebook
└── Solutions/
    ├── README.md                       # Production Solutions & Mathematical Proofs (English)
    ├── README_HINGLISH.md              # Production Solutions & Mathematical Proofs (Hinglish)
    ├── solutions.ipynb                 # Fully Executed Master Solutions Notebook
    ├── case1_svr_epsilon_tube_and_scaling.png    # 300 DPI Epsilon Tube & Scaling Effect
    ├── case2_oob_convergence_and_bootstrap.png   # 300 DPI (1-1/N)^N Derivation & Titanic OOB
    └── case3_random_forest_variance_collapse.png # 300 DPI Condorcet & Breiman's Variance Collapse
```

---

## 🔬 Systems Engineering Case Studies (Industrial Scenarios)

### 🩺 Case Study 1: Clinical Diabetes Progression Forecaster (Support Vector Regression - SVR)
- **Dataset Context**: Scikit-learn Diabetes dataset (442 clinical patients across 10 physiological predictors including age, sex, bmi, average blood pressure, and 6 blood serum metrics; target is disease progression 1 year post-baseline).
- **Core Challenge**: Unlike ordinary least squares which penalizes any non-zero residual, SVR enforces an $\epsilon$-insensitive tube where errors within $\pm \epsilon$ are ignored ($L_\epsilon = 0$). Furthermore, unscaled inputs cause catastrophic RBF kernel failure ($R^2 < 0$) due to Euclidean distance distortion.
- **Engineering Task**:
  1. Prove why dual standardization (scaling BOTH $X$ and $y$) is mathematically required.
  2. Implement an end-to-end scaled SVR pipeline and verify performance recovery.
  3. Conduct 5-fold cross-validation `GridSearchCV` over $(C \in [0.1, 1, 10, 100], \epsilon \in [0.01, 0.1, 0.2, 0.5], \gamma \in ['scale', 'auto', 0.01, 0.1])$.
  4. Inspect dual sparsity: Extract support vectors (`support_`) and prove that points inside the $\epsilon$-tube have zero dual multipliers ($\alpha_i = \alpha_i^* = 0$).

### 🚢 Case Study 2: Maritime Evacuation Survivor Modeling & OOB Validation (Titanic Dataset)
- **Dataset Context**: Titanic survivor records (`pclass`, `sex`, `fare`, `embarked`, `age`, `sibsp`, `parch`), predicting binary survival.
- **Core Challenge**: Validating high-capacity ensemble models typically requires costly K-Fold Cross-Validation or sacrificing training data for a validation split. Leo Breiman's Out-Of-Bag (OOB) evaluation provides built-in validation for free.
- **Engineering Task**:
  1. Mathematical Derivation: Prove that the probability an observation is omitted from a bootstrap sample converges to $\lim_{N \to \infty} (1 - \frac{1}{N})^N = \frac{1}{e} \approx 36.79\%$.
  2. Implement `RandomForestClassifier(n_estimators=501, oob_score=True, max_depth=4)` and verify that `rf.oob_score_` provides an unbiased estimate matching independent test set accuracy.
  3. Extract Mean Decrease in Impurity (MDI) feature importances and interpret the structural dominance of `fare` and `sex`.

### 👥 Case Study 3: Wisdom of Crowds & Ensemble Variance Collapse (Condorcet's Jury Theorem & Bagging)
- **Theoretical Context**: Mathematical foundations of aggregation and variance reduction.
- **Core Challenge**: Why does averaging unstable weak learners produce an ultra-stable strong learner? Why does Bagging work wonders on Decision Trees but fail to improve Logistic Regression?
- **Engineering Task**:
  1. Mathematical Formulation: Use the binomial distribution to prove Condorcet's Jury Theorem for $M = 3, 11, 101$ independent voters with individual accuracy $p = 0.60$.
  2. Analyze Leo Breiman's variance decomposition:
     $$\text{Var}(\bar{f}) = \rho \sigma^2 + \frac{1 - \rho}{M} \sigma^2$$
     Prove that as $M \to \infty$, variance is bounded below by $\rho \sigma^2$. Explain how Random Forest's feature subspace randomization ($\sqrt{D}$) forces $\rho \downarrow$, breaking the asymptote.
  3. Run an empirical benchmark comparing `BaggingClassifier(base_estimator=DecisionTreeClassifier())` vs `BaggingClassifier(base_estimator=LogisticRegression(max_iter=1000))` on the Titanic dataset with $M = 201$.

### ⚡ Case Study 4: Computational Scaling & Convex Optimization Duality (LinearSVR vs Kernel SVR)
- **High-Throughput Context**: Transitioning from small medical cohorts ($N = 442$) to large production clickstream pipelines ($N = 100,000$).
- **Core Challenge**: Libsvm (`SVR(kernel='linear')`) scales quadratically to cubically with sample size ($O(N^2 \sim N^3)$), choking on modern big data, whereas Liblinear (`LinearSVR`) scales linearly ($O(N \cdot D)$) via Coordinate Descent.
- **Engineering Task**:
  1. Benchmark execution time and peak memory consumption across $N \in [1000, 5000, 20000]$.
  2. Differentiate between primal Coordinate Descent (`dual=False` when $N > D$) and dual optimization.
  3. Formulate an engineering decision matrix for deploying `LinearSVR`, `SVR(kernel='rbf')`, and `SGDRegressor(loss='epsilon_insensitive')`.

---

## 📋 Problem Suite Inventory

| Problem ID | Category & Focus | Algorithmic Paradigm | Mathematical Invariant | Syllabus Link |
| :--- | :--- | :--- | :--- | :--- |
| **Problem 01** | Dual Scaled SVR Pipeline | Kernel Ridge / Tube Loss | $L_\epsilon = \max(0, \|y - \hat{y}\| - \epsilon)$, $\text{scaler}(y)$ | Notes 29.07, 29.08 |
| **Problem 02** | Systematic SVR Hyperparameter Tuning | 5-Fold Grid Search | Grid search over $(C, \epsilon, \gamma)$, $R^2 > 0.40$ | Notes 29.09 |
| **Problem 03** | Dual Sparsity & Support Vector Extractor | Convex Optimization Duality | $\alpha_i \alpha_i^* = 0$, $\xi_i > 0 \implies \alpha_i = C$ | Notes 29.02, 29.07 |
| **Problem 04** | OOB Inclusion Derivation & Calculator | Bootstrap Aggregation | $\lim_{N \to \infty} (1 - \frac{1}{N})^N = \frac{1}{e} \approx 36.8\%$ | Notes 29.15 |
| **Problem 05** | Production Titanic Random Forest Engine | Double Randomness Ensembling | $M=501$, $\text{oob\_score}=\text{True}$, $\sqrt{D}$ features | Notes 29.14, 29.16 |
| **Problem 06** | Condorcet Jury Theorem Simulator | Probabilistic Majority Voting | $P(\text{Maj}) = \sum_{k=\lfloor M/2 \rfloor + 1}^M \binom{M}{k} p^k (1-p)^{M-k}$ | Notes 29.11 |
| **Problem 07** | Breiman's Variance Decomposition Analyzer | Ensemble Correlation Dynamics | $\text{Var}(\bar{f}) = \rho \sigma^2 + \frac{1-\rho}{M}\sigma^2$, $\rho \downarrow$ via $\sqrt{D}$ | Notes 29.12, 29.14 |
| **Problem 08** | Heterogeneous Bagging Benchmark | High vs Low Variance Learners | Tree vs Logistic Regression base estimators | Notes 29.17, 29.18 |
