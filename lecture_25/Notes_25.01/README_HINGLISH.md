# Notes_25.01: Standardization aur Normalization Ka Antar [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_25_01.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 25 Overview](../README_HINGLISH.md)

---

## 📌 Executive Summary
Feature scaling kyu zaroori hai: Z-score Standardization aur Min-Max Normalization ka difference.

---

## 🎯 Mathematical Formulations

Standardization (Z-score scaling) formula:

$$
z = \frac{x - \mu}{\sigma}
$$

Jahan $\mu$ mean hai aur $\sigma$ standard deviation hai. Scaling ke baad $\mu = 0$ aur $\sigma = 1$ ho jata hai.

Min-Max Normalization formula:

$$
x_{\text{norm}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
$$

Isse saari values strict range $[0, 1]$ mein squash ho jati hain.

---

## 💡 Concept Intuition & Key Insights (Desi Style)

### Feature Scaling Kyu Zaroori Hai?
Distance-based algorithms (jaise kNN, SVM, K-Means) aur Gradient Descent based models (Logistic Regression, Neural Networks) features ke scale par heavily depend karte hain. Agar ek feature 'Salary' ($50,000$ se $2,00,000$) hai aur doosra feature 'Age' ($20$ se $60$) hai, toh Euclidean distance formula mein Salary dominance karega aur Age ka asar negligible ho jayega!

### Kab Kya Use Karein?
1. **Standardization (StandardScaler):** Jab data normal/Gaussian distribution follow karta ho, ya jab outliers present hon (StandardScaler outliers ke sath better handle karta hai).
2. **Normalization (MinMaxScaler):** Image processing (pixel values $0-255$ to $[0, 1]$), Neural Networks activation inputs, ya jab exact bounded scale $[0, 1]$ chahiye ho.

---

## 💻 Python Production Implementation

```python
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

data = np.array([[25, 50000], [35, 90000], [45, 120000], [20, 30000]])

std_scaler = StandardScaler()
minmax_scaler = MinMaxScaler()

print("Original Data:\n", data)
print("\nStandardized (Mean=0, Std=1):\n", std_scaler.fit_transform(data).round(2))
print("\nNormalized ([0, 1] Range):\n", minmax_scaler.fit_transform(data).round(2))
```
