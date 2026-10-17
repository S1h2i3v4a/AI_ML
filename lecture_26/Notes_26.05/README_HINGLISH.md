# Notes_26.05: Linear Regression GD (Step 3 — Gradients Calculation) [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne Calculus chain rule ka use karke **Step 3: Gradients ($dw$ aur $db$)** nikaalna sikhaya hai.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Gradient kya hota hai? (Slope / Dhalan).
- Weights ke respect mein derivative: $dw = \frac{1}{m} X^T (\hat{y} - y)$.
- Bias ke respect mein derivative: $db = \frac{1}{m} \sum (\hat{y} - y)$.
- Negative gradient ki taraf chalne ka concept.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Gradient Ka Asal Matlab:
Agar aap pahad par khade hain aur aapko sabse tezi se neeche utarna hai, toh gradient batata hai ki sabse teez dhalan kis disha mein hai.
- Positive slope ka matlab hai weights zyada hain, unhe ghatao.
- Negative slope ka matlab hai weights kam hain, unhe badhao.

#### 2. Formulas:
- **$dw$**: Saare features ke errors ko inputs ke sath multiply karke average nikaalta hai: $\frac{1}{m} X^T (\hat{y} - y)$.
- **$db$**: Sirf seedhe errors ka average hota hai: $\frac{1}{m} \sum (\hat{y} - y)$.

---

### 💻 Python Code

```python
import numpy as np

def compute_linear_regression_gradients(X, y_true, y_pred):
    """
    Step 3 of Gradient Descent: Compute partial derivatives of MSE cost.
    Chain Rule Derivatives:
    dw = dJ/dw = (1 / m) * X^T * (y_pred - y_true)
    db = dJ/db = (1 / m) * sum(y_pred - y_true)
    """
    m = len(y_true)
    error = y_pred - y_true

    # Vectorized gradient computation
    dw = (1.0 / m) * np.dot(X.T, error)
    db = (1.0 / m) * np.sum(error)

    return dw, db

# --- Function Call & Testing ---
X_test = np.array([[1.0, 2.0], [2.0, 1.0], [3.0, 4.0]])
y_actual = np.array([5.0, 4.0, 11.0])
y_predicted = np.array([4.5, 3.8, 10.2])

dw_grad, db_grad = compute_linear_regression_gradients(X_test, y_actual, y_predicted)
print("Weight Gradients (dw):", dw_grad.round(4))
print("Bias Gradient (db):   ", round(db_grad, 4))
```

---

### 📌 Summary Points
- Gradients batate hain ki parameters ko kitna aur kis disha mein badalna hai.
- Vectorized $X^T (\hat{y} - y)$ se saare weights ke gradients ek baar mein nikal jaate hain.
