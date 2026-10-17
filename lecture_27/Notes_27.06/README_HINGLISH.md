# Notes_27.06: Correlation Analysis Aur Heatmap [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne **Correlation Heatmap** banakar samjhaya hai: kaun se features loan approval ke liye sabse zyada zimmedar hain aur kaun se rejection ke liye.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- `df.corr()` aur Seaborn heatmap ka use.
- Positive correlation: Wo features jinke badhne se loan pass hone ka chance badhta hai (`Credit_Score`).
- Negative correlation: Wo features jinke badhne se loan reject hota hai (`DTI_Ratio`).
- Multicollinearity check karna.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Sabse Bada Hero Feature (`Credit_Score`):
Heatmap mein sabse strong positive correlation `Credit_Score` ka dikhta hai. Agar applicant ka score 750+ hai toh loan approve hone ka chance exponentially badh jata hai.

#### 2. Sabse Bada Villian Feature (`DTI_Ratio`):
Debt-to-Income (DTI) ratio ka negative correlation hota hai. Agar kisi insaan ki aamdani ka 60% hissa purani EMI bhadne mein ja raha hai, toh bank use naya loan dene se mana kar dega.

---

### 💻 Python Code

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

### 📌 Summary Points
- Credit Score positive factor hai, DTI ratio negative factor hai.
- Heatmap se model ke liye sabse important features identify hote hain.
