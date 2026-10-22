# Notes_30.13: What is Blending? — Architecture & Trade-offs
## Supervised Machine Learning (Part 6) — Boosting & Advanced Ensembles

### 📌 Conceptual Summary
Blending is a simplified variant of Stacking. Instead of K-fold cross-validation, the training set is split once into a training subset (e.g. 70%) and a hold-out blend subset (e.g. 30%). Base models are fitted on the 70% set and generate predictions on the 30% blend set. The meta-model is trained on these blend predictions. Blending is faster and simpler but discards data compared to full K-fold Stacking.

---

### 🛠️ Key Mathematical Formulations
- **Ensemble Hypothesis**: Sequential accumulation or weighted meta-combination.
- **Regularization**: Shrinkage learning rate, tree depth constraints, and out-of-fold validation.

---

### 💻 Code Artifacts & Reference Implementations
- Master Notebook: [`lecture_30.ipynb`](../novagen.ipynb)
- Interactive Heterogeneous Suite: [`ensemble_heterogenous.ipynb`](../ensemble_heterogenous.ipynb)
