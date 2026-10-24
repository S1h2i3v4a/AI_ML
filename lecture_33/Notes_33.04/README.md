# Submodule 33.04: Dropping Redundant Columns & Dimensionality Management

## Topic Overview & The Curse of Dimensionality
As feature dimensionality ($p$) grows, the volume of the enclosing space expands exponentially. In high-dimensional spaces:
- Pairwise Euclidean distances converge to nearly uniform values:
$$
\lim_{p \to \infty} \frac{\text{dist}_{\max} - \text{dist}_{\min}}{\text{dist}_{\min}} \to 0
$$
- All customer data points appear equidistant from one another, severely undermining centroid-based and linkage-based clustering.
- Redundant and collinear features inject noise and artificially weight specific concepts twice.

---

## 1. Column Pruning Logic
We eliminate 12 features categorized into three groups:

1. **Identifiers with Zero Predictive Value**:
   - `ID`: Arbitrary database primary key; induces random noise.
2. **Replaced Raw Demographic Attributes**:
   - `Year_Birth` (replaced by `Age`).
   - `Marital_Status` (replaced by `Living_With`).
   - `Kidhome`, `Teenhome` (replaced by `Total_Children`).
   - `Dt_Customer` (replaced by `Customer_Tenure_Days`).
3. **Disaggregated Expenditure Columns**:
   - `MntWines`, `MntFruits`, `MntMeatProducts`, `MntFishProducts`, `MntSweetProducts`, `MntGoldProds` (all captured in `Total_Spending`).

### Retained Purchasing Channels:
Notice that `NumDealsPurchases`, `NumWebPurchases`, `NumCatalogPurchases`, and `NumStorePurchases` were **deliberately retained** as separate features. They reveal whether a customer is a digital native, an offline store visitor, a direct-mail catalog user, or a discount bargain-hunter.

---

## 2. Python Implementation
Reference: [smartcart.ipynb](file:///c:/Users/Shivam%20Keshari/OneDrive/Desktop/AI-ML/lecture_33/SmartCart_Project/smartcart.ipynb) (Cells 16 - 20).

```python
# Define redundant feature lists
cols = ["ID", "Year_Birth", "Marital_Status", "Kidhome", "Teenhome", "Dt_Customer"]
spending_cols = ["MntWines", "MntFruits", "MntMeatProducts", "MntFishProducts", "MntSweetProducts", "MntGoldProds"]

cols_to_drop = cols + spending_cols

# Create cleaned dataframe
df_cleaned = df.drop(columns=cols_to_drop)

print("Original Shape:", df.shape)         # (2240, 27 after feature creation)
print("Cleaned Shape:", df_cleaned.shape)   # (2240, 15)
```

---

## 3. Retained Features Audit (15 Columns)
The cleaned dataframe `df_cleaned` retains 15 high-signal features:
1. `Education` (Categorical)
2. `Income` (Numeric)
3. `Recency` (Numeric)
4. `NumDealsPurchases` (Numeric)
5. `NumWebPurchases` (Numeric)
6. `NumCatalogPurchases` (Numeric)
7. `NumStorePurchases` (Numeric)
8. `NumWebVisitsMonth` (Numeric)
9. `Complain` (Binary)
10. `Response` (Binary)
11. `Age` (Numeric)
12. `Customer_Tenure_Days` (Numeric)
13. `Total_Spending` (Numeric)
14. `Total_Children` (Numeric)
15. `Living_With` (Categorical)
