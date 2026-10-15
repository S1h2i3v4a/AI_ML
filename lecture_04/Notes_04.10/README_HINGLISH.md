# 🚀 Lecture 04.10: Dictionary Methods

## 📌 Executive Summary (Saransh)
Dictionary ke pass data search karne, nikaalne, aur update karne ke powerful methods hote hain.

---

## 🔬 Deep Technical Concepts

### 1. View Objects
- `d.keys()`: Saari keys deta hai.
- `d.values()`: Saari values deta hai.
- `d.items()`: `(key, value)` pairs deta hai loop chalane ke liye.

### 2. Dictionary Comprehension
List comprehension ki tarah dictionary bhi ek line mein banayi ja sakti hai: `{w: len(w) for w in words}`.

---

## 💻 Code Example

```python
marks = {"Math": 90, "Science": 85, "English": 78}

# Keys aur Values
print("Subjects:", list(marks.keys()))
print("Scores:", list(marks.values()))

# Loop over items
for sub, score in marks.items():
    print(f"{sub} -> {score}")
```
