# Lecture 28.05: Entropy vs Gini Impurity — Mathematical Comparison & Invariants

## 📌 Executive Summary
Rigorous mathematical comparison of Entropy vs Gini, Taylor series connection, split selection concordance rates, and computational throughput considerations.

---

## 🏛️ Theoretical Formulation & Mathematical Architecture

### 🔬 The Taylor Series Mathematical Equivalence

While Shannon Entropy derives from information theory and Gini Impurity derives from variance of multinomial indicators, they are mathematically connected through the **first-order Taylor series expansion** of the natural logarithm:

$$
\ln(x) = -\sum_{n=1}^\infty \frac{(1-x)^n}{n} \approx -(1 - x) = x - 1 \quad \text{for } x \approx 1
$$

Expressing Entropy in natural log base:

$$
H_e(S) = -\sum_{k=1}^K p_k \ln(p_k)
$$

Substituting $\ln(p_k) \approx p_k - 1$:

$$
H_e(S) \approx -\sum_{k=1}^K p_k (p_k - 1) = \sum_{k=1}^K (p_k - p_k^2) = 1 - \sum_{k=1}^K p_k^2 = G(S)
$$

Thus, **Gini Impurity is the first-order Taylor polynomial approximation of Shannon Entropy**.

---

### ⚖️ Side-by-Side Architectural Summary

| Metric Feature | Shannon Entropy $H(S)$ | Gini Impurity $G(S)$ |
| :--- | :--- | :--- |
| **Formula** | $-\sum p_k \log_2 p_k$ | $1 - \sum p_k^2$ |
| **Binary Range** | $[0.0, 1.0]$ bits | $[0.0, 0.5]$ |
| **Peak (Binary)** | $1.0$ at $p=0.5$ | $0.5$ at $p=0.5$ |
| **Computation Cost** | Higher (calls `log2`, SIMD transcendentals) | Minimal (pure algebraic multiply-accumulate) |
| **Default In** | ID3, C4.5, C5.0 | CART, Scikit-Learn `DecisionTreeClassifier` |
| **Split Selection** | Slightly favors balanced splits | Slightly favors isolating dominant pure classes |

---

## 💻 Vectorized Python Implementation

```python
import numpy as np

p = np.linspace(0.01, 0.99, 100)
entropy = -p * np.log2(p) - (1-p) * np.log2(1-p)
gini = 2 * p * (1-p)
scaled_entropy = 0.5 * entropy

# Measure absolute maximum deviation between scaled entropy and Gini
max_diff = np.max(np.abs(scaled_entropy - gini))
print(f"Max absolute divergence between 0.5*Entropy and Gini: {max_diff:.4f}")
assert max_diff < 0.08, "Scaled entropy and Gini must be tightly aligned!"

```

---

## 🔬 Key Engineering Takeaways & Invariants
1. **Axis-Aligned Partitioning**: Decision trees recursively split feature space along orthogonal boundaries without requiring feature scaling.
2. **Impurity Optimization**: Split selection deterministically maximizes impurity reduction (Information Gain for classification, Variance Reduction for regression).
3. **Generalization Safeguards**: Regularization via pre-pruning (`max_depth`, `min_samples_leaf`) and post-pruning (`ccp_alpha`) prevents noisy leaf memorization.
