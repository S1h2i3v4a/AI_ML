# Lecture 28.13: Variance Reduction as Impurity Metric for Regression Trees

## 📌 Executive Summary
Mathematical formulation of Variance Reduction, Mean Squared Error (MSE) node impurity, Mean Absolute Error (MAE) median criteria, and split evaluation for regression trees.

---

## 🏛️ Theoretical Formulation & Mathematical Architecture

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

## 💻 Vectorized Python Implementation

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

## 🔬 Key Engineering Takeaways & Invariants
1. **Axis-Aligned Partitioning**: Decision trees recursively split feature space along orthogonal boundaries without requiring feature scaling.
2. **Impurity Optimization**: Split selection deterministically maximizes impurity reduction (Information Gain for classification, Variance Reduction for regression).
3. **Generalization Safeguards**: Regularization via pre-pruning (`max_depth`, `min_samples_leaf`) and post-pruning (`ccp_alpha`) prevents noisy leaf memorization.
