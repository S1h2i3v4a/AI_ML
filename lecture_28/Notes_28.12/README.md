# Lecture 28.12: Decision Tree Regressor

## 📌 Topic Overview
How does a Decision Tree work when the target variable is continuous (numerical) rather than categorical? In this lecture, we study the **Decision Tree Regressor**, understand how leaf predictions are calculated (mean/average), and examine the classroom numerical dataset.

---

## 🎯 Regression vs Classification in Trees

| Property | Decision Tree Classifier | Decision Tree Regressor |
| :--- | :--- | :--- |
| **Target Variable ($y$)** | Discrete classes (e.g., Yes/No, Cat/Dog) | **Continuous numbers** (e.g., Salary, House Price, Age) |
| **Leaf Prediction** | Majority class label (mode) | **Mean / Average ($\bar{y}$)** of leaf samples |
| **Impurity Metric** | Entropy or Gini Impurity | **Variance ($\sigma^2$), MSE, or MAE** |
| **Split Optimization** | Maximize Information Gain | Maximize **Variance Reduction** |

---

## 🍃 How Leaf Nodes Make Predictions: The Mean Value
In a classification tree, a leaf predicts the majority vote.
In a regression tree, if a leaf receives samples with target values $\{y_1, y_2, \dots, y_k\}$, the predicted value $\hat{y}$ is simply the **arithmetic mean**:

$$\hat{y} = \bar{y} = \frac{1}{k} \sum_{i=1}^k y_i$$

---

## 🧮 Blackboard Numerical Example: Target Dataset
In the video, the instructor writes a 4-sample dataset on the blackboard:

| Feature ($x$) | Target ($y$) |
| :--- | :--- |
| 1 | 2 |
| 2 | 4 |
| 3 | 6 |
| 4 | 10 |

### 1. Calculating the Mean ($\bar{y}$)
Total samples $n = 4$:

$$\bar{y} = \frac{2 + 4 + 6 + 10}{4} = \frac{22}{4} = 5.5$$

### 2. Calculating the Parent Node Variance ($V_S$)
The variance formula is:

$$V_S = \text{Var}(y) = \frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})^2$$

Calculating squared deviations from the mean ($\bar{y} = 5.5$):
- $(2 - 5.5)^2 = (-3.5)^2 = 12.25$
- $(4 - 5.5)^2 = (-1.5)^2 = 2.25$
- $(6 - 5.5)^2 = (0.5)^2 = 0.25$
- $(10 - 5.5)^2 = (4.5)^2 = 20.25$

$$\text{Sum of Squared Errors} = 12.25 + 2.25 + 0.25 + 20.25 = 35.0$$

$$V_S = \frac{35.0}{4} = 8.75$$

The instructor highlights on the blackboard: **$V_S = 8.75$**! This is the initial impurity of the parent node.

---

## 💻 Python Implementation

```python
import numpy as np
from sklearn.tree import DecisionTreeRegressor

def fit_regression_tree_example():
    """
    Fits a DecisionTreeRegressor on the 4-sample classroom dataset
    where target predictions are the mean of each leaf node.
    """
    # Classroom dataset: x = [1, 2, 3, 4], y = [2, 4, 6, 10]
    X = np.array([[1], [2], [3], [4]])
    y = np.array([2, 4, 6, 10])

    # 1. Calculate parent summary statistics
    y_mean = np.mean(y)
    y_var = np.var(y)

    # 2. Fit DecisionTreeRegressor with depth=1 (single split)
    reg = DecisionTreeRegressor(max_depth=1, random_state=42)
    reg.fit(X, y)

    # 3. Generate predictions
    predictions = reg.predict(X)

    return reg, y_mean, y_var, predictions

# --- Execute Function ---
regressor, parent_mean, parent_var, preds = fit_regression_tree_example()
print(f"Parent Mean (y_bar):   {parent_mean:.2f}")
print(f"Parent Variance (V_S): {parent_var:.2f}")
print(f"Model Predictions:     {preds}")
```

---

## 🔑 Key Takeaways
1. Decision Tree Regressors predict continuous numbers.
2. A leaf node's prediction is the **mean (average)** of the target values in that leaf.
3. Node impurity is measured using **Variance** or **Mean Squared Error (MSE)** instead of Entropy.
