# 📈 Lecture 22.09: Calculus Optimization Practice Problem [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Numpy](https://img.shields.io/badge/Numpy-Numerical%20Computing-013243.svg)](https://numpy.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 22 Par Wapas Jayein](../README_HINGLISH.md)

---

## 📌 1. Prashna (Problem Statement)

Cubic polynomial function ke critical points aur extrema calculate karein:

$$
f(x) = x^3 - 6x^2 + 9x
$$

---

## 📐 2. Kadam-dar-Kadam Solution

1. **First Derivative:**
   $$
   f'(x) = 3x^2 - 12x + 9
   $$
2. **Critical Points ($f'(x) = 0$):**
   $$
   3(x^2 - 4x + 3) = 0 \implies (x - 1)(x - 3) = 0 \implies x = 1, \; x = 3
   $$
3. **Double Differentiation ($f''(x)$):**
   $$
   f''(x) = 6x - 12
   $$
4. **Classification:**
   - $x = 1$ par: $f''(1) = 6(1) - 12 = -6 < 0$ $\implies$ **Local Maximum** ($y = 4$).
   - $x = 3$ par: $f''(3) = 6(3) - 12 = +6 > 0$ $\implies$ **Local Minimum** ($y = 0$).
5. **Inflection Point:** $f''(x) = 0 \implies x = 2$ ($y = 2$).

---

## 💻 3. Python Plotting Code

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-0.5, 4.5, 200)
y = x**3 - 6*x**2 + 9*x

plt.plot(x, y, label='f(x) = x^3 - 6x^2 + 9x')
plt.scatter([1, 3], [4, 0], color=['red', 'green'])
plt.title('Critical Points & Extrema')
plt.grid(True)
plt.legend()
plt.show()
```
