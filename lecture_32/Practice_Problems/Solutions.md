# Practice Problem Solutions: Day 32 - Unsupervised Machine Learning (Part-2)

This document contains step-by-step mathematical solutions and code architectures for the 3 case studies presented in [`README.md`](file:///c:/Users/Shivam%20Keshari/OneDrive/Desktop/AI-ML/lecture_32/Practice_Problems/README.md).

---

## Solution to Case Study 1: High-Dimensional E-Commerce Analytics & PCA Compression

### 1. The Curse of Dimensionality & Hughes Phenomenon Analysis
- **Euclidean Distance Breakdown**:
  In a 50-dimensional space, the Euclidean distance between any two customer vectors $\mathbf{p}$ and $\mathbf{q}$ is:
$$d(\mathbf{p}, \mathbf{q}) = \sqrt{\sum_{j=1}^{50} (p_j - q_j)^2}$$
  As proved in Beyer et al. (1999), as dimension $d \to \infty$:
$$\lim_{d \to \infty} \frac{\text{dist}_{\max} - \text{dist}_{\min}}{\text{dist}_{\min}} = 0$$
  In 50 dimensions, the distance from an active shopper to their "nearest neighbor" becomes virtually indistinguishable from their distance to their "farthest neighbor." The $k$-NN search loses contrast, and nearest neighbors are selected almost at random.
- **Hughes Phenomenon (Peaking Effect)**:
  - From $10 \to 20$ features: Added metrics provided strong, genuine behavioral signals (e.g., checkout attempts, cart size), allowing the model to refine user clusters.
  - From $20 \to 50$ features: Additional dimensions consisted of noisy, redundant, and weakly correlated signals (e.g., button hover counts, micro-scrolls). These noisy features expanded the volume of the feature space exponentially without providing discriminative value, drowning out the true signal.

---

### 2. Mathematical Variance Retention Calculation
Given:
- Total sum of all 50 eigenvalues: $\sum_{j=1}^{50} \lambda_j = 40.0$
- $\lambda_1 = 15.2$
- $\lambda_2 = 8.8$
- $\lambda_3 = 5.2$

#### Individual Explained Variance Ratios:
$$\text{Ratio}(PC1) = \frac{\lambda_1}{\sum \lambda_j} = \frac{15.2}{40.0} = 0.3800 \implies \mathbf{38.00\%}$$

$$\text{Ratio}(PC2) = \frac{\lambda_2}{\sum \lambda_j} = \frac{8.8}{40.0} = 0.2200 \implies \mathbf{22.00\%}$$

$$\text{Ratio}(PC3) = \frac{\lambda_3}{\sum \lambda_j} = \frac{5.2}{40.0} = 0.1300 \implies \mathbf{13.00\%}$$

#### Cumulative Explained Variance Ratio:
$$\text{Cumulative Ratio} = \text{Ratio}(PC1) + \text{Ratio}(PC2) + \text{Ratio}(PC3)$$
$$\text{Cumulative Ratio} = 38.00\% + 22.00\% + 13.00\% = \mathbf{73.00\%}$$

#### Operational Assessment:
$$\mathbf{73.00\% \ge 70.00\%}$$
**Verdict**: Reducing the dataset from **50 dimensions to 3 dimensions satisfies the platform's operational requirement**. The team successfully eliminates $94\%$ of the dimensions ($47$ out of $50$) while preserving nearly three-quarters of the platform's behavioral variance.

---

### 3. The Geometric Equivalence Proof (Ma'am's Blackboard Derivation)

```
          Y
          ^               P (Centered Customer Point)
          |              *
          |             /|
          |   d_hyp   /  |
          |         /    | d_1 (Perpendicular Error)
          |       /      |
          |     /        |
          |   /          v
          |  *-----------P'-----------> PC1 Candidate Line
          | O     d_2 (Projected Distance from Origin)
          +-----------------------------------> X
```

1. Let $O = (0, 0)$ be the origin of the centered coordinate system.
2. Let $P$ be an arbitrary customer observation vector with fixed coordinates $(x_i, y_i)$.
3. Let $P'$ be the perpendicular projection of $P$ onto the candidate principal component line.
4. Triangle $\triangle OP'P$ is a right-angled triangle with right angle at $P'$. By the Pythagorean Theorem:
$$d_1^2 + d_2^2 = d_{\text{hyp}}^2$$
5. For any given data point $P$, its original coordinates are fixed, which means its distance from the origin $d_{\text{hyp}}^2 = x_i^2 + y_i^2$ is an **immutable constant**:
$$d_1^2 = d_{\text{hyp}}^2 - d_2^2$$
6. Summing across all $n$ data points:
$$\sum_{i=1}^n d_{1, i}^2 = \sum_{i=1}^n d_{\text{hyp}, i}^2 - \sum_{i=1}^n d_{2, i}^2$$
7. Because $\sum_{i=1}^n d_{\text{hyp}, i}^2$ is a fixed scalar constant:
$$\arg\min \sum_{i=1}^n d_{1, i}^2 = \arg\max \sum_{i=1}^n d_{2, i}^2 \quad \blacksquare$$

**Conclusion**: Minimizing the perpendicular reconstruction error is mathematically identical to maximizing the projected distance (variance) from the origin.

---

## Solution to Case Study 2: Semiconductor Wafer Defect Detection with Non-Linear DBSCAN

### 1. K-Means Failure Modes
1. **Forced Centroid Assignment**: K-Means contains no mechanism for noise rejection. Every dust particle is forcibly assigned to one of the two circuit clusters.
2. **Centroid Distortion**: Because centroids are calculated as the arithmetic mean of all assigned points ($\mu = \frac{1}{|C|}\sum x_i$), a single dust contaminant situated far in the wafer periphery pulls the centroid away from the true circuit path, corrupting the geometry.
3. **Convex Shape Assumption**: K-Means partitions space via linear Voronoi polyhedra. When circuits form interlocking curved crescents, a linear boundary bisects the crescents incorrectly.

---

### 2. Hyperparameter Selection via Rule of Thumb
- **Rule of Thumb for `min_samples`**:
$$\text{min\_samples} \approx 2 \times \text{features} = 2 \times 2 = 4 \implies \text{Choose } \mathbf{4 \text{ or } 5}$$
- **Impact of $\text{min\_samples} = 100$**:
  In a dataset of 500 deposition points, requiring 100 points inside an $\epsilon$-neighborhood is excessively stringent. Almost no point will meet the threshold, causing valid circuit pathways to disintegrate into noise (`-1`).
- **Impact of $\text{min\_samples} = 1$**:
  Every isolated dust particle automatically satisfies $|N_\epsilon(p)| \ge 1$, causing trivial single-point noise clusters to be declared valid circuits.

---

### 3. Epsilon Tuning Progression & Adjacent Dust Particles
- **$\epsilon = 0.50$ (Too Large)**: The neighborhood radius spans the gap separating the two circuit tracks, causing both crescents to merge into a single massive monolithic cluster with zero noise detected.
- **$\epsilon = 0.18$ (Tuned)**: Accurately separates the two crescent tracks into Cluster 0 and Cluster 1 while isolating peripheral contaminants.
- **Adjacent Dust Particles ($d(\text{dust}_1, \text{dust}_2) < \epsilon$)**:
  Even though the two dust particles are within $\epsilon$ distance of each other:
  1. The point count in their neighborhood is only $2$ (itself + neighbor). Since $2 < \text{min\_samples} = 5$, **neither particle is a Core Point**.
  2. Because both particles are located in a remote wafer corner, neither particle is reachable from any Core Point belonging to the circuit tracks.
  3. By definition, points with $< \text{min\_samples}$ that are disconnected from all Core Points are classified as **Noise (`label = -1`)**. Both dust particles are correctly flagged as defects!

---

## Solution to Case Study 3: Clinical Endocrinology: Isolation Forest vs. LOF

### 1. Isolation Forest Anomaly Scoring
The official Anomaly Score equation is:
$$s(x, n) = 2^{-\frac{E(h(x))}{c(n)}}$$
Where:
- $h(x)$ is the path length (number of edges from root to terminal leaf).
- $E(h(x))$ is the average path length across all isolation trees in the forest.
- $c(n) = 2 \left( \ln(n - 1) + \gamma \right) - \frac{2(n - 1)}{n}$ is the average BST search length.
- $\gamma \approx 0.5772156649$ (Euler-Mascheroni constant).

#### Calculation for $P_{\text{pathological}}$:
Given: $E(h(x)) = 2.10$ and $c(6,916) = 16.52$:
$$\text{Ratio} = \frac{E(h(x))}{c(n)} = \frac{2.10}{16.52} \approx 0.127118$$
$$s(P_{\text{pathological}}, 6916) = 2^{-0.127118} \approx \mathbf{0.9156} \quad (91.56\%)$$

#### Classification Verdict:
- The anomaly score $s \approx 0.92 \to 1.0$ is substantially higher than the $0.5$ baseline.
- **Classification**: **Severe Clinical Anomaly / Hypothyroid Pathology**.
- **Scikit-Learn Prediction Label**: **`-1`**.

---

### 2. Computational Superiority in 21 Dimensions
- **Complexity**: Constructing an Isolation Forest requires $O(t \cdot \psi \log \psi)$ operations, where $t=200$ and subsample size $\psi=256$. This scales **linearly with sample size $N$**.
- **No Distance Matrix**: Pairwise distance models (KNN, DBSCAN) compute $O(N^2 \cdot d)$ distance operations. In 21 dimensions, Euclidean distances equalize due to data sparsity. Isolation Forest avoids distances completely by performing scalar orthogonal cuts across randomly selected single features.

---

### 3. The Multi-Density Subgroup Problem & LOF Resolution
- **Subgroup Failure of Global Methods**:
  If elderly patients naturally cluster with a lower baseline TSH of $1.5-2.5$ while young athletes cluster around $4.0-5.5$, a young patient exhibiting an abnormal drop to $2.2$ is severely pathological relative to their youth cohort. However, a global distance threshold treats $2.2$ as normal because it falls directly inside the elderly cluster's numerical range.
- **LOF Calculation for Patient $q$**:
  Given: $\text{lrd}_{20}(q) = 0.05$ and $\text{Average LRD of Neighbors} = 0.20$:
$$\text{LOF}_{20}(q) = \frac{\text{Average LRD of Neighbors}}{\text{lrd}_{20}(q)} = \frac{0.20}{0.05} = \mathbf{4.00}$$
- **Interpretation**:
  - The local density of patient $q$ is **4 times lower** (sparser) than the density of their 20 nearest medical peers.
  - Because $\text{LOF} = 4.00 \gg 1.0$, patient $q$ is isolated from their cohort.
  - **Scikit-Learn Prediction Label**: **`-1` (Definite Local Anomaly)**.