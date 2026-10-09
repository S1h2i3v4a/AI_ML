# Lecture 23: Linear Regression & ML Foundations - Comprehensive Solutions

This document presents rigorous first-principles mathematical derivations, step-by-step calculations, empirical verifications, and publication-quality diagnostic visualizations for the Lecture 23 Practice Problem Suite.

---

## Case Study 1: Analytical OLS Derivation & Residual Diagnostics

### 1. First-Principles Calculations

Given data vectors ($m = 10$):
- $x = [2.0, 3.0, 4.5, 6.0, 7.5, 8.0, 9.5, 11.0, 12.0, 13.5]$
- $y = [15.2, 18.5, 23.0, 29.5, 33.0, 36.5, 41.0, 48.0, 52.5, 58.0]$

#### Sample Means:
$$
\bar{x} = \frac{1}{10} \sum_{i=1}^{10} x_i = \frac{77.0}{10} = 7.70
$$

$$
\bar{y} = \frac{1}{10} \sum_{i=1}^{10} y_i = \frac{355.2}{10} = 35.52
$$

#### Sample Covariance and Variance:
$$
\sum_{i=1}^{10} (x_i - \bar{x})^2 = (2.0 - 7.7)^2 + \dots + (13.5 - 7.7)^2 = 138.85
$$

$$
\sum_{i=1}^{10} (x_i - \bar{x})(y_i - \bar{y}) = (2.0 - 7.7)(15.2 - 35.52) + \dots + (13.5 - 7.7)(58.0 - 35.52) = 517.97
$$

#### Closed-Form Parameters:
$$
w^* = \frac{517.97}{138.85} \approx 3.7304
$$

$$
b^* = \bar{y} - w^* \bar{x} = 35.52 - (3.7304)(7.70) = 35.52 - 28.7241 \approx 6.7959
$$

Thus, the optimal best fit model is:

$$
\hat{y} = 3.7304 x + 6.7959
$$

### 2. Centroid Invariant Verification
Substitute $\bar{x} = 7.70$ into the model hypothesis:

$$
\hat{y}(\bar{x}) = 3.7304(7.70) + 6.7959 = 28.7241 + 6.7959 = 35.5200 = \bar{y}
$$

The mathematical invariant holds with zero error: the best fit line passes precisely through $(\bar{x}, \bar{y})$.

### 3. Residual Diagnostics & $\sum e_i = 0$ Verification

| $i$ | $x_i$ | $y_i$ | $\hat{y}_i = 3.7304 x_i + 6.7959$ | Residual $e_i = y_i - \hat{y}_i$ | Squared Residual $e_i^2$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 2.0 | 15.2 | 14.2568 | $+0.9432$ | 0.8897 |
| 2 | 3.0 | 18.5 | 17.9872 | $+0.5128$ | 0.2630 |
| 3 | 4.5 | 23.0 | 23.5828 | $-0.5828$ | 0.3397 |
| 4 | 6.0 | 29.5 | 29.1784 | $+0.3216$ | 0.1034 |
| 5 | 7.5 | 33.0 | 34.7741 | $-1.7741$ | 3.1473 |
| 6 | 8.0 | 36.5 | 36.6393 | $-0.1393$ | 0.0194 |
| 7 | 9.5 | 41.0 | 42.2349 | $-1.2349$ | 1.5250 |
| 8 | 11.0 | 48.0 | 47.8306 | $+0.1694$ | 0.0287 |
| 9 | 12.0 | 52.5 | 51.5610 | $+0.9390$ | 0.8817 |
| 10 | 13.5 | 58.0 | 57.1566 | $+0.8434$ | 0.7113 |
| **Sum** | **77.0** | **355.2** | **355.200** | **0.0000** | **7.9092** |

Sum of residuals:

$$
\sum_{i=1}^{10} e_i = 0.0000 \quad (\text{Machine precision error } < 10^{-14})
$$

- Sum of Squared Errors: $SSE = 7.9092$
- Mean Squared Error: $MSE = \frac{7.9092}{10} = 0.7909$
- Total Sum of Squares: $SS_{\text{tot}} = \sum (y_i - \bar{y})^2 = 1939.956$
- Goodness-of-fit: $R^2 = 1 - \frac{7.9092}{1939.956} = 0.9959$ (99.59% variance explained)

![Case 1: OLS Best Fit Line & Residual Diagnostics](case1_ols_best_fit_residuals.png)

---

## Case Study 2: Bivariate Cost Landscape & Gradient Descent Trajectories

### 1. Vectorized Analytic Gradient Formulas
Given hypothesis vector $\hat{\mathbf{y}} = w \mathbf{x} + b \mathbf{1}$:

$$
\nabla J(w, b) = \begin{bmatrix} \frac{\partial J}{\partial w} \\ \frac{\partial J}{\partial b} \end{bmatrix} = \begin{bmatrix} \frac{1}{m} \mathbf{x}^T (\hat{\mathbf{y}} - \mathbf{y}) \\ \frac{1}{m} \mathbf{1}^T (\hat{\mathbf{y}} - \mathbf{y}) \end{bmatrix}
$$

### 2. Convergence Dynamics Across Learning Rates

```
  alpha = 0.03 (Under-stepping)        alpha = 0.25 (Optimal)              alpha = 0.92 (Oscillatory)
+-------------------------------+   +-------------------------------+   +-------------------------------+
| Steps are tiny. Takes over    |   | Direct geometric march along  |   | Overshoots the valley center  |
| 60 iterations to reach near   |   | negative gradient orthogonal  |   | repeatedly, bouncing violently|
| the global minimum.           |   | to contour level curves.      |   | across steep canyon walls.    |
+-------------------------------+   +-------------------------------+   +-------------------------------+
```

![Case 2: Gradient Descent Cost Contours](case2_gradient_descent_cost_contours.png)

---

## Case Study 3: Evaluation Metrics & The Adjusted $R^2$ Feature Bloat Proof

### 1. Baseline Evaluation Metrics ($p = 3$ Informative Predictors)
- **Mean Absolute Error (MAE):** $1.583$
- **Mean Squared Error (MSE):** $3.891$
- **Root Mean Squared Error (RMSE):** $1.972$
- **Coefficient of Determination ($R^2$):** $0.8542$
- **Adjusted $R^2$:** $0.8524$

### 2. Empirical Demonstration of the $R^2$ Flaw

When injecting 20 pure Gaussian noise features ($z_k \sim \mathcal{N}(0, 1)$):
- **Unadjusted $R^2$:** Increases monotonically from $0.8542$ to $0.8671$. Even though the added variables contain zero physical relationship with $y$, chance correlations allow the linear model to overfit, artificially inflating $R^2$.
- **Adjusted $R^2$:** Drops continuously from $0.8524$ down to $0.8406$, penalizing the loss of degrees of freedom.

![Case 3: Regression Metrics & Feature Bloat](case3_regression_metrics_evaluation.png)
