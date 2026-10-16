# Lecture 26.05: Linear Regression with Gradient Descent — Step 3: Analytical Gradient Derivation

## 📌 Saransh (Executive Summary)
Gradient Descent Step 3: Multivariate calculus chain rule se cost function ke partial derivatives derivation, weight gradient $dw$ aur bias gradient $db$ ka exact proof.

---

## 🔬 First-Principles Theory & Intuition
### 1. Step 3: Gradient Calculate Karna (Slope Dhoondhna)
Gradient hume batata hai ki parameter ko thoda sa badhane ya ghatane se cost function kitna badlega ya ghatega.
Hume do cheezein calculate karni hain:
1. $\frac{\partial J}{\partial \mathbf{w}}$ (Weights ka gradient, jise code mein `dw` kehte hain)
2. $\frac{\partial J}{\partial b}$ (Bias ka gradient, jise code mein `db` kehte hain)

### 2. Step-by-Step Chain Rule Derivation
Cost function:

$$
J(\mathbf{w}, b) = \frac{1}{2m} \sum_{i=1}^m \left( \hat{y}^{(i)} - y^{(i)} \right)^2
$$

Pehle power rule lagate hain: power 2 aage aayegi aur $\frac{1}{2}$ se cut jayegi:

$$
2 \cdot \frac{1}{2m} (\hat{y}^{(i)} - y^{(i)}) = \frac{1}{m} (\hat{y}^{(i)} - y^{(i)})
$$

Ab andar ka derivative:
- $w_j$ ke respect mein: $\frac{\partial}{\partial w_j} (w_j x_j) = x_j^{(i)}$
- $b$ ke respect mein: $\frac{\partial}{\partial b} (b) = 1$

Isliye final formulas bante hain:

$$
dw = \frac{\partial J}{\partial \mathbf{w}} = \frac{1}{m} X^T (\hat{\mathbf{y}} - \mathbf{y})
$$

$$
db = \frac{\partial J}{\partial b} = \frac{1}{m} \sum_{i=1}^m (\hat{y}^{(i)} - y^{(i)})
$$

Code mein yeh sirf do clean lines hain:
```python
db = (1 / m) * np.sum(y_pred - y)
dw = (1 / m) * np.dot(X.T, (y_pred - y))
```


---

## 💻 Python & NumPy Code Implementation
```python
import numpy as np

def compute_gradients(X, y, weights, bias):
    """Vectorized computation of analytical gradients dw and db."""
    m = len(y)
    y_pred = X @ weights + bias
    residuals = y_pred - y
    
    # Analytical gradients
    db = (1.0 / m) * np.sum(residuals)
    dw = (1.0 / m) * (X.T @ residuals)
    
    return dw, db

# Verification on toy data
X = np.array([[1.0], [2.0], [3.0]])
y = np.array([2.0, 4.0, 6.0])
w = np.array([0.0])
b = 0.0

dw, db = compute_gradients(X, y, w, b)
print(f"Analytical dw: {dw}, db: {db}")

```

---

## 🎯 Key Takeaways & Practical Tips
1. **Black-Box Se Azadi**: Libraries ko blind use karne ke bajaye unke andar ka math samajhna aapko top 1% engineer banata hai.
2. **Vectorization Ki Taqat**: Python loops ke bajaye NumPy array operations use karein jo C/BLAS speed provide karte hain.
3. **Debugging Mastery**: Jab loss decrease na ho raha ho, toh sabse pehle learning rate $\alpha$ aur gradient dimensions check karein.
