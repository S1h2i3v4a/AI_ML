# Lecture 26.09: Logistic Regression (Formulation & Steps)

## 📌 Topic Overview
In this lecture, Shraddha ma'am introduces **Logistic Regression** for classification, explaining the mathematical need for the **Sigmoid Activation Function** to map continuous values into probabilities between 0 and 1.

---

## 🏛️ The Sigmoid Activation Function

$$g(z) = \frac{1}{1 + e^{-z}}$$

Where $z = Xw + b$.

- When $z \to +\infty$, $g(z) \to 1$.
- When $z \to -\infty$, $g(z) \to 0$.
- When $z = 0$, $g(0) = \frac{1}{1 + 1} = 0.50$ (the decision boundary).

---

## 📊 Visual Diagram: Sigmoid S-Curve & Decision Threshold

```mermaid
flowchart LR
    LinearInput["Linear Score z = Xw + b<br/>Range: (-∞, +∞)"] --> Sigmoid["Sigmoid Function<br/>g(z) = 1 / (1 + e^-z)<br/>Range: (0, 1)"]
    Sigmoid --> DecisionIs g(z) >= 0.5 ?
    Decision -->|"Yes"| Class1["Predict Positive (Class 1)"]
    Decision -->|"No"| Class0["Predict Negative (Class 0)"]
```

---

## 💻 Python Implementation

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

## 🔑 Key Takeaways
1. Linear Regression cannot predict binary classes because straight lines exceed $[0, 1]$.
2. The Sigmoid curve squashes the continuous line into valid probabilities.
3. A threshold of $0.5$ separates Class 0 from Class 1.
