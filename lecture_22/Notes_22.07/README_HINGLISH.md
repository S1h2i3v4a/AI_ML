# 📈 Lecture 22.07: Differentiation ke Niyam aur Activation Function Derivatives [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Numpy](https://img.shields.io/badge/Numpy-Numerical%20Computing-013243.svg)](https://numpy.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 22 Par Wapas Jayein](../README_HINGLISH.md)

---

## 📌 1. Differentiation ke Buniyadi Niyam

1. **Power Rule:** $\frac{d}{dx}[x^n] = n x^{n-1}$
2. **Product Rule:** $\frac{d}{dx}[u \cdot v] = u' v + u v'$
3. **Quotient Rule:** $\frac{d}{dx}[\frac{u}{v}] = \frac{u' v - u v'}{v^2}$
4. **Chain Rule:** $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$

---

## 🧠 2. AI Activation Functions ke Derivatives

1. **Sigmoid:**
   $$
   \sigma'(x) = \sigma(x) (1 - \sigma(x))
   $$
   Iska maximum derivative sirf $0.25$ hota hai ($x = 0$ par). Is wajah se deep networks mein **Vanishing Gradient** problem hoti hai.
2. **Tanh:**
   $$
   \tanh'(x) = 1 - \tanh^2(x)
   $$
3. **ReLU:**
   Positive values par derivative hamesha $1$ rehta hai, jisse gradient fade nahi hota.

---

## 💻 3. Python Code

```python
import numpy as np

def sigmoid(x): return 1 / (1 + np.exp(-x))
def d_sigmoid(x): return sigmoid(x) * (1 - sigmoid(x))

print("Sigmoid derivative at 0:", d_sigmoid(0)) # 0.25
```
