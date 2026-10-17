# Lecture 28.06: Information Gain & Split Selection

## 📌 Topic Overview
How does a decision tree algorithm decide which feature gives the best split? The answer is **Information Gain (IG)**. In this lecture, we study the reduction-in-entropy formula and work through the exact numerical example taught on the blackboard.

---

## 🎯 What is Information Gain?
> **Information Gain measures the reduction in entropy (uncertainty) achieved after splitting a dataset based on a given feature.**

The intuition is simple:
$$	ext{Information Gain} = 	ext{Entropy of Parent} - 	ext{Weighted Entropy of Children}$$

### Mathematical Formula:

$$IG(S, A) = H(S) - \sum_{v \in 	ext{Values}(A)} rac{|S_v|}{|S|} H(S_v)$$

Where:
- $S$ = Parent dataset at the current node.
- $H(S)$ = Entropy of the parent node.
- $A$ = Feature we are evaluating.
- $v$ = A specific value or branch of feature $A$.
- $S_v$ = Subset of samples where feature $A = v$.
- $rac{|S_v|}{|S|}$ = Proportion of samples going down branch $v$ (weight).

---

## 🧮 Blackboard Numerical Walkthrough

### 1. Parent Node Entropy
Consider the parent dataset with 6 samples: $[2y, 4n]$ (2 Yes, 4 No).

$$H(S) = - rac{2}{6}\log_2\left(rac{2}{6}
ight) - rac{4}{6}\log_2\left(rac{4}{6}
ight) pprox 0.918$$

---

### 2. Candidate Feature 1: `Gender`
Splitting on `Gender` (Male vs Female):
- **Male branch ($S_M$)**: Contains 3 samples: $[2y, 1n]$.
$$H(S_M) = - rac{2}{3}\log_2\left(rac{2}{3}
ight) - rac{1}{3}\log_2\left(rac{1}{3}
ight) pprox 0.918$$
- **Female branch ($S_F$)**: Contains 3 samples: $[0y, 3n]$ (all No $\rightarrow$ Pure).
$$H(S_F) = 0.0$$

Now compute weighted child entropy:
$$	ext{Weighted Child Entropy} = rac{3}{6} \cdot H(S_M) + rac{3}{6} \cdot H(S_F) = rac{1}{2}(0.918) + rac{1}{2}(0) = 0.459$$

Now compute Information Gain for Gender:
$$IG(	ext{Gender}) = H(S) - 0.459 = 0.918 - 0.459 = 0.459$$

---

### 3. Candidate Feature 2: `Employed`
The instructor notes on the board:
$$IG(	ext{Employed}) = 0.800$$

---

### 4. Split Selection Decision
We compare the Information Gain of all candidate features:
- $IG(	ext{Gender}) = 0.459$
- $IG(	ext{Employed}) = 0.800$

Since **$0.800 > 0.459$**, the tree selects **`Employed`** as the split feature at this node!

---

## 💻 Python Implementation

```python
import numpy as np

def calculate_entropy(yes_count, no_count):
    """Calculates Shannon Entropy for binary classes."""
    total = yes_count + no_count
    if total == 0 or yes_count == 0 or no_count == 0:
        return 0.0
    p1 = yes_count / total
    p2 = no_count / total
    return -(p1 * np.log2(p1) + p2 * np.log2(p2))

def calculate_information_gain(parent_y, parent_n, left_y, left_n, right_y, right_n):
    """
    Calculates Information Gain achieved by splitting a parent node into two child branches.
    Formula: IG = H(Parent) - [ (|Left|/|Parent|)*H(Left) + (|Right|/|Parent|)*H(Right) ]
    """
    total_parent = parent_y + parent_n
    total_left = left_y + left_n
    total_right = right_y + right_n

    h_parent = calculate_entropy(parent_y, parent_n)
    h_left = calculate_entropy(left_y, left_n)
    h_right = calculate_entropy(right_y, right_n)

    weighted_child_entropy = (total_left / total_parent) * h_left + (total_right / total_parent) * h_right
    info_gain = h_parent - weighted_child_entropy
    return info_gain

# --- Execute Calculation on Classroom Video Example ---
# Parent Node: [2 Yes, 4 No]
parent_entropy = calculate_entropy(2, 4)

# Candidate 1: Split on Gender -> Male [0y, 3n], Female [2y, 1n]
ig_gender = calculate_information_gain(2, 4, 0, 3, 2, 1)

# Candidate 2: Split on Employed -> Employed [2y, 0n], Unemployed [0y, 4n]
ig_employed = calculate_information_gain(2, 4, 2, 0, 0, 4)

print(f"Parent Node Entropy:         {parent_entropy:.3f}")
print(f"Information Gain (Gender):   {ig_gender:.3f}")
print(f"Information Gain (Employed): {ig_employed:.3f}")
print("Best Split Selected:", "Employed" if ig_employed > ig_gender else "Gender")
```

---

## 🔑 Key Takeaways
1. Information Gain represents the reduction in entropy caused by a split.
2. The feature with the **highest Information Gain** is chosen as the split node.
3. When using Gini Impurity, the equivalent metric is **Gini Gain**.
