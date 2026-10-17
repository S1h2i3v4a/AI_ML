# Notes_27.09: Feature Engineering Se Model Sudharna [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne **Feature Engineering** karke model ki accuracy aur precision ko aur behtar banane ke practical tareeqe sikhaye hain.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Feature Engineering kya hoti hai?
- `DTI_Ratio` ka square ($DTI^2$) kyu banaya gaya?
- `Credit_Score` ka square ($Score^2$) kyu banaya gaya?
- Income ka Logarithm (`log1p`) nikalna.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. DTI Ka Square Kyu Kiya?
Agar kisi ka Debt-to-Income ratio 10% se 20% hota hai toh itna khatra nahi hota. Lekin agar 50% se 60% hota hai toh default hone ka khatra **exponentially badh jata hai**! Squaring ($DTI^2$) karne se model ko yeh non-linear khatra asani se samajh aa jata hai.

#### 2. Income Ka Log Transformation:
Kyunki income bohot right-skewed thi (kuch log croron kamate hain), log lene se saare numbers ek sundar bell-curve (normal distribution) mein aa jaate hain.

---

### 💻 Python Code

```python
import numpy as np
import pandas as pd

def engineer_non_linear_loan_features(df):
    """
    Applies domain-specific non-linear transformations:
    1. DTI_Ratio_sq: Quadratic penalty for high debt-to-income (DTI^2)
    2. Credit_Score_sq: Non-linear reward for stellar credit scores (Score^2)
    3. Applicant_Income_log: Log transformation compressing income skewness
    """
    df_feat = df.copy()

    # 1. Polynomial non-linear terms
    if 'DTI_Ratio' in df_feat.columns:
        df_feat['DTI_Ratio_sq'] = df_feat['DTI_Ratio'] ** 2
    
    if 'Credit_Score' in df_feat.columns:
        df_feat['Credit_Score_sq'] = df_feat['Credit_Score'] ** 2

    # 2. Log transformation to normalize income skewness
    if 'Applicant_Income' in df_feat.columns:
        df_feat['Applicant_Income_log'] = np.log1p(df_feat['Applicant_Income'])

    return df_feat

# --- Function Call & Testing ---
# engineered_df = engineer_non_linear_loan_features(encoded_df)
# print("Features after Engineering:", [c for c in engineered_df.columns if '_sq' in c or '_log' in c])
```

---

### 📌 Summary Points
- Naye smart features banane se model ki accuracy badhti hai.
- Polynomial terms ($DTI^2$) non-linear risk ko capture karte hain.
