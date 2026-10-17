# Lecture 28.10: Pre-Pruning Implementation & GridSearchCV

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Video mein ma'am dwara likha gaya `max_depths = [2, 3, 4, 5, 6, 7, 8, 9, 10]` loop.
- Har depth par test accuracy ka live result aur `depth=4` par peak accuracy ($82.5\%$).
- Kyun depth 4 ke baad accuracy wapas girne lagti hai.
- `GridSearchCV` ka use karke best hyperparameters ko automatically dhoondhna.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Video Ka Systematic Loop Demonstration
Pichhle lecture mein baseline model ka test score $77.5\%$ tha.
Ma'am ne video mein loop likhkar alag-alag depths test ki:

```python
max_depths = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for depth in max_depths:
model = DecisionTreeClassifier(max_depth=depth, random_state=42)
model.fit(X_train, y_train)
acc = model.score(X_test, y_test)
print(f"for depth={depth}, accuracy={acc}")
```

#### 2. Screen Par Aaya Exact Output
- `depth=2` $\r\rightarrow 77.2\%$
- `depth=3` $\r\rightarrow 80.6\%$
- **`depth=4` $\r\rightarrow 82.5\%$** (Sabse acchi accuracy!)
- `depth=5` $\r\rightarrow 79.5\%$
- `depth=6` $\r\rightarrow 78.4\%$
- `depth=7` $\r\rightarrow 78.0\%$
- `depth=8` $\r\rightarrow 79.1\%$
- `depth=9` $\r\rightarrow 76.5\%$
- `depth=10` $\r\rightarrow 79.1\%$

#### 3. Ma'am Ka Core Observation
Ma'am ne explain kiya:
- Jab depth 2 se 4 hui, model ne ache patterns seekhe aur accuracy $77\%$ se badhkar **$82.5\%$** ho gayi!
- Lekin jaise hi depth 4 se aage gayi (5, 6, 7...), model ne fir se noise ko rattna shuru kar diya aur test accuracy gir gayi!
- Isse prove hota hai ki Titanic dataset par **`max_depth=4`** sabse best sweet-spot hai.

#### 4. `GridSearchCV` Se Automation
Ek-ek karke loop chalane ke bajaye hum `GridSearchCV` use kar sakte hain jo `max_depth`, `min_samples_leaf`, aur `min_samples_split` ke sabhi combinations ko 5-fold cross validation se evaluate karta hai.

---

### 💻 Python Code

```python
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

param_grid = {
'max_depth': [3, 4, 5, 6],
'min_samples_leaf': [1, 2, 5, 10],
'min_samples_split': [2, 5, 10]
}

grid = GridSearchCV(
DecisionTreeClassifier(random_state=42),
param_grid,
cv=5,
scoring='accuracy'
)
grid.fit(X_train, y_train)

print("Best Parameters:", grid.best_params_)
print(f"Best CV Accuracy: {grid.best_score_:.4f}")
```

---

### 📌 Summary Points
- Pre-pruning se test accuracy 77.5% se badhkar 82.5% ho gayi.
- `depth=4` par peak milta hai, uske baad tree overfit karne lagta hai.
- `GridSearchCV` best parameters ko bina manual loop ke automatically select karta hai.
