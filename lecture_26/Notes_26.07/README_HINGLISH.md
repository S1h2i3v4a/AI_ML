# Lecture 26.07: Linear Regression with Ordinary Least Squares (OLS) — Closed-Form Normal Equation

## 📌 Saransh (Executive Summary)
Linear Regression with OLS (Ordinary Least Squares): Matrix calculus se Closed-Form Normal Equation $\theta = (X_b^T X_b)^{-1} X_b^T y$ ka proof aur implementation.

---

## 🔬 First-Principles Theory & Intuition
### 1. OLS (Ordinary Least Squares) Kya Hai?
Gradient Descent mein hume baar-baar loop chalana padta hai aur learning rate adjust karni padti hai.
Lekin Linear Regression ke liye ek exact closed-form analytical mathematical formula exist karta hai jisse bina kisi iteration ke direct exact answers mil jate hain!

### 2. Normal Equation Ka Proof
Cost function matrix form mein:

$$
J(\boldsymbol{\theta}) = (X_b \boldsymbol{\theta} - \mathbf{y})^T (X_b \boldsymbol{\theta} - \mathbf{y}) = \boldsymbol{\theta}^T X_b^T X_b \boldsymbol{\theta} - 2 \mathbf{y}^T X_b \boldsymbol{\theta} + \mathbf{y}^T \mathbf{y}
$$

Jab hum iska derivative zero ke barabar set karte hain:

$$
\nabla_\boldsymbol{\theta} J = 2 X_b^T X_b \boldsymbol{\theta} - 2 X_b^T \mathbf{y} = 0
$$

$$
X_b^T X_b \boldsymbol{\theta} = X_b^T \mathbf{y}
$$

Dono taraf $(X_b^T X_b)^{-1}$ se multiply karne par hume milti hai **Normal Equation**:

$$
\boldsymbol{\theta} = (X_b^T X_b)^{-1} X_b^T \mathbf{y}
$$

- Isme $\theta[0]$ directly intercept/bias ban jata hai.
- $\theta[1:]$ saare feature weights ban jate hain.


---

## 💻 Python & NumPy Code Implementation
```python
import numpy as np

class LinearRegressionOLS:
    """Analytical Linear Regression via Closed-Form Normal Equation."""
    def __init__(self):
        self.bias = None
        self.weights = None

    def fit(self, X, y):
        m, n = X.shape
        # Augment bias column [1, X]
        X_b = np.c_[np.ones((m, 1)), X]
        
        # Closed-form Normal Equation: theta = (X_b^T X_b)^(-1) X_b^T y
        theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
        
        self.bias = theta[0]
        self.weights = theta[1:]

    def predict(self, X):
        return self.bias + np.dot(X, self.weights)

# Test with Lecture Example
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

ols = LinearRegressionOLS()
ols.fit(X, y)
print("OLS Bias:       ", ols.bias)
print("OLS Weights:    ", ols.weights)
print("OLS Predictions:", ols.predict(X))

```

---

## 🎯 Key Takeaways & Practical Tips
1. **Black-Box Se Azadi**: Libraries ko blind use karne ke bajaye unke andar ka math samajhna aapko top 1% engineer banata hai.
2. **Vectorization Ki Taqat**: Python loops ke bajaye NumPy array operations use karein jo C/BLAS speed provide karte hain.
3. **Debugging Mastery**: Jab loss decrease na ho raha ho, toh sabse pehle learning rate $\alpha$ aur gradient dimensions check karein.
