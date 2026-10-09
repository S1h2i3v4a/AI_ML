# 📈 Lecture 22.06: Differentiation aur Instantaneous Rate of Change [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Numpy](https://img.shields.io/badge/Numpy-Numerical%20Computing-013243.svg)](https://numpy.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 22 Par Wapas Jayein](../README_HINGLISH.md)

---

## 📌 1. Differentiation Kya Hai?

**Differentiation** kisi bhi curve ke kisi ek specific point par **instantaneous rate of change** (turant badlav ki gati) nikaalne ki vidhi hai.

- **Secant Line:** Curve ke do points ko jodne wali line ka average slope.
- **Tangent Line:** Jab dono points ke beech ka gap $h \to 0$ ho jaye, toh secant line tangent line ban jati hai.

Formal Limit Definition:

$$
f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
$$

---

## 📐 2. First Principles Derivation ($f(x) = x^2$)

$$
f'(x) = \lim_{h \to 0} \frac{(x + h)^2 - x^2}{h} = \lim_{h \to 0} \frac{2xh + h^2}{h} = 2x
$$

AI mein derivative humein yeh batata hai ki parameter ko halka sa hilane par loss kitna change hoga.

---

## 💻 3. Python Numerical Differentiation

```python
def f(x): return x**2
x = 3.0
h = 1e-5
deriv = (f(x + h) - f(x)) / h
print(f"Calculated: {deriv:.4f}, Exact: {2*x}")
```
