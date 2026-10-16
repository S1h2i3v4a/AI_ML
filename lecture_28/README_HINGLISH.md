# 🌲 Lecture 28: Supervised Machine Learning (Part 4) — Decision Trees
## Mathematical Foundations, Algorithmic Splitting & Production Pruning

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.9.1-orange.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#)

🌐 **Language Navigation:** [English](README.md) | **हिंदी / Hinglish**

**Lecture 28: Supervised Machine Learning (Part 4) — Decision Trees** mein aapka swagat hai! Yeh non-linear hierarchical decision trees ka first-principles masterclass hai. Is module mein recursive binary splitting (Hunt's algorithm / CART), information-theoretic impurity metrics (Shannon Entropy, Gini Impurity), Taylor series mathematical equivalence, Information Gain aur C4.5 Gain Ratio, unconstrained trees ki overfitting pathology, structural pre-pruning (`max_depth`, `min_samples_leaf`), Leo Breiman ka Minimal Cost-Complexity post-pruning (`ccp_alpha`), Variance Reduction par based Decision Tree Regressors, aur complete **ShopSmart E-Commerce Purchase Prediction Project** (12,330 sessions, F1 benchmark > 0.55) cover kiya gaya hai.

---

### 📂 Course Assets aur Reference Files

| Asset Name | Description | Direct Link |
| :--- | :--- | :--- |
| **Syllabus Overview** | Official lecture visual index aur video duration screenshot | [`00_Day_31_Contents.jpeg`](00_Day_31_Contents.jpeg) |
| **ShopSmart E-Commerce Dataset** | 12,330 browsing sessions ka official CSV database (18 features) | [`shop_smart_ecommerce.csv`](shop_smart_ecommerce.csv) |
| **Official Solution Notebook** | Official lecture Jupyter Notebook implementation | [`shop_solution_original.ipynb`](shop_solution_original.ipynb) |
| **Assignment Brief (Part 1)** | Problem statement aur F1 benchmark (> 0.55) ka screenshot | [`Day_31_Assignment_Part1.jpeg`](assets/Day_31_Assignment_Part1.jpeg) |
| **Assignment Feature Schema (Part 2)** | Dataset ke attributes aur schema explanation ka screenshot | [`Day_31_Assignment_Part2.jpeg`](assets/Day_31_Assignment_Part2.jpeg) |

---

### 🗺️ Submodules aur Topics ka Index

| Submodule | Topic Title | Core Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **28.01** | Decision Trees ka Introduction aur Partitioning | Inductive bias, axis-aligned hyperplanes, tree anatomy (root, internal, leaf), white-box IF-THEN rules | [Notes](Notes_28.01/README_HINGLISH.md) \| [PDF](Notes_28.01/notes.pdf) \| [Notebook](Notes_28.01/lecture_28_01.ipynb) |
| **28.02** | Decision Tree Classifier aur Hunt's Algorithm | Hunt's greedy recursive algorithm, continuous midpoint thresholds, terminal leaves par majority voting | [Notes](Notes_28.02/README_HINGLISH.md) \| [PDF](Notes_28.02/notes.pdf) \| [Notebook](Notes_28.02/lecture_28_02.ipynb) |
| **28.03** | Entropy as an Impurity Metric — Shannon Theory | Shannon entropy H(S) = -sum(p_k log2 p_k), bits of surprise, concavity, pure vs mixed node bounds | [Notes](Notes_28.03/README_HINGLISH.md) \| [PDF](Notes_28.03/notes.pdf) \| [Notebook](Notes_28.03/lecture_28_03.ipynb) |
| **28.04** | Gini Impurity — Formulation aur Mechanics | Misclassification probability G(S) = 1 - sum(p_k^2), binary curve 2p(1-p), high computational speed | [Notes](Notes_28.04/README_HINGLISH.md) \| [PDF](Notes_28.04/notes.pdf) \| [Notebook](Notes_28.04/lecture_28_04.ipynb) |
| **28.05** | Entropy vs Gini Impurity — Mathematical Comparison | Taylor series approximation link, 0.5*H(p) vs G(p) curve alignment, 98%+ split selection agreement | [Notes](Notes_28.05/README_HINGLISH.md) \| [PDF](Notes_28.05/notes.pdf) \| [Notebook](Notes_28.05/lecture_28_05.ipynb) |
| **28.06** | Information Gain aur Split Selection Mechanics | Weighted child impurity reduction, mutual information, C4.5 SplitInfo aur Gain Ratio regularization | [Notes](Notes_28.06/README_HINGLISH.md) \| [PDF](Notes_28.06/notes.pdf) \| [Notebook](Notes_28.06/lecture_28_06.ipynb) |
| **28.07** | Pruning Decision Trees — Overfitting aur Generalization | Unconstrained tree overfitting (leaf size = 1), bias-variance tradeoff, pre-pruning vs post-pruning | [Notes](Notes_28.07/README_HINGLISH.md) \| [PDF](Notes_28.07/notes.pdf) \| [Notebook](Notes_28.07/lecture_28_07.ipynb) |
| **28.08** | Common Pruning Rules aur Hyperparameter Tuning | max_depth, min_samples_split, min_samples_leaf, max_leaf_nodes, aur min_impurity_decrease | [Notes](Notes_28.08/README_HINGLISH.md) \| [PDF](Notes_28.08/notes.pdf) \| [Notebook](Notes_28.08/lecture_28_08.ipynb) |
| **28.09** | Decision Tree Classifier Implementation (Scikit-Learn) | DecisionTreeClassifier API, class_weight='balanced', tree_ attributes inspection, plot_tree visualization | [Notes](Notes_28.09/README_HINGLISH.md) \| [PDF](Notes_28.09/notes.pdf) \| [Notebook](Notes_28.09/lecture_28_09.ipynb) |
| **28.10** | Pre-Pruning Implementation aur Regularization | GridSearchCV tuning (max_depth & min_samples_leaf), validation curve, generalization gap shrinkage | [Notes](Notes_28.10/README_HINGLISH.md) \| [PDF](Notes_28.10/notes.pdf) \| [Notebook](Notes_28.10/lecture_28_10.ipynb) |
| **28.11** | Post-Pruning Implementation — Minimal Cost-Complexity | Minimal cost-complexity R_alpha(T) = R(T) + alpha|T|, effective ccp_alphas path traversal, CV tuning | [Notes](Notes_28.11/README_HINGLISH.md) \| [PDF](Notes_28.11/notes.pdf) \| [Notebook](Notes_28.11/lecture_28_11.ipynb) |
| **28.12** | Decision Tree Regressor — Continuous Partitioning | Continuous target y in R, disjoint orthogonal regions R_m, regional sample mean c_m = y_bar prediction | [Notes](Notes_28.12/README_HINGLISH.md) \| [PDF](Notes_28.12/notes.pdf) \| [Notebook](Notes_28.12/lecture_28_12.ipynb) |
| **28.13** | Variance Reduction as Impurity Metric for Regressors | Node MSE impurity, variance reduction split selection, MAE median criteria for outlier robustness | [Notes](Notes_28.13/README_HINGLISH.md) \| [PDF](Notes_28.13/notes.pdf) \| [Notebook](Notes_28.13/lecture_28_13.ipynb) |
| **28.14** | Decision Tree Regressor Implementation (Scikit-Learn) | DecisionTreeRegressor API, non-linear curve fitting, regression evaluation metrics (MSE, RMSE, R^2) | [Notes](Notes_28.14/README_HINGLISH.md) \| [PDF](Notes_28.14/notes.pdf) \| [Notebook](Notes_28.14/lecture_28_14.ipynb) |

---

### 🧪 Practice Problems aur Systems Engineering Suite

Decision tree algorithms aur regularization mechanics par based industrial problem set:
- **Questions Folder**: [`Practice_Problems/Questions/README_HINGLISH.md`](Practice_Problems/Questions/README_HINGLISH.md) \| [`questions.pdf`](Practice_Problems/Questions/questions.pdf) \| [`questions.ipynb`](Practice_Problems/Questions/questions.ipynb)
- **Solutions Folder**: [`Practice_Problems/Solutions/README_HINGLISH.md`](Practice_Problems/Solutions/README_HINGLISH.md) \| [`solutions.pdf`](Practice_Problems/Solutions/solutions.pdf) \| [`solutions.ipynb`](Practice_Problems/Solutions/solutions.ipynb)

#### 8 Core Algorithmic Problems:
1. `ShannonEntropyCalculator`: Pure NumPy Shannon entropy calculation ($0 \log_2 0 \equiv 0$ safety ke sath).
2. `GiniImpurityEvaluator`: Pure NumPy Gini impurity aur weighted child split evaluation.
3. `ContinuousSplitFinder`: Continuous features par midpoint threshold search maximizing Gini gain.
4. `GainRatioOptimizer`: High-cardinality fragmentation ko penalize karne wala C4.5 SplitInfo metric.
5. `VarianceReductionSplitter`: Continuous regression trees mein sample variance reduction split selection.
6. `CostComplexityPruningPathAnalyzer`: Effective alphas sequence aur monotonic leaf shrinkage analysis.
7. `PrePruningGridSearchOptimizer`: Stratified cross-validation se depth aur leaf hyperparameters tune karna.
8. `ShopSmartPurchasePredictorPipeline`: ColumnTransformer + Pruned DecisionTree pipeline (F1 > 0.55 benchmark).

#### 🔬 Systems Engineering Case Studies (300 DPI Graphics):
- **Case Study 1**: Impurity Metrics Comparison Curve ($H(p)$ vs $G(p)$ vs Misclassification Error) ([Diagram](Practice_Problems/Solutions/case1_entropy_vs_gini_impurity_curve.png))
- **Case Study 2**: Minimal Cost-Complexity Post-Pruning Path (`ccp_alpha`) on ShopSmart Data ([Diagram](Practice_Problems/Solutions/case2_cost_complexity_pruning_ccp_alpha_path.png))
- **Case Study 3**: Decision Tree Depth Overfitting Frontier aur Bias-Variance Decomposition ([Diagram](Practice_Problems/Solutions/case3_decision_tree_depth_overfitting_frontier.png))
