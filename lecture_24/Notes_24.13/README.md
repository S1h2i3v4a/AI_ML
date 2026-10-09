# Module 24.13: Logistic Regression — Intuition & The Sigmoid Function

## 1. Why Linear Regression Fails for Classification

In binary classification problems, the target label is categorical: $y \in \{0, 1\}$.
Attempting to fit a linear regression hypothesis $\hat{y} = \mathbf{w}^T \mathbf{x} + b$ directly creates two fundamental mathematical flaws:

```
 Flaw 1: Unbounded Output Range
 Linear regression outputs real values on (-inf, +inf).
 Probabilities must be strictly bounded in [0, 1]. A prediction of \hat{y} = 2.4 or -0.8 is physically meaningless!

 Flaw 2: Extreme Outlier Sensitivity
 A single extreme positive outlier far to the right shifts the fitted regression line,
 tilting the decision boundary threshold and causing severe misclassification of existing points!
```

---

## 2. From Odds and Logits to the Sigmoid Function

To map continuous inputs $\mathbf{w}^T \mathbf{x} + b \in (-\infty, \infty)$ into valid calibrated probabilities $p \in (0, 1)$, we progress through three mathematical steps:

### Step 1: Probability to Odds Ratio
The **Odds** of an event is the ratio of probability of occurrence to probability of non-occurrence:

$$
\text{Odds} = \frac{p}{1 - p} \in [0, \infty)
$$

### Step 2: The Logit Function (Log-Odds)
Taking the natural logarithm of the odds produces the **Logit**:

$$
\text{Logit}(p) = \ln\left( \frac{p}{1 - p} \right) \in (-\infty, \infty)
$$

### Step 3: Inverting the Logit (The Sigmoid Function)
We set the linear predictor equal to the log-odds:

$$
\ln\left( \frac{p}{1 - p} \right) = \mathbf{w}^T \mathbf{x} + b = z
$$

Exponentiating both sides:

$$
\frac{p}{1 - p} = e^z \implies p = e^z (1 - p) \implies p (1 + e^z) = e^z
$$

Solving for probability $p$:

$$
p = \sigma(z) = \frac{e^z}{1 + e^z} = \frac{1}{1 + e^{-z}}
$$

```
               \sigma(z) ^
                       1 |                  .-------------
                         |                /
                     0.5 |--------------* (z = 0, \sigma = 0.5)
                         |             /
                       0 | -----------'
                         +-------------------------------> z
                                      0
```

---

## 3. Mathematical Properties of the Sigmoid Function

1. **Symmetric S-Curve:** Centered at the inflection point $(0, 0.5)$.
2. **Asymptotes:** $\lim_{z \to \infty} \sigma(z) = 1$ and $\lim_{z \to -\infty} \sigma(z) = 0$.
3. **Analytic Derivative:** The derivative expresses cleanly in terms of the function itself:
   $$
   \sigma'(z) = \frac{d}{dz} \left( \frac{1}{1 + e^{-z}} \right) = \frac{e^{-z}}{(1 + e^{-z})^2} = \sigma(z) \left( 1 - \sigma(z) \right)
   $$

---

## 4. The Linear Decision Boundary

To assign discrete binary class labels $\hat{y} \in \{0, 1\}$, we apply a standard probability threshold $\tau = 0.5$:

$$
\hat{y} = \begin{cases} 1 & \text{if } P(y=1|\mathbf{x}) \ge 0.5 \\ 0 & \text{if } P(y=1|\mathbf{x}) < 0.5 \end{cases}
$$

Because $\sigma(z) \ge 0.5 \iff z \ge 0$, the decision boundary satisfies:

$$
\mathbf{w}^T \mathbf{x} + b = 0
$$

This equation defines a **hyperplane** partitioning feature space into two prediction regions.
