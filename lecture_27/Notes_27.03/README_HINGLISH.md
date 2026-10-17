# Notes_27.03: Missing Values Ko Handle Karna [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne dataset ke missing (khali) values ko dhoondh kar unhe **SimpleImputer** se bharne ka standard tareeqa sikhaya hai.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- `df.isnull().sum()` se missing values check karna.
- Rows ko delete kyu nahi karna chahiye?
- Numerical features ke liye **Median / Mean** strategy.
- Categorical features ke liye **Most Frequent (Mode)** strategy.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Data Delete Kyu Na Karein?
Agar 1,000 mein se 200 rows mein koi ek value missing hai, aur aap `dropna()` chala do, toh 20% real customer data waste ho jayega! Isliye hum **Imputation** (khali jagah ko statistical value se bharna) karte hain.

#### 2. Konse Feature Ko Kaise Bharein?
- **Numbers (Income, Credit Score)**: Agar Income mein koi bohot ameer insaan (outlier) hai, toh **Median** sabse safe rehta hai.
- **Text / Categories (Employment, Marital Status)**: Jo category sabse zyada baar aayi ho (**Mode / Most Frequent**), use khali jagah par rakh dete hain.

---

### 📊 Visual Flowchart: Missing Value Imputation

```mermaid
flowchart TD
    A["Missing Values Check Karo"] --> BColumn Ka Type Kya Hai?
    B -->|"Numbers (Income, Score)"| C["Median / Mean Lagao"]
    B -->|"Categories (Salaried, Urban)"| D["Mode (Most Frequent) Lagao"]
    C --> E["Dataset 100% Ready (No NaN Values)"]
    D --> E
```

---

### 💻 Python Code

```python
import pandas as pd
from sklearn.impute import SimpleImputer

def impute_loan_missing_values(df):
    """
    Imputes missing values using statistical strategies:
    - Numerical features (Income, DTI, Credit_Score): Mean or Median strategy
    - Categorical features (Employment, Marital_Status): Most Frequent (Mode) strategy
    """
    df_clean = df.copy()

    # Identify numerical and categorical columns with missing values
    num_cols = df_clean.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = df_clean.select_dtypes(include=['object']).columns

    # 1. Numerical Imputation (Median is robust against extreme outliers)
    num_imputer = SimpleImputer(strategy='median')
    df_clean[num_cols] = num_imputer.fit_transform(df_clean[num_cols])

    # 2. Categorical Imputation (Most frequent / Mode)
    cat_imputer = SimpleImputer(strategy='most_frequent')
    df_clean[cat_cols] = cat_imputer.fit_transform(df_clean[cat_cols])

    missing_remaining = df_clean.isnull().sum().sum()
    return df_clean, missing_remaining

# --- Function Call & Testing ---
# clean_df, nulls_left = impute_loan_missing_values(raw_df)
# print("Remaining Missing Values after Imputation:", nulls_left)
```

---

### 📌 Summary Points
- Rows drop karne ke bajaye statistical imputation karein.
- Numerical ke liye median aur categorical ke liye mode best hai.
