# Notes_27.05: Feature Encoding (Text Se Numbers Banana) [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne text columns (jaise `Employment_Status`, `Property_Area`) ko machine learning ke liye numbers mein convert karne ka tareeqa sikhaya hai.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Machine Learning algorithms ko text kyu samajh nahi aata?
- **LabelEncoder**: Binary (0 aur 1) columns ke liye.
- **One-Hot Encoding**: Multiple categories ke liye.
- `drop_first=True` kyu lagate hain (Dummy Variable Trap se bachav).

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Label Encoding:
Agar column mein sirf do hi options hain (jaise `Married` / `Single`, ya `Loan_Approved`: Yes / No), toh hum seedha unhe **0 aur 1** bana dete hain.

#### 2. One-Hot Encoding Aur Dummy Trap:
Agar column mein 3 options hain: `Urban`, `Semi-Urban`, `Rural`:
Agar hum unhe 0, 1, 2 denge toh model sochega ki Rural (2) Urban (0) se bada hai! Isliye hum naye boolean columns banate hain.
Aur `drop_first=True` lagane se ek column kam banta hai, jisse multicollinearity nahi hoti.

---

### 📊 Visual Flowchart: Encoding Ka Tareeqa

```mermaid
flowchart TD
    A["Text Column"] --> BKitne Options Hain?
    B -->|"Sirf 2 Options (Yes/No)"| C["LabelEncoder: 0 aur 1 banao"]
    B -->|"3 ya Zyada Options (Urban/Rural/Semi)"| D["One-Hot Encoding: pd.get_dummies(drop_first=True)"]
```

---

### 💻 Python Code

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

### 📌 Summary Points
- Text columns ko numbers mein convert karna mandatory hai.
- Multi-category ke liye `get_dummies(drop_first=True)` use karein.
