# 🌲 Lecture 28: Supervised Machine Learning (Part 4) — Decision Trees
## Mathematical Foundations, Algorithmic Splitting & Production Pruning

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.9.1-orange.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#)

🌐 **Language Navigation:** **English** | [हिंदी / Hinglish](README_HINGLISH.md)

Welcome to **Lecture 28: Supervised Machine Learning (Part 4) — Decision Trees**, a deep first-principles masterclass covering non-linear hierarchical decision trees for classification and regression. This module covers recursive binary splitting (Hunt's algorithm / CART), information-theoretic impurity metrics (Shannon Entropy, Gini Impurity), Taylor series mathematical equivalence, Information Gain and C4.5 Gain Ratio, the pathology of unconstrained tree memorization, structural pre-pruning (`max_depth`, `min_samples_leaf`), Leo Breiman's Minimal Cost-Complexity post-pruning (`ccp_alpha`), Decision Tree Regressors with Variance Reduction, and the end-to-end **ShopSmart E-Commerce Purchase Prediction Project** (12,330 sessions, meeting F1 benchmark > 0.55).

---

### 📂 Course Assets & Reference Files

| Asset Name | Description | Resource Link |
| :--- | :--- | :--- |
| **Syllabus Overview** | Official lecture visual index and video duration breakdown | [`00_Day_31_Contents.jpeg`](00_Day_31_Contents.jpeg) |
| **ShopSmart E-Commerce Dataset** | 12,330 visitor clickstream records across 18 behavioral features | [`shop_smart_ecommerce.csv`](shop_smart_ecommerce.csv) |
| **Official Solution Notebook** | Original reference implementation with EDA and hyperparameter grid search | [`shop_solution_original.ipynb`](shop_solution_original.ipynb) |
| **Assignment Brief (Part 1)** | Official project description, business context & F1 benchmark (> 0.55) | [`Day_31_Assignment_Part1.jpeg`](assets/Day_31_Assignment_Part1.jpeg) |
| **Assignment Feature Schema (Part 2)** | Official attribute dictionary and descriptions screenshot | [`Day_31_Assignment_Part2.jpeg`](assets/Day_31_Assignment_Part2.jpeg) |

---

### 🗺️ Submodules & Topic Architecture Index

| Submodule | Topic Title | Core Engineering Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **28.01** | Introduction to Decision Trees & Non-Linear Partitioning | Inductive bias, axis-aligned hyperplanes, tree anatomy (root, internal, leaf), white-box IF-THEN rules | [Notes](Notes_28.01/README.md) \| [PDF](Notes_28.01/notes.pdf) \| [Notebook](Notes_28.01/lecture_28_01.ipynb) |
| **28.02** | Decision Tree Classifier & Recursive Binary Splitting | Hunt's greedy algorithm, continuous midpoint thresholding, plurality majority voting at terminal leaves | [Notes](Notes_28.02/README.md) \| [PDF](Notes_28.02/notes.pdf) \| [Notebook](Notes_28.02/lecture_28_02.ipynb) |
| **28.03** | Entropy as an Impurity Metric — Shannon Information Theory | Shannon entropy H(S) = -sum(p_k log2 p_k), bits of surprise, concavity, pure vs mixed node bounds | [Notes](Notes_28.03/README.md) \| [PDF](Notes_28.03/notes.pdf) \| [Notebook](Notes_28.03/lecture_28_03.ipynb) |
| **28.04** | Gini Impurity — Formulation & Mathematical Mechanics | Probability of misclassification G(S) = 1 - sum(p_k^2), binary curve 2p(1-p), computational efficiency | [Notes](Notes_28.04/README.md) \| [PDF](Notes_28.04/notes.pdf) \| [Notebook](Notes_28.04/lecture_28_04.ipynb) |
| **28.05** | Entropy vs Gini Impurity — Comparison & Invariants | Taylor series approximation link, 0.5*H(p) vs G(p) alignment, 98%+ split selection concordance | [Notes](Notes_28.05/README.md) \| [PDF](Notes_28.05/notes.pdf) \| [Notebook](Notes_28.05/lecture_28_05.ipynb) |
| **28.06** | Information Gain & Split Selection Mechanics | Weighted child impurity reduction, mutual information, C4.5 SplitInfo and Gain Ratio regularizer | [Notes](Notes_28.06/README.md) \| [PDF](Notes_28.06/notes.pdf) \| [Notebook](Notes_28.06/lecture_28_06.ipynb) |
| **28.07** | Pruning Decision Trees — Overfitting & Generalization | Why unconstrained trees overfit (leaf size = 1), bias-variance tradeoff, pre-pruning vs post-pruning | [Notes](Notes_28.07/README.md) \| [PDF](Notes_28.07/notes.pdf) \| [Notebook](Notes_28.07/lecture_28_07.ipynb) |
| **28.08** | Common Pruning Rules & Hyperparameter Regularization | max_depth, min_samples_split, min_samples_leaf, max_leaf_nodes, and min_impurity_decrease | [Notes](Notes_28.08/README.md) \| [PDF](Notes_28.08/notes.pdf) \| [Notebook](Notes_28.08/lecture_28_08.ipynb) |
| **28.09** | Decision Tree Classifier Implementation in Scikit-Learn | DecisionTreeClassifier API, class_weight='balanced', inspecting tree_ attributes, export_text & plot_tree | [Notes](Notes_28.09/README.md) \| [PDF](Notes_28.09/notes.pdf) \| [Notebook](Notes_28.09/lecture_28_09.ipynb) |
| **28.10** | Pre-Pruning Implementation & Regularization Dynamics | GridSearchCV tuning across max_depth & min_samples_leaf, validation curve, closing generalization gap | [Notes](Notes_28.10/README.md) \| [PDF](Notes_28.10/notes.pdf) \| [Notebook](Notes_28.10/lecture_28_10.ipynb) |
| **28.11** | Post-Pruning Implementation — Minimal Cost-Complexity | Minimal cost-complexity criterion R_alpha(T) = R(T) + alpha|T|, effective ccp_alphas path, CV tuning | [Notes](Notes_28.11/README.md) \| [PDF](Notes_28.11/notes.pdf) \| [Notebook](Notes_28.11/lecture_28_11.ipynb) |
| **28.12** | Decision Tree Regressor — Continuous Partitioning | Continuous response y in R, disjoint regions R_m, optimal constant prediction c_m = sample mean | [Notes](Notes_28.12/README.md) \| [PDF](Notes_28.12/notes.pdf) \| [Notebook](Notes_28.12/lecture_28_12.ipynb) |
| **28.13** | Variance Reduction as Impurity Metric for Regressors | Node MSE impurity, variance reduction split selection, MAE median criteria for outlier robustness | [Notes](Notes_28.13/README.md) \| [PDF](Notes_28.13/notes.pdf) \| [Notebook](Notes_28.13/lecture_28_13.ipynb) |
| **28.14** | Decision Tree Regressor Implementation in Scikit-Learn | DecisionTreeRegressor API, non-linear function fitting, evaluation metrics (MSE, RMSE, R^2 score) | [Notes](Notes_28.14/README.md) \| [PDF](Notes_28.14/notes.pdf) \| [Notebook](Notes_28.14/lecture_28_14.ipynb) |

---

### 🧪 Practice Problems & Systems Engineering Suite

A comprehensive industrial problem set designed to test first-principles decision tree algorithms and regularization:
- **Questions Directory**: [`Practice_Problems/Questions/README.md`](Practice_Problems/Questions/README.md) \| [`questions.pdf`](Practice_Problems/Questions/questions.pdf) \| [`questions.ipynb`](Practice_Problems/Questions/questions.ipynb)
- **Solutions Directory**: [`Practice_Problems/Solutions/README.md`](Practice_Problems/Solutions/README.md) \| [`solutions.pdf`](Practice_Problems/Solutions/solutions.pdf) \| [`solutions.ipynb`](Practice_Problems/Solutions/solutions.ipynb)

#### Core Algorithmic Problems:
1. `ShannonEntropyCalculator`: Pure NumPy multi-class entropy calculation with $0 \log_2 0 \equiv 0$.
2. `GiniImpurityEvaluator`: Pure NumPy Gini impurity and weighted child split evaluation.
3. `ContinuousSplitFinder`: Midpoint threshold search on continuous features maximizing Gini gain.
4. `GainRatioOptimizer`: C4.5 Split Information penalty regularizing high-cardinality fragmentation.
5. `VarianceReductionSplitter`: Continuous regression tree split selection via sample variance drop.
6. `CostComplexityPruningPathAnalyzer`: Extracting effective alphas and analyzing monotonic leaf shrinkage.
7. `PrePruningGridSearchOptimizer`: Stratified cross-validation over depth and leaf constraints.
8. `ShopSmartPurchasePredictorPipeline`: End-to-end ColumnTransformer + DecisionTree exceeding F1 > 0.55.

#### 🔬 Systems Engineering Case Studies (300 DPI Visualizations):
- **Case Study 1**: Impurity Metrics Comparison Across Binary Probability ([Figure](Practice_Problems/Solutions/case1_entropy_vs_gini_impurity_curve.png))
- **Case Study 2**: Minimal Cost-Complexity Post-Pruning Path (`ccp_alpha`) on ShopSmart Data ([Figure](Practice_Problems/Solutions/case2_cost_complexity_pruning_ccp_alpha_path.png))
- **Case Study 3**: Decision Tree Depth vs Overfitting Frontier & Bias-Variance Decomposition ([Figure](Practice_Problems/Solutions/case3_decision_tree_depth_overfitting_frontier.png))
