# Lecture 03.10: For Loops: Sequence Traversal Aur Iterator Protocol (हिंग्लिश)

## 📌 Module Overview
Python mein for loops ka architecture, Iterable vs Iterator ka farq, aur sequence traversal.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Python Ka For Loop Kaise Kaam Karta Hai?
C/C++ mein for loop counter-based hota hai (`i=0; i<n; i++`). Lekin Python ka `for` loop asal mein **Iterator Protocol** par chalta hai. Yeh kisi bhi sequence ya iterable ke elements ko ek-ek karke visit karta hai.

### 2. Internal Mechanism
Under the hood Python yeh karta hai:
1. `iter(iterable)` call karke ek iterator object leta hai.
2. Baar-baar `next()` call karke agla element laata hai.
3. Jab elements khatam ho jaate hain, toh `StopIteration` exception catch karke loop cleanly terminate ho jaata hai.

---

## 💻 Python Code Aur Implementation
```python
# Demonstrating underlying iterator protocol
fruits = ["apple", "banana", "cherry"]
iterator = iter(fruits)

print("First item:", next(iterator))
print("Second item:", next(iterator))
print("Third item:", next(iterator))
# next(iterator) now would raise StopIteration
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Har operation ki asymptotic execution limits.
- **Space Complexity:** Memory footprint aur call stack activation analysis.
