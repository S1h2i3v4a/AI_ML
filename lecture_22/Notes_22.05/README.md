# 📈 Lecture 22.05: Input Transformations: Scaling & Shifts

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Numpy](https://img.shields.io/badge/Numpy-Numerical%20Computing-013243.svg)](https://numpy.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Lecture 22](../README.md)

---

## 📌 1. Input Argument Transformations

When arithmetic operations are applied **inside** the function's argument:

$$
y = f(c \cdot x + d)
$$

they transform the graph **horizontally** along the x-axis. Notice that horizontal transformations act counter-intuitively compared to vertical transformations.

| Transformation | Equation | Geometric Effect | Counter-Intuitive Rule |
| :--- | :--- | :--- | :--- |
| **Horizontal Shift Right** | $y = f(x - d)$ with $d > 0$ | Shifts the curve right by $d$ units | Minus sign shifts **right** |
| **Horizontal Shift Left** | $y = f(x + d)$ with $d > 0$ | Shifts the curve left by $d$ units | Plus sign shifts **left** |
| **Horizontal Compression** | $y = f(c \cdot x)$ with $c > 1$ | Compresses curve toward y-axis by $\frac{1}{c}$ | Multiplying by $c > 1$ **shrinks** width |
| **Horizontal Stretch** | $y = f(c \cdot x)$ with $0 < c < 1$ | Stretches curve away from y-axis by $\frac{1}{c}$ | Dividing by $c$ **widens** curve |
| **Horizontal Reflection** | $y = f(-x)$ | Reflects curve across the y-axis | Inverts horizontal direction |

---

## 📐 2. The Affine Input Transformation in Neural Networks

In deep learning, every neuron's pre-activation value is an **affine input transformation**:

$$
z = w \cdot x + b
$$

1. **Weight $w$ (Input Scaling):** Stretches or compresses the input feature space. In Sigmoid activations $\sigma(w x + b)$, a large $w$ steepens the transition, acting like a step function.
2. **Bias $b$ (Input Shift):** Shifts the decision threshold left or right, determining the activation baseline.

```mermaid
graph LR
    x["Input Feature x"] --> Scale["Scale by w: w * x"]
    Scale --> Shift["Shift by b: w * x + b"]
    Shift --> Act["Non-linear Activation σ(w * x + b)"]
    Act --> Out["Output Activation a"]
```

### Feature Standardization as an Input Map:
Data normalization maps inputs via an affine scaling and shifting:

$$
\tilde{x} = \frac{x - \mu}{\sigma} = \left(\frac{1}{\sigma}\right) x - \left(\frac{\mu}{\sigma}\right)
$$

---

## 💻 3. Python Implementation: Visualizing Horizontal Shifts & Scaling

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 400)
base = x**2

plt.figure(figsize=(9, 5))
plt.plot(x, base, 'k-', lw=2, label='Base: f(x) = x^2')
plt.plot(x, (x - 2)**2, 'r--', lw=2, label='Shift Right: f(x - 2)')
plt.plot(x, (x + 2)**2, 'b-.', lw=2, label='Shift Left: f(x + 2)')
plt.plot(x, (2 * x)**2, 'g:', lw=2, label='Horizontal Compression: f(2x)')
plt.plot(x, (0.5 * x)**2, 'm--', lw=2, label='Horizontal Stretch: f(0.5x)')

plt.axhline(0, color='gray', lw=1)
plt.axvline(0, color='gray', lw=1)
plt.title('Horizontal Input Transformations on f(x) = x^2', fontsize=12, fontweight='bold')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.ylim(0, 15)
plt.show()
```
