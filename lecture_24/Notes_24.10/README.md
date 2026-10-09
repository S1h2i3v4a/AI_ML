# Module 24.10: Lasso Regression Implementation & Shrinkage Paths

## 1. End-to-End Implementation Workflow

Applying regularized regression in practice requires three mandatory preprocessing prerequisites:

```
+---------------------------------------------------------------------------------------+
| 1. Categorical Dummy Encoding: pd.get_dummies(df, drop_first=True)                    |
| 2. Train-Test Split: 80% Training, 20% Unseen Testing Data                           |
| 3. Mandatory Standardization: StandardScaler() fitted STRICTLY on training split     |
+---------------------------------------------------------------------------------------+
```

### Why Feature Scaling is Mandatory for Regularization:
Regularization applies a uniform penalty $\lambda |w_j|$ across all parameters.
- If Feature $A$ is measured in dollars ($\$10^6$) and Feature $B$ in age ($10^1$), the unscaled weight $w_A$ is naturally tiny while $w_B$ is large.
- The regularizer would penalize $w_B$ severely simply because of its arbitrary physical unit!
- Standardization brings all features to mean 0 and variance 1, ensuring fair, scale-invariant shrinkage.

---

## 2. Tracing the Regularization Path

A **regularization path** plots parameter weights $w_j$ on the vertical axis against the regularization strength $\lambda$ (or $\log(\alpha)$) on the horizontal axis:
- As $\lambda \to 0$: Weights equal the unconstrained Ordinary Least Squares solution.
- As $\lambda \to \infty$: All weights are progressively forced to zero ($w_j = 0$).
- The order in which coefficients hit zero reveals their relative empirical importance.
