# 🚀 Lecture 04.01: Python Mein Strings aur Immutability

## 📌 Executive Summary (Saransh)
Python mein String text data ko represent karne ke liye use hoti hai. Yeh **Immutable** (aparivartaniye) hoti hai, yaani ek baar banne ke baad iska koi bhi character badla nahi ja sakta.

---

## 🔬 Deep Technical Concepts

### 1. Immutability Ka Niyam
Agar aap `s = "Python"` likhte hain aur `s[0] = 'J'` karne ki koshish karte hain, toh Python `TypeError` de dega. Koi bhi badlav karne par Python naya string object banata hai.

### 2. Indexing System
- Forward Index: $0$ se shuru hota hai (pehla character $0$ par).
- Backward / Negative Index: $-1$ se shuru hota hai (aakhri character $-1$ par).

---

## 💻 Code Example

```python
s = "Machine Learning"

print("Pura String:", s)
print("Length (len):", len(s))
print("Pehla Akshar (s[0]):", s[0])
print("Aakhri Akshar (s[-1]):", s[-1])
```
