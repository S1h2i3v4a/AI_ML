# Notes_25.02: Using StandardScaler & Preventing Data Leakage

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_25_02.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Lecture 25 Overview](../README.md)

---

## 📌 Executive Summary
Scikit-Learn StandardScaler implementation and preventing data leakage across train and test splits.

---

## 🎯 Mathematical Formulations

Training Set parameters:

$$
\mu_{\text{train}} = \frac{1}{n_{\text{train}}} \sum_{i=1}^{n_{\text{train}}} x_i, \qquad \sigma_{\text{train}} = \sqrt{\frac{1}{n_{\text{train}}} \sum_{i=1}^{n_{\text{train}}} (x_i - \mu_{\text{train}})^2}
$$

Transformation rule (Strict Data Hygiene):

$$
X_{\text{train, scaled}} = \frac{X_{\text{train}} - \mu_{\text{train}}}{\sigma_{\text{train}}}, \qquad X_{\text{test, scaled}} = \frac{X_{\text{test}} - \mu_{\text{train}}}{\sigma_{\text{train}}}
$$

---

## 💡 Conceptual Principles & Architecture

### Golden Rule: Data Leakage Kya Hota Hai?
Kayi beginners galti se poore dataset par pehle `scaler.fit_transform(X)` kar dete hain aur fir train/test split karte hain. Yeh bohot badi galti hai jise **Data Leakage** kehte hain!
- Agar aap test set ki information ($\mu$ aur $\sigma$) scaling mein include kar lete hain, toh aapka model test data ki distribution pehle hi "cheat" kar leta hai.
- **Sahi Tareeqa:** Pehle `train_test_split` karein. Fir scaler ko **sirf training set** par `fit` karein (`scaler.fit_transform(X_train)`), aur test set par **sirf `transform`** karein (`scaler.transform(X_test)`).

---

## 💻 Python Production Implementation

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[22, 45000], [38, 85000], [26, 52000], [50, 110000], [30, 68000], [42, 95000]])
y = np.array([0, 1, 0, 1, 0, 1])

# 1. First Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# 2. Fit ONLY on Train, Transform Both
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # ONLY transform! Never fit on test!

print("Train Mean:", scaler.mean_)
print("Train Scaled:\n", X_train_scaled.round(2))
print("Test Scaled (using train mean/std):\n", X_test_scaled.round(2))
```
