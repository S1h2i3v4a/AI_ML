# Notes_26.03: Linear Regression GD (Step 1 — Initialization) [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne Gradient Descent ka **Pehla Step (Step 1)** samjhaya hai: parameters ($w$ aur $b$) ko shuruat mein kya value dein aur hyperparameters kaise set karein.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Weights ($w$) aur Bias ($b$) ko zero initialize karna.
- Linear regression mein zero initialization safe kyu hota hai?
- Learning rate ($\alpha$) aur Epochs ka role.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Zero Initialization Kyu Safe Hai?
Linear regression ka loss function ek **Convex Parabola** (single minimum waala katora) hota hai. Isme multiple local minima nahi hote. Isliye aap chahe $w=0, b=0$ se shuru karo, Gradient Descent hamesha ghum kar sahi bottom par hi pahuchega!

#### 2. Core Hyperparameters:
- **`learning_rate` ($\alpha$)**: Har step mein kitna aage badhna hai (jaise $0.01$). Agar bohot bada loge toh katora cross kar jaoge; bohot chhota loge toh bohot slow chaloge.
- **`epochs`**: Poori cycle ko kitni baar chalana hai (jaise 1000 baar).

---

### 💻 Python Code

```python
import numpy as np

def initialize_parameters(n_features):
    """
    Step 1 of Gradient Descent: Initialize parameters.
    In Linear Regression, initializing weights to zeros is safe
    because the MSE cost surface is strictly convex (parabolic).
    """
    weights = np.zeros(n_features)
    bias = 0.0
    return weights, bias

# --- Function Call & Testing ---
w_init, b_init = initialize_parameters(n_features=5)
print("Initialized Weights Vector (Zeros):", w_init)
print("Initialized Bias Scalar:           ", b_init)
```

---

### 📌 Summary Points
- Step 1: Weights ko zero vector aur bias ko 0.0 se shuru karo.
- Learning rate aur epochs hyperparameters hain.
