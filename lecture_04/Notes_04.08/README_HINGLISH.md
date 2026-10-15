# 🚀 Lecture 04.08: Tuple Methods aur Unpacking

## 📌 Executive Summary (Saransh)
Tuples immutable hote hain, isliye inme add/delete wale methods nahi hote. Inke paas sirf do methods hote hain: `count()` aur `index()`.

---

## 🔬 Deep Technical Concepts

### 1. Methods
- `count(val)`: Gin kar batata hai ki value kitni baar aayi hai.
- `index(val)`: Batata hai ki value pehli baar kis position par aayi.

### 2. Tuple Unpacking
Tuple ke elements ko ek sath multiple variables mein divide karna: `a, b = (10, 20)`.

---

## 💻 Code Example

```python
grades = ('A', 'B', 'A', 'C', 'A')

print("Total 'A':", grades.count('A'))
print("First 'B' at index:", grades.index('B'))

# Unpacking
person = ("Shradha", 21, "Engineer")
name, age, profession = person
print(f"{name} is a {age}-year-old {profession}")
```
