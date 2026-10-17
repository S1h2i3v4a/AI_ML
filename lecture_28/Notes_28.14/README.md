# Lecture 28.14: Decision Tree Regressor in Scikit-Learn

## 📌 Topic Overview
In this final submodule, we implement `DecisionTreeRegressor` in Python using Scikit-Learn on the **Diabetes dataset** (`load_diabetes(as_frame=True)`), observe severe overfitting in continuous space (negative $R^2$ on test data!), visualize the tree with `plot_tree`, and resolve it using pre-pruning.

---

## 🩺 Dataset & Setup
- **Dataset**: `load_diabetes(as_frame=True).frame` (442 samples, 10 physiological features).
- **Target**: Continuous measure of disease progression one year after baseline.
- **Split**: `train_test_split(X, y, test_size=0.3, random_state=42)`.

---

## ⚠️ Unpruned Regression Tree: Extreme Overfitting
When we fit an unrestricted `DecisionTreeRegressor()`:
- **Train MSE**: `0.0`
- **Train $R^2$**: `1.0` (100% memorization!)
- **Test MSE**: `5530.51`
- **Test $R^2$**: **`-0.024`** (Negative $R^2$!)

### Why is Test $R^2$ Negative?
A negative $R^2$ means the unpruned tree is performing **worse than a simple horizontal line predicting the overall mean** ($\bar{y}$)! The tree created hundreds of tiny leaves to fit individual training outliers, which fail disastrously on test points.

---

## ✂️ Fixing the Model with Pre-Pruning
By constraining the tree using `max_depth` and `min_samples_leaf`:
- The tree stops memorizing noise.
- The test $R^2$ turns from negative to positive.
- The test MSE drops significantly.

---

## 💻 Python Implementation from Lecture

```python
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load data
df = load_diabetes(as_frame=True).frame
X = df.drop(columns=["target"])
y = df["target"]

# 2. Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Unpruned Baseline Model
base_model = DecisionTreeRegressor(random_state=42)
base_model.fit(X_train, y_train)

print("--- UNPRUNED BASELINE MODEL ---")
print("MSE Train:", mean_squared_error(y_train, base_model.predict(X_train)))
print("MSE Test: ", mean_squared_error(y_test, base_model.predict(X_test)))
print("R2 Train: ", r2_score(y_train, base_model.predict(X_train)))
print("R2 Test:  ", r2_score(y_test, base_model.predict(X_test)))

# 4. Pre-Pruned Model
pruned_model = DecisionTreeRegressor(max_depth=3, min_samples_leaf=15, random_state=42)
pruned_model.fit(X_train, y_train)

print("\n--- PRE-PRUNED MODEL (max_depth=3, min_samples_leaf=15) ---")
print("MSE Test: ", mean_squared_error(y_test, pruned_model.predict(X_test)))
print("R2 Test:  ", r2_score(y_test, pruned_model.predict(X_test)))
```

---

## 🔑 Key Takeaways
1. Unconstrained regression trees easily overfit, causing $R^2$ to become negative on test data.
2. `plot_tree` allows visual inspection of leaf sizes and split criteria.
3. Pre-pruning via `max_depth` and `min_samples_leaf` is essential to achieve positive generalization performance.
