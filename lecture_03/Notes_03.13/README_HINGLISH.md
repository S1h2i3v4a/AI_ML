# Lecture 03.13: Sum of N Numbers: Loop Accumulation vs Gauss Formula (हिंग्लिश)

## 📌 Module Overview
First N natural numbers ka addition: Iterative loop O(N) vs Carl Friedrich Gauss ka direct O(1) formula.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Iterative Loop Approach
Loop ke dwara sum calculate karne par hum $N$ steps run karte hain:

$$
S_N = 1 + 2 + 3 + \dots + N
$$

Iska time complexity $\mathcal{O}(N)$ hota hai.

### 2. Gauss Ka Closed-Form Formula
Carl Friedrich Gauss ne prove kiya tha ki numbers ko pairs mein add karke direct constant time $\mathcal{O}(1)$ mein result nikala ja sakta hai:

$$
S_N = \frac{N(N + 1)}{2}
$$

Agar $N = 10^{12}$ bhi ho, toh formula fraction of a microsecond mein exact answer de deta hai bina kisi loop ke.

---

## 💻 Python Code Aur Implementation
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

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Har operation ki asymptotic execution limits.
- **Space Complexity:** Memory footprint aur call stack activation analysis.
