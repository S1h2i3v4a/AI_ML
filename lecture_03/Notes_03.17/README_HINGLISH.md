# Lecture 03.17: Lambda Functions: Anonymous Callables (हिंग्लिश)

## 📌 Module Overview
Anonymous functions (`lambda`), single-expression syntax, functional primitives (`map`, `filter`), aur sorting keys.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Lambda Functions Kya Hain?
Lambda function ek anonymous (bina naam ka) inline function hota hai jo single line expression ke roop mein likha jata hai:

```python
lambda x, y: x + y
```

Alonzo Church ki $\lambda$-calculus par aadharit yeh syntax lightweight callbacks ke liye banaya gaya hai.

### 2. Best Use Cases
Lambdas tab use karne chahiye jab function sirf ek hi jagah chote se transformation ke liye chahiye ho, jaise sorting keys (`key=lambda x: x[1]`), ya `map()` aur `filter()` ke andar.

---

## 💻 Python Code Aur Implementation
```python
# Sorting complex data via lambda key
students = [
    ("Alice", 88),
    ("Bob", 95),
    ("Charlie", 78),
    ("Diana", 92)
]

# Sort by marks descending
sorted_by_marks = sorted(students, key=lambda s: s[1], reverse=True)
print("Ranked Students:", sorted_by_marks)
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Har operation ki asymptotic execution limits.
- **Space Complexity:** Memory footprint aur call stack activation analysis.
