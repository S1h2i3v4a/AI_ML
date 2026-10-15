# 🚀 Lecture 02.04: Keywords aur Comments

## 📌 Executive Summary (Saransh)
Keywords Python ke wo reserved words hain jinka matlab interpreter ke liye pehle se fix hota hai. Aap inka naam kisi variable ya function ke liye use nahi kar sakte. Comments hamare code ko explain karne ke liye hote hain jise Python skip kar deta hai.

---

## 🔬 Deep Technical Concepts

### 1. Python Keywords
Python mein 35 keywords hote hain jaise: `if`, `else`, `for`, `while`, `class`, `def`, `return`, `True`, `False`, `None`, etc. Inhe verify karne ke liye `keyword` module use hota hai.

### 2. Comments Ka Upyog
- Single line ke liye `#` use karein.
- Multi-line documentation ke liye triple quotes `""" ... """` (Docstrings) use karein jo runtime par `__doc__` mein store rehte hain.

---

## 💻 Code Example

```python
import keyword

# Keywords ki list dekhna
print("Total Keywords:", len(keyword.kwlist))

# Single-line comment
# Yeh ek mathematical calculation hai
a = 10
b = 20
sum_val = a + b # Dono ka jod
print("Sum =", sum_val)
```
