# Module 24.01: Feature Engineering — Categorical Encoding

## 1. The Necessity of Encoding in Mathematical Modeling

Machine Learning algorithms operate on numerical vectors in Euclidean space $\mathbb{R}^d$. Mathematical operations such as matrix multiplications ($\mathbf{X} \mathbf{w}$), Euclidean distance calculations ($\|\mathbf{x}_i - \mathbf{x}_j\|_2$), and inner products cannot directly ingest non-numeric strings or categorical symbols.

```
Raw Categorical Feature                 Mathematical Mapping                Numerical Feature Matrix
["Red", "Blue", "Green"]       --->        f: S -> R^k          --->        [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

Categorical variables are bifurcated into two foundational mathematical types:
1. **Nominal Variables:** Categories possess no intrinsic mathematical ordering or hierarchical ranking (e.g., Color: `["Red", "Blue", "Green"]`, Country: `["India", "USA", "Germany"]`).
2. **Ordinal Variables:** Categories possess a well-defined natural order or magnitude ranking, though intervals between levels may not be uniform (e.g., Education: `["High School", "Bachelors", "Masters", "PhD"]`, Size: `["S", "M", "L", "XL"]`).

---

## 2. Encoding Strategies

### 1. Label / Ordinal Encoding
Ordinal encoding maps each discrete category $c_k$ to an integer scalar $k \in \{0, 1, \dots, K-1\}$ based on the established rank order:

$$
f(c_k) = k \quad \text{where} \quad c_0 < c_1 < \dots < c_{K-1}
$$

> **Critical Warning for Nominal Data:** If applied to nominal variables (e.g., Red = 0, Blue = 1, Green = 2), linear and distance-based models mistakenly assume that:
> $$
> \text{Green} > \text{Blue} > \text{Red} \quad \text{and} \quad \text{Green} - \text{Blue} = \text{Blue} - \text{Red}
> $$
> This induces artificial, non-existent geometric constraints into the feature space.

### 2. One-Hot Encoding (OHE)
One-Hot Encoding converts a categorical feature with $K$ unique levels into $K$ binary indicator columns:

$$
\mathbf{x}_{\text{OHE}}^{(i)} = [z_1^{(i)}, z_2^{(i)}, \dots, z_K^{(i)}]^T \in \{0, 1\}^K
$$

Where:
$$
z_k^{(i)} = \begin{cases} 1 & \text{if sample } i \text{ belongs to category } k \\ 0 & \text{otherwise} \end{cases}
$$

Under One-Hot Encoding, every category becomes an orthogonal basis vector in $\mathbb{R}^K$:
- Distance between any two distinct categories $j \ne k$ is identical: $\|\mathbf{e}_j - \mathbf{e}_k\|_2 = \sqrt{1^2 + (-1)^2} = \sqrt{2}$.
- Eliminates any spurious hierarchical ranking.

---

## 3. Comparison Matrix of Encoding Techniques

| Encoding Method | Target Variable Type | Dimensionality Impact | Risk of Spurious Order | Best Algorithms |
| :--- | :--- | :--- | :--- | :--- |
| **Ordinal Encoding** | Ordinal only | Preserves $d$ ($1 \to 1$) | High if applied to nominal | Tree models, Gradient Boosting |
| **One-Hot Encoding** | Nominal ($K < 50$) | Expands $d \to d + K$ | None (Orthogonal) | Linear Models, Neural Networks, SVM |
| **Target Encoding** | High cardinality nominal | Preserves $d$ ($1 \to 1$) | Moderate (Target leakage risk) | GBDT, CatBoost, LightGBM |
| **Frequency Encoding** | High cardinality nominal | Preserves $d$ ($1 \to 1$) | Low | Tree-based Ensembles |
