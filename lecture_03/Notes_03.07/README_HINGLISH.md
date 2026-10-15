# Lecture 03.07: Loops Ke Practice Examples (हिंग्लिश)

## 📌 Module Overview
While loop ke practical algorithms: Counters, accumulators, sentinel user inputs, aur digit operations.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Standard While Loop Patterns
- **Counter Pattern:** $1$ se $N$ tak count karna.
- **Accumulator Pattern:** Numbers ka running sum ya product calculate karna.
- **Sentinel Pattern:** Jab tak user "Quit" na bole, tab tak chalte rehna.
- **Digit Extraction Pattern:** Modulo $10$ se rightmost digit lena aur integer division $// 10$ se us digit ko hatana.

---

## 💻 Python Code Aur Implementation
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

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Har operation ki asymptotic execution limits.
- **Space Complexity:** Memory footprint aur call stack activation analysis.
