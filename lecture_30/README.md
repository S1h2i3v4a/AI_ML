# 🚀 Lecture 30: Supervised Machine Learning (Part 6) — Boosting & Advanced Ensembles
## Gradient Boosting, AdaBoost, XGBoost, Voting, Stacking, Blending & NovaGen Lab Project

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.9.1-orange.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Ensemble-red.svg)](https://xgboost.readthedocs.io/)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#)

🌐 **Language Navigation:** **English** | [हिंदी / Hinglish](README_HINGLISH.md)

Welcome to **Lecture 30: Supervised Machine Learning (Part 6)**, a comprehensive masterclass covering sequential boosting and heterogeneous ensemble architectures. This module covers Gradient Boosting for regression and classification (pseudo-residuals, shrinkage learning rate), AdaBoost (adaptive sample reweighting and decision stumps), modern gradient boosting algorithms (XGBoost second-order Taylor expansion), Homogeneous vs Heterogeneous ensembles, Voting Classifiers (Hard vs Soft Voting), Stacking (Out-of-Fold meta-learning), Blending (hold-out validation split), and the complete industrial **NovaGen Research Labs Healthcare Risk Project** (9,549 patient records, optimizing for high clinical Recall > 94%).

---

### 📂 Course Assets & Reference Files

| Asset Name | Description | Resource Link |
| :--- | :--- | :--- |
| **Syllabus Overview** | Official lecture visual index and video breakdown | [`00_Day_33_Contents.jpeg`](00_Day_33_Contents.jpeg) \| [`assets/Topics.jpg`](assets/Topics.jpg) |
| **NovaGen Clinical Dataset** | 9,549 patient records across 22 physiological & lifestyle indicators | [`novagen_dataset.csv`](novagen_dataset.csv) |
| **Official NovaGen Notebook** | Teacher baseline notebook evaluating LR, KNN, RF, GB, and Voting | [`novagen.ipynb`](novagen.ipynb) |
| **Official Assignment PDF** | Official project brief and clinical sensitivity requirements | [`Supervised ML _Assignment5.pdf`](assets/Supervised%20ML%20_Assignment5.pdf) |
| **Gradient Boosting Reference** | Reference implementation of GB Regressor and Classifier | [`gradient_boosting.ipynb`](gradient_boosting.ipynb) |
| **AdaBoost Reference** | Reference implementation of AdaBoost with decision stumps | [`adaboost.ipynb`](adaboost.ipynb) |
| **XGBoost Reference** | Reference implementation of XGBClassifier with parameter tuning | [`xgboost_classification.ipynb`](xgboost_classification.ipynb) |
| **Heterogeneous Ensemble Suite** | Reference implementation of Voting, Stacking, and Blending | [`ensemble_heterogenous.ipynb`](ensemble_heterogenous.ipynb) |

---

### 🗺️ Submodules & Topic Architecture Index

| Submodule | Topic Title | Core Engineering Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **30.01** | Gradient Boosting Regressor Intuition | Differentiable loss minimization, pseudo-residuals $r_{im} = -\partial L/\partial F$, shrinkage rate $\nu$ | [Notes](Notes_30.01/README.md) |
| **30.02** | Gradient Boosting Classifier Intuition | Log-odds space $F(x)$, binary cross-entropy probability residuals $y_i - p_i$, Newton-Raphson leaf updates | [Notes](Notes_30.02/README.md) |
| **30.03** | GB Regressor Implementation | `GradientBoostingRegressor`, `n_estimators`, `learning_rate`, `subsample` | [Notes](Notes_30.03/README.md) |
| **30.04** | GB Classifier Implementation | `GradientBoostingClassifier`, staged deviance curves, probability calibration | [Notes](Notes_30.04/README.md) |
| **30.05** | AdaBoost Intuition & Mathematics | Exponential loss, sample reweighting $w_i \exp(-\alpha_m y_i h_m)$, estimator weight $\alpha_m$, decision stumps | [Notes](Notes_30.05/README.md) |
| **30.06** | AdaBoost Classifier Implementation | `AdaBoostClassifier(estimator=DecisionTreeClassifier(max_depth=1))`, boundary evolution | [Notes](Notes_30.06/README.md) |
| **30.07** | Other Boosting Algorithms Taxonomy | XGBoost (2nd order Taylor), LightGBM (leaf-wise best-first), CatBoost (oblivious trees) | [Notes](Notes_30.07/README.md) |
| **30.08** | XGBoost Classification Implementation | `xgb.XGBClassifier`, Hessian & Gradient evaluation, regularization $\gamma, \lambda$ | [Notes](Notes_30.08/README.md) |
| **30.09** | Homogeneous vs Heterogeneous Ensembles | Single inductive bias (RF, GB) vs multi-model diversity (Voting, Stacking, Blending) | [Notes](Notes_30.09/README.md) |
| **30.10** | Voting Classifier Logic — Hard vs Soft | Plurality majority vote vs weighted probability averaging $\arg\max \sum w_m P_m(k)$ | [Notes](Notes_30.10/README.md) |
| **30.11** | Voting Classifier Implementation | `VotingClassifier(voting='soft')`, combining LR, KNN, and Decision Trees | [Notes](Notes_30.11/README.md) |
| **30.12** | Stacking Classifier Logic — Meta-Learning | Two-tier architecture: Level-0 base models, Level-1 meta-learner, Out-of-Fold cross-validation | [Notes](Notes_30.12/README.md) |
| **30.13** | What is Blending? Architecture & Trade-offs | Single hold-out validation set vs K-Fold cross-validation, computational latency vs data efficiency | [Notes](Notes_30.13/README.md) |
| **30.14** | Stacking Classifier Implementation | `StackingClassifier(final_estimator=LogisticRegression(), cv=5)`, multi-model meta-features | [Notes](Notes_30.14/README.md) |

---

### 🧪 Practice Problems & Systems Engineering Suite

A focused, industrial problem set featuring **exactly 3 comprehensive case studies** explained simply:
- **Practice Problems Overview**: [`Practice_Problems/README.md`](Practice_Problems/README.md) | [हिंदी / Hinglish](Practice_Problems/README_HINGLISH.md)
- **Questions Directory**: [`Practice_Problems/Questions/README.md`](Practice_Problems/Questions/README.md) | [`questions.ipynb`](Practice_Problems/Questions/questions.ipynb)
- **Solutions Directory**: [`Practice_Problems/Solutions/README.md`](Practice_Problems/Solutions/README.md) | [`solutions.ipynb`](Practice_Problems/Solutions/solutions.ipynb)

#### 🔬 3 Systems Engineering Case Studies (300 DPI Visualizations):
1. **Case Study 1**: NovaGen Clinical Triage Recall Benchmark ([Figure](Practice_Problems/Solutions/case1_novagen_model_recall_comparison.png))
2. **Case Study 2**: AdaBoost Adaptive Sample Reweighting Mechanics ([Figure](Practice_Problems/Solutions/case2_adaboost_stump_weighting_mechanism.png))
3. **Case Study 3**: Stacking vs Blending Architecture Comparison ([Figure](Practice_Problems/Solutions/case3_stacking_vs_blending_architecture.png))
