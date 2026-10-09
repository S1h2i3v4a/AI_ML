# ⚖️ Lecture 23.05: Regression vs. Classification [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-1.4%2B-orange.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 23 Par Wapas Jayein](../README_HINGLISH.md)

---

## 📌 1. Regression aur Classification mein Antar

- **Regression:** Jab hume koi **continuous number** predict karna ho (Jaise: Insurance charges, Salary, Temperature).
  - Formula: $\hat{y} = w x + b$
  - Loss: Mean Squared Error (MSE)
- **Classification:** Jab hume **discrete category ya class** predict karni ho (Jaise: Email Spam hai ya nahi, Customer churn karega ya nahi).
  - Output: 0 ya 1 (Binary) ya Multiple Classes.
  - Loss: Cross-Entropy / Log Loss.

---

## 💻 2. Python Code

```python
import numpy as np

# Regression Target
y_regression = [12.5, 45.2, 89.1, 102.4]

# Classification Target
y_classification = [0, 1, 1, 0]
```
