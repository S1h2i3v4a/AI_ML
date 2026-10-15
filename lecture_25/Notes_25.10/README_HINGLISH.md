# Notes_25.10: Python Mein kNN Classifier Ka Code [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_25_10.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 25 Overview](../README_HINGLISH.md)

---

## 📌 Executive Summary
Heart dataset par StandardScaler ke sath kNN model train aur evaluate karna.

---

## 🎯 Mathematical Formulations

Uniform vs Distance-Weighted Voting:

$$
w_i = \frac{1}{d(\mathbf{x}, \mathbf{x}_i)}, \qquad \hat{y} = \arg\max_c \sum_{i \in N_K, y_i = c} w_i
$$

---

## 💡 Concept Intuition & Key Insights (Desi Style)

### Feature Scaling kNN Ke Liye Compulsory Hai!
kNN geometry aur distances par nirbhar karta hai. Agar hum data scale nahi karenge, toh bada feature distance ko dominate karega aur accuracy dramatically drop ho jayegi.

---

## 💻 Python Production Implementation

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("heart.csv")
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5, weights='distance')
knn.fit(X_train_s, y_train)
print("kNN Accuracy:", accuracy_score(y_test, knn.predict(X_test_s)).round(4))
```
