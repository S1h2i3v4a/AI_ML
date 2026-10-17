# Notes_26.04: Linear Regression GD (Step 2 — MSE Cost Calculation) [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne Gradient Descent ka **Doosra Step (Step 2)** samjhaya hai: **Mean Squared Error (MSE)** cost function ka formula aur iska code.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Prediction error (residuals) kya hota hai?
- Mean Squared Error ka formula: $J = \frac{1}{2m} \sum (\hat{y} - y)^2$.
- Formula mein $\frac{1}{2}$ kyu lagaya jata hai?
- Python mein vectorized cost calculation.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. MSE Formula Ka Logic
Har sample par model ka error hota hai: $(\hat{y} - y)$.
1. Agar hum sirf error jodein, toh positive aur negative error aapas mein cancel ho kar 0 ban sakte hain!
2. Isliye hum **Square** karte hain: $(\hat{y} - y)^2$. Square karne se saare errors positive ho jaate hain aur badi galtiyon par bohot bada penalty lagta hai.
3. Fir sabhi samples ka average nikaalne ke liye $m$ se divide karte hain.

#### 2. Formula Mein 1/2 Kyu Aaya?
Derivative lete waqt jab power 2 aage aati hai, toh yeh $\frac{1}{2}$ se cut ho jaati hai! Yeh sirf calculus ko aasan aur clean banane ke liye lagaya jata hai.

---

### 💻 Python Code

```python
import numpy as np

def compute_mse_cost(y_true, y_pred):
    """
    Step 2 of Gradient Descent: Compute Mean Squared Error (MSE) Cost.
    Formula: J = (1 / (2 * m)) * sum((y_pred - y_true)^2)
    
    The 1/2 factor simplifies calculus derivatives.
    """
    m = len(y_true)
    if m == 0:
        return 0.0
    error_residuals = y_pred - y_true
    cost = (1.0 / (2.0 * m)) * np.sum(error_residuals ** 2)
    return float(cost)

# --- Function Call & Testing ---
actual_vals    = np.array([3.0, -0.5, 2.0, 7.0])
predicted_vals = np.array([2.5,  0.0, 2.0, 8.0])

loss = compute_mse_cost(actual_vals, predicted_vals)
print(f"Calculated MSE Loss (J): {loss:.4f}")
```

---

### 📌 Summary Points
- Step 2 model ke error ko measure karta hai.
- MSE hamesha positive value deta hai.
