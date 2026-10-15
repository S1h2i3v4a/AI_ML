# Notes_25.15: Scikit-Learn Pipelines: Zero Data Leakage Architecture [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_25_15.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 25 Overview](../README_HINGLISH.md)

---

## 📌 Executive Summary
Data preprocessing aur model ko ek single Pipeline mein bind karna taaki data leakage na ho.

---

## 🎯 Mathematical Formulations

Pipeline Composite Transformation Map:

$$
\mathbf{x} \xrightarrow{\text{Step 1: Scaler}} \mathbf{z} = \frac{\mathbf{x} - \mu_{\text{fold}}}{\sigma_{\text{fold}}} \xrightarrow{\text{Step 2: Model}} \hat{y} = f(\mathbf{z})
$$

---

## 💡 Concept Intuition & Key Insights (Desi Style)

### Pipeline Kyu Industry Standard Hai?
1. **Zero Data Leakage:** Jab hum K-Fold Cross Validation mein Pipeline use karte hain, toh `StandardScaler` har fold ke andar independently fit hota hai. Validation fold ka data training fold ke scaler mein kabhi leak nahi hota!
2. **Clean Code & Reusability:** Preprocessing aur prediction ek hi single object ban jaata hai: `pipe.fit(X_train, y_train)` aur `pipe.predict(X_new)`.
3. **Easy Production Deployment:** Production server par alag se scaler file aur model file manage nahi karni padti; ek single `.pkl` pipeline file deploy ho jati hai.

---

## 💻 Python Production Implementation

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("heart.csv")
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Production Pipeline
model_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', KNeighborsClassifier(n_neighbors=7, weights='distance'))
])

model_pipeline.fit(X_train, y_train)
test_accuracy = model_pipeline.score(X_test, y_test)
print(f"Production Pipeline Test Accuracy: {test_accuracy:.4f}")
```
