# Notes_25.14: Cross Validation for Hyperparameter Tuning (GridSearchCV)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_25_14.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Lecture 25 Overview](../README.md)

---

## 📌 Executive Summary
Exhaustive grid search with cross-validation to select optimal K and distance metrics.

---

## 🎯 Mathematical Formulations

Optimal Hyperparameter Selection:

$$
\theta^* = \arg\max_{\theta \in \Theta} \frac{1}{K} \sum_{k=1}^K \text{Metric}\left( f_{\theta}(\mathcal{D}_{\text{train}}^{(-k)}), \mathcal{D}_{\text{val}}^{(k)} \right)
$$

---

## 💡 Conceptual Principles & Architecture

### GridSearchCV Kaise Kaam Karta Hai?
Hum hyperparameters ki ek dictionary pass karte hain (jaise `n_neighbors`: $[3, 5, 7, 9, 11]$ aur `weights`: `['uniform', 'distance']`).
GridSearchCV har combination par K-Fold Cross Validation run karta hai aur mathematically sabse best hyperparameter $\theta^*$ select kar leta hai!

---

## 💻 Python Production Implementation

```python
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import pandas as pd

df = pd.read_csv("heart.csv")
X = df.drop("target", axis=1)
y = df["target"]

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier())
])

param_grid = {
    'knn__n_neighbors': [3, 5, 7, 9, 11, 15],
    'knn__weights': ['uniform', 'distance'],
    'knn__p': [1, 2]  # 1=Manhattan, 2=Euclidean
}

grid = GridSearchCV(pipe, param_grid, cv=5, scoring='accuracy')
grid.fit(X, y)

print("Best Parameters:", grid.best_params_)
print(f"Best CV Accuracy: {grid.best_score_:.4f}")
```
