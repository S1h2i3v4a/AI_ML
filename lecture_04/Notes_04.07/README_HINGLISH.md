# 🚀 Lecture 04.07: Python Tuples

## 📌 Executive Summary (Saransh)
Tuple bhi list ki tarah ordered data store karta hai, lekin yeh **Immutable** (badla nahi ja sakta) hota hai. Isko round brackets `()` se banaya jata hai.

---

## 🔬 Deep Technical Concepts

### 1. Tuple vs List
- **Tuple:** Fixed size, fast, memory kam leta hai, aur badla nahi ja sakta.
- **List:** Dynamic size, mutable, memory thodi zyada leta hai.

### 2. Hashable Keys
Kyunki tuple immutable hai, isliye isse dictionary ki key banaya ja sakta hai (list ko nahi banaya ja sakta).

---

## 💻 Code Example

```python
# Tuple banana
coordinates = (10.0, 20.0)
print("Coordinates:", coordinates)

# Single element tuple (comma zaroori hai)
single = (5,)
print("Single Tuple:", type(single))
```
