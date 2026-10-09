# 🌐 Lecture 23.03: Types of Machine Learning: Unsupervised aur RL [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-1.4%2B-orange.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 23 Par Wapas Jayein](../README_HINGLISH.md)

---

## 📌 1. Unsupervised Learning

Unsupervised Learning mein **unlabeled data** hota hai (koi target variable $y$ nahi hota).
Model ka kaam hota hai data ke andar chhipe hue patterns, groups ya clusters ko dhoondhna:
- **Clustering:** Customers ko unke kharch ke hisaab se groups mein baantna (K-Means).
- **Dimensionality Reduction:** High-dimensional data ko kam dimensions mein compress karna (PCA).

---

## 🎮 2. Reinforcement Learning (RL)

Reinforcement Learning mein ek **Agent** ek dynamic **Environment** ke saath interact karta hai.
- **Action** leta hai.
- Achhe action par **Reward** milta hai aur galat par **Penalty**.
- Goal hota hai total cumulative reward ko maximize karna (jaise: Chess khelna, self-driving car).

---

## 💻 3. Python Code

```python
from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print("Cluster assignments:", kmeans.labels_)
```
