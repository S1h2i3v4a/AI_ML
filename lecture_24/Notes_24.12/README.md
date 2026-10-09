# Module 24.12: ElasticNet Overview (Hybrid L1 + L2 Regularization)

## 1. Limitations of Pure Lasso and Pure Ridge

While Lasso and Ridge are foundational, both suffer from distinct operational limitations in high-dimensional real-world settings:

| Scenario | Lasso Limitation | Ridge Limitation |
| :--- | :--- | :--- |
| **Collinear Feature Groups** | Arbitrarily selects **one** feature from a correlated cluster and drops the rest to zero, discarding group signal. | Retains **all** features with shared small weights; cannot perform feature selection. |
| **High Dimensions ($p > m$)** | Can select at most $m$ features before saturating, regardless of how many true predictive signals exist. | Retains all $p$ features, risking overfitting. |

---

## 2. Mathematical Formulation of ElasticNet

Introduced by Zou and Hastie (2005), **ElasticNet** synthesizes both penalties into a single convex objective:

$$
J_{\text{ElasticNet}}(\mathbf{w}, b) = \frac{1}{2m} \sum_{i=1}^m \left( \hat{y}^{(i)} - y^{(i)} \right)^2 + \alpha \left[ \rho \|\mathbf{w}\|_1 + \frac{1 - \rho}{2} \|\mathbf{w}\|_2^2 \right]
$$

Where:
- $\alpha \ge 0$: Total regularization strength.
- $\rho \in [0, 1]$ (the `l1_ratio` parameter): Balances the mixture between L1 and L2 penalties:
  - $\rho = 1.0 \implies$ Pure Lasso Regression.
  - $\rho = 0.0 \implies$ Pure Ridge Regression.
  - $0 < \rho < 1.0 \implies$ Hybrid ElasticNet.

---

## 3. The "Grouping Effect" Advantage

ElasticNet provides the **grouping effect**:
- Strongly correlated features share similar regression coefficients and enter or leave the model together as a group (inherited from L2).
- Simultaneously, entire groups of irrelevant features are cleanly set to zero (inherited from L1).
- The geometry of ElasticNet's constraint contour combines the sharp vertices of the L1 diamond with the strictly convex curvature of the L2 sphere, eliminating non-unique solutions.
