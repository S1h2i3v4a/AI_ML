# Lecture 03.12: The range() Function: Lazy Arithmetic Progressions (हिंग्लिश)

## 📌 Module Overview
Python ka range() type: start, stop, step arguments, lazy arithmetic evaluation, aur O(1) constant memory footprint.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Range Function Kya Hai?
Python 3 mein `range()` koi list nahi banata, balki ek immutable sequence type object hota hai jo numbers ko "lazily" (on-demand) generate karta hai.

### 2. Syntax Aur Arguments
- `range(stop)`: $0$ se shuru hokar `stop - 1` tak.
- `range(start, stop)`: `start` se shuru hokar `stop - 1` tak.
- `range(start, stop, step)`: `start` se har baar `step` jodte hue `stop` se pehle tak.

### 3. O(1) Constant Memory Footprint
Chahe aap `range(10)` likho ya `range(10_000_000_000)`, Python memory mein sirf teen numbers (`start`, `stop`, `step`) store karta hai. Iska memory usage hamesha 48 bytes rehta hai!

---

## 💻 Python Code Aur Implementation
```python
import sys

r_small = range(10)
r_huge = range(1_000_000_000)

print("Size of range(10):", sys.getsizeof(r_small), "bytes")
print("Size of range(1 billion):", sys.getsizeof(r_huge), "bytes")
print("Range indexing r_huge[500]:", r_huge[500])
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Har operation ki asymptotic execution limits.
- **Space Complexity:** Memory footprint aur call stack activation analysis.
