# 📈 Lecture 23.07: Starting with Linear Regression

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-1.4%2B-orange.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Lecture 23](../README.md)

---

## 📌 1. What is Linear Regression?

**Linear Regression** is a fundamental supervised learning algorithm that models the relationship between a continuous scalar target variable $y$ and one or more explanatory feature variables $\mathbf{x}$ by fitting a linear equation to observed data.

### 1. Simple Linear Regression (Single Feature $x$):

$$
\hat{y} = w x + b \qquad\text{or}\qquad \hat{y} = \beta_1 x + \beta_0
$$

where:
- $w$ (or $\beta_1$) is the **weight / slope**, representing the change in $\hat{y}$ per unit change in $x$.
- $b$ (or $\beta_0$) is the **bias / intercept**, representing the predicted value of $y$ when $x = 0$.

### 2. Multiple Linear Regression ($p$ Features):

$$
\hat{y} = w_1 x_1 + w_2 x_2 + \dots + w_p x_p + b = \mathbf{w}^T \mathbf{x} + b
$$

In compact matrix notation for $N$ observations:

$$
\hat{\mathbf{y}} = X \mathbf{w} + b \mathbf{1}
$$

```mermaid
graph LR
    x["Feature Vector x"] --> Mult["Dot Product with Weights: w^T x"]
    Mult --> Add["Add Bias: w^T x + b"]
    Add --> yhat["Predicted Target y_hat"]
```

---

## 📐 2. Geometric Interpretation Across Dimensions

- **1 Feature ($p = 1$):** The model fits a **Straight Line** in 2D Euclidean space ($\mathbb{R}^2$).
- **2 Features ($p = 2$):** The model fits a **2D Plane** in 3D Euclidean space ($\mathbb{R}^3$).
- **$p$ Features ($p \ge 3$):** The model fits a **$(p)$-dimensional Hyperplane** in $\mathbb{R}^{p+1}$.

---

## 🔍 3. Interpreting Model Parameters

Consider an insurance charges prediction model:

$$
\text{charges} = 250 \cdot (\text{age}) + 330 \cdot (\text{bmi}) + 23800 \cdot (\text{smoker}) - 11000
$$

1. **Slope for `age` ($+250$):** Holding all other features constant, each additional year of age increases predicted healthcare charges by $\$250$.
2. **Slope for `smoker` ($+23800$):** Smokers are predicted to incur $\$23,800$ more in annual medical charges than non-smokers.
3. **Intercept ($-11000$):** Baseline offset adjustment.

---

## 💻 4. Python Implementation: Visualizing a 1D Linear Hypothesis

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic linear trend
np.random.seed(42)
x = np.linspace(10, 60, 50)  # Age
y = 250 * x + 2000 + np.random.randn(50) * 1500  # Charges

# Specific parameters
w, b = 250.0, 2000.0

plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='#1f77b4', alpha=0.7, label='Observed Data Points (x, y)')
plt.plot(x, w * x + b, color='#d62728', lw=2.5, label=f'Hypothesis Line: y = {w}*x + {b}')

plt.title('Simple Linear Regression: Hypothesis Line', fontsize=12, fontweight='bold')
plt.xlabel('Age (Years)', fontsize=11)
plt.ylabel('Charges ($)', fontsize=11)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()
```
