# 📈 Lecture 22.05: Input Transformations: Scaling aur Shifts [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Numpy](https://img.shields.io/badge/Numpy-Numerical%20Computing-013243.svg)](https://numpy.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 22 Par Wapas Jayein](../README_HINGLISH.md)

---

## 📌 1. Input Transformations (Horizontal Badlav)

Jab function ke argument ke andar badlav kiya jata hai ($y = f(c \cdot x + d)$), toh graph **horizontally** badalta hai:
- $f(x - d)$: Graph **right side** shift hota hai (counter-intuitive: minus hone par right jaata hai).
- $f(x + d)$: Graph **left side** shift hota hai.
- $f(c \cdot x)$ ($c > 1$): Graph horizontally compress (sankucha) hota hai.
- $f(c \cdot x)$ ($0 < c < 1$): Graph horizontally stretch (chauda) hota hai.
- $f(-x)$: Y-axis ke along reflection.

---

## 📐 2. Machine Learning mein Upyog

Neural Network layer ka pre-activation:

$$
z = w \cdot x + b
$$

- $w$ input feature ko scale karta hai.
- $b$ decision boundary ko shift karta hai.
- Feature standardization ($z = \frac{x - \mu}{\sigma}$) input scaling aur shifting ka perfect example hai.

---

## 💻 3. Python Plotting Code

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)
plt.plot(x, x**2, label='f(x) = x^2')
plt.plot(x, (x - 2)**2, label='f(x - 2) (Shift Right)')
plt.plot(x, (x + 2)**2, label='f(x + 2) (Shift Left)')
plt.legend()
plt.grid(True)
plt.show()
```
