# Lecture 28.14: Decision Tree Regressor Code (Diabetes Dataset & Overfitting)

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Scikit-Learn ke `load_diabetes` dataset par `DecisionTreeRegressor` ka implementation.
- Video mein ma'am dwara dikhaya gaya extreme overfitting ka result:
- `MSE train: 0.0`, `r^2 train: 1.0`
- `MSE test: 5530.51`, **`r^2 test: -0.024`** (Negative $R^2$ score!).
- Negative $R^2$ ka aasan bhasha mein matlab.
- `plot_tree` se massive tree ko visualize karna.
- Pre-pruning (`max_depth=3`, `min_samples_leaf=15`) se test $R^2$ ko positive karna.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Diabetes Dataset Load Karna
Video mein ma'am ne Scikit-Learn ka `load_diabetes(as_frame=True).frame` load kiya. Isme 442 patients ka data hai aur continuous target disease progression score hai.

#### 2. Baseline Model Aur Screen Ka Shocking Result
Jab ma'am ne bina restriction ke `DecisionTreeRegressor()` train kiya, toh output aaya:
- `MSE train: 0.0`
- `MSE test: 5530.51`
- `r^2 train: 1.0`
- **`r^2 test: -0.024`**

Ma'am ne screen par highlight kiya:
> **Train par error 0 hai aur $R^2$ 1.0 hai, lekin test par $R^2$ negative (-0.024) ho gaya!**

#### 3. Negative $R^2$ Ka Matlab Kya Hai?
$R^2 = 0$ ka matlab hota hai ki model dataset ke overall average jitna hi kaam kar raha hai.
Lekin agar $R^2$ **negative** ho gaya, toh iska matlab hai ki hamara complex decision tree ek simple seedhi average line se bhi **zyada bura** predict kar raha hai! Tree ne training ke ek-ek point ko ratt kar massive overfitting kar li hai.

#### 4. Pre-Pruning Se Solution
Ma'am ne tree par do restrictions lagayi:
- `max_depth = 3`
- `min_samples_leaf = 15`

Iske lagate hi:
- Test MSE 5530 se ghat kar substantially kam ho gaya.
- Test $R^2$ negative se badhkar healthy positive score ban gaya!

---

### 💻 Python Code

```python
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. Data load
df = load_diabetes(as_frame=True).frame
X = df.drop(columns=["target"])
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. Baseline Tree (Extreme Overfit)
base = DecisionTreeRegressor(random_state=42)
base.fit(X_train, y_train)

print(f"Base Train R2: {r2_score(y_train, base.predict(X_train)):.2f}")
print(f"Base Test R2:  {r2_score(y_test, base.predict(X_test)):.4f}")

# 3. Pruned Tree
pruned = DecisionTreeRegressor(max_depth=3, min_samples_leaf=15, random_state=42)
pruned.fit(X_train, y_train)

print(f"Pruned Test R2: {r2_score(y_test, pruned.predict(X_test)):.4f}")
```

---

### 📌 Summary Points
- Regression trees bina pruning ke train par 100% memorization kar leti hain lekin test par negative $R^2$ de sakti hain.
- Negative $R^2$ severe overfitting ko darshata hai.
- `max_depth` aur `min_samples_leaf` lagane se regression tree generalizable ban jaati hai.
