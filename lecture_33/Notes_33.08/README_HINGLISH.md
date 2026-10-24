# Submodule 33.08: High-Dimensional Data Visualization (PCA 2D vs 3D Projections) (Hinglish)

## Topic Overview & Dimensionality Reduction
Hamara customer transaction data abhi **18 dimensions** ($\mathbb{R}^{18}$) mein hai. Hum insaan maximum 3 dimensions ko hi visualize kar sakte hain.

18-dimensional space ko compress karne aur visualize karne ke liye **Principal Component Analysis (PCA)** use kiya jata hai. PCA un orthogonal directions (eigenvectors) ko dhundhta hai jahan data ka variance maximum ho:

$$
\Sigma = \frac{1}{n} X^T X
$$
$$
\Sigma v_k = \lambda_k v_k
$$

yahan $\lambda_k$ $k$-th component ka explained variance represent karta hai.

---

## 1. 2D vs 3D PCA: Kitni Information Retain Hui?

Reference: [smartcart.ipynb](file:///c:/Users/Shivam%20Keshari/OneDrive/Desktop/AI-ML/lecture_33/SmartCart_Project/smartcart.ipynb) (Cells 40 - 45).

### 2D Projection:
- $PC_1$: **23.16%** variance capture karta hai.
- $PC_2$: **11.39%** variance capture karta hai.
- Total 2D Variance: $23.16\% + 11.39\% = \mathbf{34.55\%}$.
- *Problem*: 65% se zyada information loose ho jati hai, jisse overlapping clusters aapas mein mix ho jate hain.

### 3D Projection:
- $PC_3$: **10.41%** additional variance capture karta hai.
- Total 3D Variance: $23.16\% + 11.39\% + 10.41\% = \mathbf{44.95\%} \approx 45\%$.
- 3D space mein data points ki depth aur separation visual roop se significantly better dikhti hai.

---

## 2. Python Code Implementation (3D PCA Plot)
Reference: [smartcart.ipynb](file:///c:/Users/Shivam%20Keshari/OneDrive/Desktop/AI-ML/lecture_33/SmartCart_Project/smartcart.ipynb) (Cells 43 - 45).

```python
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 3-Component PCA fit karna
pca = PCA(n_components=3, random_state=42)
X_pca = pca.fit_transform(X_scaled)

print("Explained Variance Ratio:", pca.explained_variance_ratio_)
# Output: [0.23163158, 0.11385454, 0.10405815]
print("Total Variance Captured:", pca.explained_variance_ratio_.sum())
# Output: ~44.95%

# 3D Matplotlib Scatter Plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], alpha=0.6, s=15)
ax.set_xlabel("PCA 1")
ax.set_ylabel("PCA 2")
ax.set_zlabel("PCA 3")
ax.set_title("3D PCA Customer Projection")
plt.show()
```

---

## 3. Ma'am ki Key Observations aur Algorithm Selection
1. 3D PCA plot mein data do broad clouds mein dikhta hai (low spenders vs high spenders), lekin points ke beech continuous transition hai.
2. **DBSCAN Kyun Use Nahi Kiya?**: Ma'am ne clearly bataya ki e-commerce customer data continuous density ka hota hai. Agar hum DBSCAN lagayein, toh woh 30 se zyada chote-chote clusters bana deta hai aur valuable customers ko noise mark kar deta hai. 30+ clusters business marketing ke liye impractical hote hain.
3. Isliye **K-Means** aur **Agglomerative Hierarchical Clustering** ko compare kiya jayega.
