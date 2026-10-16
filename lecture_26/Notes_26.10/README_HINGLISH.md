# Lecture 26.10: Logistic Regression from Scratch — Vectorized Implementation & Decision Boundaries

## 📌 Saransh (Executive Summary)
Logistic Regression ki complete OOP implementation: `_sigmoid()`, `fit()`, `get_probabilities()`, `predict()`, aur 2D decision boundary visualization.

---

## 🔬 First-Principles Theory & Intuition
### 1. Logistic Regression Class Ka Full Structure
Is class mein char important methods hote hain:
1. `_sigmoid(self, z)`: Raw continuous score $z$ ko probability $[0, 1]$ mein convert karta hai.
2. `fit(self, X, y)`: Gradient descent chala kar weights aur bias update karta hai.
3. `get_probabilities(self, X)`: Har test instance ke liye $P(y=1)$ return karta hai.
4. `predict(self, X, threshold=0.5)`: Agar probability $\ge 0.5$ hai toh class 1, warna class 0 return karta hai.

### 2. Decision Boundary Ki Equation
Jab probability exactly $0.5$ hoti hai, tab Sigmoid input $z = 0$ hota hai:

$$
w_1 x_1 + w_2 x_2 + b = 0 \implies x_2 = -\frac{w_1}{w_2} x_1 - \frac{b}{w_2}
$$

Yeh line dono classes ko separate karti hai!


---

## 💻 Python & NumPy Code Implementation
```python
import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.01, n_iter=1000):
        self.bias = None
        self.weights = None
        self.lr = learning_rate
        self.n_iter = n_iter

    def _sigmoid(self, z):
        return 1.0 / (1.0 + np.exp(-z))

    def fit(self, X, y):
        m, n = X.shape
        self.bias = 0.0
        self.weights = np.zeros(n)

        for i in range(self.n_iter):
            z = self.bias + np.dot(X, self.weights)
            y_pred = self._sigmoid(z)

            db = (1.0 / m) * np.sum(y_pred - y)
            dw = (1.0 / m) * np.dot(X.T, (y_pred - y))

            self.bias -= self.lr * db
            self.weights -= self.lr * dw

    def get_probabilities(self, X):
        z = self.bias + np.dot(X, self.weights)
        return self._sigmoid(z)

    def predict(self, X, threshold=0.5):
        probabilities = self.get_probabilities(X)
        y_pred_bool = probabilities >= threshold
        return y_pred_bool.astype(int)

# Lecture Dataset
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 0, 1, 1])

model = LogisticRegression(learning_rate=0.1, n_iter=2000)
model.fit(X, y)

print("Predictions:  ", model.predict(X))
print("Probabilities:", model.get_probabilities(X))

```

---

## 🎯 Key Takeaways & Practical Tips
1. **Black-Box Se Azadi**: Libraries ko blind use karne ke bajaye unke andar ka math samajhna aapko top 1% engineer banata hai.
2. **Vectorization Ki Taqat**: Python loops ke bajaye NumPy array operations use karein jo C/BLAS speed provide karte hain.
3. **Debugging Mastery**: Jab loss decrease na ho raha ho, toh sabse pehle learning rate $\alpha$ aur gradient dimensions check karein.
