# Day 20 - Lecture 20.14: Random Variables (Yadrichhik Char) [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](lecture_20_14.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 20 Module Par Wapas Jayein](../README_HINGLISH.md)

---

## 1. Paribhasha (Definition)

**Random Variable** koi aam variable nahi hota; yeh ek **mathematical function** hota hai jo sample space $\mathcal{S}$ ke outcomes ko real numbers $\mathbb{R}$ me convert karta hai:

$$
\boxed{X: \mathcal{S} \to \mathbb{R}}
$$

---

## 2. Discrete vs. Continuous Random Variables

| Gun (Property) | Discrete Random Variable | Continuous Random Variable |
| :--- | :--- | :--- |
| **Values** | Ginne yogya (Countable) jaise $0, 1, 2$ | Continuous range jaise height, weight $[a, b]$ |
| **Function** | PMF: $p(x) = P(X = x)$ | PDF: $f(x)$ |
| **Single Point** | $P(X = x) > 0$ ho sakta hai | $P(X = x) = 0$ hamesha |
| **Sum / Integral** | $\sum p(x) = 1.0$ | $\int f(x)dx = 1.0$ |

---

## 3. Cumulative Distribution Function (CDF)

$$
\boxed{F(x) = P(X \le x)}
$$

Continuous variables ke liye PDF aur CDF ka relation:

$$
\boxed{f(x) = \frac{d}{dx} F(x)}
$$

---

## 4. Python Implementation

```python
import numpy as np

# 3 coins ke heads ka PMF
x_vals = [0, 1, 2, 3]
pmf = [1/8, 3/8, 3/8, 1/8]
cdf = np.cumsum(pmf)

for x, p, c in zip(x_vals, pmf, cdf):
    print(f"X = {x}: PMF = {p:.3f}, CDF = {c:.3f}")
```

---

## 5. Mukhya Batein (Key Takeaways) & Interview Points
- **Single Point Trap:** Continuous random variable me exact ek point ki probability hamesha 0 hoti hai ($P(X = 5.0) = 0$); probability hamesha area under the curve (interval) se aati hai.
