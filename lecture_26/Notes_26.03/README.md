# Lecture 26.03: Linear Regression GD (Step 1 — Initialization)

## 📌 Topic Overview
In this lecture, Shraddha ma'am explains **Step 1 of Gradient Descent**: how to initialize weights and bias, and set learning hyperparameters.

---

## ⚙️ Hyperparameters & Initialization
1. **Weights Initialization**: Set $w = \mathbf{0}$ (vector of zeros of length $d$). Because linear regression has a strictly convex loss surface, zero initialization is completely safe and guaranteed to converge.
2. **Bias Initialization**: Set $b = 0.0$.
3. **Learning Rate ($\alpha$)**: Step size taken along the negative gradient (e.g., $0.01$ or $0.001$).
4. **Number of Iterations ($epochs$)**: Total passes through the gradient update loop.

---

## 💻 Python Implementation

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

## 🔑 Key Takeaways
1. Linear Regression parameters can be safely initialized to zeros.
2. Neural networks require random initialization to break symmetry, but convex linear models do not.
