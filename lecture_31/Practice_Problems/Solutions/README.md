# Lecture 31: Unsupervised Machine Learning (Clustering) — Practice Problem Solutions

[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#)
[![Solutions PDF](https://img.shields.io/badge/PDF-Solutions-green.svg)](solutions.pdf)
[![Questions](https://img.shields.io/badge/Questions-Review-orange.svg)](../Questions/README.md)

---

## 📌 Rigorous Mathematical & Code Solutions

---

### 🏢 Solution 1: E-Commerce Customer Segmentation (K-Means & Silhouette)

#### 1. Mathematical Inertia Derivation & Monotonicity
Within-Cluster Sum of Squares (WCSS / Inertia) measures the cumulative squared Euclidean distance between every observation and its assigned cluster centroid:

$$
\text{WCSS}(K) = \sum_{k=1}^K \sum_{\mathbf{x}_i \in S_k} \| \mathbf{x}_i - \mathbf{C}_k \|^2, \quad \text{where } \mathbf{C}_k = \frac{1}{|S_k|} \sum_{\mathbf{x}_i \in S_k} \mathbf{x}_i
$$

- **Monotonic Decay**: When $K$ increases to $K+1$, an existing cluster partition $S_k$ is subdivided into two partitions. Because the center of mass uniquely minimizes squared Euclidean distances, subdividing any cluster strictly reduces or maintains the sum of squared distances to the new local centroids:
$$\min_{\mathbf{C}_a, \mathbf{C}_b} \left( \sum_{\mathbf{x} \in S_a} \| \mathbf{x} - \mathbf{C}_a \|^2 + \sum_{\mathbf{x} \in S_b} \| \mathbf{x} - \mathbf{C}_b \|^2 \right) \le \sum_{\mathbf{x} \in S_k} \| \mathbf{x} - \mathbf{C}_k \|^2$$
- **Trivial Bound at $K = N$**: When $K = N$, each observation forms its own singleton centroid ($\mathbf{C}_i = \mathbf{x}_i$). Consequently, $\| \mathbf{x}_i - \mathbf{C}_i \|^2 = 0$, yielding $\text{WCSS} = 0$. This provides zero compression or actionable grouping, representing complete geometric overfitting.

#### 2. Silhouette Coefficient Computation
- **Identification of $b(i)$**: Nearest-cluster distance $b(i)$ represents the minimum average distance from observation $i$ to points in any other cluster $C \neq A$:
$$b(i) = \min \{ d(i, B), d(i, C) \} = \min(4.20, 2.90) = 2.90$$
- **Calculation of $s(i)$**:
$$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))} = \frac{2.90 - 1.85}{\max(1.85, 2.90)} = \frac{1.05}{2.90} \approx +0.3621$$
- **Interpretation**: Observation $i$ is positively clustered ($s(i) > 0$), confirming it is substantially closer to its own cluster members ($1.85$) than to the nearest alternative cluster ($2.90$). However, because $s(i) < 0.50$, it lies in the moderate density margin of the cluster rather than at the dense core ($s > 0.70$).

#### 3. Automated Elbow Detection via KneeLocator
`kneed.KneeLocator` automates elbow identification by fitting a normalized difference curve:
1. Normalize $K$ and $\text{WCSS}$ onto the unit interval $[0, 1]$.
2. Construct a secant reference line connecting the endpoints $(K_{\min}, \text{WCSS}_{\max})$ and $(K_{\max}, \text{WCSS}_{\min})$.
3. Compute the perpendicular distance from each empirical curve point to this diagonal secant line.
4. The point of maximum perpendicular distance corresponds to the maximum negative curvature (inflection point), returned programmatically as `knee.elbow`.

---

### 🧬 Solution 2: Oncological Gene Expression Microarray (Hierarchical Clustering)

#### 1. Linkage Criteria Comparison
- **Single Linkage**:
$$d_{\text{single}}(A, B) = \min_{\mathbf{x} \in A, \mathbf{y} \in B} \| \mathbf{x} - \mathbf{y} \|$$
  Measures dissimilarity by the single closest pair of points between clusters.
- **Complete Linkage**:
$$d_{\text{complete}}(A, B) = \max_{\mathbf{x} \in A, \mathbf{y} \in B} \| \mathbf{x} - \mathbf{y} \|$$
  Measures dissimilarity by the most distant pair of points between clusters.
- **Chaining Phenomenon in Single Linkage**: Because single linkage only requires a single close pair to fuse clusters, a chain of isolated noisy points bridging two distinct biological subtypes will cause the algorithm to fuse them into a single elongated, stringy cluster.
- **Ward's Linkage Objective**: Ward's linkage merges clusters $A$ and $B$ that minimize the increase in total Error Sum of Squares (ESS):
$$\Delta \text{ESS}_{AB} = \frac{|A| |B|}{|A| + |B|} \| \mathbf{m}_A - \mathbf{m}_B \|^2$$
  where $\mathbf{m}_A, \mathbf{m}_B$ are cluster mean vectors. This preserves spherical, compact, minimum-variance clusters.

#### 2. Dendrogram Cutting & Optimal K Determination
Let us analyze the vertical gaps between successive merge heights:
- Gap between 2-cluster and 3-cluster merge: $\Delta h_1 = 24.5 - 14.0 = 10.5$ (Huge vertical distance!)
- Gap between 3-cluster and 4-cluster merge: $\Delta h_2 = 14.0 - 13.2 = 0.8$ (Tiny vertical gap)
- Gap between 4-cluster and 5-cluster merge: $\Delta h_3 = 13.2 - 7.1 = 6.1$ (Substantial vertical gap)
- Gap between 5-cluster and 6-cluster merge: $\Delta h_4 = 7.1 - 6.8 = 0.3$ (Negligible gap)

- **Longest Unbroken Segment**: The vertical range between $h = 14.0$ and $h = 24.5$ spans $\Delta h = 10.5$ units with zero horizontal merge lines.
- **Threshold Selection**: An optimal cut threshold $\theta = 19.0$ placed midway along this vertical segment cleanly bisects the 2 primary branches.
- **Optimal Subtypes**:
  - For major primary cancer families: **$K = 2$** (cut at $\theta = 19.0$).
  - For granular subtypes: The second longest vertical gap occurs between $h = 7.1$ and $h = 13.2$ (span $6.1$); cutting at $\theta = 10.0$ yields **$K = 4$** distinct subtypes.

---

### 🚗 Solution 3: Urban Ride-Sharing Hotspots (DBSCAN vs K-Means)

#### 1. Geometric Failure of K-Means on Curved Spatial Streams
- **Linear Voronoi Partitioning**: K-Means defines cluster boundaries as linear hyperplanes (Voronoi tessellation) equidistant between cluster centroids. When passenger queues follow a winding, curved riverbank or crescent-shaped highway, no combination of spherical Voronoi cells can enclose the curve without bisecting it or merging unrelated parallel roads.
- **Outlier Corruption**: K-Means forces every single data point into a cluster. When GPS sensor glitches place coordinates 15 kilometers offshore, the nearest centroid is pulled significantly off-center toward the glitch, degrading the cluster center for all legitimate passengers.

#### 2. DBSCAN Point Classifications ($\epsilon = 250\text{m}, \text{MinPts} = 8$)
- **Core Point $p$**: Point $p$ is a Core Point if its 250-meter closed disk contains at least 8 observations (including $p$):
$$|N_{\epsilon=250}(p)| \ge 8, \quad \text{where } N_\epsilon(p) = \{ q \mid \text{distance}(p, q) \le 250\text{m} \}$$
- **Border Point $q$**: Point $q$ is a Border Point if it contains fewer than 8 neighbors ($|N_\epsilon(q)| < 8$), but lies within 250 meters of at least one Core Point $p$:
$$\exists p \in \text{Core Points} \quad \text{such that } q \in N_\epsilon(p)$$
- **Noise / Outlier Tagging**: Any observation $r$ that contains fewer than 8 neighbors and does not fall within 250m of any Core Point is classified as **Noise**. In scikit-learn, DBSCAN flags all noise points with integer label **`-1`**.

#### 3. Density Connectivity & Manifold Tracing
- **Direct Density-Reachability**: Point $p$ is directly density-reachable from point $q$ if $p \in N_\epsilon(q)$ and $q$ is a Core Point.
- **Density-Reachability**: Point $p$ is density-reachable from point $q$ if there exists an ordered chain of core points $p_1, p_2, \dots, p_k$ such that each $p_{i+1}$ is directly density-reachable from $p_i$.
- **Density-Connectivity**: Point $p$ and point $q$ are density-connected if there exists an intermediate point $o$ such that both $p$ and $q$ are density-reachable from $o$.
- **Manifold Assembly**: Because density-connectivity is symmetric and transitive across overlapping $\epsilon$-balls, DBSCAN seamlessly chains together hundreds of adjacent core points along a 10-kilometer winding highway, forming a unified, non-linear cluster of arbitrary geometric shape.
