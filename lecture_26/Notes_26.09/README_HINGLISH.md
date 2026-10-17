# Notes_26.09: Logistic Regression Ke Steps Aur Sigmoid Function [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne classification ke liye **Logistic Regression** ka concept samjhaya hai: Linear equation $z = Xw + b$ ko **Sigmoid function** se guzar kar probability (0 se 1) kaise banaya jata hai.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Classification mein seedha Linear Regression kyu fail hota hai?
- **Sigmoid Function** ($g(z) = \frac{1}{1 + e^{-z}}$) ka S-shape curve.
- 0.5 decision threshold ka matlab.
- Logistic Regression ke core steps.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Linear Line Se Probability Kyu Nahi Banti?
Linear line seedhi hoti hai: wo $-\infty$ se $+\infty$ tak chali jaati hai. Probability kabhi 1 se badi ya 0 se chhoti nahi ho sakti. Isliye hume ek aisi function chahiye jo kisi bhi number ko **0 aur 1 ke beech** mein lock kar de.

#### 2. Sigmoid Function Ka Formula:
$$g(z) = \frac{1}{1 + e^{-z}}$$
- Agar $z = 0$ hai, toh $g(z) = 0.5$ hota hai.
- Agar $z$ bohot bada positive number hai, toh $g(z) \approx 1$.
- Agar $z$ bohot bada negative number hai, toh $g(z) \approx 0$.

---

### 📊 Visual Flowchart: Probability Se Decision Tak

```mermaid
flowchart TD
    A["Input x"] --> B["Linear Formula: z = w*x + b"]
    B --> C["Sigmoid Function: g(z) = 1 / (1 + e^-z)"]
    C --> DKya probability >= 0.5 hai?
    D -->|"Haan"| E["Predict: Class 1"]
    D -->|"Nahi"| F["Predict: Class 0"]
```

---

### 💻 Python Code

```python
import numpy as np

def compute_sigmoid(z):
    """
    Sigmoid activation function: g(z) = 1 / (1 + exp(-z))
    Maps any real-valued number (-inf, +inf) strictly into (0, 1),
    allowing continuous values to represent probabilities.
    """
    # Clip z to prevent numerical overflow in exp(-z)
    z_clipped = np.clip(z, -500, 500)
    return 1.0 / (1.0 + np.exp(-z_clipped))

def predict_class_label(probability, threshold=0.5):
    """Classifies probability into 0 or 1 based on decision threshold."""
    return 1 if probability >= threshold else 0

# --- Function Call & Testing ---
test_z_values = np.array([-5.0, -1.0, 0.0, 1.0, 5.0])
probabilities = compute_sigmoid(test_z_values)

print("Linear score (z):", test_z_values)
print("Sigmoid Probabilities (0 to 1):", probabilities.round(4))
print("Class Predictions (threshold=0.5):", [predict_class_label(p) for p in probabilities])
```

---

### 📌 Summary Points
- Sigmoid function continuous numbers ko probability (0 se 1) mein convert karta hai.
- Default threshold 0.5 hota hai.
