# Lecture 03.18: Factorial of N: Iterative Vs Recursive Formulation (हिंग्लिश)

## 📌 Module Overview
Factorial calculation: Mathematical formula $N!$, iterative loop accumulator, recursive call stack, base cases, aur CPython recursion limit.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Factorial Ka Mathematical Formula
Kisi bhi non-negative integer $N$ ke liye:

$$
N! = \prod_{i=1}^{N} i = 1 \times 2 \times 3 \times \dots \times N
$$

Base case $0! = 1$ hota hai.

### 2. Iterative Vs Recursive Architecture
- **Iterative Approach:** Simple `for` loop se multiply karta hai. Iska space complexity $\mathcal{O}(1)$ rehta hai.
- **Recursive Approach:** Function apne aap ko baar-baar call karta hai (`factorial(n-1)`). Har call stack par ek naya frame banata hai. Agar $N > 1000$ ho jaye, toh CPython `RecursionError: maximum recursion depth exceeded` throw kar deta hai.

---

## 💻 Python Code Aur Implementation
```python
def factorial_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial undefined for negative integers")
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial undefined for negative integers")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)

print("10! (Iterative):", factorial_iterative(10))
print("10! (Recursive):", factorial_recursive(10))
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Har operation ki asymptotic execution limits.
- **Space Complexity:** Memory footprint aur call stack activation analysis.
