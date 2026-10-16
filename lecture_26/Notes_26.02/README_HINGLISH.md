# Lecture 26.02: Linear Regression from Scratch — Mathematical Formulation & Hypothesis

## 📌 Saransh (Executive Summary)
Linear Regression ke mathematical hypothesis ka deep breakdown, feature space se continuous target mapping, Best Fit Line (BFL) geometry, aur affine hyperplanes ka algebraic structure.

---

## 🔬 First-Principles Theory & Intuition
### 1. Linear Regression Ka Core Objective
Supervised learning regression task mein hamare paas $m$ samples ka data hota hai:

$$
\mathcal{D} = \left\{ (\mathbf{x}^{(1)}, y^{(1)}), (\mathbf{x}^{(2)}, y^{(2)}), \dots, (\mathbf{x}^{(m)}, y^{(m)}) \right\}
$$

Jahan $\mathbf{x}^{(i)}$ input features hain aur $y^{(i)}$ continuous real number target value hai (jaise house price, salary, ya temperature).

### 2. Hypothesis Function Ki Formulation
Linear Regression ka fundamental assumption yeh hai ki target variable $y$, input features ka ek linear combination hai:

$$
h_\theta(\mathbf{x}) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_d x_d
$$

- $\theta_0$ ko **Bias ya Intercept** kehte hain. Yeh line/hyperplane ka vertical position define karta hai jab saare features zero hon.
- $\theta_1, \dots, \theta_d$ ko **Weights ya Slopes** kehte hain. Yeh batate hain ki kisi feature ke 1 unit badhne se target kitna badlega.

### 3. Best Fit Line (BFL) Ki Geometry
2D space ($d=1$) mein yeh line $y = mx + c$ banti hai.
Multi-dimensional space ($d > 1$) mein yeh line ek $(d+1)$-dimensional **Hyperplane** ban jaati hai.
Humara goal aise optimal $\mathbf{w}$ aur $b$ dhoondhna hai jisse predicted line aur actual data points ke beech ka gap (residual error) minimum ho sake.


---

## 💻 Python & NumPy Code Implementation
```python
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic linear regression dataset
np.random.seed(42)
m = 50
X = 2 * np.random.rand(m, 1)
true_w = 3.5
true_b = 4.2
y = true_w * X + true_b + np.random.randn(m, 1) * 0.8

# Hypothesis prediction function
def predict_linear(X, w, b):
    return X @ w + b

# Evaluate with sample weights
w_init = np.array([[2.0]])
b_init = 2.0
y_pred = predict_linear(X, w_init, b_init)

print(f"Sample X shape: {X.shape}, y shape: {y.shape}")
print(f"Predictions first 5: \n{y_pred[:5].flatten()}")

```

---

## 🎯 Key Takeaways & Practical Tips
1. **Black-Box Se Azadi**: Libraries ko blind use karne ke bajaye unke andar ka math samajhna aapko top 1% engineer banata hai.
2. **Vectorization Ki Taqat**: Python loops ke bajaye NumPy array operations use karein jo C/BLAS speed provide karte hain.
3. **Debugging Mastery**: Jab loss decrease na ho raha ho, toh sabse pehle learning rate $\alpha$ aur gradient dimensions check karein.
