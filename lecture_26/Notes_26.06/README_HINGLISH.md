# Notes_26.06: Linear Regression GD (Step 4 — Update Rule Aur Poora Model) [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne Gradient Descent ka aakhri step (**Step 4: Parameter Updates**) samjhaya hai aur chaaron steps ko ek complete **Object-Oriented Programming (OOP) Class** mein assemble karke dikhaya hai.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Parameter update formula: $w := w - \alpha \cdot dw$ aur $b := b - \alpha \cdot db$.
- Learning rate $\alpha$ ka role.
- 4 steps ko assemble karke complete `LinearRegressionScratch` class banana.
- Synthetic data par model ko train karke true slope aur intercept nikalna.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Step 4: Update Rule Ka Logic
Har epoch mein hum weights ko thoda sa sudharte hain:
- $w = w - \alpha \cdot dw$
- $b = b - \alpha \cdot db$

Gradients batate hain ki error kis taraf badh raha hai, toh hum minus ($-$) sign lagakar error ke ulte (opposite) disha mein step lete hain taaki error har round mein kam hota jaye!

#### 2. Chaaron Steps Ka Ek Glance:
1. **Step 1**: $w=0, b=0$ se shuru karo.
2. **Step 2**: Prediction $\hat{y} = Xw + b$ aur error $J$ nikalo.
3. **Step 3**: Dhalan (gradients $dw, db$) calculate karo.
4. **Step 4**: Weights aur bias ko update karo ($w = w - \alpha dw$).

---

### 📊 Visual Flowchart: Gradient Descent Ka Poora Loop

```mermaid
flowchart TD
    A["Step 1: w = 0, b = 0 se start karo"] --> B["Epoch Loop Shuru"]
    B --> C["Step 2: y_hat = Xw + b aur Cost J nikalo"]
    C --> D["Step 3: Gradients dw aur db calculate karo"]
    D --> E["Step 4: Parameters update karo: w = w - lr*dw"]
    E --> FEpochs khatam huye?
    F -->|"Nahi"| B
    F -->|"Haan"| G["Model Train Ho Gaya! (Best Fit Line Mil Gayi)"]
```

---

### 💻 Python Code

```python
import numpy as np

class LinearRegressionScratch:
    """
    Complete Scratch Implementation of Linear Regression with Gradient Descent:
    Step 1: Initialize weights (w) and bias (b) to zeros.
    Step 2: Predict y_hat and calculate MSE cost.
    Step 3: Compute gradients (dw, db).
    Step 4: Update parameters: w = w - lr * dw, b = b - lr * db.
    """
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.lr = learning_rate
        self.epochs = epochs
        self.w = None
        self.b = None
        self.cost_history = []

    def fit(self, X, y):
        m, d = X.shape
        # Step 1: Initialize
        self.w = np.zeros(d)
        self.b = 0.0
        self.cost_history = []

        for _ in range(self.epochs):
            # Step 2: Hypothesis & Cost
            y_hat = np.dot(X, self.w) + self.b
            cost = (1.0 / (2.0 * m)) * np.sum((y_hat - y) ** 2)
            self.cost_history.append(cost)

            # Step 3: Gradients
            error = y_hat - y
            dw = (1.0 / m) * np.dot(X.T, error)
            db = (1.0 / m) * np.sum(error)

            # Step 4: Parameter Updates
            self.w -= self.lr * dw
            self.b -= self.lr * db

        return self

    def predict(self, X):
        return np.dot(X, self.w) + self.b

# --- Function Call & Testing ---
np.random.seed(42)
X_synthetic = 2 * np.random.rand(100, 1)
# True relationship: y = 4 + 3x
y_synthetic = 4 + 3 * X_synthetic.squeeze() + np.random.randn(100) * 0.2

model = LinearRegressionScratch(learning_rate=0.1, epochs=500)
model.fit(X_synthetic, y_synthetic)

print(f"True slope: 3.0 | Learned Weight (w): {model.w[0]:.4f}")
print(f"True bias:  4.0 | Learned Bias (b):   {model.b:.4f}")
print(f"Initial Cost: {model.cost_history[0]:.4f} -> Final Cost: {model.cost_history[-1]:.4f}")
```

---

### 📌 Summary Points
- 4 simple steps ko loop mein chalane se model fit hota hai.
- Scratch class Scikit-Learn ke `fit()` aur `predict()` API ki tarah hi kaam karti hai.
