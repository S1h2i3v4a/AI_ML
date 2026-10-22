# Notes_30.04: Gradient Boosting Classifier in Scikit-Learn
## Supervised Machine Learning (Part 6) — Boosting & Advanced Ensembles

### 📌 Conceptual Summary
Classification workflow using `GradientBoostingClassifier`. Demonstrates probability calibration via `predict_proba()`, monitoring stage-by-stage staged deviance via `staged_predict_proba()`, feature importances (Mean Decrease in Impurity), and early stopping to prevent overfitting.

---

### 🛠️ Key Mathematical Formulations
- **Ensemble Hypothesis**: Sequential accumulation or weighted meta-combination.
- **Regularization**: Shrinkage learning rate, tree depth constraints, and out-of-fold validation.

---

### 💻 Code Artifacts & Reference Implementations
- Master Notebook: [`lecture_30.ipynb`](../novagen.ipynb)
- Interactive Heterogeneous Suite: [`ensemble_heterogenous.ipynb`](../ensemble_heterogenous.ipynb)
