# Lecture 03.13: Sum of N Numbers

## 📌 Executive Summary
Sum of first N natural numbers: Iterative O(N) accumulation compared against Gauss's closed-form O(1) formula.

---

## 🔬 Theoretical Foundations & Principles
### 1. Loop Accumulation ($\\mathcal{O}(N)$)
Summing elements iteratively executes $N$ additions and pointer rebinding operations:

$$
S_N = \sum_{i=1}^{N} i
$$

### 2. Gauss's Closed-Form Equation ($\\mathcal{O}(1)$)
Using pairing symmetries, Carl Friedrich Gauss proved the closed-form arithmetic sum:

$$
S_N = \frac{N(N + 1)}{2}
$$

Executing in $\mathcal{O}(1)$ constant time and zero auxiliary space.

---

## 💻 Production Implementation & Code
```python
def sum_iterative(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_gauss(n: int) -> int:
    return (n * (n + 1)) // 2

n_val = 1_000_000
print("Loop Sum:", sum_iterative(n_val))
print("Gauss Sum:", sum_gauss(n_val))
```

---

## ⚙️ Algorithmic Complexity & Systems Analysis
- **Time Complexity:** Detailed in respective algorithmic operations.
- **Auxiliary Space:** Memory bounds and CPython frame management.
