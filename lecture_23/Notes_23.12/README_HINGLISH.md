# Module 23.12: Linear Regression Foundations Ka Summary

## 1. Teeno Core Pillars Ka Revision

Linear Regression poori tarah in teen pillars par tikka hai:

1. **Hypothesis:** $\hat{y} = \mathbf{w}^T \mathbf{x} + b$ (Straight line ya Hyperplane).
2. **Cost Function:** $J(\mathbf{w}, b) = \frac{1}{2m} \sum (\hat{y}^{(i)} - y^{(i)})^2$ (Strictly convex bowl).
3. **Solver:** Minimum parameters dhoondhne ka tareeqa (Normal Equation vs Gradient Descent).

---

## 2. Normal Equation vs Gradient Descent

Machine Learning mein model train karne ke do tareeqe hote hain:

### 1. Normal Equation (Closed-form Exact Solution):
$$
\mathbf{w}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}
$$
- Koi learning rate $\alpha$ ya loop ki zaroorat nahi hoti.
- Lekin jab features $d > 10,000$ se zyada ho jate hain, to $(X^T X)^{-1}$ matrix inversion compute karna $\mathcal{O}(d^3)$ complexity ki wajah se computer ko hang kar deta hai.

### 2. Gradient Descent (Iterative Solution):
$$
\mathbf{w} := \mathbf{w} - \alpha \nabla J(\mathbf{w})
$$
- Ye massive datasets aur millions of features par smoothly kaam karta hai.
- Lekin isme learning rate $\alpha$ tune karna padta hai aur feature scaling zaroori hoti hai.

---

## 3. Gradient Descent Ke 3 Types

1. **Batch Gradient Descent:** Poore dataset ko dekh kar 1 step leta hai. Bohot smooth hota hai par bade dataset par slow.
2. **Stochastic Gradient Descent (SGD):** Har 1 single data point ko dekh kar 1 step leta hai. Bohot fast hota hai par rasta zig-zag hota hai.
3. **Mini-Batch Gradient Descent:** 32, 64 ya 128 samples ka batch lekar step leta hai. GPU vectorization ka best use karta hai aur modern deep learning ka gold standard hai.

---

## 4. Feature Scaling Kyu Zaroori Hai?

Agar ek feature age (18-60) hai aur doosra salary (20,000-5,00,000) hai, to cost surface bohot lamba aur patla ellipse ban jayega. Isse gradient descent bohot zig-zag karega.
Jab hum features ko scale (StandardScaler: mean=0, std=1) kar dete hain, to surface ek perfect circular bowl ban jata hai, jisse gradient descent seedha center ki taraf fast converge hota hai!
