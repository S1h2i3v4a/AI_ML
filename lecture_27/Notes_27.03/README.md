# Lecture 27.03: Handling Missing Values — Statistical Imputation Strategies

## 📌 Executive Summary
Theoretical framework for handling missing data, MCAR vs MAR mechanisms, Scikit-Learn SimpleImputer, and preventing information leakage during statistical imputation.

---

## 🏛️ Theoretical Formulation & Mathematical Architecture

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

## 💻 Vectorized Python Implementation

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

## 🔬 Key Engineering Takeaways & Invariants
1. **Mathematical Grounding**: Every transformation and classification step directly addresses the underlying empirical distribution and financial risk constraints.
2. **Reproducibility**: Clean, leak-free pipeline partitioning guarantees that performance metrics match production operating realities.
3. **Domain Alignment**: Aligning model evaluation with the asymmetric cost of financial errors protects institutional solvency.
