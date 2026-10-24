# Submodule 33.06: Feature Correlation Matrix & Heatmap Analysis (Hinglish)

## Topic Overview & Mathematical Formulation
Encoding aur scaling se pehle features ke aapas ke linear relationships ko check karna zaroori hota hai. Iske liye hum **Pearson Correlation Coefficient ($r$)** calculate karte hain:

$$
r_{XY} = \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum_{i=1}^{n} (X_i - \bar{X})^2}\sqrt{\sum_{i=1}^{n} (Y_i - \bar{Y})^2}}
$$

- $r = +1$: Strong positive correlation (ek feature badhega toh dusra bhi badhega).
- $r = 0$: No correlation (dono features aapas mein independent hain).
- $r = -1$: Strong negative correlation (ek feature badhega toh dusra ghatega).

---

## 1. Python Code Implementation
Reference: [smartcart.ipynb](file:///c:/Users/Shivam%20Keshari/OneDrive/Desktop/AI-ML/lecture_33/SmartCart_Project/smartcart.ipynb) (Cells 24 - 28).

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Numeric features ka correlation matrix calculate karna
corr = df_cleaned.corr(numeric_only=True)

# Heatmap plot karna
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr,
    annot=True,
    annot_kws={"size": 6},
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.show()
```

---

## 2. Heatmap se Mili Key Business Insights

| Feature Pair | Correlation ($r$) | Nature | Business Explanation |
| :--- | :---: | :--- | :--- |
| **`Income` vs `Total_Spending`** | **+0.79** | Strong Positive | Dataset ka sabse strong correlation! Income badhegi toh total spending bhi proportionally badhegi. |
| **`Total_Spending` vs `NumCatalogPurchases`** | **+0.78** | Strong Positive | Jo log zyada spend karte hain, woh catalog se direct khareedte hain. |
| **`Income` vs `NumCatalogPurchases`** | **+0.69** | Positive | High income wale customers catalogs se purchase karte hain. |
| **`Income` vs `NumStorePurchases`** | **+0.63** | Positive | High income customers physical stores mein visit karke shopping karte hain. |
| **`Income` vs `NumWebVisitsMonth`** | **-0.65** | Strong Negative | High income customers website par bar-bar browse nahi karte; low-income log website bar-bar browse karte hain (window shopping). |
| **`NumStorePurchases` vs `NumWebVisitsMonth`** | **-0.43** | Moderate Negative | Jo log physical store se shopping karte hain, unki monthly website visits kaafi kam hoti hain. |
| **`Customer_Tenure_Days`, `Complain`, `Response`** | **$\approx 0.0$** | Independent | Yeh features independent information provide karte hain (white color in heatmap). |

---

## 3. Takeaway
Correlation matrix ne prove kiya ki dataset mein do prominent dimensions hain:
1. **Financial Power**: Income, Total Spending, Catalog Purchases.
2. **Channel Behavior**: Store & Catalog vs Repeated Website Browsing.
Yeh collinearity confirm karti hai ki **PCA (Principal Component Analysis)** dimensionality reduce karne ke liye perfectly suited hai!
