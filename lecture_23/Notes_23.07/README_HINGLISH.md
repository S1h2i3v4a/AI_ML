# 📈 Lecture 23.07: Linear Regression ki Shuruat [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-1.4%2B-orange.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 23 Par Wapas Jayein](../README_HINGLISH.md)

---

## 📌 1. Linear Regression Kya Hai?

**Linear Regression** ek fundamental supervised algorithm hai jo continuous target $y$ aur features $x$ ke beech ek seedhi line (linear relationship) fit karta hai:

$$
\hat{y} = w x + b
$$

- $w$ (**Weight / Slope**): Yeh batata hai ki $x$ ke 1 unit badhne par $y$ kitna badhega.
- $b$ (**Bias / Intercept**): Yeh batata hai ki jab $x = 0$ ho, toh $y$ ki value kya hogi.

Agar multiple features hon:

$$
\hat{y} = w_1 x_1 + w_2 x_2 + \dots + w_p x_p + b
$$

---

## 📐 2. Geometrical Meaning

- 1 Feature: 2D space mein ek **Straight Line**.
- 2 Features: 3D space mein ek **Flat Plane**.
- $p$ Features: Multi-dimensional space mein ek **Hyperplane**.

---

## 💻 3. Python Code

```python
import numpy as np

# Hypothesis function
def predict(x, w, b):
    return w * x + b

print("Prediction for x=30 (w=250, b=2000):", predict(30, 250, 2000))
```
