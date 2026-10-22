# Notes_30.10: Voting Classifier Logic — Hard vs Soft Voting
## Supervised Machine Learning (Part 6) — Boosting & Advanced Ensembles

### 📌 Conceptual Summary
Aggregation logic: Hard Voting takes a simple majority vote among base classifiers $\hat{y} = \text{mode}(C_1(x), \dots, C_M(x))$. Soft Voting computes the weighted average of predicted class probabilities $\hat{p}(k) = \sum_{m=1}^M w_m P_m(y=k|x)$ and chooses the argmax. Soft voting consistently outperforms hard voting because it incorporates the confidence of each base classifier.

---

### 🛠️ Key Mathematical Formulations
- **Ensemble Hypothesis**: Sequential accumulation or weighted meta-combination.
- **Regularization**: Shrinkage learning rate, tree depth constraints, and out-of-fold validation.

---

### 💻 Code Artifacts & Reference Implementations
- Master Notebook: [`lecture_30.ipynb`](../novagen.ipynb)
- Interactive Heterogeneous Suite: [`ensemble_heterogenous.ipynb`](../ensemble_heterogenous.ipynb)
