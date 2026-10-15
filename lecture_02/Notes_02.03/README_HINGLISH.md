# 🚀 Lecture 02.03: Data Types aur Type System

## 📌 Executive Summary (Saransh)
Data type yeh batata hai ki variable ke paas kis tarah ka data store hai aur uspar kaun-kaun se operations perform kiye ja sakte hain. Python ek **Dynamically Typed** aur **Strongly Typed** language hai.

---

## 🔬 Deep Technical Concepts

### 1. Basic Data Types
1. **`int`:** Poore number (Whole numbers, e.g., $10, -50, 1000$). Python mein integer ki koi overflow limit nahi hoti.
2. **`float`:** Decimal wale numbers (e.g., $3.14, -0.005, 10.0$).
3. **`str`:** Text data jo single ya double quotes ke andar ho (e.g., `"Python"`).
4. **`bool`:** Sach ya Jhooth (`True` ya `False`).
5. **`None`:** Empty ya null value ko represent karne ke liye special type `NoneType`.

### 2. Type Checking Function
Variable ka type janne ke liye built-in `type()` function use hota hai.

---

## 💻 Code Example

```python
x = 10
pi = 3.14
course = "AI/ML Prime"
status = True
empty = None

print("x ka type:", type(x))
print("pi ka type:", type(pi))
print("course ka type:", type(course))
print("status ka type:", type(status))
print("empty ka type:", type(empty))
```
