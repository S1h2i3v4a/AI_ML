# Module 24.09: Regularization — Ridge Regression (L2 Norm)

## 1. Mathematical Formulation of Ridge Regression (Tikhonov Regularization)

Ridge Regression penalizes the **squared Euclidean norm (L2 norm)** of the model weights:

$$
J_{\text{Ridge}}(\mathbf{w}, b) = \frac{1}{2m} \sum_{i=1}^m \left( \hat{y}^{(i)} - y^{(i)} \right)^2 + \frac{\lambda}{2} \|\mathbf{w}\|_2^2
$$

Where:

$$
\|\mathbf{w}\|_2^2 = \sum_{j=1}^p w_j^2 = \mathbf{w}^T \mathbf{w}
$$

The factor of $\frac{1}{2}$ cancels out the exponent 2 during differentiation.

---

## 2. Analytical Closed-Form Solution: The Ridge Normal Equation

Unlike Lasso (whose L1 absolute value has non-differentiable cusps requiring numerical coordinate descent), Ridge Regression is continuously differentiable everywhere.
Differentiating $J_{\text{Ridge}}(\mathbf{w})$ with respect to $\mathbf{w}$:

$$
\nabla_{\mathbf{w}} J_{\text{Ridge}} = \frac{1}{m} \mathbf{X}^T (\mathbf{X} \mathbf{w} - \mathbf{y}) + \lambda \mathbf{w} = 0
$$

Solving for $\mathbf{w}$:

$$
(\mathbf{X}^T \mathbf{X} + m \lambda \mathbf{I}) \mathbf{w} = \mathbf{X}^T \mathbf{y}
$$

Standardizing the formulation (absorbing $m$ into $\lambda$):

$$
\mathbf{w}_{\text{Ridge}}^* = (\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^T \mathbf{y}
$$

### Mathematical Salvation from Multicollinearity:
In standard OLS, if features are multicollinear, $\mathbf{X}^T \mathbf{X}$ is singular and non-invertible.
In Ridge Regression:
- We add $\lambda \mathbf{I}$ (where $\lambda > 0$) along the principal diagonal.
- All eigenvalues $\sigma_i$ are shifted by $+\lambda$: $\sigma_i(\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I}) = \sigma_i + \lambda > 0$.
- **The matrix is guaranteed to be strictly positive definite and invertible!** Ridge always has a unique, stable analytical solution.

---

## 3. Geometric Intuition: Smooth Shrinkage vs. Sparsity

In parameter space, the constraint region $\|\mathbf{w}\|_2^2 \le C$ forms a smooth **circle** (or hypersphere in higher dimensions):

```
              w2 ^
                 |         _--_
                 |       /      \   L2 Circular Constraint: w1^2 + w2^2 <= C
                 |      |        |
                 |       \      /
   --------------+--------^----+---------> w1
                 |         \--/
                 |           *  <-- Smooth tangency point (w1 != 0, w2 != 0)
```

Because the boundary of a circle is completely smooth with no sharp corners, the loss contour makes contact at an arbitrary point along the curve:
- Weights are shrunk smoothly toward zero ($w_j \to 0$), but are **almost never set strictly to zero**.
- Ridge retains all features, reducing their variance while preserving their informational contribution.
