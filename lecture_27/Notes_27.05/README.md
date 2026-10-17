# Lecture 27.05: Feature Encoding (Nominal, Ordinal & Dummies)

## 📌 Topic Overview
In this lecture, Shraddha ma'am demonstrates how to convert text categorical attributes into numerical vectors using **Label Encoding** and **One-Hot Encoding**, avoiding the Dummy Variable Trap.

---

## 🏛️ Encoding Strategy

```mermaid
flowchart TD
    Cat["Categorical Feature"] --> DecisionIs it Binary or Multi-Category?
    Decision -->|"Binary (e.g. Yes/No, Approved/Rejected)"| Label["LabelEncoder<br/>Maps to 0 and 1"]
    Decision -->|"Multi-Category (e.g. Urban/Rural/Semi-Urban)"| OHE["One-Hot Encoding<br/>pd.get_dummies(drop_first=True)<br/>Avoids dummy trap!"]
```

---

## 💻 Python Implementation

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def encode_loan_features(df):
    """
    Encodes categorical features into numerical representations:
    - Binary features / Target: LabelEncoder (0 and 1)
    - Nominal multi-category features: One-Hot Encoding (pd.get_dummies with drop_first=True)
    """
    df_encoded = df.copy()

    # 1. Label encode binary target and binary attributes
    le = LabelEncoder()
    if 'Loan_Approved' in df_encoded.columns:
        df_encoded['Loan_Approved'] = le.fit_transform(df_encoded['Loan_Approved'])

    # 2. Convert nominal categories with pd.get_dummies(drop_first=True)
    nominal_cols = ['Employment_Status', 'Marital_Status', 'Property_Area', 'Loan_Purpose']
    existing_nominals = [c for c in nominal_cols if c in df_encoded.columns]
    
    df_encoded = pd.get_dummies(df_encoded, columns=existing_nominals, drop_first=True)

    return df_encoded

# --- Function Call & Testing ---
# encoded_df = encode_loan_features(clean_df)
# print("Encoded DataFrame Shape:", encoded_df.shape)
```

---

## 🔑 Key Takeaways
1. Machine learning models require numerical matrices; text categories must be encoded.
2. Always use `drop_first=True` in One-Hot Encoding to eliminate perfect multicollinearity.
