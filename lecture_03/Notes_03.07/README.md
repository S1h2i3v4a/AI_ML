# Lecture 03.07: Practice Examples (Loops)

## 📌 Executive Summary
Hands-on while loop patterns: Counter sequences, cumulative accumulators, sentinel input loops, and digit extraction.

---

## 🔬 Theoretical Foundations & Principles
### 1. Canonical Loop Design Patterns
- **Counter-Controlled Loop:** Iterates a fixed number of times based on an integer counter.
- **Accumulator Pattern:** Progressively combines sequence elements into a running aggregate.
- **Sentinel Loop:** Continues indefinitely until a specific marker value is encountered.
- **Successive Division (Digit Deconstruction):** Uses $N \pmod{10}$ and $N // 10$ to inspect digits in integer arithmetic.

---

## 💻 Production Implementation & Code
```python
# Digit extraction pattern via while loop
def extract_digits_reversed(n: int) -> list[int]:
    digits = []
    temp = abs(n)
    if temp == 0:
        return [0]
    while temp > 0:
        digit = temp % 10
        digits.append(digit)
        temp //= 10
    return digits

print("Digits of 48392:", extract_digits_reversed(48392))
```

---

## ⚙️ Algorithmic Complexity & Systems Analysis
- **Time Complexity:** Detailed in respective algorithmic operations.
- **Auxiliary Space:** Memory bounds and CPython frame management.
