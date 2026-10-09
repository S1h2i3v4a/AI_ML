# Module 23.08: What is the Best Fit Line? (Residuals & Ordinary Least Squares)

## 1. Introduction: The Criterion for "Best Fit"

Given a set of two-dimensional observation points $(x^{(1)}, y^{(1)}), (x^{(2)}, y^{(2)}), \dots, (x^{(m)}, y^{(m)})$, infinitely many candidate straight lines $\hat{y} = w x + b$ can be drawn through the scatter plot. Determining the **best fit line** requires establishing an objective mathematical criterion that measures how closely the candidate line approximates the empirical observations.

```
          y ^
            |                     * (x_i, y_i)
            |                    /|
            |                   / | e_i = y_i - \hat{y}_i (Residual)
            |                  /  v
            |           *     /--------- \hat{y} = w x + b
            |          /|    /
            |         / |   /
            |        *  |  /
            |           v /
            +------------------------------> x
```

---

## 2. Defining the Residual (Error)

For any observation $(x^{(i)}, y^{(i)})$, the candidate line predicts:

$$
\hat{y}^{(i)} = w x^{(i)} + b
$$

The deviation between the empirical ground truth $y^{(i)}$ and the candidate prediction $\hat{y}^{(i)}$ is known as the **residual** (or error) $e^{(i)}$:

$$
e^{(i)} = y^{(i)} - \hat{y}^{(i)} = y^{(i)} - (w x^{(i)} + b)
$$

### Why Not Minimize the Raw Sum of Residuals?
If we defined total error as $\sum_{i=1}^m e^{(i)}$:
- Positive residuals (points lying above the line) cancel out negative residuals (points lying below the line).
- A completely erratic line passing nowhere near the data points could have $\sum_{i=1}^m e^{(i)} = 0$ purely through destructive interference of positive and negative errors.

### Why Not Minimize the Sum of Absolute Residuals (MAE / L1 Norm)?
If we minimized $\sum_{i=1}^m |e^{(i)}|$:
- The absolute value function $f(u) = |u|$ is non-differentiable at $u = 0$.
- It lacks a clean closed-form analytical derivative, making matrix inversion and standard calculus optimization mathematically cumbersome.

---

## 3. Ordinary Least Squares (OLS) Criterion

The foundational solution, established independently by Carl Friedrich Gauss and Adrien-Marie Legendre, is the **Ordinary Least Squares (OLS)** principle. We define the objective as minimizing the **Sum of Squared Errors (SSE)**:

$$
SSE(w, b) = \sum_{i=1}^m \left( e^{(i)} \right)^2 = \sum_{i=1}^m \left( y^{(i)} - (w x^{(i)} + b) \right)^2
$$

### Mathematical Properties of OLS:
1. **Positivity:** Squaring guarantees $(e^{(i)})^2 \ge 0$. Errors cannot cancel out.
2. **Disproportionate Penalty on Outliers:** A deviation of 4 units contributes $4^2 = 16$ to the error, whereas a deviation of 1 unit contributes $1^2 = 1$. OLS heavily penalizes large errors.
3. **Smoothness and Differentiability:** The function $SSE(w, b)$ is continuously differentiable across all $w, b \in \mathbb{R}$, yielding a strictly convex paraboloid with an exact analytical minimum.

---

## 4. Analytical Derivation of the OLS Closed-Form Solution

To find $w$ and $b$ that minimize $SSE(w, b)$, we set the partial derivatives with respect to $b$ and $w$ to zero.

### Step 1: Derivative with Respect to Intercept $b$
$$
\frac{\partial SSE}{\partial b} = \frac{\partial}{\partial b} \sum_{i=1}^m \left( y^{(i)} - w x^{(i)} - b \right)^2 = -2 \sum_{i=1}^m \left( y^{(i)} - w x^{(i)} - b \right) = 0
$$

Dividing by $-2m$:

$$
\frac{1}{m} \sum_{i=1}^m y^{(i)} - w \left( \frac{1}{m} \sum_{i=1}^m x^{(i)} \right) - b = 0 \implies \bar{y} - w \bar{x} - b = 0
$$

Thus, the optimal intercept is:

$$
b = \bar{y} - w \bar{x}
$$

> **Crucial Geometric Insight:** The optimal best fit line **always passes through the sample mean centroid** $(\bar{x}, \bar{y})$.

### Step 2: Derivative with Respect to Slope $w$
Substitute $b = \bar{y} - w \bar{x}$ into the error term:

$$
y^{(i)} - \hat{y}^{(i)} = y^{(i)} - (w x^{(i)} + \bar{y} - w \bar{x}) = (y^{(i)} - \bar{y}) - w (x^{(i)} - \bar{x})
$$

Differentiating $SSE$ with respect to $w$:

$$
\frac{\partial SSE}{\partial w} = -2 \sum_{i=1}^m (x^{(i)} - \bar{x}) \left[ (y^{(i)} - \bar{y}) - w (x^{(i)} - \bar{x}) \right] = 0
$$

Distributing the summation:

$$
\sum_{i=1}^m (x^{(i)} - \bar{x})(y^{(i)} - \bar{y}) - w \sum_{i=1}^m (x^{(i)} - \bar{x})^2 = 0
$$

Solving for $w$:

$$
w = \frac{\sum_{i=1}^m (x^{(i)} - \bar{x})(y^{(i)} - \bar{y})}{\sum_{i=1}^m (x^{(i)} - \bar{x})^2} = \frac{\text{Cov}(x, y)}{\text{Var}(x)}
$$

---

## 5. Summary Table

| Property | Symbol | Formula | Statistical Meaning |
| :--- | :--- | :--- | :--- |
| **Residual** | $e^{(i)}$ | $y^{(i)} - \hat{y}^{(i)}$ | Vertical error between truth and fit |
| **Objective** | $SSE$ | $\sum_{i=1}^m (e^{(i)})^2$ | Sum of squared vertical distances |
| **Optimal Slope** | $w^*$ | $\frac{\text{Cov}(x, y)}{\text{Var}(x)}$ | Ratio of sample covariance to sample feature variance |
| **Optimal Intercept**| $b^*$ | $\bar{y} - w^* \bar{x}$ | Ensures line passes through $(\bar{x}, \bar{y})$ |
