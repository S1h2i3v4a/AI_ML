# Module 23.09: What is the Cost Function? (MSE & the $1/(2m)$ Factor)

## 1. Loss Function vs. Cost Function

In machine learning terminology, it is vital to distinguish between a **Loss Function** and a **Cost Function**:

```
+-------------------------------------------------------------------------+
| Single Training Example (x^(i), y^(i))  --->  Loss Function: L(y, \hat{y}) |
| Entire Dataset of m Examples            --->  Cost Function: J(w, b)    |
+-------------------------------------------------------------------------+
```

- **Loss Function $L(\hat{y}^{(i)}, y^{(i)})$:** Quantifies the discrepancy for a **single** individual training instance $i$. For squared loss:
  $$
  L(\hat{y}^{(i)}, y^{(i)}) = \frac{1}{2} \left( \hat{y}^{(i)} - y^{(i)} \right)^2
  $$
- **Cost Function $J(w, b)$:** Measures the aggregate performance of the model parameters across the **entire dataset** of $m$ training instances. It is the empirical risk over the sample distribution.

---

## 2. Mathematical Definition of the Linear Regression Cost Function

For standard univariate Linear Regression with hypothesis $\hat{y}^{(i)} = w x^{(i)} + b$, the cost function is defined as:

$$
J(w, b) = \frac{1}{2m} \sum_{i=1}^m \left( \hat{y}^{(i)} - y^{(i)} \right)^2 = \frac{1}{2m} \sum_{i=1}^m \left( w x^{(i)} + b - y^{(i)} \right)^2
$$

---

## 3. Mathematical Rationale for the $\frac{1}{2m}$ Factor

Why do we divide by $2m$ instead of merely minimizing the raw sum of squared errors $\sum (y - \hat{y})^2$?

### 1. The $\frac{1}{m}$ Factor (Sample Size Invariance)
- If we do not divide by $m$, the total error increases linearly as more data points are added ($m \to 10^6 \implies \text{Error} \to \infty$).
- Dividing by $m$ computes the **average** squared error per observation.
- This makes the cost magnitude and learning rate $\alpha$ robust and invariant to the size of the training set.

### 2. The $\frac{1}{2}$ Factor (Mathematical Elegance in Calculus)
- When minimizing $J(w, b)$ via gradient descent or analytical differentiation, we must take the derivative with respect to parameters:
  $$
  \frac{\partial}{\partial w} \left[ \frac{1}{2} (u)^2 \right] = \frac{1}{2} \cdot 2 u \cdot \frac{\partial u}{\partial w} = u \cdot \frac{\partial u}{\partial w}
  $$
- The constant coefficient $\frac{1}{2}$ cleanly cancels out the exponent $2$ that drops down via the power rule of calculus!
- Without $\frac{1}{2}$, every gradient update formula would carry an extraneous factor of $2$, complicating calculations without altering the location of the minimum:
  $$
  \arg\min J(w, b) = \arg\min \left( \frac{1}{2m} \sum_{i=1}^m (e^{(i)})^2 \right) = \arg\min \left( \sum_{i=1}^m (e^{(i)})^2 \right)
  $$

---

## 4. Cost as a Function of Parameters

It is essential to understand what is fixed and what varies in $J(w, b)$:
- **Fixed Quantities:** The empirical dataset $(x^{(1)}, y^{(1)}), \dots, (x^{(m)}, y^{(m)})$ consists of fixed historical constants.
- **Independent Variables:** The weights $w$ and $b$ are the variables. The cost function maps parameter space $\mathbb{R}^2$ to a non-negative real scalar $\mathbb{R}_{\ge 0}$:
  $$
  J: \mathbb{R}^2 \to \mathbb{R}_{\ge 0}
  $$

The optimization objective of linear regression is formalized as:

$$
(w^*, b^*) = \arg\min_{w, b} J(w, b)
$$
