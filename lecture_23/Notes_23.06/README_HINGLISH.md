# 🛠️ Lecture 23.06: Scikit-Learn (sklearn) ka Parichay [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-1.4%2B-orange.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 23 Par Wapas Jayein](../README_HINGLISH.md)

---

## 📌 1. Scikit-Learn Kya Hai?

**Scikit-Learn (`sklearn`)** Python ki sabse popular aur powerful Machine Learning library hai.
Iska API design itna consistent aur standardized hai ki chahe aap Linear Regression use karein ya Random Forest, code ka format hamesha same rehta hai:
1. `model.fit(X_train, y_train)`: Model ko train karta hai.
2. `model.predict(X_test)`: Naye data par prediction karta hai.
3. `model.score(X_test, y_test)`: Accuracy ya $R^2$ score calculate karta hai.

---

## 🏛️ 2. Sklearn ke 3 Main Components

- **Estimator:** Jo data se parameters seekhta hai (`fit()`).
- **Transformer:** Jo data ko transform karta hai (`transform()`, jaise `StandardScaler`).
- **Predictor:** Jo predictions deta hai (`predict()`).

---

## 💻 3. Python Code

```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3]])
y = np.array([2, 4, 6])

model = LinearRegression()
model.fit(X, y)

print("Weight:", model.coef_)         # [2.]
print("Intercept:", model.intercept_) # 0.0
```
