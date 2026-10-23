# 🚀 Lecture 30: Supervised Machine Learning (Part 6) — Boosting & Advanced Ensembles
## Gradient Boosting, AdaBoost, XGBoost, Voting, Stacking, Blending & NovaGen Lab Project

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.9.1-orange.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Ensemble-red.svg)](https://xgboost.readthedocs.io/)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#)

🌐 **Language Navigation:** **English** | [हिंदी / Hinglish](README_HINGLISH.md)

Welcome to **Lecture 30: Supervised Machine Learning (Part 6)**, a comprehensive masterclass covering sequential boosting and heterogeneous ensemble architectures. This module covers Gradient Boosting for regression and classification (pseudo-residuals, shrinkage learning rate), AdaBoost (adaptive sample reweighting and decision stumps), modern gradient boosting algorithms (XGBoost second-order Taylor expansion, LightGBM, CatBoost), Homogeneous vs Heterogeneous ensembles, Voting Classifiers (Hard vs Soft Voting), Stacking (Out-of-Fold meta-learning), Blending (hold-out validation split), and the complete industrial **NovaGen Research Labs Healthcare Risk Project** (9,549 patient records, optimizing for high clinical Recall > 94%).

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
| **30.01** | Gradient Boosting Regressor Intuition | Differentiable loss minimization, pseudo-residuals r = y - y_hat, shrinkage rate eta, sequential residual tree fitting | [Notes](Notes_30.01/README.md) \| [PDF](Notes_30.01/notes.pdf) \| [Hinglish](Notes_30.01/README_HINGLISH.md) \| [Hinglish PDF](Notes_30.01/notes_hinglish.pdf) \| [Notebook](Notes_30.01/lecture_30_01.ipynb) |
| **30.02** | Gradient Boosting Classifier Intuition | Log-odds space F(x), logistic sigmoid probability residuals y_i - p_i, leaf output updates | [Notes](Notes_30.02/README.md) \| [PDF](Notes_30.02/notes.pdf) \| [Hinglish](Notes_30.02/README_HINGLISH.md) \| [Hinglish PDF](Notes_30.02/notes_hinglish.pdf) \| [Notebook](Notes_30.02/lecture_30_02.ipynb) |
| **30.03** | GB Regressor Implementation in Scikit-Learn | GradientBoostingRegressor, n_estimators, learning_rate, subsample, MSE and R2 evaluation | [Notes](Notes_30.03/README.md) \| [PDF](Notes_30.03/notes.pdf) \| [Hinglish](Notes_30.03/README_HINGLISH.md) \| [Hinglish PDF](Notes_30.03/notes_hinglish.pdf) \| [Notebook](Notes_30.03/lecture_30_03.ipynb) |
| **30.04** | GB Classifier Implementation in Scikit-Learn | GradientBoostingClassifier, loss='log_loss', precision, recall, feature importances | [Notes](Notes_30.04/README.md) \| [PDF](Notes_30.04/notes.pdf) \| [Hinglish](Notes_30.04/README_HINGLISH.md) \| [Hinglish PDF](Notes_30.04/notes_hinglish.pdf) \| [Notebook](Notes_30.04/lecture_30_04.ipynb) |
| **30.05** | AdaBoost Intuition & Mathematics | Exponential loss, sample reweighting w_i * exp(-alpha * y * h), stump voting power alpha, decision stumps | [Notes](Notes_30.05/README.md) \| [PDF](Notes_30.05/notes.pdf) \| [Hinglish](Notes_30.05/README_HINGLISH.md) \| [Hinglish PDF](Notes_30.05/notes_hinglish.pdf) \| [Notebook](Notes_30.05/lecture_30_05.ipynb) |
| **30.06** | AdaBoost Classifier Implementation | AdaBoostClassifier(estimator=DecisionTreeClassifier(max_depth=1)), staged score convergence | [Notes](Notes_30.06/README.md) \| [PDF](Notes_30.06/notes.pdf) \| [Hinglish](Notes_30.06/README_HINGLISH.md) \| [Hinglish PDF](Notes_30.06/notes_hinglish.pdf) \| [Notebook](Notes_30.06/lecture_30_06.ipynb) |
| **30.07** | Other Boosting Algorithms Taxonomy | XGBoost (2nd order Taylor), LightGBM (histogram binning, leaf-wise), CatBoost (oblivious trees) | [Notes](Notes_30.07/README.md) \| [PDF](Notes_30.07/notes.pdf) \| [Hinglish](Notes_30.07/README_HINGLISH.md) \| [Hinglish PDF](Notes_30.07/notes_hinglish.pdf) \| [Notebook](Notes_30.07/lecture_30_07.ipynb) |
| **30.08** | XGBoost Classification Implementation | xgb.XGBClassifier, Hessian & Gradient evaluation, regularization gamma, lambda, colsample_bytree | [Notes](Notes_30.08/README.md) \| [PDF](Notes_30.08/notes.pdf) \| [Hinglish](Notes_30.08/README_HINGLISH.md) \| [Hinglish PDF](Notes_30.08/notes_hinglish.pdf) \| [Notebook](Notes_30.08/lecture_30_08.ipynb) |
| **30.09** | Homogeneous vs Heterogeneous Ensembles | Single inductive bias (RF, GB) vs multi-model diversity (Voting, Stacking, Blending) | [Notes](Notes_30.09/README.md) \| [PDF](Notes_30.09/notes.pdf) \| [Hinglish](Notes_30.09/README_HINGLISH.md) \| [Hinglish PDF](Notes_30.09/notes_hinglish.pdf) \| [Notebook](Notes_30.09/lecture_30_09.ipynb) |
| **30.10** | Voting Classifier Logic — Hard vs Soft | Plurality majority vote vs weighted probability averaging, probability calibration | [Notes](Notes_30.10/README.md) \| [PDF](Notes_30.10/notes.pdf) \| [Hinglish](Notes_30.10/README_HINGLISH.md) \| [Hinglish PDF](Notes_30.10/notes_hinglish.pdf) \| [Notebook](Notes_30.10/lecture_30_10.ipynb) |
| **30.11** | Voting Classifier & Regressor Implementation | VotingClassifier(voting='soft') and VotingRegressor, combining LR, KNN, Decision Tree, SVC | [Notes](Notes_30.11/README.md) \| [PDF](Notes_30.11/notes.pdf) \| [Hinglish](Notes_30.11/README_HINGLISH.md) \| [Hinglish PDF](Notes_30.11/notes_hinglish.pdf) \| [Notebook](Notes_30.11/lecture_30_11.ipynb) |
| **30.12** | Stacking Classifier Logic — Meta-Learning | Two-tier architecture: Level-0 base models, Level-1 meta-learner, Out-Of-Fold (OOF) CV split | [Notes](Notes_30.12/README.md) \| [PDF](Notes_30.12/notes.pdf) \| [Hinglish](Notes_30.12/README_HINGLISH.md) \| [Hinglish PDF](Notes_30.12/notes_hinglish.pdf) \| [Notebook](Notes_30.12/lecture_30_12.ipynb) |
| **30.13** | What is Blending? Architecture & Trade-offs | Single holdout validation set vs K-Fold cross-validation, computational latency vs data efficiency | [Notes](Notes_30.13/README.md) \| [PDF](Notes_30.13/notes.pdf) \| [Hinglish](Notes_30.13/README_HINGLISH.md) \| [Hinglish PDF](Notes_30.13/notes_hinglish.pdf) \| [Notebook](Notes_30.13/lecture_30_13.ipynb) |
| **30.14** | Stacking Classifier Implementation | StackingClassifier(final_estimator=LogisticRegression(), cv=5), multi-model meta-features | [Notes](Notes_30.14/README.md) \| [PDF](Notes_30.14/notes.pdf) \| [Hinglish](Notes_30.14/README_HINGLISH.md) \| [Hinglish PDF](Notes_30.14/notes_hinglish.pdf) \| [Notebook](Notes_30.14/lecture_30_14.ipynb) |

---

### 🧪 Practice Problems & Systems Engineering Suite

A focused, industrial problem set featuring **exactly 3 comprehensive case studies** derived strictly from Lecture 30:
- **Practice Problems Overview**: [`Practice_Problems/README.md`](Practice_Problems/README.md) | [हिंदी / Hinglish](Practice_Problems/README_HINGLISH.md)
- **Questions Directory**: [`Practice_Problems/Questions/README.md`](Practice_Problems/Questions/README.md) | [PDF](Practice_Problems/Questions/questions.pdf) | [`questions.ipynb`](Practice_Problems/Questions/questions.ipynb)
- **Solutions Directory**: [`Practice_Problems/Solutions/README.md`](Practice_Problems/Solutions/README.md) | [PDF](Practice_Problems/Solutions/solutions.pdf) | [`solutions.ipynb`](Practice_Problems/Solutions/solutions.ipynb)

#### 🔬 3 Systems Engineering Case Studies (300 DPI Visualizations):
1. **Case Study 1**: NovaGen Clinical Triage Recall Benchmark ([Figure](Practice_Problems/Solutions/case1_novagen_model_recall_comparison.png))
2. **Case Study 2**: AdaBoost Adaptive Sample Reweighting Mechanics ([Figure](Practice_Problems/Solutions/case2_adaboost_stump_weighting_mechanism.png))
3. **Case Study 3**: Stacking vs Blending Multi-Tier Architecture Comparison ([Figure](Practice_Problems/Solutions/case3_stacking_vs_blending_architecture.png))
