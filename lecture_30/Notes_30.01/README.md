# Notes_30.01: Gradient Boosting Regressor Intuition
## Supervised Machine Learning (Part 6) — Boosting & Advanced Ensembles

### 📌 Conceptual Summary
Mathematical formulation of Gradient Tree Boosting. Gradient Boosting optimizes an arbitrary differentiable loss function $L(y, F(x))$ by iteratively fitting base regression trees to negative gradients (pseudo-residuals) $r_{im} = -\left[\frac{\partial L(y_i, F(x_i))}{\partial F(x_i)}\right]_{F=F_{m-1}}$. For mean squared error loss $L(y, F) = \frac{1}{2}(y - F)^2$, the pseudo-residual simplifies directly to the ordinary arithmetic residual $r_{im} = y_i - F_{m-1}(x_i)$. Predictions are sequentially accumulated via shrinkage learning rate $\nu$: $F_m(x) = F_{m-1}(x) + \nu h_m(x)$.

---

### 🛠️ Key Mathematical Formulations
- **Ensemble Hypothesis**: Sequential accumulation or weighted meta-combination.
- **Regularization**: Shrinkage learning rate, tree depth constraints, and out-of-fold validation.

---

### 💻 Code Artifacts & Reference Implementations
- Master Notebook: [`lecture_30.ipynb`](../novagen.ipynb)
- Interactive Heterogeneous Suite: [`ensemble_heterogenous.ipynb`](../ensemble_heterogenous.ipynb)
