# Notes_30.05: AdaBoost Classifier — Intuition & Mathematics
## Supervised Machine Learning (Part 6) — Boosting & Advanced Ensembles

### 📌 Conceptual Summary
Yoav Freund & Robert Schapire's Adaptive Boosting (AdaBoost.M1). Starts with uniform sample weights $w_i^{(1)} = \frac{1}{N}$. At each iteration $m$, train a weak learner (decision stump $h_m(x)$ with depth 1). Compute weighted error $\epsilon_m = \sum_{y_i \neq h_m(x_i)} w_i^{(m)}$. Calculate estimator weight $\alpha_m = \frac{1}{2} \ln\left(\frac{1 - \epsilon_m}{\epsilon_m}\right)$. Update sample weights: $w_i^{(m+1)} = w_i^{(m)} \exp(-\alpha_m y_i h_m(x_i))$ and re-normalize. Misclassified samples receive increased weights, forcing subsequent stumps to focus on difficult instances.

---

### 🛠️ Key Mathematical Formulations
- **Ensemble Hypothesis**: Sequential accumulation or weighted meta-combination.
- **Regularization**: Shrinkage learning rate, tree depth constraints, and out-of-fold validation.

---

### 💻 Code Artifacts & Reference Implementations
- Master Notebook: [`lecture_30.ipynb`](../novagen.ipynb)
- Interactive Heterogeneous Suite: [`ensemble_heterogenous.ipynb`](../ensemble_heterogenous.ipynb)
