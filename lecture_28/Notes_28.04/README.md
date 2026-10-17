# Lecture 28.04: Gini Impurity

## 📌 Topic Overview
In this lecture, we study the second major impurity metric: **Gini Impurity**. This is the default metric used by CART and Scikit-Learn. We examine who invented it, its formula, range, and blackboard calculation.

---

## 🏛️ What is Gini Impurity?
Named after the Italian statistician and demographer **Corrado Gini**, Gini Impurity measures:
> **The likelihood of a random element being misclassified if it were randomly labeled according to the class distribution in the dataset.**

The general formula is:

$$GI = 1 - \sum_{i=1}^c (p_i)^2$$

For binary classification (`Yes` and `No`):

$$GI = 1 - (p_{	ext{yes}}^2 + p_{	ext{no}}^2)$$

---

## 📊 Range of Gini Impurity for Binary Classification
- **Minimum Value = 0.0**: When all samples belong to a single class (completely pure).
- **Maximum Value = 0.5**: When classes are equally split (50% Yes and 50% No).

$$	ext{Max } GI = 1 - (0.5^2 + 0.5^2) = 1 - (0.25 + 0.25) = 1 - 0.5 = 0.5$$

> **Key Distinction**: While maximum Entropy is **1.0**, maximum Gini Impurity for binary classification is **0.5**!

---

## 🧮 Numerical Examples from Blackboard

### Example 1: Impure Node $[3n, 3y]$
- Total samples = 6
- $p_y = rac{3}{6} = 0.5$, $p_n = rac{3}{6} = 0.5$

$$GI = 1 - (p_y^2 + p_n^2) = 1 - \left( rac{1}{4} + rac{1}{4} 
ight) = 1 - rac{1}{2} = 0.5$$

### Example 2: Pure Node $[0n, 3y]$
- Total samples = 3
- $p_y = rac{3}{3} = 1.0$, $p_n = 0.0$

$$GI = 1 - (1.0^2 + 0.0^2) = 1 - 1 = 0.0$$

---

## 📈 Comparing Curves: Entropy vs Gini Impurity
On the blackboard, the instructor plots both curves on the same axes:
- The **orange curve (Entropy)** peaks at **1.0** when $p=0.5$.
- The **blue curve (Gini Impurity)** peaks at **0.5** when $p=0.5$.
- Both curves share the exact same minima ($0.0$) at $p=0$ and $p=1$.

Because both curves have virtually identical shapes, they almost always agree on which feature split is best!

---

## 💻 Python Implementation

```python
def gini_impurity(y_count, n_count):
total = y_count + n_count
if total == 0:
return 0.0
p_y = y_count / total
p_n = n_count / total
return 1.0 - (p_y**2 + p_n**2)

print("Gini of [3y, 3n] (50-50):", gini_impurity(3, 3))
print("Gini of [0y, 3n] (Pure): ", gini_impurity(0, 3))
print("Gini of [2y, 1n]:        ", round(gini_impurity(2, 1), 4))
```

---

## 🔑 Key Takeaways
1. Gini Impurity measures the probability of misclassification.
2. For binary classification, Gini ranges from **0.0 (pure)** to **0.5 (maximum impurity)**.
3. Because Gini only requires squaring numbers (no logarithms), it is computationally faster than Entropy.
