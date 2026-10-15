# Notes_25.13: Cross Validation Kya Hota Hai? (K-Fold & Stratified) [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_25_13.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 25 Overview](../README_HINGLISH.md)

---

## 📌 Executive Summary
K-Fold aur Stratified K-Fold Cross Validation ka complete mathematical intuition.

---

## 🎯 Mathematical Formulations

K-Fold Cross Validation Estimator:

$$
\text{CV}_K = \frac{1}{K} \sum_{k=1}^K \text{Score}_k
$$

Stratified Fold Class Ratio Invariant:

$$
\frac{N_{k, +}}{N_k} \approx \frac{N_{+}}{N} \quad \forall \; k \in \{1, 2, \dots, K\}
$$

---

## 💡 Concept Intuition & Key Insights (Desi Style)

### Single Train-Test Split Ki Kamzori:
Agar hum sirf ek baar train/test split karte hain, toh ho sakta hai ki test set mein coincidental easy ya tough examples chale jayein. Isse performance estimate unstable ho jata hai.
### K-Fold Solution:
Dataset ko $K$ equal hisso (folds) mein divide kiya jata hai. Har iteration mein 1 fold test set banta hai aur baki $K-1$ folds train set bante hain. Yeh process $K$ baar chalta hai aur sabhi scores ka average nikala jata hai!
- **Stratified K-Fold:** Imbalanced classification mein use hota hai taaki har fold mein positive aur negative class ka ratio original dataset jaisa hi barabar rahe.

---

## 💻 Python Production Implementation

```python
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import pandas as pd

df = pd.read_csv("heart.csv")
X = df.drop("target", axis=1)
y = df["target"]

pipe = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_val_score(pipe, X, y, cv=skf, scoring='accuracy')
print("5-Fold Scores:", scores.round(4))
print(f"Mean CV Accuracy: {scores.mean():.4f} (+/- {scores.std():.4f})")
```
