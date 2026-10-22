# Notes_30.12: Stacking Classifier Logic — Meta-Learning
## Supervised Machine Learning (Part 6) — Boosting & Advanced Ensembles

### 📌 Conceptual Summary
Stacked Generalization (David Wolpert). Level-0 base models generate predictions on the training data. A Level-1 meta-model (typically Logistic Regression or Ridge) learns how to optimally combine these predictions. Crucial requirement: Level-0 predictions must be generated using Out-of-Fold (OOF) cross-validation to prevent target leakage into the meta-model.

---

### 🛠️ Key Mathematical Formulations
- **Ensemble Hypothesis**: Sequential accumulation or weighted meta-combination.
- **Regularization**: Shrinkage learning rate, tree depth constraints, and out-of-fold validation.

---

### 💻 Code Artifacts & Reference Implementations
- Master Notebook: [`lecture_30.ipynb`](../novagen.ipynb)
- Interactive Heterogeneous Suite: [`ensemble_heterogenous.ipynb`](../ensemble_heterogenous.ipynb)
