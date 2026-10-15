# Lecture 03.08: Multiplication Table of N

## 📌 Executive Summary
Mathematical sequence generation, arithmetic progression, formatted tabular alignment, and range iteration.

---

## 🔬 Theoretical Foundations & Principles
### 1. Arithmetic Progression Definition
The multiplication table of integer $N$ for multipliers $i \in \{1, 2, \dots, K\}$ forms an arithmetic progression with common difference $d = N$:

$$
a_i = N \cdot i, \quad a_{i+1} - a_i = N
$$

### 2. String Format Alignment
Use Python f-string alignment specifiers (`{N:2d} x {i:2d} = {N*i:3d}`) to generate clean columnar alignment.

---

## 💻 Production Implementation & Code
```python
def print_multiplication_table(n: int, max_multiplier: int = 10) -> None:
    print(f"--- Multiplication Table for N = {n} ---")
    for i in range(1, max_multiplier + 1):
        product = n * i
        print(f"{n:>3d}  x  {i:>2d}  =  {product:>4d}")

print_multiplication_table(7, 10)
```

---

## ⚙️ Algorithmic Complexity & Systems Analysis
- **Time Complexity:** Detailed in respective algorithmic operations.
- **Auxiliary Space:** Memory bounds and CPython frame management.
