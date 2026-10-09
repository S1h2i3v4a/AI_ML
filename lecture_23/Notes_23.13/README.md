# Module 23.13: Linear Regression Hands-On Implementation (Insurance Dataset)

## 1. End-to-End Supervised Learning Pipeline

In this module, we execute an end-to-end industry standard implementation of Linear Regression using the real-world `insurance.csv` dataset.

```
+------------------------------------------------------------------------------------+
| 1. Data Ingestion & Inspection (EDA)                                               |
|    - Shape, data types, missing values, distributions                              |
+-----------------------------------------+------------------------------------------+
                                          |
                                          v
+------------------------------------------------------------------------------------+
| 2. Feature Engineering & Preprocessing                                             |
|    - One-Hot Encoding for categorical features (sex, smoker, region)                |
|    - Train-Test Split (80% Train, 20% Test)                                        |
|    - Feature Scaling (StandardScaler)                                              |
+-----------------------------------------+------------------------------------------+
                                          |
                                          v
+------------------------------------------------------------------------------------+
| 3. Model Training & Parameter Interpretation                                       |
|    - Fit LinearRegression on training data                                         |
|    - Extract learned coefficients w_j and intercept b                               |
+-----------------------------------------+------------------------------------------+
                                          |
                                          v
+------------------------------------------------------------------------------------+
| 4. Evaluation & Diagnostic Plots                                                   |
|    - Actual vs. Predicted scatter plot                                             |
|    - Residual analysis                                                             |
+------------------------------------------------------------------------------------+
```

---

## 2. Dataset Overview: Medical Cost Personal Datasets

The `insurance.csv` dataset contains individual medical records:
- `age`: Age of primary beneficiary (integer)
- `sex`: Insurance contractor gender (`female`, `male`)
- `bmi`: Body mass index ($kg / m^2$) (ideal: 18.5 to 24.9)
- `children`: Number of children / dependents covered
- `smoker`: Smoking status (`yes`, `no`)
- `region`: Beneficiary's residential area in US (`northeast`, `northwest`, `southeast`, `southwest`)
- **Target `charges`:** Individual medical costs billed by health insurance ($).

---

## 3. Categorical Encoding (Dummy Variables)

Linear models cannot process string variables directly. We apply **One-Hot Encoding** (or dummy encoding with `drop_first=True` to prevent the dummy variable trap of multi-collinearity):

$$
\text{smoker\_yes} = \begin{cases} 1 & \text{if smoker} = \text{'yes'} \\ 0 & \text{if smoker} = \text{'no'} \end{cases}
$$

When a categorical feature has $k$ levels, we generate $k-1$ binary indicators. The omitted level serves as the reference baseline absorbed into the intercept $b$.

---

## 4. Model Training & Interpreting Learned Coefficients

In scikit-learn:
```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

The prediction equation is:

$$
\hat{y} = b + w_1 x_1 + w_2 x_2 + \dots + w_p x_p
$$

- **Intercept $b$:** The expected baseline charges when all numerical features are zero and categorical indicators are at reference values.
- **Coefficient $w_j$:** The expected change in target charges ($\Delta y$) for a 1-unit increase in feature $x_j$, holding all other features strictly constant (*ceteris paribus*).
  - For example, smoking status yields an enormous positive coefficient $w_{\text{smoker\_yes}} \approx +\$23,800$, reflecting massive risk premiums.
