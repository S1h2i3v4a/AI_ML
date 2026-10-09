# Day 21 - Lecture 21.6: Practice Problems: Coordinate Geometry & Linear Boundaries [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_21_06.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 21 Module Par Wapas Jayein](../README_HINGLISH.md)

---

## 1. Practice Problems

Coordinate geometry aur linear boundary concepts par based practical sawal:

### Problem 1: Point Classification
Decision line $2x_1 + 5x_2 - 10 = 0$ ke liye points classify karein:
- $P_1(3, 2) \implies 2(3) + 5(2) - 10 = +6 > 0 \implies \text{Class } +1$.
- $P_2(1, 1) \implies 2(1) + 5(1) - 10 = -3 < 0 \implies \text{Class } -1$.
- $P_3(0, 2) \implies 0 \implies \text{Boundary Par}$.

### Problem 2: Point ki Doori
Point $P_1(3, 2)$ ki boundary se perpendicular doori:

$$
\boxed{d = \frac{|6|}{\sqrt{2^2 + 5^2}} = \frac{6}{\sqrt{29}} \approx 1.1142}
$$

---

## 2. Python Code

```python
import numpy as np

w = np.array([2.0, 5.0])
b = -10.0
p1 = np.array([3.0, 2.0])

dist = abs(np.dot(w, p1) + b) / np.linalg.norm(w)
print(f"Distance to boundary: {dist:.4f}")
```

---

## 3. Mukhya Batein (Key Takeaways) & Interview Points
- **Geometric Margin:** Model ka raw output score $\mathbf{w}^T \mathbf{x} + b$ scale par depend karta hai, lekin geometric distance $\frac{\mathbf{w}^T \mathbf{x} + b}{\|\mathbf{w}\|}$ scale-invariant hoti hai.
