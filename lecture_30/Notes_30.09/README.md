# Notes_30.09: Homogeneous vs Heterogeneous Ensembles
## Supervised Machine Learning (Part 6) — Boosting & Advanced Ensembles

### 📌 Conceptual Summary
Ensemble paradigm comparison: Homogeneous ensembles (Bagging, Random Forests, Gradient Boosting) use multiple instances of the same base algorithm (e.g. decision trees). Heterogeneous ensembles (Voting, Stacking, Blending) combine fundamentally diverse inductive biases (e.g. combining Linear Models, SVM, KNN, and Trees) to minimize correlated model errors.

---

### 🛠️ Key Mathematical Formulations
- **Ensemble Hypothesis**: Sequential accumulation or weighted meta-combination.
- **Regularization**: Shrinkage learning rate, tree depth constraints, and out-of-fold validation.

---

### 💻 Code Artifacts & Reference Implementations
- Master Notebook: [`lecture_30.ipynb`](../novagen.ipynb)
- Interactive Heterogeneous Suite: [`ensemble_heterogenous.ipynb`](../ensemble_heterogenous.ipynb)
