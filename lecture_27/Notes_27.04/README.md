# Lecture 27.04: Exploratory Data Analysis (EDA)

## 📌 Topic Overview
In this lecture, Shraddha ma'am conducts **Exploratory Data Analysis (EDA)** on the loan dataset, examining class balance, income distributions, and detecting severe right-skewness and outliers.

---

## 🔍 Key Findings from EDA
1. **Target Distribution**: Approximately 68% of applications were Approved and 32% were Rejected.
2. **Income Skewness**: `Applicant_Income` has heavy right-skewness (most people earn ₹30k–₹70k, but a few high earners make ₹2,00,000+).
3. **Outlier Detection**: Boxplots reveal several wealth outliers that require scaling or non-linear transformation.

---

## 💻 Python Implementation

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

## 🔑 Key Takeaways
1. Visualizing histograms and boxplots reveals skewness before modeling.
2. Never treat high-income applicants as erroneous anomalies; in banking, high income is a genuine positive signal!
