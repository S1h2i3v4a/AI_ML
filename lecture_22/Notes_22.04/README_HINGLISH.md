# 📈 Lecture 22.04: Functions par Operations: Scalar Multiplication aur Addition [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Numpy](https://img.shields.io/badge/Numpy-Numerical%20Computing-013243.svg)](https://numpy.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 22 Par Wapas Jayein](../README_HINGLISH.md)

---

## 📌 1. Functions par Operations

Do functions $f(x)$ aur $g(x)$ ke liye:
- **Addition:** $(f + g)(x) = f(x) + g(x)$
- **Scalar Multiplication:** $(c \cdot f)(x) = c \cdot f(x)$

---

## 📐 2. Vertical Transformations (Geometrical Asar)

Jab hum function ke bahar koi operation karte hain, toh graph **vertically** badalta hai:
- $a \cdot f(x)$ ($a > 1$): Vertical stretch (lamba khinch jata hai).
- $a \cdot f(x)$ ($0 < a < 1$): Vertical compression (chapti ho jata hai).
- $-f(x)$: X-axis ke along flip (reflection).
- $f(x) + d$: Upar shift hota hai.
- $f(x) - d$: Neeche shift hota hai.

ResNets mein residual connections $(y = x + F(x))$ functions addition ka sabse bada real-world udaharan hain.

---

## 💻 3. Python Plotting Code

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 200)
plt.plot(x, x**2, label='f(x) = x^2')
plt.plot(x, 2 * x**2, label='2 * f(x) (Stretch)')
plt.plot(x, x**2 + 3, label='f(x) + 3 (Shift Up)')
plt.legend()
plt.grid(True)
plt.show()
```
