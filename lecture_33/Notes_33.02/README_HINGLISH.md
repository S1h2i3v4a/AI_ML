# Submodule 33.02: Handling Missing Values (Median Imputation on Income) (Hinglish)

## Topic Overview & Mathematical Rationale
Clustering algorithms (jaise K-Means ya Hierarchical Clustering) geometric distance (jaise Euclidean distance) par rely karte hain:
$$
d(u, v) = \sqrt{\sum_{i=1}^{p} (u_i - v_i)^2}
$$
Agar kisi bhi row mein `NaN` value ho, toh distance calculate nahi ho sakti aur algorithm crash ho jayega. Isliye missing data ko handle karna mandatory hai.

Hamare exploratory check mein `Income` column mein exactly 24 missing values mili thi (~1.07% of dataset).

---

## 1. Mean vs Median Imputation: Kaunsa Chune?
Financial data (jaise Income) hamesha positively skewed hota hai kyunki kuch super-rich customers average ko artificially high push kar dete hain.

- **Mean ($\mu$)**: Outliers ke prati bahut sensitive hota hai.
$$
\mu = \frac{1}{n}\sum_{i=1}^{n} x_i
$$
- **Median ($M$)**: Robust non-parametric metric jo distribution ke exact 50th percentile ko represent karta hai:
$$
M = \begin{cases} X_{\left(\frac{n+1}{2}\right)} & \text{if } n \text{ is odd} \\ \frac{X_{\left(\frac{n}{2}\right)} + X_{\left(\frac{n}{2}+1\right)}}{2} & \text{if } n \text{ is even} \end{cases}
$$

Isliye Ma'am ne Income ke missing values ko fill karne ke liye **Median** choose kiya.

---

## 2. Python Code Implementation
Reference: [smartcart.ipynb](file:///c:/Users/Shivam%20Keshari/OneDrive/Desktop/AI-ML/lecture_33/SmartCart_Project/smartcart.ipynb) (Cells 05 - 08).

```python
# Missing Income values ko median se fill karna
df["Income"] = df["Income"].fillna(df["Income"].median())

# Verification: Null count check karna
print("Remaining null values in Income:", df["Income"].isnull().sum()) # Output: 0
print("Total nulls in dataset:", df.isnull().sum().sum())              # Output: 0
```

---

## 3. Verification & Outcome
1. Missing values 24 se drop hokar 0 ho gayi.
2. Saare 2,240 customer records preserve ho gaye (koi data drop nahi karna pada).
