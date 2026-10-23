# Lecture 30.03: Gradient Boosting Regressor Ka Python Code — Scikit-Learn Implementation [Hinglish]

[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_30_03.ipynb)
[![English Notes](https://img.shields.io/badge/Notes-English-blue.svg)](README.md)
[![English PDF](https://img.shields.io/badge/PDF-English-red.svg)](notes.pdf)
[![Hinglish PDF](https://img.shields.io/badge/PDF-Hinglish-green.svg)](notes_hinglish.pdf)

---

## 📌 Topic Overview
Production implementation of GradientBoostingRegressor in Scikit-Learn. Covers dataset synthesis via make_regression, hyperparameter calibration (n_estimators, learning_rate, max_depth, subsample, loss='squared_error'), model fitting, and multi-metric regression evaluation (MSE, RMSE, R^2 score).

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Scikit-Learn se `GradientBoostingRegressor` import aur instantiate karna.
- Important Hyperparameters: `n_estimators`, `learning_rate`, `max_depth`, `subsample`, `loss`.
- Model training (`.fit`) aur continuous prediction (`.predict`) pipeline.
- Evaluation Metrics: Mean Squared Error (MSE), Root Mean Squared Error (RMSE), aur R2 Score.
- Stochastic Gradient Boosting (`subsample=0.8`) se variance kam karne ka tarika.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation
**Scikit-Learn API**: Scikit-Learn ke `ensemble` module mein `GradientBoostingRegressor` available hota hai: `from sklearn.ensemble import GradientBoostingRegressor`.

**Crucial Hyperparameters**:

- `loss='squared_error'`: Standard Mean Squared Error (MSE) loss function optimize karta hai.
- `n_estimators=100`: Sequential decision trees ki total ginti (jitne zyaada trees, utna deeply fit karega).
- `learning_rate=0.1`: Har tree ke contribution ko shrink karta hai. Agar learning_rate kam karein (e.g. 0.05), toh n_estimators badhana padega!
- `max_depth=3`: Har individual tree ki maximum gehrai (boosting mein shallow trees = weak learners use hote hain taaki overfit na ho).
- `subsample=0.8`: Stochastic Gradient Boosting — har tree ko train karne ke liye 80% random rows choose karta hai.

**Evaluation Metrics**: Regression model ko evaluate karne ke liye: $R^2$ score (jitna 1.0 ke kareeb utna accha) aur RMSE (Root Mean Squared Error).

---

### 📊 Visual Flowchart / Diagram

```mermaid
flowchart LR
    A["Raw Regression Features (X, y)"] --> B["Train-Test Partition (80/20)"]
    B --> C["Configure GradientBoostingRegressor(lr=0.1, n_est=100)"]
    C --> D["Fit Sequential Trees on Pseudo-Residuals"]
    D --> E["Inference on Unseen X_test"]
    E --> F["Metrics: R2 Score, RMSE, MSE"]
```

---

### 🛠️ Mathematical Formulations
The mean squared error loss and coefficient of determination $R^2$ are evaluated as:

$$
\text{MSE} = \frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2, \quad \text{RMSE} = \sqrt{\text{MSE}}
$$

$$
R^2 = 1 - \frac{\sum_{i=1}^N (y_i - \hat{y}_i)^2}{\sum_{i=1}^N (y_i - \bar{y})^2}
$$

---

### 💻 Python Code Implementation

```python
import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

def train_gradient_boosting_regressor(n_samples=500, n_features=6, n_estimators=100, learning_rate=0.1, max_depth=3):
    """
    Builds, trains, and evaluates a Scikit-Learn GradientBoostingRegressor pipeline.
    
    Returns:
    --------
    model : GradientBoostingRegressor
        Trained gradient boosting model.
    metrics : dict
        Evaluation metrics on test partition (MSE, RMSE, R2).
    """
    # 1. Generate synthetic regression dataset
    X, y = make_regression(
        n_samples=n_samples, n_features=n_features, noise=10.0, random_state=42
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # 2. Instantiate and fit GradientBoostingRegressor
    gbr = GradientBoostingRegressor(
        loss='squared_error',
        learning_rate=learning_rate,
        n_estimators=n_estimators,
        max_depth=max_depth,
        subsample=0.8,
        random_state=42
    )
    gbr.fit(X_train, y_train)
    
    # 3. Predict on unseen test partition
    y_pred = gbr.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    metrics = {
        "mse": float(mse),
        "rmse": float(rmse),
        "r2_score": float(r2)
    }
    
    return gbr, metrics

# ----------------- Driver Execution & Testing -----------------
if __name__ == "__main__":
    trained_gbr, perf_metrics = train_gradient_boosting_regressor(
        n_estimators=100, learning_rate=0.1, max_depth=3
    )
    
    print("=" * 60)
    print("--- SCIKIT-LEARN GRADIENT BOOSTING REGRESSOR PIPELINE ---")
    print(f"Trained Estimators (Trees) : {len(trained_gbr.estimators_)}")
    print(f"Test Mean Squared Error (MSE): {perf_metrics['mse']:.3f}")
    print(f"Test Root MSE (RMSE)         : {perf_metrics['rmse']:.3f}")
    print(f"Test R^2 Determination Score : {perf_metrics['r2_score']:.4f}")
    print("=" * 60)
```

---

### 📌 Summary Points & Key Takeaways
1. **Sequential Learning**: Har agla model pichhle model ki galtiyon ko seekhta hai.
2. **Shrinkage (Learning Rate)**: 0.1 jaise chote kadam lene se model overfit hone se bachta hai.
3. **Weak Learners**: Boosting mein shallow decision trees (depth 1 se 3) use kiye jaate hain.
