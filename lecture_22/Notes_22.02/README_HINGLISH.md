# 📈 Lecture 22.02: Ganitiya Functions aur Real-World Transformations [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Numpy](https://img.shields.io/badge/Numpy-Numerical%20Computing-013243.svg)](https://numpy.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 22 Par Wapas Jayein](../README_HINGLISH.md)

---

## 📌 1. Function Kya Hota Hai?

Ek **Function** $f: X \to Y$ ek mathematical rule hota hai jo input set $X$ ke har element ko output set $Y$ ke **sirf aur sirf ek** unique element se map karta hai.

- **Domain ($X$):** Sabhi valid inputs ka set jiske liye function defined hai.
- **Codomain ($Y$):** Target set jisme output aane ki sambhavna hoti hai.
- **Range:** Woh actual outputs ka set jo function produce karta hai ($\text{Range} \subseteq \text{Codomain}$).

---

## 📐 2. AI mein Mukhya Function Types

1. **Root Functions ($y = \sqrt{x}$):**
   - Inputs non-negative hone chahiye ($x \ge 0$).
   - AI mein Euclidean distance aur standard deviation nikaalne mein use hota hai.
2. **Trigonometric Functions ($y = \sin(x), y = \cos(x)$):**
   - Output hamesha $[-1, 1]$ ke beech bounded hota hai.
   - Transformers mein **Positional Encodings** ke liye use hota hai taaki tokens ki position capture ho sake.
3. **Exponential aur Logarithm ($e^x, \ln(x)$):**
   - $e^x$ numbers ko positive banata hai (Softmax probabilities).
   - $\ln(x)$ multiplicative probabilities ko additive banata hai (Cross-Entropy loss calculation).

---

## 💻 3. Python Plotting Code

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 200)
y = np.sin(x)

plt.plot(x, y, label='y = sin(x)', color='blue')
plt.axhline(0, color='black', ls='--')
plt.axvline(0, color='black', ls='--')
plt.title('Sine Function')
plt.legend()
plt.grid(True)
plt.show()
```
