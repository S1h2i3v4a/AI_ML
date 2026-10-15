# 🚀 Lecture 02.13: Foundational Problem Solving & Numerical Synthesis

## 📌 Executive Architectural Summary
This lecture integrates all core fundamentals introduced across Day 02: standard input parsing, arithmetic operators, explicit type casting, and standard output formatting into an end-to-end numerical problem-solving pipeline.

---

## 🔬 Core Engineering Mechanics

### 1. Mathematical Average Formulation
For two numbers $a, b \in \mathbb{R}$:
$$
\mu = rac{a + b}{2}
$$
For $N$ numbers $x_1, x_2, \dots, x_N$:
$$
\mu = rac{1}{N} \sum_{i=1}^{N} x_i
$$

### 2. Edge Case Analysis
- **Parentheses Precedence:** Writing `a + b / 2` calculates $a + rac{b}{2}$ due to division binding tighter than addition. The grouping `(a + b) / 2` is strictly required.

---

## 💻 Production Python Implementation

```python
# Problem: Compute Average of 2 Numbers from User Inputs

def compute_average(val1: float, val2: float) -> float:
    """Calculates arithmetic mean with strict operator precedence."""
    return (val1 + val2) / 2.0

# Test Case 1: Integers resulting in float
n1, n2 = 5, 10
avg1 = compute_average(n1, n2)
print(f"Average of {n1} and {n2} = {avg1:.2f}")

# Test Case 2: Floating point inputs
f1, f2 = 12.5, 7.3
avg2 = compute_average(f1, f2)
print(f"Average of {f1} and {f2} = {avg2:.2f}")
```
