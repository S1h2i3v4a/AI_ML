# Lecture 26.11: K-Nearest Neighbors (KNN) from Scratch — Metric Space & Lazy Learning Formulation

## 📌 Saransh (Executive Summary)
K-Nearest Neighbors (KNN) classifier ka first-principles foundation, non-parametric lazy learning, Euclidean distance metric, aur hyperparameter $k$ selection.

---

## 🔬 First-Principles Theory & Intuition
### 1. Lazy Learner Ka Matlab Kya Hai?
Linear Regression ya Logistic Regression mein `fit()` chalane ke baad mathematical weights mil jate hain aur training data ko delete bhi kar dein toh model predict kar sakta hai.
Lekin KNN ek **Lazy Learner** hai:
- `fit()` ke time par koi math ya calculation nahi hoti! Yeh sirf training points ko memory mein save kar leta hai.
- Asli calculation `predict()` ke time par hoti hai jab har naye point ka distance saare puraane points se nikalna padta hai.

### 2. Euclidean Distance Ka Formula
Do points ke beech ka shortest straight-line distance nikalne ke liye Pythagorean theorem use hota hai:

$$
d(\mathbf{x}_1, \mathbf{x}_2) = \sqrt{\sum_{j=1}^d (x_{1j} - x_{2j})^2}
$$

### 3. $k$ Ki Value Kaise Chunein?
- Agar $k=1$ chuna: Model overfit karega, ek single noisy outlier point se galat prediction de dega.
- Agar $k$ bohot bada chuna: Model underfit karega aur hamesha majority class hi bolega.
- Binary classification mein $k$ hamesha **odd number (3, 5, 7)** chunna chahiye taaki voting mein tie na ho!


---

## 💻 Python & NumPy Code Implementation
```python
import numpy as np

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

# Verify distance computation
p1 = np.array([1.0, 2.0])
p2 = np.array([4.0, 6.0])
dist = euclidean_distance(p1, p2)
print(f"Distance between {p1} and {p2}: {dist:.4f} (Expected: 5.0)")

```

---

## 🎯 Key Takeaways & Practical Tips
1. **Black-Box Se Azadi**: Libraries ko blind use karne ke bajaye unke andar ka math samajhna aapko top 1% engineer banata hai.
2. **Vectorization Ki Taqat**: Python loops ke bajaye NumPy array operations use karein jo C/BLAS speed provide karte hain.
3. **Debugging Mastery**: Jab loss decrease na ho raha ho, toh sabse pehle learning rate $\alpha$ aur gradient dimensions check karein.
