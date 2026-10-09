# Lecture 23: Linear Regression & ML Foundations - Practice Problem Suite

This production practice problem suite challenges you to apply first-principles mathematical derivations, numerical optimization, and real-world statistical evaluation across 3 in-depth engineering case studies.

---

## Case Study 1: Analytical OLS Derivation & Residual Diagnostics

### Theoretical Context
A high-growth digital enterprise measures advertising expenditures ($x$, in $\$1,000$s) and the resulting sales revenues ($y$, in $\$1,000$s) across 10 operational quarters:

$$
x = [2.0, 3.0, 4.5, 6.0, 7.5, 8.0, 9.5, 11.0, 12.0, 13.5]
$$

$$
y = [15.2, 18.5, 23.0, 29.5, 33.0, 36.5, 41.0, 48.0, 52.5, 58.0]
$$

### Problem Statements:
1. **First-Principles Derivation:** Compute the sample means $\bar{x}$ and $\bar{y}$. Calculate the sample covariance $\text{Cov}(x, y)$ and variance $\text{Var}(x)$.
2. **Optimal Parameter Vector:** Compute the closed-form Ordinary Least Squares slope $w^*$ and intercept $b^*$:
   $$
   w^* = \frac{\sum_{i=1}^m (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^m (x_i - \bar{x})^2}, \quad b^* = \bar{y} - w^* \bar{x}
   $$
3. **Centroid Invariant Check:** Prove mathematically and check computationally that the point $(\bar{x}, \bar{y})$ lies exactly on the line.
4. **Residual Sum Invariant:** Compute each individual residual $e_i = y_i - \hat{y}_i$. Demonstrate that $\sum_{i=1}^{10} e_i = 0$ (within floating-point machine precision $\epsilon < 10^{-14}$).
5. **Loss Metrics:** Compute the Sum of Squared Errors ($SSE$), Mean Squared Error ($MSE$), and the Total Sum of Squares ($SS_{\text{tot}}$).

---

## Case Study 2: Bivariate Cost Landscape & Gradient Descent Trajectories

### Theoretical Context
Consider an empirical dataset of $m = 60$ standardized observations $(x^{(i)}, y^{(i)})$ governed by an underlying linear generator with Gaussian measurement noise.

The bivariate Mean Squared Error cost function is formulated as:

$$
J(w, b) = \frac{1}{2m} \sum_{i=1}^m \left( w x^{(i)} + b - y^{(i)} \right)^2
$$

### Problem Statements:
1. **Analytic Gradient Derivation:** Express the exact mathematical formulas for the partial derivatives $\frac{\partial J}{\partial w}$ and $\frac{\partial J}{\partial b}$.
2. **Vectorized GD Implementation:** Implement a Batch Gradient Descent optimizer from scratch without using any machine learning libraries.
3. **Learning Rate Regimes:** Simulate and record parameter trajectories $(w^{(t)}, b^{(t)})$ and cost history $J^{(t)}$ across 60 iterations under three learning rate regimes:
   - Under-stepping: $\alpha = 0.03$
   - Optimal convergence: $\alpha = 0.25$
   - Oscillatory / near-divergence: $\alpha = 0.92$
4. **Contour Geometry:** Formulate a 2D contour plot over parameter space $(w, b) \in [1, 6] \times [9, 15]$. Overlay the optimization paths taken by all three learning rates to analyze convergence dynamics.

---

## Case Study 3: Evaluation Metrics & The Adjusted $R^2$ Feature Bloat Proof

### Theoretical Context
When engineering models for high-dimensional business data, practitioners often inject numerous candidate features. While unadjusted $R^2$ monotonically increases or remains unchanged when adding features, degrees-of-freedom penalized metrics expose uninformative predictors.

### Problem Statements:
1. **Baseline Model:** Train an Ordinary Least Squares model on $m = 250$ synthetic observations with $p = 3$ true informative predictors.
2. **Baseline Metric Suite:** Compute the complete metric suite: MAE, MSE, RMSE, and $R^2$.
3. **Feature Bloat Injection:** Progressively append 20 independent standard Gaussian noise features $z_k \sim \mathcal{N}(0, 1)$ ($k = 1, \dots, 20$).
4. **Metric Divergence Proof:** For total feature counts $k \in [3, 23]$, calculate both $R^2$ and Adjusted $R^2$:
   $$
   R^2_{\text{adj}} = 1 - \left[ \frac{(1 - R^2)(m - 1)}{m - k - 1} \right]
   $$
5. **Diagnostic Visualizations:** Plot $R^2$ vs $R^2_{\text{adj}}$ across feature counts. Plot the residual scatter plot vs fitted values $\hat{y}$ to verify homoscedasticity.
