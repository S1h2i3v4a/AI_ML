# Notes_26.10: Scratch Se Logistic Regression Ka Code [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne pure Python aur NumPy se **Logistic Regression ki poori class** scratch se likh kar dikhayi hai.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- `LogisticRegressionScratch` class ka architecture.
- Binary Cross-Entropy (Log-Loss) aur gradients ka formula.
- `fit()`, `predict_proba()` aur `predict()` methods likhna.
- Scikit-Learn ke data par model ko test karna.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Code Ka Structure:
1. `__init__`: Learning rate aur epochs set karta hai.
2. `_sigmoid`: Linear values ko 0 aur 1 ke beech compress karta hai.
3. `fit`: Gradients $dw = \frac{1}{m} X^T (\hat{y} - y)$ nikaal kar weights update karta hai.
4. `predict`: Agar probability 0.5 se badi hai toh 1, varna 0 output deta hai.

---

### 💻 Python Code

```python
import numpy as np

class LogisticRegressionScratch:
    """
    Complete Scratch Implementation of Logistic Regression using Vectorized NumPy:
    - Hypothesis: y_hat = sigmoid(X * w + b)
    - Loss: Binary Cross-Entropy (Log-Loss)
    - Gradients: dw = (1/m) * X^T * (y_hat - y), db = (1/m) * sum(y_hat - y)
    - Updates: w = w - lr * dw, b = b - lr * db
    """
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.lr = learning_rate
        self.epochs = epochs
        self.w = None
        self.b = None

    def _sigmoid(self, z):
        z_safe = np.clip(z, -500, 500)
        return 1.0 / (1.0 + np.exp(-z_safe))

    def fit(self, X, y):
        m, d = X.shape
        self.w = np.zeros(d)
        self.b = 0.0

        for _ in range(self.epochs):
            # 1. Forward pass: compute probabilities
            linear_model = np.dot(X, self.w) + self.b
            y_hat = self._sigmoid(linear_model)

            # 2. Gradients
            error = y_hat - y
            dw = (1.0 / m) * np.dot(X.T, error)
            db = (1.0 / m) * np.sum(error)

            # 3. Parameter updates
            self.w -= self.lr * dw
            self.b -= self.lr * db

        return self

    def predict_proba(self, X):
        return self._sigmoid(np.dot(X, self.w) + self.b)

    def predict(self, X, threshold=0.5):
        probs = self.predict_proba(X)
        return (probs >= threshold).astype(int)

# --- Function Call & Testing ---
from sklearn.datasets import make_classification
X_data, y_data = make_classification(n_samples=200, n_features=2, n_redundant=0, random_state=42)

clf = LogisticRegressionScratch(learning_rate=0.1, epochs=1000)
clf.fit(X_data, y_data)
predictions = clf.predict(X_data)
acc = np.mean(predictions == y_data)

print(f"Scratch Logistic Regression Accuracy: {acc*100:.2f}%")
print(f"Learned Weights: {clf.w.round(4)} | Learned Bias: {clf.b:.4f}")
```

---

### 📌 Summary Points
- Scratch Logistic Regression model bina kisi external ML library ke kaam karta hai.
- Iska accuracy standard Scikit-Learn model ke barabar aata hai.
