# 🚀 Lecture 04.14: Class Practice Problems (Part c) - Dictionary Invert Karna

## 📌 Executive Summary (Saransh)
Dictionary ko invert karne ka matlab hai keys ko values aur values ko keys banana.

---

## 🔬 Deep Technical Concepts

### 1. Collision Handling
Agar do students ke same grade hain (jaise Alice: A aur Charlie: A), toh direct invert karne par ek naam overwrite ho jayega. Isliye naye dictionary mein value ke andar **list** banayi jati hai taaki dono bache reh sakein.

---

## 💻 Code Example

```python
grades = {"Alice": "A", "Bob": "B", "Charlie": "A"}

inverted = {}
for name, grade in grades.items():
    if grade not in inverted:
        inverted[grade] = []
    inverted[grade].append(name)

print("Inverted Dict:", inverted)
# {'A': ['Alice', 'Charlie'], 'B': ['Bob']}
```
