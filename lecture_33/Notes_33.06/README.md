# Submodule 33.06: Feature Correlation Matrix & Heatmap Analysis

## Topic Overview & Mathematical Formulation
Before performing feature encoding, scaling, and dimensionality reduction, we must analyze the linear interdependencies among our features. The pairwise relationship between two continuous variables $X$ and $Y$ is quantified using the **Pearson Correlation Coefficient ($r$)**:

$$
r_{XY} = \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum_{i=1}^{n} (X_i - \bar{X})^2}\sqrt{\sum_{i=1}^{n} (Y_i - \bar{Y})^2}}
$$

where:
- $r = +1$: Perfect positive linear correlation.
- $r = 0$: No linear relationship (orthogonal features).
- $r = -1$: Perfect negative linear correlation.

---

## 1. Python Implementation
Reference: [smartcart.ipynb](file:///c:/Users/Shivam%20Keshari/OneDrive/Desktop/AI-ML/lecture_33/SmartCart_Project/smartcart.ipynb) (Cells 24 - 28).

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Compute Pearson correlation matrix on numeric features
corr = df_cleaned.corr(numeric_only=True)

# Generate heatmap visualization
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr,
    annot=True,
    annot_kws={"size": 6},
    cmap="coolwarm"
)
plt.title("Feature Correlation Heatmap")
plt.show()
```

---

## 2. In-Depth Correlation Analysis & Business Findings

| Feature Pair | Correlation ($r$) | Direction | Business Interpretation |
| :--- | :---: | :--- | :--- |
| **`Income` vs `Total_Spending`** | **+0.79** | Strong Positive | Strongest economic driver. High household earnings directly translate to high consumer expenditure. |
| **`Total_Spending` vs `NumCatalogPurchases`** | **+0.78** | Strong Positive | High spenders heavily utilize premium curated product catalogs. |
| **`Income` vs `NumCatalogPurchases`** | **+0.69** | Moderate Positive | Affluent customers strongly favor mail/digital catalog channels. |
| **`Total_Spending` vs `NumStorePurchases`** | **+0.67** | Moderate Positive | High spenders frequently shop in physical retail stores. |
| **`Income` vs `NumStorePurchases`** | **+0.63** | Moderate Positive | Higher income correlates with higher in-person store visits. |
| **`Income` vs `NumWebVisitsMonth`** | **-0.65** | Strong Negative | High earners visit the e-commerce website less frequently; low-income customers browse frequently. |
| **`NumStorePurchases` vs `NumWebVisitsMonth`** | **-0.43** | Moderate Negative | Offline brick-and-mortar shoppers do not spend time browsing online web pages. |
| **`Customer_Tenure_Days`, `Complain`, `Response`** | **$\approx 0.0$** | Neutral / Orthogonal | These attributes capture independent dimensions of customer behavior (loyalty duration and friction). |

---

## 3. Methodological Takeaways
1. High multicollinearity between `Income`, `Total_Spending`, and `NumCatalogPurchases` confirms that financial capacity is the primary variance axis in this dataset.
2. The strong negative relationship between income and website visits indicates clear behavioral dichotomy: **Affluent Spenders (low browsing, direct high-value purchases)** vs **Budget Browsers (high browsing, low purchase conversion)**.
3. This strong collinearity provides ideal justification for **Principal Component Analysis (PCA)** to condense these correlated axes into orthogonal principal components.
