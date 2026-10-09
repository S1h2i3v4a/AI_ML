# 🔄 Lecture 23.04: Supervised Machine Learning ka Workflow [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-1.4%2B-orange.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 23 Par Wapas Jayein](../README_HINGLISH.md)

---

## 📌 1. Machine Learning Project Lifecycle

Ek machine learning model banane ke 7 steps hote hain:
1. **Problem Definition:** Predict kya karna hai (Regression ya Classification).
2. **Data Collection & Cleaning:** Missing values aur outliers handle karna.
3. **Feature Preprocessing:** Categorical data encode karna (e.g., Male/Female -> 0/1).
4. **Train-Test Split:** Data ko 80% Train aur 20% Test mein divide karna.
5. **Model Training:** Algorithm choose karke `fit()` karna.
6. **Model Evaluation:** Test set par $R^2$ ya RMSE check karna.
7. **Deployment:** Production server par deploy karna.

---

## ⚖️ 2. Train-Test Split Kyu Zaroori Hai?

Agar hum usi data par model ko test karenge jispar usse train kiya gaya hai, toh humein pata nahi chalega ki model naye data par kaisa perform karega.
- **Overfitting (Ratta Marna):** Training data par 100% accuracy lekin test data par fail.
- **Underfitting:** Model itna basic hai ki training data bhi seekh nahi paya.

---

## 💻 3. Python Code

```python
from sklearn.model_selection import train_test_split
import numpy as np

X = np.arange(10).reshape(-1, 1)
y = 2 * X.squeeze()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Train size:", len(X_train), "Test size:", len(X_test))
```
