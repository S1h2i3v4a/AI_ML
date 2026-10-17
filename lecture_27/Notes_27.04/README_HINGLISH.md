# Notes_27.04: Exploratory Data Analysis (EDA) [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne **Exploratory Data Analysis (EDA)** karke data ke patterns, distributions, aur outliers ko visual charts se samjhaya hai.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Target feature (`Loan_Approved`) ka class balance check karna.
- Income aur Loan Amount ka distribution (Histogram aur KDE plot).
- Boxplot se outliers (aswabhavik values) pehchanna.
- Skewed data ko samajhna.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Target Balance:
Data mein lagbhag 68% logon ka loan approve hua hai aur 32% ka reject. Isse pata chalta hai ki data halka sa imbalanced hai.

#### 2. Income Ka Right-Skewness:
Zyadatar applicants ki income ₹30,000 se ₹80,000 ke beech mein hai. Lekin kuch log aise hain jinki income ₹2 Lakh ya ₹3 Lakh hai. Yeh points boxplot mein **Outliers** ban kar dikhte hain. Banking mein in ameer logon ko drop nahi karte, balki log transformation se unka skew theek karte hain.

---

### 💻 Python Code

```python
import matplotlib.pyplot as plt
import seaborn as sns

def perform_loan_eda(df):
    """
    Performs core exploratory data analysis:
    - Target class balance inspection
    - Numerical distributions (Income, Loan Amount)
    - Outlier identification using boxplots
    """
    # 1. Target distribution
    target_counts = df['Loan_Approved'].value_counts()
    target_proportions = df['Loan_Approved'].value_counts(normalize=True)

    # 2. Outlier summary for Income
    q25 = df['Applicant_Income'].quantile(0.25)
    q75 = df['Applicant_Income'].quantile(0.75)
    iqr = q75 - q25
    upper_fence = q75 + 1.5 * iqr

    outliers_count = (df['Applicant_Income'] > upper_fence).sum()

    eda_summary = {
        'target_proportions': target_proportions.to_dict(),
        'income_iqr': float(iqr),
        'upper_fence': float(upper_fence),
        'outlier_samples': int(outliers_count)
    }
    return eda_summary

# --- Function Call & Testing ---
# summary = perform_loan_eda(clean_df)
# print("Target Balance:", summary['target_proportions'])
# print(f"Income Outlier Fence: Rs {summary['upper_fence']:,.2f}")
# print(f"Outliers Count: {summary['outlier_samples']}")
```

---

### 📌 Summary Points
- EDA se model banane se pehle data ki bimariyan samajh aati hain.
- Outliers ko delete karne se pehle business context dekhna zaroori hai.
