# Notes_30.06: AdaBoost Implementation in Scikit-Learn
## Supervised Machine Learning (Part 6) — Boosting & Advanced Ensembles

### 📌 Conceptual Summary
Implementation using `AdaBoostClassifier(estimator=DecisionTreeClassifier(max_depth=1), n_estimators=50, learning_rate=1.0)`. Analyzing stump decision boundaries, stagewise error curves, and sensitivity to noisy outlier points due to exponential weight amplification.

---

### 🛠️ Key Mathematical Formulations
- **Ensemble Hypothesis**: Sequential accumulation or weighted meta-combination.
- **Regularization**: Shrinkage learning rate, tree depth constraints, and out-of-fold validation.

---

### 💻 Code Artifacts & Reference Implementations
- Master Notebook: [`lecture_30.ipynb`](../novagen.ipynb)
- Interactive Heterogeneous Suite: [`ensemble_heterogenous.ipynb`](../ensemble_heterogenous.ipynb)
