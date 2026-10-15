# Notes_25.08: Python Mein Naive Bayes Ka Implementation [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_25_08.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 25 Overview](../README_HINGLISH.md)

---

## 📌 Executive Summary
Heart disease dataset par GaussianNB train karna aur metrics evaluate karna.

---

## 🎯 Mathematical Formulations

Model Log-Likelihood Decision Boundary:

$$
\log P(y \mid \mathbf{x}) \propto \log P(y) + \sum_{j=1}^d \log P(x_j \mid y)
$$

---

## 💡 Concept Intuition & Key Insights (Desi Style)

### Log-Probabilities Kyu Use Karte Hain?
Jab d-dimensions bohot bada hota hai (e.g. text classification mein $10,000$ words), toh small probabilities ($0.001 	imes 0.002 	imes \dots$) multiply karte-karte computer ke floating point precision se bahar nikal kar underflow ($0.0$) ho jaati hain.
Logarithm lene se multiplication addition ban jata hai: $\log(a \cdot b) = \log a + \log b$, jisse underflow bilkul prevent ho jata hai!

---

## 💻 Python Production Implementation

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

df = pd.read_csv("heart.csv")
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)

print("Classification Report:\n", classification_report(y_test, y_pred))
```
