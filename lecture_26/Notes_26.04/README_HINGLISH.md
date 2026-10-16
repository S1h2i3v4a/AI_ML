# Lecture 26.04: Linear Regression with Gradient Descent — Step 2: Mean Squared Error (MSE) Cost Function

## 📌 Saransh (Executive Summary)
Gradient Descent Step 2: Mean Squared Error (MSE) cost function ka mathematical derivation, $\frac{1}{2m}$ scaling ka logic, aur convex loss surface ka visual breakdown.

---

## 🔬 First-Principles Theory & Intuition
### 1. Step 2: Predictions Calculate Karna Aur Cost Compute Karna
Model jab weights initialize kar leta hai, tab woh har iteration mein pehle prediction $\hat{y}$ calculate karta hai:

$$
\hat{y}^{(i)} = \mathbf{w}^T \mathbf{x}^{(i)} + b
$$

Aur phir check karta hai ki model ne kitni badi galti (error / residual) ki:

$$
e^{(i)} = \hat{y}^{(i)} - y^{(i)}
$$

### 2. Mean Squared Error (MSE) Ka Formula
Sari galtiyon ka square karke average nikalne ko Mean Squared Error kehte hain:

$$
J(\mathbf{w}, b) = \frac{1}{2m} \sum_{i=1}^m \left( \hat{y}^{(i)} - y^{(i)} \right)^2
$$

### 3. Formula Mein $\frac{1}{2}$ Kyun Lagate Hain?
Square term $(z)^2$ ka derivative $2z$ hota hai.
Agar hum formula mein pehle se $\frac{1}{2}$ laga denge, toh derivative lete waqt 2 aur $\frac{1}{2}$ aapas mein cancel out ho jayenge!
Is mathematical convenience se derivative bilkul clean aur simple ban jata hai.


---

## 💻 Python & NumPy Code Implementation
```python
import numpy as np

def compute_mse_cost(X, y, weights, bias):
    """Compute vectorized Mean Squared Error cost J(w, b)."""
    m = len(y)
    y_pred = X @ weights + bias
    residuals = y_pred - y
    cost = (1.0 / (2.0 * m)) * np.sum(residuals ** 2)
    return cost

# Test cost computation
X_demo = np.array([[1.0], [2.0], [3.0], [4.0]])
y_demo = np.array([2.0, 4.0, 6.0, 8.0])

w_good = np.array([2.0])
b_good = 0.0

w_bad = np.array([0.5])
b_bad = 1.0

print(f"Optimal Parameters Cost: {compute_mse_cost(X_demo, y_demo, w_good, b_good):.6f}")
print(f"Sub-optimal Parameters Cost: {compute_mse_cost(X_demo, y_demo, w_bad, b_bad):.6f}")

```

---

## 🎯 Key Takeaways & Practical Tips
1. **Black-Box Se Azadi**: Libraries ko blind use karne ke bajaye unke andar ka math samajhna aapko top 1% engineer banata hai.
2. **Vectorization Ki Taqat**: Python loops ke bajaye NumPy array operations use karein jo C/BLAS speed provide karte hain.
3. **Debugging Mastery**: Jab loss decrease na ho raha ho, toh sabse pehle learning rate $\alpha$ aur gradient dimensions check karein.
