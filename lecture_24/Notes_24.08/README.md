# Module 24.08: Regularization — Lasso Regression (L1 Norm)

## 1. What is Regularization?

**Regularization** is an algorithmic technique designed to prevent overfitting by penalizing excessive model complexity. It modifies the loss function to discourage parameter weights from taking large, unstable values:

$$
\mathcal{L}_{\text{regularized}}(\mathbf{w}) = \mathcal{L}_{\text{data}}(\mathbf{w}) + \lambda \cdot \Omega(\mathbf{w})
$$

Where:
- $\mathcal{L}_{\text{data}}(\mathbf{w})$: Empirical loss on training data (e.g., Mean Squared Error).
- $\Omega(\mathbf{w})$: Model complexity penalty term.
- $\lambda \ge 0$ (often denoted as $\alpha$): Regularization hyperparameter governing the tradeoff between data fit and parameter shrinkage.

---

## 2. Mathematical Formulation of Lasso (Least Absolute Shrinkage and Selection Operator)

Lasso imposes an **L1 norm penalty** on the weight vector $\mathbf{w}$:

$$
J_{\text{Lasso}}(\mathbf{w}, b) = \frac{1}{2m} \sum_{i=1}^m \left( \hat{y}^{(i)} - y^{(i)} \right)^2 + \lambda \|\mathbf{w}\|_1
$$

Where the L1 norm is the sum of absolute parameter weights:

$$
\|\mathbf{w}\|_1 = \sum_{j=1}^p |w_j|
$$

> **Important Modeling Convention:** The intercept parameter $b$ is **never regularized**. Penalizing the intercept would unfairly force predictions toward zero regardless of the target variable's baseline level.

---

## 3. Geometric Intuition: Why Lasso Induces Sparsity (Feature Selection)

Lasso optimization can be formulated as an equivalent constrained optimization problem (via Karush-Kuhn-Tucker duality):

$$
\min_{\mathbf{w}} \frac{1}{2m} \|\mathbf{X} \mathbf{w} - \mathbf{y}\|_2^2 \quad \text{subject to} \quad \sum_{j=1}^p |w_j| \le C
$$

```
              w2 ^
                 |         / \
                 |        /   \  L1 Diamond Constraint: |w1| + |w2| <= C
                 |       /     \
                 |      /       \
   --------------+-----+---------+------> w1
                 |      \       /
                 |       \  *  /  <-- Corner contact point (w1 = 0, w2 = w*)
                 |        \   /
                 |         \ /
```

### The Geometry of Axis Corners:
1. In 2D parameter space, the constraint region $\|\mathbf{w}\|_1 \le C$ is a **diamond** (rhombus) with sharp corners positioned exactly on the coordinate axes ($w_1 = 0$ or $w_2 = 0$).
2. The elliptical contours of the quadratic MSE loss expand outwards from the unconstrained OLS minimum.
3. Due to the sharp geometric vertices of the diamond, the expanding ellipse will almost always make its first point of tangency **at a corner on the axis**.
4. Consequently, Lasso forces redundant or uninformative feature weights strictly to **zero** ($w_j = 0$).
5. **Key Advantage:** Lasso performs automatic **embedded feature selection**, producing sparse, highly interpretable models.
