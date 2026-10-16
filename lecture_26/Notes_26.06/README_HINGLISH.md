# Lecture 26.06: Linear Regression with Gradient Descent — Step 4: Parameter Updates & Scratch Implementation

## 📌 Saransh (Executive Summary)
Gradient Descent Step 4: Parameter update rule $\theta := \theta - \alpha \nabla J$, pure Python aur NumPy se full `LinearRegression` class implementation, aur live training run.

---

## 🔬 First-Principles Theory & Intuition
### 1. Step 4: Parameters Ko Update Karna
Gradients $dw$ aur $db$ calculate karne ke baad, parameters ko downhill step karwaya jata hai:

$$
\mathbf{w} := \mathbf{w} - \alpha \cdot dw
$$

$$
b := b - \alpha \cdot db
$$

Negative sign $(-)$ isliye lagaya jata hai kyunki gradient uphill (chadhai) ki taraf point karta hai, aur hume loss ko kam (downhill) karna hai!

### 2. Pure NumPy Class Implementation
Charo steps ko combine karke class banai jaati hai:
1. `__init__`: `lr` aur `n_iter` store karta hai.
2. `fit(X, y)`: Zero initialization karta hai aur loop chala kar predictions, gradients, aur updates perform karta hai.
3. `predict(X)`: Fitted parameters se naye test data par $\hat{y} = X \mathbf{w} + b$ return karta hai.


---

## 💻 Python & NumPy Code Implementation
```python
import numpy as np

class LinearRegression:
    """Production-grade Linear Regression with Vectorized Batch Gradient Descent."""
    def __init__(self, lr=0.01, n_iter=1000):
        self.lr = lr
        self.n_iter = n_iter
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        m, n = X.shape
        self.weights = np.zeros(n)
        self.bias = 0.0

        for i in range(self.n_iter):
            # STEP 2 - calc y_pred
            y_pred = self.bias + np.dot(X, self.weights)
            
            # STEP 3 - calc gradient
            db = (1.0 / m) * np.sum(y_pred - y)
            dw = (1.0 / m) * np.dot(X.T, (y_pred - y))
            
            # STEP 4 - convergence theorem - params update
            self.bias -= self.lr * db
            self.weights -= self.lr * dw

    def predict(self, X):
        return self.bias + np.dot(X, self.weights)

# Test with Lecture Example
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression(lr=0.01, n_iter=1000)
model.fit(X, y)

y_pred = model.predict(X)
print("Fitted Weights:", model.weights)
print("Fitted Bias:   ", model.bias)
print("Predictions:   ", y_pred)

```

---

## 🎯 Key Takeaways & Practical Tips
1. **Black-Box Se Azadi**: Libraries ko blind use karne ke bajaye unke andar ka math samajhna aapko top 1% engineer banata hai.
2. **Vectorization Ki Taqat**: Python loops ke bajaye NumPy array operations use karein jo C/BLAS speed provide karte hain.
3. **Debugging Mastery**: Jab loss decrease na ho raha ho, toh sabse pehle learning rate $\alpha$ aur gradient dimensions check karein.
