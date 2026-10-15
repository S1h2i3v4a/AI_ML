# 🚀 Lecture 02.07: Relational Operators & Comparison Mechanics

## 📌 Executive Architectural Summary
Relational (comparison) operators evaluate the order and equality relations between operands according to mathematical order theory, returning a strict Boolean value (`True` or `False`).

---

## 🔬 Core Engineering Mechanics

### 1. Relational Operators Suite
- `==`: Equality ($a = b$)
- `!=`: Inequality ($a 
e b$)
- `>`: Strictly greater than ($a > b$)
- `<`: Strictly less than ($a < b$)
- `>=`: Greater than or equal to ($a \ge b$)
- `<=`: Less than or equal to ($a \le b$)

### 2. Chained Comparisons Feature
Python uniquely supports chained relational expressions:
$$
a < b < c \iff (a < b) \land (b < c)
$$
Importantly, operand $b$ is evaluated **only once** in Python's AST execution.

---

## 💻 Production Python Implementation

```python
x, y = 15, 20

print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x > y:  {x > y}")
print(f"x < y:  {x < y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")

# Chained Comparison
val = 15
print("Chained: 10 < val <= 20 ->", 10 < val <= 20)
print("Chained: 10 < val < 15 ->", 10 < val < 15)
```
