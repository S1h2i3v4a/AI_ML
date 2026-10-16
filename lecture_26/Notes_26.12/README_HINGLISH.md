# Lecture 26.12: K-Nearest Neighbors (KNN) from Scratch — Multi-Dimensional Implementation & Plurality Voting

## 📌 Saransh (Executive Summary)
KNNClassifier ki complete pure Python aur NumPy implementation: `_euclidean_dist()`, `_predict_one()`, `np.argsort()`, `np.bincount()` plurality voting, aur Seaborn visualization.

---

## 🔬 First-Principles Theory & Intuition
### 1. KNN Algorithm Ke 4 Steps
Code ke andar prediction ka process 4 steps mein hota hai:
1. **Distance Calculation**: Test point se saare training points ka Euclidean distance calculate karna.
2. **Sorting (`np.argsort`)**: Saare distances ko ascending order mein sort karke sabse nazdeeki $k$ points ke indices nikalna.
3. **Neighbor Labels**: Un $k$ nearest points ke original labels (`y_train`) fetch karna.
4. **Majority Voting (`np.bincount` + `np.argmax`)**: Jis class ke sabse zyada padosi honge, wahi winner class predict ho jayegi!

### 2. Live Verification
Lecture ke example data par test karke dekhte hain:
- Points $(1, 2), (2, 3), (3, 3)$ class 0 hain.
- Points $(6, 5), (7, 7)$ class 1 hain.
- Query $(2, 2)$ predict karta hai `0` aur $(6, 6)$ predict karta hai `1`!


---

## 💻 Python & NumPy Code Implementation
```python
import numpy as np
import pandas as pd

class KNNClassifier:
    def __init__(self, k=3):
        self.k = k

    def _euclidean_dist(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def _predict_one(self, x):
        distances = [self._euclidean_dist(x, x_train) for x_train in self.X_train]
        knn_indices = np.argsort(distances)[:self.k]
        knn_classes = [self.y_train[i] for i in knn_indices]
        majority_class = np.argmax(np.bincount(knn_classes))
        return majority_class

    def predict(self, X):
        return np.array([self._predict_one(x) for x in X])

# Lecture Dataset
X_train = np.array([
    [1, 2],
    [2, 3],
    [3, 3],
    [6, 5],
    [7, 7]
])
y_train = np.array([0, 0, 0, 1, 1])

X_test = np.array([
    [2, 2],
    [6, 6]
])

knn = KNNClassifier(k=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print("KNN Test Predictions for [[2, 2], [6, 6]]:", y_pred)

```

---

## 🎯 Key Takeaways & Practical Tips
1. **Black-Box Se Azadi**: Libraries ko blind use karne ke bajaye unke andar ka math samajhna aapko top 1% engineer banata hai.
2. **Vectorization Ki Taqat**: Python loops ke bajaye NumPy array operations use karein jo C/BLAS speed provide karte hain.
3. **Debugging Mastery**: Jab loss decrease na ho raha ho, toh sabse pehle learning rate $\alpha$ aur gradient dimensions check karein.
