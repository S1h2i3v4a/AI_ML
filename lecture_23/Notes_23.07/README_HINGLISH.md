# Notes_23.07: Linear Regression Ki Shuruat [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne **Linear Regression** ka core concept samjhaya hai: $y = mx + c$ ki straight line se machine learning model kaise predictions karta hai.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Linear Regression kya hoti hai?
- Straight line ki equation: $y = mx + c$ (ya $\hat{y} = w_1 x + w_0$).
- Slope ($m$) aur Intercept ($c$) ka real-world matlab.
- Experience vs Salary ka blackboard example.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Straight Line Ki Equation:

$$
\hat{y} = mx + c
$$

- **$x$ (Input Feature)**: Jaise kisi employee ka Experience (saalon mein).
- **$m$ (Slope / Weight)**: Har 1 saal experience badhne par salary kitni badhegi? (Jaise ₹2.5 Lakh per year).
- **$c$ (Intercept / Bias)**: Agar kisi ka 0 saal experience hai (Fresher), toh uski base salary kitni hogi? (Jaise ₹3.0 Lakh).
- **$\hat{y}$ (Predicted Output)**: Model dwara predict ki gayi salary.

---

### 📊 Visual Flowchart: Equation Flow

```mermaid
flowchart LR
    A["Experience x"] --> B["Multiply by Slope m (₹2.5L)"]
    B --> C["Add Base Intercept c (₹3L)"]
    C --> D["Final Salary Prediction y_hat"]
```

---

### 💻 Python Code

```python
import numpy as np

def compute_linear_regression_line(x_vals, m, c):
    """
    Computes Linear Regression line predictions:
        y_hat = m * x + c
        
    Args:
        x_vals: 1D array of input feature values
        m: Slope (Weight / Coefficient w1)
        c: Intercept (Bias w0)
        
    Returns:
        1D array of predicted y_hat values
    """
    y_hat = m * np.array(x_vals) + c
    return y_hat

# --- Function Call & Testing ---
# Experience in years (x) vs Salary in lakhs (y)
experience = np.array([1, 2, 3, 4, 5])
# Suppose m = 2.5 (2.5 Lakhs per year of exp) and c = 3.0 (Base salary 3 Lakhs)
predicted_salary = compute_linear_regression_line(experience, m=2.5, c=3.0)

print(f"{'Experience (Years)':<20} | {'Predicted Salary (Lakhs)':<25}")
print("-" * 50)
for exp, sal in zip(experience, predicted_salary):
    print(f"{exp:<20} | {sal:<25.2f}")
```

---

### 📌 Summary Points
- Linear regression data points ke beech se ek best fit straight line guzaarti hai.
- $m$ line ka dhalan batata hai aur $c$ line ka starting point.
