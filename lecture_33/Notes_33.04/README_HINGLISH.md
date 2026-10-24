# Submodule 33.04: Dropping Redundant Columns & Dimensionality Management (Hinglish)

## Topic Overview & The Curse of Dimensionality
Jab machine learning data mein bahut zyada features hote hain, toh use **Curse of Dimensionality** kehte hain. 
High dimensions ke andar:
- Har data point doosre data point se almost equidistant lagne lagta hai:
$$
\lim_{p \to \infty} \frac{\text{dist}_{\max} - \text{dist}_{\min}}{\text{dist}_{\min}} \to 0
$$
- Euclidean distance ki clustering power degrade ho jati hai.
- Redundant aur correlated features algorithm ko artificially mislead karte hain.

Isliye jin features ko humne naye features mein combine kar liya hai, un purane columns ko drop karna essential hai.

---

## 1. Columns Drop Karne ka Rationale
Humne total 12 columns drop kiye:

1. **Non-predictive Identifier**:
   - `ID`: Sirf serial/database key hai, iska customer behavior se koi lena dena nahi hai.
2. **Replaced Demographics**:
   - `Year_Birth` $\to$ `Age` ne replace kiya.
   - `Marital_Status` $\to$ `Living_With` ne replace kiya.
   - `Kidhome`, `Teenhome` $\to$ `Total_Children` ne replace kiya.
   - `Dt_Customer` $\to$ `Customer_Tenure_Days` ne replace kiya.
3. **Replaced Individual Spends**:
   - Wine, fruits, meat, fish, sweets, gold ke 6 columns $\to$ `Total_Spending` ne replace kiya.

### Purchasing Channels ko Kyun Rakha?
`NumWebPurchases`, `NumCatalogPurchases`, `NumStorePurchases`, aur `NumDealsPurchases` ko Ma'am ne drop nahi kiya, kyunki yeh customer ke purchasing habits (online shopper vs offline store buyer vs discount seeker) ka crucial insight dete hain.

---

## 2. Python Code Implementation
Reference: [smartcart.ipynb](file:///c:/Users/Shivam%20Keshari/OneDrive/Desktop/AI-ML/lecture_33/SmartCart_Project/smartcart.ipynb) (Cells 16 - 20).

```python
# Drop hone wale columns ki list
cols = ["ID", "Year_Birth", "Marital_Status", "Kidhome", "Teenhome", "Dt_Customer"]
spending_cols = ["MntWines", "MntFruits", "MntMeatProducts", "MntFishProducts", "MntSweetProducts", "MntGoldProds"]

cols_to_drop = cols + spending_cols

# Redundant columns drop karke df_cleaned banana
df_cleaned = df.drop(columns=cols_to_drop)

print("Original Features:", df.shape[1])         # 27
print("Cleaned Features:", df_cleaned.shape[1])   # 15
```

---

## 3. Retained Features (15 Columns)
`df_cleaned` mein 15 clean features bache: `Education`, `Income`, `Recency`, `NumDealsPurchases`, `NumWebPurchases`, `NumCatalogPurchases`, `NumStorePurchases`, `NumWebVisitsMonth`, `Complain`, `Response`, `Age`, `Customer_Tenure_Days`, `Total_Spending`, `Total_Children`, `Living_With`.
