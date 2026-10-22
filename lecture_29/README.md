# ⚔️ Lecture 29: Supervised Machine Learning (Part 5) — Support Vector Machines & Ensemble Learning
## Mathematical Foundations, Dual Optimization, Non-Linear Kernels & Ensemble Architectures

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.9.1-orange.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#)

🌐 **Language Navigation:** **English** | [हिंदी / Hinglish](README_HINGLISH.md)

Welcome to **Lecture 29: Supervised Machine Learning (Part 5)**, a dual-focus deep dive bridging **Support Vector Machines (SVM)** and **Ensemble Learning**. This comprehensive curriculum covers maximum margin classifiers, soft-margin duality, Mercer kernels (RBF, Polynomial, Sigmoid), Support Vector Regression (SVR) with $\epsilon$-insensitive tubes, coordinate descent scaling (`LinearSVR`), and hyperparameter tuning via `GridSearchCV`. In parallel, it explores the foundational theory of **Ensemble Methods**, dissecting Bootstrap Aggregation (Bagging), Sequential Error Reweighting (Boosting), Random Forests with double randomness, Out-Of-Bag (OOB) mathematical derivations ($1/e \approx 36.8\% implication), and production meta-estimators (`BaggingClassifier`).

---

### 📂 Course Assets & Reference Files

| Asset Name | Description | Resource Link |
| :--- | :--- | :--- |
| **Syllabus Overview** | Official lecture visual index and video breakdown | [`00_Day_32_Contents.jpeg`](00_Day_32_Contents.jpeg) |
| **SVR Implementation Reference** | Reference teacher implementation on Diabetes dataset | [`svr_implementation_reference.ipynb`](svr_implementation_reference.ipynb) |
| **OOB & Random Forest Reference** | Reference teacher notebook on Titanic dataset & OOB score | [`code_oob_reference.ipynb`](code_oob_reference.ipynb) |

---

### 🗺️ Submodules & Topic Architecture Index

| Submodule | Topic Title | Core Engineering Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **29.01** | Introduction to Support Vector Machines (SVM) | Maximal margin hyperplane, geometric separation, decision boundaries, convex hull intuition | [Notes](Notes_29.01/README.md) \| [PDF](Notes_29.01/notes.pdf) \| [Hinglish PDF](Notes_29.01/notes_hinglish.pdf) \| [Notebook](Notes_29.01/lecture_29_01.ipynb) |
| **29.02** | SVM Classifier Intuition — Maximum Margin & Support Vectors | Functional vs geometric margin, dual optimization, support vector identification, invariance to non-support vectors | [Notes](Notes_29.02/README.md) \| [PDF](Notes_29.02/notes.pdf) \| [Hinglish PDF](Notes_29.02/notes_hinglish.pdf) \| [Notebook](Notes_29.02/lecture_29_02.ipynb) |
| **29.03** | Classification Hyperparameters — Regularization C & Gamma | Soft-margin penalty C, slack variables, RBF kernel spread gamma, bias-variance tradeoff | [Notes](Notes_29.03/README.md) \| [PDF](Notes_29.03/notes.pdf) \| [Hinglish PDF](Notes_29.03/notes_hinglish.pdf) \| [Notebook](Notes_29.03/lecture_29_03.ipynb) |
| **29.04** | Kernel Trick in SVM — Projecting into Higher Dimensions | Non-linear separation, Mercer's Theorem, inner product kernel representation, mapping function phi(x) | [Notes](Notes_29.04/README.md) \| [PDF](Notes_29.04/notes.pdf) \| [Hinglish PDF](Notes_29.04/notes_hinglish.pdf) \| [Notebook](Notes_29.04/lecture_29_04.ipynb) |
| **29.05** | Common Kernel Types — Linear, Polynomial, RBF & Sigmoid | Comparative kernel taxonomy, polynomial degree & coef0, Gaussian RBF metric space, Mercer conditions | [Notes](Notes_29.05/README.md) \| [PDF](Notes_29.05/notes.pdf) \| [Hinglish PDF](Notes_29.05/notes_hinglish.pdf) \| [Notebook](Notes_29.05/lecture_29_05.ipynb) |
| **29.06** | SVM Classifier Implementation in Scikit-Learn | StandardScaler preprocessing, SVC class_weight='balanced', ROC-AUC evaluation, decision boundaries | [Notes](Notes_29.06/README.md) \| [PDF](Notes_29.06/notes.pdf) \| [Hinglish PDF](Notes_29.06/notes_hinglish.pdf) \| [Notebook](Notes_29.06/lecture_29_06.ipynb) |
| **29.07** | Support Vector Regression (SVR) Intuition — Epsilon-Insensitive Tube | Epsilon-tube margin, slack variables xi & xi*, zero loss region, sparse dual support vectors | [Notes](Notes_29.07/README.md) \| [PDF](Notes_29.07/notes.pdf) \| [Hinglish PDF](Notes_29.07/notes_hinglish.pdf) \| [Notebook](Notes_29.07/lecture_29_07.ipynb) |
| **29.08** | SVR Implementation in Scikit-Learn — Diabetes Regression | StandardScaler on X and y, target inverse transformation, R2 score, RMSE evaluation | [Notes](Notes_29.08/README.md) \| [PDF](Notes_29.08/notes.pdf) \| [Hinglish PDF](Notes_29.08/notes_hinglish.pdf) \| [Notebook](Notes_29.08/lecture_29_08.ipynb) |
| **29.09** | Hyperparameter Optimization via GridSearchCV for SVR | Systematic grid search across C, epsilon, and gamma, 5-fold cross-validation, validation surfaces | [Notes](Notes_29.09/README.md) \| [PDF](Notes_29.09/notes.pdf) \| [Hinglish PDF](Notes_29.09/notes_hinglish.pdf) \| [Notebook](Notes_29.09/lecture_29_09.ipynb) |
| **29.10** | LinearSVR vs SVR — Liblinear vs Libsvm Architectural Comparison | O(N) Coordinate Descent via Liblinear vs O(N^2 - N^3) Libsvm, duality, memory footprints | [Notes](Notes_29.10/README.md) \| [PDF](Notes_29.10/notes.pdf) \| [Hinglish PDF](Notes_29.10/notes_hinglish.pdf) \| [Notebook](Notes_29.10/lecture_29_10.ipynb) |
| **29.11** | Introduction to Ensemble Learning — Wisdom of Crowds | Condorcet's Jury Theorem, weak vs strong learners, Hard Voting vs Soft Voting aggregation | [Notes](Notes_29.11/README.md) \| [PDF](Notes_29.11/notes.pdf) \| [Hinglish PDF](Notes_29.11/notes_hinglish.pdf) \| [Notebook](Notes_29.11/lecture_29_11.ipynb) |
| **29.12** | Bootstrap Aggregation (Bagging) — Variance Reduction Mechanics | Uniform bootstrap sampling with replacement, sample variance reduction Var(bar_X) = sigma^2 / M, parallel execution | [Notes](Notes_29.12/README.md) \| [PDF](Notes_29.12/notes.pdf) \| [Hinglish PDF](Notes_29.12/notes_hinglish.pdf) \| [Notebook](Notes_29.12/lecture_29_12.ipynb) |
| **29.13** | Boosting Paradigm — Sequential Adaptive Learning | Additive stagewise modeling, error reweighting, residual targeting, bias reduction dynamics | [Notes](Notes_29.13/README.md) \| [PDF](Notes_29.13/notes.pdf) \| [Hinglish PDF](Notes_29.13/notes_hinglish.pdf) \| [Notebook](Notes_29.13/lecture_29_13.ipynb) |
| **29.14** | Random Forest Classifier & Regressor — Double Randomness Principle | Row bootstrapping + feature bagging (sqrt(D) / D/3), tree de-correlation, variance stabilization | [Notes](Notes_29.14/README.md) \| [PDF](Notes_29.14/notes.pdf) \| [Hinglish PDF](Notes_29.14/notes_hinglish.pdf) \| [Notebook](Notes_29.14/lecture_29_14.ipynb) |
| **29.15** | Out-Of-Bag (OOB) Evaluation — First-Principles Mathematical Derivation | Derivation of lim (1 - 1/N)^N = 1/e = 36.8%, 63.2% sample inclusion, built-in validation without CV | [Notes](Notes_29.15/README.md) \| [PDF](Notes_29.15/notes.pdf) \| [Hinglish PDF](Notes_29.15/notes_hinglish.pdf) \| [Notebook](Notes_29.15/lecture_29_15.ipynb) |
| **29.16** | Random Forest Implementation with OOB Score in Scikit-Learn | Titanic dataset survival modeling, oob_score=True, n_estimators=501 tuning, feature importances | [Notes](Notes_29.16/README.md) \| [PDF](Notes_29.16/notes.pdf) \| [Hinglish PDF](Notes_29.16/notes_hinglish.pdf) \| [Notebook](Notes_29.16/lecture_29_16.ipynb) |
| **29.17** | Decision Tree vs Random Forest — Comparative Benchmark & Trade-offs | Single hierarchical tree vs de-correlated ensemble, variance vs interpretability, latency profiles | [Notes](Notes_29.17/README.md) \| [PDF](Notes_29.17/notes.pdf) \| [Hinglish PDF](Notes_29.17/notes_hinglish.pdf) \| [Notebook](Notes_29.17/lecture_29_17.ipynb) |
| **29.18** | BaggingClassifier & BaggingRegressor in Scikit-Learn | Flexible meta-estimator API, max_samples, max_features, bootstrap_features, KNN/Tree baselines | [Notes](Notes_29.18/README.md) \| [PDF](Notes_29.18/notes.pdf) \| [Hinglish PDF](Notes_29.18/notes_hinglish.pdf) \| [Notebook](Notes_29.18/lecture_29_18.ipynb) |

---

### 🛠️ Key Mathematical & Algorithmic Milestones
1. **Geometric & Dual Margin Formulation**:
   Maximizing margin $\frac{2}{\|\mathbf{w}\|}$ subject to $y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1 - \xi_i$.
2. **Mercer's Kernel Transformation**:
   Inner product evaluation in Hilbert feature space $K(\mathbf{x}, \mathbf{x}') = \phi(\mathbf{x})^T \phi(\mathbf{x}')$ without explicit dimensional expansion.
3. **$\\epsilon$-Insensitive Tube Loss in SVR**:
   $L_\epsilon(y, f(\mathbf{x})) = \max(0, |y - f(\mathbf{x})| - \epsilon)$ leading to sparse dual representations.
4. **Bootstrap Variance Reduction**:
   Ensembling $M$ de-correlated estimators yields $\text{Var}(\bar{f}) = \rho \sigma^2 + \frac{1 - \rho}{M} \sigma^2$, collapsing variance to $\rho \sigma^2$.
5. **Out-Of-Bag (OOB) Convergence Derivation**:
   Probability of a sample being excluded from a bootstrap replicate converges to $\lim_{N \to \infty} (1 - \frac{1}{N})^N = \frac{1}{e} \approx 36.79\%$.

---

### 🧪 Practice Problems & Systems Engineering Suite

A comprehensive industrial problem set designed to test first-principles SVM and Ensemble algorithms:
- **Practice Problems Overview**: [Practice_Problems/README.md](Practice_Problems/README.md) | [हिंदी / Hinglish](Practice_Problems/README_HINGLISH.md)
- **Questions Directory**: [Practice_Problems/Questions/README.md](Practice_Problems/Questions/README.md) | [questions.ipynb](Practice_Problems/Questions/questions.ipynb)
- **Solutions Directory**: [Practice_Problems/Solutions/README.md](Practice_Problems/Solutions/README.md) | [solutions.ipynb](Practice_Problems/Solutions/solutions.ipynb)

#### 🔬 Systems Engineering Case Studies (300 DPI Visualizations):
- **Case Study 1**: SVR Epsilon-Insensitive Tube & Target Scaling Effect ([Figure](Practice_Problems/Solutions/case1_svr_epsilon_tube_and_scaling.png))
- **Case Study 2**: Out-Of-Bag (OOB) Mathematical Convergence & Random Forest Validation ([Figure](Practice_Problems/Solutions/case2_oob_convergence_and_bootstrap.png))
- **Case Study 3**: Wisdom of Crowds & Leo Breiman's Variance Decomposition ([Figure](Practice_Problems/Solutions/case3_random_forest_variance_collapse.png))
