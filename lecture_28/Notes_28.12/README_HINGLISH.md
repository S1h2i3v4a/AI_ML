# Lecture 28.12: Decision Tree Regressor — Continuous Partitioning aur Piecewise Constants

## 📌 Executive Summary (Hinglish)
Continuous target regression ke liye Decision Trees ka formulation, feature space ko orthogonal regions $R_m$ mein partition karna, aur regional sample mean $\bar{y}_m$ se prediction karna.

---

### 📋 Is Topic/Section Mein Hum Kya Cover Kar Rahe Hain?
1. Decision Tree Regressor ka objective: Continuous target variable $y \in \mathbb{R}$ ko predict karna.
2. Feature space ko $M$ disjoint hyper-rectangles $R_1, R_2, \dots, R_M$ mein partition karna.
3. Optimal leaf output: Regional sample mean $c_m = \text{mean}(y_i \mid \mathbf{x}_i \in R_m)$.
4. Piecewise constant step-function approximation ki non-linear characteristics.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**Continuous Regression**: Classification mein classes hoti hain, jabki regression mein continuous numerical values predict karni hoti hain (jaise house prices ya customer lifetime spend).

**Space Partitioning**: Regressor feature space ko orthogonal boxes $R_m$ mein divide karta hai. Har box ke andar model ek constant horizontal value predict karta hai.

**Leaf Mean Calculation**: Squared error loss $\sum (y_i - c)^2$ ko minimize karne wala optimal constant value sample mean $\bar{y} = \frac{1}{N_m} \sum y_i$ hoti hai.

**Piecewise Constant Nature**: Tree smooth linear lines draw nahi karti balki stair-case (step function) curve banati hai, jo non-linear trends ko naturally approximate karti hai.

---

## 🏛️ Mathematical Architecture & Detailed Theory

### 📈 Regression Trees & Piecewise Constant Approximations

When the target supervisory response is continuous ($y \in \mathbb{R}$), the tree partitions the domain $\mathcal{X}$ into $M$ disjoint orthogonal regions $\{R_1, R_2, \dots, R_M\}$:

$$
\mathcal{X} = \bigcup_{m=1}^M R_m \quad \text{where } R_j \cap R_k = \emptyset \quad \forall j \neq k
$$

The model represents the global continuous response function as a linear combination of indicator basis functions:

$$
\boxed{
f(\mathbf{x}) = \sum_{m=1}^M c_m \cdot \mathbb{I}(\mathbf{x} \in R_m)
}
$$

---

### 📐 Mathematical Derivation of Optimal Leaf Prediction $c_m$

Under the classical Sum of Squared Errors (SSE) loss criterion:

$$
J(c_m) = \sum_{i \in R_m} (y_i - c_m)^2
$$

To find the minimizing constant $c_m^*$, compute the partial derivative with respect to $c_m$ and set to zero:

$$
\frac{\partial J}{\partial c_m} = -2 \sum_{i \in R_m} (y_i - c_m) = 0
$$

$$
\sum_{i \in R_m} y_i - |R_m| c_m = 0 \implies \boxed{c_m^* = \frac{1}{|R_m|} \sum_{i \in R_m} y_i = \bar{y}_{R_m}}
$$

Thus, the optimal leaf prediction under squared error loss is strictly the **sample mean** of all training instances assigned to region $R_m$.

---

## 💻 Python Implementation & Code Example

```python
import numpy as np
from sklearn.tree import DecisionTreeRegressor

# Generate non-linear 1D sine signal
np.random.seed(42)
X_1d = np.sort(np.random.uniform(0, 10, 80)).reshape(-1, 1)
y_1d = np.sin(X_1d).ravel() + np.random.normal(0, 0.1, 80)

reg = DecisionTreeRegressor(max_depth=3, random_state=42)
reg.fit(X_1d, y_1d)

preds = reg.predict(X_1d)
print("Unique Piecewise Constant Levels:", len(np.unique(preds)))
assert len(np.unique(preds)) <= 2**3, "Depth 3 tree cannot have more than 8 distinct levels"

```

---

## 🎯 Quick Revision Points (Interview Notes)
- **Scale Invariance**: Decision Trees monotonically invariant hote hain, isliye inme `StandardScaler` mandatory nahi hota.
- **Gini vs Entropy**: Gini speed mein 10x faster hota hai kyunki logarithm computation ki zaroorat nahi padti.
- **Pruning Necessity**: Unconstrained decision tree hamesha overfit karti hai; `min_samples_leaf` aur `ccp_alpha` sabse effective regularizers hain.
