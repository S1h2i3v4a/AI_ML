# Module 23.14: Evaluation Metrics for Regression (MAE, MSE, RMSE, $R^2$, and Adjusted $R^2$)

## 1. Why Classification Accuracy Fails for Regression

In classification problems, target outputs are discrete labels ($y \in \{0, 1\}$), permitting simple metric ratios such as $\frac{\text{Correct}}{\text{Total}}$.
In regression, predictions $\hat{y}$ are continuous real numbers ($\hat{y} \in \mathbb{R}$). The probability of an exact floating-point match $P(\hat{y} = y) = 0$.
Consequently, regression evaluation relies on **distance-based error norms** and **variance-explained ratios**.

---

## 2. Distance-Based Error Metrics

### 1. Mean Absolute Error (MAE)
MAE measures the average absolute magnitude of the prediction errors:

$$
\text{MAE} = \frac{1}{m} \sum_{i=1}^m |y_i - \hat{y}_i|
$$

- **Units:** Exact same units as the target variable $y$.
- **Robustness:** Robust to outliers because errors scale linearly ($|e_i|$). It treats all deviations proportionally.

### 2. Mean Squared Error (MSE)
MSE computes the average of the squared prediction deviations:

$$
\text{MSE} = \frac{1}{m} \sum_{i=1}^m (y_i - \hat{y}_i)^2
$$

- **Units:** Squared units of the target ($y^2$, e.g., $\$^{2}$).
- **Outlier Sensitivity:** Highly sensitive to outliers. A single severe error drastically inflates MSE due to the quadratic exponent.

### 3. Root Mean Squared Error (RMSE)
RMSE is the square root of the Mean Squared Error:

$$
\text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{m} \sum_{i=1}^m (y_i - \hat{y}_i)^2}
$$

- **Units:** Restores the original target unit $y$ while preserving the quadratic penalty on large outliers.
- **Mathematical Property:** $\text{RMSE} \ge \text{MAE}$ always. The difference $\text{RMSE} - \text{MAE}$ reflects the variance in error magnitudes.

---

## 3. Relative Goodness-of-Fit: $R^2$ Score

The **Coefficient of Determination** ($R^2$) quantifies the proportion of target variance explained by the model compared to a baseline naive model that always predicts the sample mean $\bar{y}$.

$$
R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}} = 1 - \frac{\sum_{i=1}^m (y_i - \hat{y}_i)^2}{\sum_{i=1}^m (y_i - \bar{y})^2}
$$

Where:
- **$SS_{\text{res}}$ (Residual Sum of Squares):** Unexplained variance in predictions.
- **$SS_{\text{tot}}$ (Total Sum of Squares):** Total empirical variance in ground truth $y$.

```
Value of R^2         Interpretation
-------------------------------------------------------------------------------------------------
R^2 = 1.0           Perfect model (zero residual errors; all points lie precisely on hyperplane).
R^2 = 0.0           Model performs identically to predicting the sample mean \bar{y} for all inputs.
R^2 < 0.0           Model performs WORSE than simply predicting the mean!
```

---

## 4. The Pitfall of $R^2$ and the Adjusted $R^2$ Solution

### The Fundamental Flaw of $R^2$:
As additional feature variables are added to a regression model ($p \to p + 1$), $SS_{\text{res}}$ can **never increase**; it either decreases or stays constant.
Even if a completely random, useless noise feature is added, $R^2$ will artificially increase or remain unchanged. It never penalizes model bloat!

### The Adjusted $R^2$ Metric:
Adjusted $R^2$ introduces a degrees-of-freedom penalty for every additional predictor feature $p$:

$$
R^2_{\text{adj}} = 1 - \left[ \frac{(1 - R^2)(m - 1)}{m - p - 1} \right]
$$

Where:
- $m$: Total sample size.
- $p$: Total number of independent predictors/features.

### Behavioral Properties:
1. If a newly added feature meaningfully reduces $SS_{\text{res}}$ beyond chance, $R^2_{\text{adj}}$ **increases**.
2. If a newly added feature offers negligible predictive value, the penalty term $\frac{m-1}{m-p-1}$ dominates, and $R^2_{\text{adj}}$ **decreases**.
3. $R^2_{\text{adj}} \le R^2$ always holds.

---

## 5. Comparative Evaluation Summary

| Metric | Formula | Units | Sensitivity to Outliers | Primary Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **MAE** | $\frac{1}{m}\sum \|y_i - \hat{y}_i\|$ | Same as $y$ | Low (Robust) | Business metrics requiring intuitive linear interpretation |
| **MSE** | $\frac{1}{m}\sum (y_i - \hat{y}_i)^2$ | Squared $y^2$ | High | Loss function during model training optimization |
| **RMSE**| $\sqrt{\text{MSE}}$ | Same as $y$ | High | Diagnostic evaluation when large errors are dangerous |
| **$R^2$** | $1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}$ | Unitless $\in (-\infty, 1]$ | Medium | Evaluating explanatory variance of univariate models |
| **$R^2_{\text{adj}}$**| $1 - \frac{(1-R^2)(m-1)}{m-p-1}$ | Unitless $\in (-\infty, 1]$ | Medium | Comparing multiple regression models with different feature counts |
