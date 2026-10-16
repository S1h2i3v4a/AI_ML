# Lecture 27.05: Feature Encoding — Binary, Ordinal aur One-Hot Dummy Variable Traps

## 📌 Executive Summary (Hinglish)
Categorical attributes ko numerical matrix space mein map karna, binary target aur ordinal variables ke liye LabelEncoder, aur multicollinearity se bachne ke liye OneHotEncoder(drop='first').

---

### 📋 Is Topic/Section Mein Hum Kya Cover Kar Rahe Hain?
1. Non-predictive identifier `Applicant_ID` ko drop karna taaki model overfitting na kare.
2. Target variable `Loan_Approved` aur ordinal feature `Education_Level` par `LabelEncoder` apply karna.
3. Multi-class nominal features par `OneHotEncoder(drop='first')` apply karna.
4. Dummy Variable Trap aur matrix invertibility $(\mathbf{X}^T \mathbf{X})^{-1}$ par iska mathematical impact.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**Dropping Identifier**: `Applicant_ID` database primary key hai jisme zero causal information hoti hai. Ise drop karna mandatory hai.

**Label Encoding**: `Loan_Approved` string levels ('No', 'Yes') ko binary digits (0, 1) mein transform kiya jaata hai. `Education_Level` ko integer ranks (0, 1, 2) diye jaate hain.

**One-Hot Encoding**: Nominal features jaise `Gender`, `Employment_Status`, `Marital_Status`, `Loan_Purpose`, `Property_Area`, `Employer_Category` ke liye orthogonal dummy columns bante hain.

**Dummy Variable Trap**: Agar kisi feature ke $K$ categories hain aur hum $K$ columns retain karein, toh unka sum hamesha bias vector $\mathbf{1}$ ke barabar ho jaata hai, leading to perfect multicollinearity. Isliye `drop='first'` se $K-1$ columns bante hain.

---

## 🏛️ Mathematical Architecture & Detailed Theory

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

## 💻 Python Implementation & Code Example

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

## 🎯 Quick Revision Points (Interview Notes)
- **Objective**: Credit risk modeling mein precision hamesha accuracy se zyada important hoti hai.
- **Data Invariant**: SimpleImputer aur StandardScaler ko hamesha training data par `fit` karke test set par sirf `transform` kiya jaata hai.
- **Decision Boundary**: Non-linear feature transformations ($DTI^2$, $Credit^2$) linear models ko non-linear patterns capture karne ki capability provide karte hain.
