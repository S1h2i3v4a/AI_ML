# Lecture 27.05: Feature Encoding — Nominal, Ordinal & Dummy Variable Traps

## 📌 Executive Summary
Encoding categorical features into numerical matrix space, LabelEncoder for binary/ordinal structures, OneHotEncoder with drop='first' to prevent multicollinear rank deficiency.

---

## 🏛️ Theoretical Formulation & Mathematical Architecture

### 🔢 The Mathematical Need for Categorical Encoding

Machine learning estimators (such as Logistic Regression, KNN, Support Vector Machines, and Neural Networks) operate strictly on real-valued vector spaces:

$$
\mathbf{x} \in \mathbb{R}^d
$$

Categorical strings cannot participate in inner products $\mathbf{w}^T \mathbf{x}$ or Euclidean distance calculations $\|\mathbf{x}_i - \mathbf{x}_j\|_2$ without being deterministically mapped to numerical scalars.

---

### 🛡️ The Dummy Variable Trap & Matrix Invertibility

When encoding a categorical variable $C$ with $K$ distinct categories into binary indicator columns:

$$
\mathbf{d}_k = egin{bmatrix} \mathbb{I}(c_1 = k) \ \mathbb{I}(c_2 = k) \ dots \ \mathbb{I}(c_m = k) \end{bmatrix} \quad 	ext{for } k = 1, 2, \dots, K
$$

The sum across all $K$ dummy columns equals the intercept column vector $\mathbf{1}$:

$$
\sum_{k=1}^K \mathbf{d}_k = \mathbf{1}
$$

If all $K$ columns are included in a design matrix with an explicit intercept term, the columns become **linearly dependent**:

$$
\mathbf{d}_K = \mathbf{1} - \sum_{k=1}^{K-1} \mathbf{d}_k
$$

#### Mathematical Consequences:
1. The Gram matrix $\mathbf{X}^T \mathbf{X}$ becomes **singular**:
   
$$
   \det(\mathbf{X}^T \mathbf{X}) = 0
$$

2. In OLS and unregularized Logistic Regression, weights $\mathbf{w}$ become non-unique and have infinite variance.
3. Setting `drop='first'` produces exactly $K-1$ linearly independent columns, using the dropped category as the baseline reference state.

---

## 💻 Vectorized Python Implementation

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

df = pd.read_csv("loan_approval_data.csv").dropna()
df = df.drop(columns=["Applicant_ID"])

# 1. Label Encoding for target and ordinal
le_target = LabelEncoder()
df["Loan_Approved"] = le_target.fit_transform(df["Loan_Approved"])

le_edu = LabelEncoder()
df["Education_Level"] = le_edu.fit_transform(df["Education_Level"])

# 2. One-Hot Encoding with drop='first'
ohe_cols = ["Employment_Status", "Marital_Status", "Loan_Purpose", "Property_Area", "Gender", "Employer_Category"]
ohe = OneHotEncoder(drop="first", sparse_output=False)
encoded_arr = ohe.fit_transform(df[ohe_cols])
encoded_df = pd.DataFrame(encoded_arr, columns=ohe.get_feature_names_out(ohe_cols), index=df.index)

# Merge
df_encoded = pd.concat([df.drop(columns=ohe_cols), encoded_df], axis=1)
print("Encoded Design Matrix Shape:", df_encoded.shape)

```

---

## 🔬 Key Engineering Takeaways & Invariants
1. **Mathematical Grounding**: Every transformation and classification step directly addresses the underlying empirical distribution and financial risk constraints.
2. **Reproducibility**: Clean, leak-free pipeline partitioning guarantees that performance metrics match production operating realities.
3. **Domain Alignment**: Aligning model evaluation with the asymmetric cost of financial errors protects institutional solvency.
