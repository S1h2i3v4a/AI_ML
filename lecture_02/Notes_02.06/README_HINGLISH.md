# 🚀 Lecture 02.06: Arithmetic Operators

## 📌 Executive Summary (Saransh)
Arithmetic operators mathematical calculations (+, -, *, /, //, %, **) perform karte hain. Python 3 mein `/` hamesha floating-point number return karta hai.

---

## 🔬 Deep Technical Concepts

### 1. Operators Ki List
- `+`: Addition (Jodna)
- `-`: Subtraction (Ghatana)
- `*`: Multiplication (Guna)
- `/`: True Division (Hamesha float answer dega, jaise `4 / 2 = 2.0`)
- `//`: Floor Division (Decimal ke bina neeche ki taraf round karta hai, `5 // 2 = 2`)
- `%`: Modulo (Remainder / Sheshphal nikalta hai)
- `**`: Power / Exponent (jaise `2 ** 3 = 8`)

### 2. Floor Division aur Negative Numbers
Negative number mein `//` hamesha choti value (left side on number line) ki taraf jata hai:
`-7 // 2` ka answer `-4` aayega, `-3` nahi!

---

## 💻 Code Example

```python
x = 10
y = 3

print("x + y =", x + y) # 13
print("x / y =", x / y) # 3.3333333333333335
print("x // y =", x // y) # 3
print("x % y =", x % y) # 1
print("x ** y =", x ** y) # 10^3 = 1000
```
