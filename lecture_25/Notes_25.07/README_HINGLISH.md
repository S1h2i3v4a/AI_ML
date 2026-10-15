# Notes_25.07: Naive Bayes Ke Prakar: Gaussian, Multinomial, Bernoulli [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_25_07.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 25 Overview](../README_HINGLISH.md)

---

## 📌 Executive Summary
GaussianNB, MultinomialNB, aur BernoulliNB ke beech ka difference aur kab kaunsa use karein.

---

## 🎯 Mathematical Formulations

Gaussian Naive Bayes Likelihood (Normal PDF):

$$
P(x_j \mid y) = \frac{1}{\sqrt{2\pi \sigma_{j, y}^2}} \exp\left( -\frac{(x_j - \mu_{j, y})^2}{2\sigma_{j, y}^2} \right)
$$

Multinomial Likelihood:

$$
P(\mathbf{x} \mid y) = \frac{(\sum x_i)!}{\prod x_i!} \prod p_{i, y}^{x_i}
$$

---

## 💡 Concept Intuition & Key Insights (Desi Style)

### Kaunsa Model Kab Lagayein?
1. **GaussianNB:** Jab features continuous real numbers hon (jaise Age, Blood Pressure, Temperature). Yeh assume karta hai ki har feature class ke andar Gaussian/Normal distribution follow karta hai.
2. **MultinomialNB:** Text classification jahan word frequency count (Bag of Words / TF-IDF) hota hai (jaise text documents, sentiment analysis).
3. **BernoulliNB:** Jab features binary yes/no ($1$ ya $0$) indicators hon (jaise word present hai ya absent).

---

## 💻 Python Production Implementation

```python
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
import numpy as np

# Continuous features -> GaussianNB
X_cont = np.array([[1.2, 5.4], [2.1, 4.8], [5.6, 1.2], [6.2, 0.9]])
y = [0, 0, 1, 1]
gnb = GaussianNB().fit(X_cont, y)
print("GaussianNB Classes:", gnb.classes_)
```
