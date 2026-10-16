# Lecture 28.13: Variance Reduction as Impurity Metric for Regression Trees

## 📌 Executive Summary (Hinglish)
Variance Reduction ka mathematical formulation, MSE node impurity, MAE median criteria, aur regression trees mein optimal continuous split selection.

---

### 📋 Is Topic/Section Mein Hum Kya Cover Kar Rahe Hain?
1. Regression impurity metric: Node Mean Squared Error $MSE(S) = \frac{1}{|S|} \sum (y_i - \bar{y})^2$.
2. Variance Reduction split selection formula: $\Delta V(S, A) = \text{Var}(S) - \left( \frac{|S_L|}{|S|} \text{Var}(S_L) + \frac{|S_R|}{|S|} \text{Var}(S_R) \right)$.
3. MSE criterion vs MAE criterion ($L_1$ loss minimizing absolute deviation via median).
4. Outlier robustness: MAE criterion extreme regression outliers se resistant rehta hai.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**Node Variance as Impurity**: Classification mein impurity classes ke mix hone se banti hai, jabki regression mein impurity target values ke spread (sample variance) se measure hoti hai.

**Variance Reduction**: Split select karte samay dekha jaata hai ki parent node ki variance se child nodes ki weighted variance kitni ghati hai. Maximum drop wala split winner banta hai.

**MSE vs MAE**: Standard criterion MSE mean predict karta hai. Agar dataset mein extreme price outliers hon, toh `criterion='absolute_error'` median predict karta hai.

**L1 Robustness**: Median-based regression outlier data points se shift nahi hota, providing clean piece-wise medians.

---

## 🏛️ Mathematical Architecture & Detailed Theory

### 📉 Variance Reduction Formulation

In regression trees, node impurity is defined by the **Sample Variance** (or Mean Squared Error) of the continuous supervisory target $y$ within node $S$:

$$
I_{\text{MSE}}(S) = \frac{1}{|S|} \sum_{i \in S} (y_i - \bar{y}_S)^2 = \text{Var}(y \mid i \in S)
$$

For a proposed split on feature $A$ generating left subset $S_L$ and right subset $S_R$:

$$
\boxed{
\Delta V(S, A) = I_{\text{MSE}}(S) - \left( \frac{|S_L|}{|S|} I_{\text{MSE}}(S_L) + \frac{|S_R|}{|S|} I_{\text{MSE}}(S_R) \right)
}
$$

The optimal split maximizes the reduction in variance $\Delta V(S, A)$, forcing children to be tightly clustered around their respective local means.

---

### 🛡️ Mean Absolute Error (MAE) Median Alternative

Under $L_1$ loss:

$$
J_{\text{MAE}}(c) = \sum_{i \in S} |y_i - c|
$$

The minimizing constant is the **sample median**:

$$
c^* = \text{median}(y_i \mid i \in S)
$$

Impurity under MAE is the Mean Absolute Deviation from the median:

$$
I_{\text{MAE}}(S) = \frac{1}{|S|} \sum_{i \in S} |y_i - \text{median}(y)|
$$

MAE provides extreme resistance against wild regression outliers (such as ₹10 crore luxury property transactions in standard housing data).

---

## 💻 Python Implementation & Code Example

```python
import numpy as np

def compute_variance_reduction(parent_y, left_y, right_y):
    n_p, n_l, n_r = len(parent_y), len(left_y), len(right_y)
    var_p = np.var(parent_y)
    weighted_child_var = (n_l / n_p) * np.var(left_y) + (n_r / n_p) * np.var(right_y)
    return var_p - weighted_child_var

# Test
p_vals = np.array([1.0, 2.0, 9.0, 10.0])
l_vals = np.array([1.0, 2.0])       # tight cluster around 1.5
r_vals = np.array([9.0, 10.0])      # tight cluster around 9.5

vr = compute_variance_reduction(p_vals, l_vals, r_vals)
print("Variance Reduction for clean split:", round(vr, 4))
assert vr > 0, "Clean separation must reduce continuous variance"

```

---

## 🎯 Quick Revision Points (Interview Notes)
- **Scale Invariance**: Decision Trees monotonically invariant hote hain, isliye inme `StandardScaler` mandatory nahi hota.
- **Gini vs Entropy**: Gini speed mein 10x faster hota hai kyunki logarithm computation ki zaroorat nahi padti.
- **Pruning Necessity**: Unconstrained decision tree hamesha overfit karti hai; `min_samples_leaf` aur `ccp_alpha` sabse effective regularizers hain.
