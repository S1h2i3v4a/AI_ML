# Submodule 33.02: Handling Missing Values (Median Imputation on Income)

## Topic Overview & Mathematical Rationale
In unsupervised distance-based algorithms (such as K-Means, Agglomerative Hierarchical Clustering, or PCA), distance metrics such as Euclidean distance:
$$
d(u, v) = \sqrt{\sum_{i=1}^{p} (u_i - v_i)^2}
$$
cannot be evaluated if even a single attribute value contains `NaN`. Consequently, missing data must be rigorously imputed prior to running vector space transformations.

In our audit, `Income` contained exactly 24 missing values (~1.07% of the dataset).

---

## 1. Mean vs Median Imputation in Financial Data
Financial distributions such as customer income exhibit strong positive right-skewness due to high earners.

- **Arithmetic Mean ($\mu$)**: Highly sensitive to extreme values. A single multi-millionaire drastically inflates $\mu$.
$$
\mu = \frac{1}{n}\sum_{i=1}^{n} x_i
$$
- **Median ($M$)**: Robust order statistic representing the true 50th percentile (central tendency), completely unaffected by skewness:
$$
M = \begin{cases} X_{\left(\frac{n+1}{2}\right)} & \text{if } n \text{ is odd} \\ \frac{X_{\left(\frac{n}{2}\right)} + X_{\left(\frac{n}{2}+1\right)}}{2} & \text{if } n \text{ is even} \end{cases}
$$

Because household income is naturally skewed and contains extreme outliers, **median imputation** is the statistically sound strategy.

---

## 2. Python Code Implementation
Reference: [smartcart.ipynb](file:///c:/Users/Shivam%20Keshari/OneDrive/Desktop/AI-ML/lecture_33/SmartCart_Project/smartcart.ipynb) (Cells 05 - 08).

```python
# Impute missing Income values using the distribution median
df["Income"] = df["Income"].fillna(df["Income"].median())

# Verify zero remaining null values
print("Remaining null values in Income:", df["Income"].isnull().sum()) # Output: 0
print("Total dataset null values:", df.isnull().sum().sum())          # Output: 0
```

---

## 3. Verification & Impact
1. Missing count dropped from 24 to 0.
2. Preserved the full sample size ($N = 2,240$) without discarding customer records.
3. Avoided introducing artificial variance into the distance matrix.
