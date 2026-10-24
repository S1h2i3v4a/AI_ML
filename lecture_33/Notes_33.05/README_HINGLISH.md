# Submodule 33.05: Handling Outliers (Visual Detection & Statistical Bounds) (Hinglish)

## Topic Overview & Motivation
Outliers woh unusual data points hote hain jo normal customer distribution se bahut door hote hain. Unsupervised learning mein outliers kaafi harmful hote hain:
- **K-Means Centroid Distortion**: K-Means centroid calculate karne ke liye mean use karta hai. Ek single extreme outlier centroid ko apni taraf kheench leta hai aur cluster structure bigad deta hai.
- **PCA Distortion**: PCA maximum variance ki direction dhundhta hai. Agar ek outlier \$666,666 par baitha ho, toh PCA component usi outlier ki direction align ho jayega aur baki sabhi 2,239 points compress ho jayenge.

---

## 1. Pairplot se Outlier Detection
Outliers ko visually dekhne ke liye Ma'am ne numerical columns ka pairplot banaya:
`cols = ["Income", "Recency", "Response", "Age", "Total_Spending", "Total_Children"]`

Reference: [smartcart.ipynb](file:///c:/Users/Shivam%20Keshari/OneDrive/Desktop/AI-ML/lecture_33/SmartCart_Project/smartcart.ipynb) (Cell 22).

```python
cols = ["Income", "Recency", "Response", "Age", "Total_Spending", "Total_Children"]
sns.pairplot(df_cleaned[cols])
plt.show()
```

### Pairplot se Mili Key Insights:
1. **Age Outliers**: Kuch customers ki age 120 saal se upar dikh rahi thi (Birth year 1893, 1899 etc.). Yeh clearly invalid data entry errors hain.
2. **Income Outliers**: Ek customer ki income \$666,666 thi jo normal population (\$20k se \$160k) se bilkul alag akele scatter plot mein stand out kar rahi thi.

---

## 2. Statistical Filtering Bounds
Ma'am ne do logical bounds define kiye:
1. $\text{Age} < 90$: Data entry errors wale unrealistic ages ko remove kiya.
2. $\text{Income} < 600,000$: \$666,666 wale isolated financial outlier ko remove kiya.

### Crucial Engineering Tip:
Har step par dataframe ka state preserve karna (`df_cleaned`, `df_encoded`, `X_scaled`) best practice hai. Agar in-place replace karoge aur baad mein debug karna pada, toh pura notebook dobara chalana padega.

---

## 3. Python Code Implementation
Reference: [smartcart.ipynb](file:///c:/Users/Shivam%20Keshari/OneDrive/Desktop/AI-ML/lecture_33/SmartCart_Project/smartcart.ipynb) (Cell 23).

```python
print("Data size with outliers:", len(df_cleaned)) # 2240

# Outliers ko remove karna
df_cleaned = df_cleaned[(df_cleaned["Age"] < 90)]
df_cleaned = df_cleaned[(df_cleaned["Income"] < 600_000)]

print("Data size without outliers:", len(df_cleaned)) # 2236
```

### Result:
- Exactly **4 outliers** drop hue (2,240 $\to$ 2,236 rows).
- Ab dataset completely clean aur outlier-free hai.
