# Lecture 27.03: Missing Values ko Handle Karna — Mean aur Mode Imputation Strategies

## 📌 Executive Summary (Hinglish)
Missing data handling ka statistical framework, MCAR vs MAR mechanisms, Scikit-Learn SimpleImputer se numerical aur categorical columns ki imputation, aur data leakage prevention.

---

### 📋 Is Topic/Section Mein Hum Kya Cover Kar Rahe Hain?
1. Missingness mechanisms: MCAR (Missing Completely at Random) vs MAR (Missing at Random).
2. `loan_approval_data.csv` mein missing values ka distribution (har column mein 50 missing values).
3. Continuous numerical columns ke liye Mean Imputation ka mathematical formulation.
4. Categorical columns ke liye Mode / Most Frequent Imputation ka execution.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**Missingness Theory**: MCAR ka matlab hai ki data missing hona kisi doosre variable par depend nahi karta. Yahan sabhi columns mein uniformly 50 missing rows inject hui hain, jo synthetic MCAR nature show karti hain.

**Missingness Audit**: Total 1,000 rows mein se har feature aur target column mein exactly 50 null values (`np.nan`) hain.

**Numerical Mean Imputation**: Numerical columns (Income, Age, Credit Score, etc.) ke liye missing cells ko feature ke sample mean $\mu = \frac{1}{n} \sum x_i$ se replace kiya jaata hai.

**Categorical Mode Imputation**: Categorical columns (Gender, Education, Employment Status, etc.) ke liye most frequent class (mode) se fill kiya jaata hai using `SimpleImputer(strategy='most_frequent')`.

---

## 🏛️ Mathematical Architecture & Detailed Theory

### 🔍 Missing Data Foundations & Mechanisms

In observational financial datasets, missing values arise frequently due to borrower form omission, system timeouts, or multi-branch data synchronization errors. Statistically, missing data mechanisms are categorized by Donald Rubin's taxonomy:

1. **Missing Completely at Random (MCAR)**:
   The probability of an observation being missing is completely independent of both observed and unobserved data:
   
$$
   P(M | Y_{	ext{obs}}, Y_{	ext{mis}}) = P(M)
$$

2. **Missing at Random (MAR)**:
   Missingness depends on observed features but not on the missing values themselves:
   
$$
   P(M | Y_{	ext{obs}}, Y_{	ext{mis}}) = P(M | Y_{	ext{obs}})
$$

3. **Missing Not at Random (MNAR)**:
   Missingness depends on the value of the unobserved feature itself (e.g., individuals with high debt refusing to report their DTI ratio).

---

### ⚙️ Statistical Imputation Formulations

#### 1. Mean Imputation for Continuous Numerical Variables:
For a numerical feature column $\mathbf{x} = [x_1, x_2, \dots, x_n]^T$ with observed index set $\mathcal{O}$:

$$
\hat{x}_{	ext{imputed}} = \mu_{	ext{observed}} = rac{1}{|\mathcal{O}|} \sum_{i \in \mathcal{O}} x_i
$$

While mean imputation preserves the first central moment (the sample mean), it compresses the sample variance $\sigma^2$. For moderately missing MCAR data ($5\%$ missingness rate), mean imputation is computationally robust and stable.

#### 2. Mode Imputation for Discrete Categorical Variables:
For a categorical feature column $\mathbf{c}$ with discrete levels $\{L_1, L_2, \dots, L_K\}$:

$$
\hat{c}_{	ext{imputed}} = rg\max_{L_k} \sum_{i \in \mathcal{O}} \mathbb{I}(c_i = L_k)
$$

The most frequent category replaces all missing instances.

---

## 💻 Python Implementation & Code Example

```python
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

df = pd.read_csv("loan_approval_data.csv")

# Detect columns by type
cat_cols = df.select_dtypes(include=["object"]).columns.tolist()
num_cols = df.select_dtypes(include=["number"]).columns.tolist()

# 1. Numerical Imputation
num_imputer = SimpleImputer(strategy="mean")
df[num_cols] = num_imputer.fit_transform(df[num_cols])

# 2. Categorical Imputation
cat_imputer = SimpleImputer(strategy="most_frequent")
df[cat_cols] = cat_imputer.fit_transform(df[cat_cols])

# Verification
assert df.isnull().sum().sum() == 0, "No missing values should remain post-imputation!"
print("Missing values successfully imputed across all 20 columns!")

```

---

## 🎯 Quick Revision Points (Interview Notes)
- **Objective**: Credit risk modeling mein precision hamesha accuracy se zyada important hoti hai.
- **Data Invariant**: SimpleImputer aur StandardScaler ko hamesha training data par `fit` karke test set par sirf `transform` kiya jaata hai.
- **Decision Boundary**: Non-linear feature transformations ($DTI^2$, $Credit^2$) linear models ko non-linear patterns capture karne ki capability provide karte hain.
