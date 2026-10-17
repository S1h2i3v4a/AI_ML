# Notes_26.07: Linear Regression With OLS (Normal Equation) [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne Linear Regression ka **Analytical (Direct) Solution** samjhaya hai: bina kisi loop ya learning rate ke, **Normal Equation** se direct answer nikalna.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Ordinary Least Squares (OLS) kya hota hai?
- Normal Equation: $\theta = (X_b^T X_b)^{-1} X_b^T y$.
- $X$ mein 1 ka bias column add karna ($X_b = [1, X]$).
- Bina kisi iteration ke direct exact weights nikalna.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Normal Equation Ka Jadu:
Gradient Descent mein humein 1000 baar loop chalana padta hai aur learning rate adjust karni padti hai. 
Lekin OLS ek aisi direct mathematical equation hai jo ek hi jhatke mein exact optimum answer de deti hai:

$$\theta = (X_b^T X_b)^{-1} X_b^T y$$

Yahan $(X_b^T X_b)^{-1}$ matrix ka inverse hota hai.

---

### 💻 Python Code

```python
import numpy as np

def linear_regression_ols_normal_equation(X, y):
    """
    Solves Linear Regression analytically using the Ordinary Least Squares (OLS)
    Normal Equation: theta = (X_b^T * X_b)^(-1) * X_b^T * y
    Zero iterations required; computes the exact global optimum in a single step.
    """
    m = len(y)
    # Add bias intercept column of ones to X: X_b = [1, X]
    X_b = np.c_[np.ones((m, 1)), X]

    # Analytical solution via Normal Equation
    theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

    bias = theta_best[0]
    weights = theta_best[1:]

    return weights, bias

# --- Function Call & Testing ---
np.random.seed(42)
X_toy = 2 * np.random.rand(100, 1)
y_toy = 4 + 3 * X_toy.squeeze() + np.random.randn(100) * 0.1

w_ols, b_ols = linear_regression_ols_normal_equation(X_toy, y_toy)
print(f"True slope: 3.0 | OLS Weight: {w_ols[0]:.4f}")
print(f"True bias:  4.0 | OLS Bias:   {b_ols:.4f}")
```

---

### 📌 Summary Points
- OLS mein na loop chahiye, na learning rate.
- Exact minimum seedha milta hai.
