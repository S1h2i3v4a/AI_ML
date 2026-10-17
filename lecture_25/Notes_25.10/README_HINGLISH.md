# Notes_25.09: kNN (K Nearest Neighbours) Ka Concept [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne **k-Nearest Neighbors (kNN)** algorithm ka visual concept samjhaya hai: doori (distance) kaise nikaalte hain aur majority voting se naye point ka faisla kaise hota hai.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- kNN algorithm asal mein kya hota hai? (Lazy learner ka matlab).
- Naye data point ke liye decision lene ke 3 steps.
- **Euclidean Distance** aur **Manhattan Distance** ka formula.
- $K$ ki value hamesha **Odd (visham: 3, 5, 7)** kyu chunni chahiye?
- Majority voting ka simple rule.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. kNN Kaise Kaam Karta Hai? (Padosi Rule)
Yeh algorithm bolta hai: *"Aap jaise logon ke sath rehte ho, aap waise hi bante ho!"*
Jab koi naya data point aata hai:
1. Sabhi purane points se uski doori (distance) calculate karo.
2. Sabse kareebi **$K$ padosi** chun lo.
3. Padosiyon mein **Majority Vote** karao — jis class ke padosi zyada honge, naya point usi class ka maan liya jayega!

#### 2. Distance Formulas:
- **Euclidean Distance** (Seedhi doori / Pythagoras rule):

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

- **Manhattan Distance** (Grid / City-block doori):

$$d = |x_2 - x_1| + |y_2 - y_1|$$

#### 3. $K$ Hamesha Odd Kyu Rakhein?
Binary classification (0 ya 1) mein agar aap $K=4$ (even number) rakhoge, toh ho sakta hai 2 padosi 0 bole aur 2 padosi 1 bole! Tie ho jayega aur model confuse ho jayega. Isliye hamesha $K=3, 5, 7$ jaisi odd values rakhi jaati hain taaki tie na ho.

---

### 📊 Visual Flowchart: kNN Prediction Process

```mermaid
flowchart TD
    A["Naya Point Aaya"] --> B["Sabhi Training Points se Distance Nikalo"]
    B --> C["Top K Kareebi Padosi Chun Lo"]
    C --> DPadosiyon Ka Majority Vote
    D -->|"Zyada Padosi Class 1 Ke"| E["Predict: Class 1"]
    D -->|"Zyada Padosi Class 0 Ke"| F["Predict: Class 0"]
```

---

### 💻 Python Code

```python
import numpy as np

def predict_knn_majority_vote(query_point, dataset_points, dataset_labels, k=3):
    """
    Manual demonstration of k-Nearest Neighbors classification:
    Calculates Euclidean distances, picks the k nearest neighbors,
    and returns the plurality majority class label.
    """
    query = np.asarray(query_point)
    points = np.asarray(dataset_points)
    labels = np.asarray(dataset_labels)

    # 1. Euclidean distance: sqrt(sum((x2 - x1)^2))
    distances = np.sqrt(np.sum((points - query) ** 2, axis=1))

    # 2. Find indices of k smallest distances
    nearest_indices = np.argsort(distances)[:k]
    nearest_labels = labels[nearest_indices]

    # 3. Plurality majority vote
    counts = np.bincount(nearest_labels)
    predicted_class = int(np.argmax(counts))

    return predicted_class, nearest_labels, distances[nearest_indices]

# --- Function Call & Testing ---
# Class 0: Cyan Crosses | Class 1: Orange Circles
training_pts = [[1, 2], [2, 3], [3, 3], [6, 5], [7, 7], [8, 6]]
training_lbl = [0, 0, 0, 1, 1, 1]
new_point    = [5, 5]

pred, neighbors, dists = predict_knn_majority_vote(new_point, training_pts, training_lbl, k=3)
print(f"Query Point: {new_point}")
print(f"3 Nearest Neighbor Labels: {neighbors} (Distances: {dists.round(2)})")
print(f"Majority Predicted Class:  Class {pred}")
```

---

### 📌 Summary Points
- kNN ko pehle se model train karne ki zaroorat nahi padti (Lazy Learner).
- Prediction ke time saara distance calculate hota hai.
- Hamesha odd $K$ chunein taaki voting mein tie na ho.
