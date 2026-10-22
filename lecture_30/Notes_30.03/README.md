# Notes_30.03: Gradient Boosting Regressor in Scikit-Learn
## Supervised Machine Learning (Part 6) — Boosting & Advanced Ensembles

### 📌 Conceptual Summary
Practical implementation using `GradientBoostingRegressor`. Hyperparameter regularizers: `n_estimators` (number of boosting stages), `learning_rate` (shrinkage parameter $\nu \in (0, 1]$), `max_depth` (typically 3 to 5 to keep base learners weak), `subsample` (stochastic gradient boosting row subsampling), and `loss='squared_error'` or `'absolute_error'`.

---

### 🛠️ Key Mathematical Formulations
- **Ensemble Hypothesis**: Sequential accumulation or weighted meta-combination.
- **Regularization**: Shrinkage learning rate, tree depth constraints, and out-of-fold validation.

---

### 💻 Code Artifacts & Reference Implementations
- Master Notebook: [`lecture_30.ipynb`](../novagen.ipynb)
- Interactive Heterogeneous Suite: [`ensemble_heterogenous.ipynb`](../ensemble_heterogenous.ipynb)
