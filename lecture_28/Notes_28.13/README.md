# Lecture 28.13: Variance Reduction

## 📌 Topic Overview
In classification, we used Information Gain (reduction in entropy) to choose the best split. In regression trees, the equivalent metric is **Variance Reduction (VR)**. In this lecture, we study the formula and examine the step-by-step blackboard comparison of split candidates.

---

## 🎯 What is Variance Reduction?
> **Variance Reduction measures how much the target variance drops after splitting a node into child subsets.**

$$\text{Variance Reduction} = \text{Variance of Parent} - \text{Weighted Variance of Children}$$

### Mathematical Formula:

$$VR = V_S - \left( \frac{|S_L|}{|S|} V_L + \frac{|S_R|}{|S|} V_R \right)$$

Where:
- $V_S$ = Variance of the parent node.
- $V_L, V_R$ = Variance of the left and right child subsets.
- $\frac{|S_L|}{|S|}, \frac{|S_R|}{|S|}$ = Proportion of samples going to the left and right children.

---

## 🧮 Blackboard Numerical Example: Comparing Splits
Dataset: $x = [1, 2, 3, 4]$, $y = [2, 4, 6, 10]$.
From the previous lecture, parent variance is:
$$V_S = 8.75$$

### Case 1: Split at $x \le 2$
- **Left Child ($S_L$)**: Contains samples with $x \in \{1, 2\} \r\rightarrow y \in \{2, 4\}$.
- Mean: $\bar{y}_L = \frac{2 + 4}{2} = 3$.
- Variance: $V_L = \frac{(2-3)^2 + (4-3)^2}{2} = \frac{1 + 1}{2} = 1.0$.
- **Right Child ($S_R$)**: Contains samples with $x \in \{3, 4\} \r\rightarrow y \in \{6, 10\}$.
- Mean: $\bar{y}_R = \frac{6 + 10}{2} = 8$.
- Variance: $V_R = \frac{(6-8)^2 + (10-8)^2}{2} = \frac{4 + 4}{2} = 4.0$.

#### Weighted Variance of Children:
$$\text{Weighted Child Variance} = \frac{2}{4}(1.0) + \frac{2}{4}(4.0) = 0.5 + 2.0 = 2.5$$

#### Variance Reduction for Case 1:
$$VR_1 = V_S - 2.5 = 8.75 - 2.5 = 6.25$$

---

### Case 2: Split at $x \le 3$
- **Left Child**: $y \in \{2, 4, 6\} \r\rightarrow \bar{y} = 4, V_L = \frac{4 + 0 + 4}{3} = \frac{8}{3} \approx 2.67$.
- **Right Child**: $y \in \{10\} \r\rightarrow V_R = 0$ (single point $\r\rightarrow$ zero variance).
- Weighted Child Variance: $\frac{3}{4}(2.67) + \frac{1}{4}(0) = 2.0$.
- Variance Reduction for Case 2:
$$VR_2 = 8.75 - 2.0 = 6.75$$

### Selection Decision:
Since **$VR_2 (6.75) > VR_1 (6.25)$**, the algorithm selects split candidate 2 ($x \le 3$) because it achieves a greater reduction in variance!

---

## 💻 Python Implementation

```python
import numpy as np

def variance_reduction(y_parent, y_left, y_right):
v_parent = np.var(y_parent)
v_left = np.var(y_left)
v_right = np.var(y_right)

w_left = len(y_left) / len(y_parent)
w_right = len(y_right) / len(y_parent)

weighted_child_var = (w_left * v_left) + (w_right * v_right)
return v_parent - weighted_child_var

y = np.array([2, 4, 6, 10])

# Case 1: Split at x <= 2
vr_case1 = variance_reduction(y, y[:2], y[2:])
print(f"Case 1 (x <= 2) Variance Reduction: {vr_case1:.2f}")

# Case 2: Split at x <= 3
vr_case2 = variance_reduction(y, y[:3], y[3:])
print(f"Case 2 (x <= 3) Variance Reduction: {vr_case2:.2f}")
```

---

## 🔑 Key Takeaways
1. Variance Reduction is the regression equivalent of Information Gain.
2. The tree evaluates all potential split thresholds and picks the one that maximizes Variance Reduction.
3. A higher Variance Reduction means the child subsets are more tightly clustered around their respective means.
