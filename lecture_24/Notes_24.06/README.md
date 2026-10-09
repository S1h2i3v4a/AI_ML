# Module 24.06: How to Fix Underfitting & Overfitting

## 1. The Engineering Balance: Bias-Variance Optimization

Machine learning practitioners must calibrate model capacity to find the sweet spot where total generalization error is minimized:

```
Error ^
      |      \                     /  Validation Error
      |       \                   /
      |        \     Optimal     /
      |         \    Capacity   /
      |          \      |      /
      |           \_____v_____/
      |            \         /
      |             \_______/_______ Training Error
      +------------------------------------------> Model Complexity
           Underfitting          Overfitting
           (High Bias)          (High Variance)
```

---

## 2. Concrete Strategies to Mitigate Underfitting (High Bias)

When a model suffers from underfitting ($\mathcal{L}_{\text{train}}$ is high):

| Action | Technical Implementation | Why it Works |
| :--- | :--- | :--- |
| **1. Increase Model Capacity** | Use non-linear models (Polynomial, Splines, Trees, Neural Nets) | Expands hypothesis space $\mathcal{H}$ |
| **2. Feature Engineering** | Add polynomial powers ($x^2, x^3$) and interaction terms ($x_1 x_2$) | Projects input into higher-dimensional linear separable space |
| **3. Decrease Regularization** | Reduce penalty $\lambda$ (decrease $\alpha$ in Lasso/Ridge) | Allows parameter weights $\mathbf{w}$ more freedom to fit data |
| **4. Train for Longer** | Increase iterations, tune learning rate $\alpha$ | Ensures optimizer reaches convergence minimum |

---

## 3. Concrete Strategies to Mitigate Overfitting (High Variance)

When a model suffers from overfitting ($\mathcal{L}_{\text{val}} \gg \mathcal{L}_{\text{train}}$):

| Action | Technical Implementation | Why it Works |
| :--- | :--- | :--- |
| **1. Apply Regularization** | Add L1 (Lasso) or L2 (Ridge) penalty to cost function | Constrains weight norms, preventing explosive coefficients |
| **2. Acquire More Data** | Data collection, data augmentation | Constrains variance; sample distribution converges to population |
| **3. Dimensionality Reduction** | Feature selection, PCA, drop noise columns | Eliminates spurious chance correlations in high dimensions |
| **4. Cross-Validation** | K-Fold cross validation, early stopping | Halts training before validation loss begins to diverge |
| **5. Simplify Model Architecture** | Reduce polynomial degree, prune decision trees | Restricts hypothesis complexity to match true signal complexity |
