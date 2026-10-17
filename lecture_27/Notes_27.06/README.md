# Lecture 27.06: Correlation Analysis & Heatmap

## 📌 Topic Overview
In this lecture, Shraddha ma'am plots the **Correlation Heatmap** (`sns.heatmap(df.corr())`), analyzing which financial attributes exhibit the strongest relationship with loan approval.

---

## 📈 Key Correlation Findings
1. **Strongest Positive Driver**: `Credit_Score` (higher bureau score significantly boosts approval probability).
2. **Strongest Negative Driver**: `DTI_Ratio` (Debt-to-Income ratio; high existing debt drives rejections).
3. **Savings & Collateral**: Moderate positive correlation with approval.

---

## 💻 Python Implementation

```python
import pandas as pd
import seaborn as sns

def analyze_feature_correlations(df, target_col='Loan_Approved'):
    """
    Computes Pearson correlation matrix and identifies top risk drivers:
    - Positive drivers: Features that increase approval probability (e.g. Credit_Score)
    - Negative drivers: Features that increase rejection probability (e.g. DTI_Ratio)
    """
    corr_matrix = df.corr()
    target_corrs = corr_matrix[target_col].sort_values(ascending=False)

    top_positive = target_corrs.index[1:4].tolist()
    top_negative = target_corrs.index[-3:].tolist()

    insights = {
        'target_correlations': target_corrs.to_dict(),
        'top_positive_drivers': top_positive,
        'top_negative_drivers': top_negative
    }
    return insights

# --- Function Call & Testing ---
# insights = analyze_feature_correlations(encoded_df)
# print("Top Positive Approval Factors:", insights['top_positive_drivers'])
# print("Top Negative Risk Factors:    ", insights['top_negative_drivers'])
```

---

## 🔑 Key Takeaways
1. A correlation heatmap quickly reveals feature relationships before training.
2. Multicollinear features (correlation > 0.85) should be inspected to avoid redundancy.
