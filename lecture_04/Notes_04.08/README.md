# 🚀 Lecture 04.08: Tuple Methods & Structural Sequence Unpacking

## 📌 Executive Architectural Summary
Because tuples are immutable, they do not expose mutator methods (`append`, `pop`, `sort`). Their interface is focused exclusively on inspection (`count`, `index`) and structural sequence unpacking.

---

## 🔬 Core Engineering Mechanics

### 1. Tuple Methods
- `t.count(x)`: Returns the number of occurrences of value $x$ in $\mathcal{O}(N)$ time.
- `t.index(x, [start, [stop]])`: Returns the first index of value $x$, raising `ValueError` if absent.

### 2. Sequence Unpacking Formalism
Python allows mapping tuple elements directly into multiple identifiers:
$$
(x_1, x_2, \dots, x_N) = T \implies x_i = T[i-1] \quad orall i \in \{1, \dots, N\}
$$
Extended unpacking with `*` captures variable-length slices.

---

## 💻 Production Python Implementation

```python
records = (10, 20, 30, 20, 40, 20, 50)

# Methods
print(f"Count of 20: {records.count(20)}")
print(f"Index of 40: {records.index(40)}")

# Structural Unpacking
point = (1920, 1080)
width, height = point
print(f"Resolution: {width}x{height}")

# Extended Unpacking with *
scores = (100, 95, 88, 72, 65)
first, second, *remaining = scores
print(f"First: {first}, Second: {second}, Others: {remaining}")
```
