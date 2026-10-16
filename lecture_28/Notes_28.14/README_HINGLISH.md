# Lecture 28.14: Decision Tree Regressor Implementation in Scikit-Learn

## 📌 Executive Summary (Hinglish)
Scikit-Learn DecisionTreeRegressor ka complete production pipeline, multi-dimensional tabular regression, hyperparameter tuning, aur Linear Regression ke sath comparison.

---

### 📋 Is Topic/Section Mein Hum Kya Cover Kar Rahe Hain?
1. `DecisionTreeRegressor` class ka configuration aur parameter tuning.
2. Overfitting visualization: Unpruned regressor vs regularized smooth step approximation.
3. Evaluation metrics: Mean Squared Error (MSE), Root MSE (RMSE), aur $R^2$ coefficient of determination.
4. DecisionTreeRegressor vs Linear Regression: Non-linear response surface capability.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**API Implementation**: `from sklearn.tree import DecisionTreeRegressor` se continuous estimator initialize karke fit kiya jaata hai.

**Overfitting Trap**: Regression trees classification se bhi zyada aggressively overfit kar sakti hain, jahan har single training point ke liye separate step create ho jaata hai.

**Evaluation Metrics**: Regression performance measure karne ke liye $R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}$ aur RMSE calculate karte hain.

**Linear vs Tree Benchmark**: Linear regression sirf straight slope fit karta hai, jabki DecisionTreeRegressor non-linear sinusoidal ya multi-threshold pricing surfaces ko naturally fit kar leta hai.

---

## 🏛️ Mathematical Architecture & Detailed Theory

### 💻 DecisionTreeRegressor API & Evaluation Framework

In Scikit-Learn, `DecisionTreeRegressor` implements regression tree induction with support for `criterion='squared_error'`, `'friedman_mse'`, `'absolute_error'`, and `'poisson'`.

#### Evaluation Metrics Formulation:

1. **Mean Squared Error (MSE)**:
   
$$
   \text{MSE} = \frac{1}{m} \sum_{i=1}^m (y_i - \hat{y}_i)^2
$$

2. **Root Mean Squared Error (RMSE)**:
   
$$
   \text{RMSE} = \sqrt{\text{MSE}}
$$

3. **Coefficient of Determination ($R^2$)**:
   
$$
   \boxed{
   R^2 = 1 - \frac{\sum_{i=1}^m (y_i - \hat{y}_i)^2}{\sum_{i=1}^m (y_i - \bar{y})^2} = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}}
   }
$$

Where $R^2 = 1.0$ represents a perfect regression fit, and $R^2 = 0.0$ corresponds to a naive baseline predicting the global mean $\bar{y}$.

---

## 💻 Python Implementation & Code Example

```python
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Fit regularized regressor
reg_model = DecisionTreeRegressor(max_depth=4, min_samples_leaf=5, random_state=42)
reg_model.fit(X_1d, y_1d)

preds = reg_model.predict(X_1d)
mse = mean_squared_error(y_1d, preds)
r2 = r2_score(y_1d, preds)

print(f"Regression MSE: {mse:.4f}")
print(f"Regression R^2: {r2:.4f}")
assert r2 > 0.80, "Depth 4 tree must capture non-linear sine trend with high R^2"

```

---

## 🎯 Quick Revision Points (Interview Notes)
- **Scale Invariance**: Decision Trees monotonically invariant hote hain, isliye inme `StandardScaler` mandatory nahi hota.
- **Gini vs Entropy**: Gini speed mein 10x faster hota hai kyunki logarithm computation ki zaroorat nahi padti.
- **Pruning Necessity**: Unconstrained decision tree hamesha overfit karti hai; `min_samples_leaf` aur `ccp_alpha` sabse effective regularizers hain.
