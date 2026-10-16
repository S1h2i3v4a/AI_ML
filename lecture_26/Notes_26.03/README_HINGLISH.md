# Lecture 26.03: Linear Regression with Gradient Descent — Step 1: Model & Parameter Initialization

## 📌 Saransh (Executive Summary)
Gradient Descent workflow ka Step 1: Object-Oriented class design, weights aur bias ki initialization strategies, aur learning rate hyperparameters ki setting.

---

## 🔬 First-Principles Theory & Intuition
### 1. Step 1: Class Setup Aur Weights Initialization
Gradient Descent ek iterative process hai jo step-by-step best parameters dhoondhta hai. Is process ko shuru karne ke liye pehla step hota hai parameters ko initialize karna.

### 2. Zero Initialization Safe Kyun Hai?
Deep Neural Networks mein agar saare weights zero kar diye jayein, toh saare neurons same output produce karte hain (symmetry breaking problem).
Lekin Linear Regression mein cost function ek **Convex Paraboloid (Katori / Bowl shape)** hota hai. Iska sirf ek hi global minimum hota hai, koi local minima nahi hota!
Isliye weights ko `np.zeros(n)` aur bias ko `0` se initialize karna 100% mathematically safe aur standard practice hai:

$$
\mathbf{w} = [0, 0, \dots, 0]^T, \quad b = 0
$$

### 3. Hyperparameters Ka Role
- **Learning Rate ($\alpha$)**: Har step mein kitna bada kadam lena hai. Agar bohot chhota hoga toh saalon lag jayenge; agar bohot bada hoga toh minimum se aage nikal kar diverge ho jayega.
- **Iterations (`n_iter`)**: Loop kitni baar chalana hai (e.g. 1000 epochs).


---

## 💻 Python & NumPy Code Implementation
```python
import numpy as np

class LinearRegressionGDStep1:
    """Step 1: Boilerplate OOP Model Architecture with Parameter Initialization."""
    def __init__(self, lr=0.01, n_iter=1000):
        self.lr = lr
        self.n_iter = n_iter
        self.weights = None
        self.bias = None
        
    def _initialize_parameters(self, n_features: int):
        self.weights = np.zeros(n_features)
        self.bias = 0.0
        print(f"Initialized weights shape: {self.weights.shape}, bias: {self.bias}")

model = LinearRegressionGDStep1(lr=0.01, n_iter=1000)
model._initialize_parameters(n_features=5)
print("Initial weights:", model.weights)

```

---

## 🎯 Key Takeaways & Practical Tips
1. **Black-Box Se Azadi**: Libraries ko blind use karne ke bajaye unke andar ka math samajhna aapko top 1% engineer banata hai.
2. **Vectorization Ki Taqat**: Python loops ke bajaye NumPy array operations use karein jo C/BLAS speed provide karte hain.
3. **Debugging Mastery**: Jab loss decrease na ho raha ho, toh sabse pehle learning rate $\alpha$ aur gradient dimensions check karein.
