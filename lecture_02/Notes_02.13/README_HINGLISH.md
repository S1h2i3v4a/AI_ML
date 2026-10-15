# 🚀 Lecture 02.13: Do Numbers Ka Average aur Problem Solving

## 📌 Executive Summary (Saransh)
Yeh lecture Day 02 ke sabhi concepts (input lena, float casting, arithmetic calculation aur print formatting) ko mila kar ek real-world problem solve karta hai: Do numbers ka Average nikalna.

---

## 🔬 Deep Technical Concepts

### 1. Formula
Do numbers $a$ aur $b$ ka average hota hai:
$$
	ext{Average} = rac{a + b}{2}
$$

### 2. Common Galti
Agar aap likhte hain `a + b / 2`, toh Python pehle `b / 2` karega aur phir `a` jode ga! Isliye brackets lagana zaroori hai: `(a + b) / 2`.

---

## 💻 Code Example

```python
# Average nikalne ka complete program
a = 5.0
b = 10.0

average = (a + b) / 2
print("1st Number:", a)
print("2nd Number:", b)
print("Average =", average)
```
