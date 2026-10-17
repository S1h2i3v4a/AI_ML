# Lecture 28.10: Pre-Pruning Implementation in Python

## 📌 Topic Overview
In this lecture, we implement **Pre-Pruning** on the Titanic dataset. We systematically iterate over different tree depths (`max_depth`), discover the optimal depth where test accuracy peaks, and automate hyperparameter tuning with `GridSearchCV`.

---

## 🔍 The Systematic Depth Search Loop
In the video, the instructor writes a clean loop over candidate depths:
```python
max_depths = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for depth in max_depths:
model = DecisionTreeClassifier(max_depth=depth, random_state=42)
model.fit(X_train, y_train)
acc = model.score(X_test, y_test)
print(f"for depth={depth}, accuracy={acc}")
```

### Actual Output from the Lecture:
- `for depth=2,  accuracy = 0.772`
- `for depth=3,  accuracy = 0.806`
- **`for depth=4,  accuracy = 0.825`** $\leftarrow$ **PEAK PERFORMANCE!**
- `for depth=5,  accuracy = 0.795`
- `for depth=6,  accuracy = 0.784`
- `for depth=7,  accuracy = 0.780`
- `for depth=8,  accuracy = 0.791`
- `for depth=9,  accuracy = 0.765`
- `for depth=10, accuracy = 0.791`

### Key Takeaway from the Results:
As `max_depth` increases from 2 to 4, the model learns meaningful feature splits and accuracy climbs to **82.5%**. 
Beyond depth 4, the tree starts memorizing noise, and testing accuracy steadily degrades! Thus, **`max_depth=4`** is the optimal sweet spot.

---

## ⚙️ Automated Tuning with `GridSearchCV`
Instead of tuning one parameter by hand, we can use Scikit-Learn's `GridSearchCV` to cross-validate multiple hyperparameters simultaneously (`max_depth`, `min_samples_leaf`, and `min_samples_split`).

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
'max_depth': [3, 4, 5, 6],
'min_samples_leaf': [1, 2, 5, 10],
'min_samples_split': [2, 5, 10]
}

grid = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid, cv=5, scoring='accuracy')
grid.fit(X_train, y_train)

print("Best Parameters:", grid.best_params_)
print("Best Cross-Validation Score:", grid.best_score_)
```

---

## 🔑 Key Takeaways
1. Pre-pruning via `max_depth` stops the tree from growing overly complex branches.
2. In the Titanic dataset, `depth=4` achieved the peak test accuracy of 82.5% (compared to 77.5% unpruned).
3. `GridSearchCV` automates the search across combinations of `max_depth`, `min_samples_leaf`, and `min_samples_split`.
