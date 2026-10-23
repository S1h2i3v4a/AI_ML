# Lecture 31: Unsupervised Machine Learning (Clustering) — Practice Problem Suite

[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#)
[![Questions PDF](https://img.shields.io/badge/PDF-Questions-red.svg)](questions.pdf)
[![Solutions](https://img.shields.io/badge/Solutions-Available-brightgreen.svg)](../Solutions/README.md)

---

## 📌 Comprehensive Syllabus-Aligned Case Study Problems

These 3 case-based practice problems are strictly aligned with the Day 31 curriculum (**K-Means Clustering, Elbow Method, Silhouette Analysis, Hierarchical Agglomerative Clustering, Dendrogram Distance Thresholds, and DBSCAN Density Outlier Detection**).

---

### 🏢 Case Study 1: E-Commerce Retail Customer Segmentation via K-Means & Silhouette Optimization

**Industry Context**:
An international omni-channel retail corporation manages transactional purchase history for $N = 25,000$ active loyalty club members. The analytics department has compiled 4 normalized spending features:
1. $x_1$: `Annual_Grocery_Spend`
2. $x_2$: `Annual_Electronics_Spend`
3. $x_3$: `Annual_Apparel_Spend`
4. $x_4$: `Annual_Luxury_Spend`

The Chief Marketing Officer (CMO) requires distinct behavioral personas for targeted promotional campaigns, but the management team disagrees on whether $K=3, K=4$, or $K=5$ segments should be maintained.

#### 📝 Problem Specifications & Deliverables:
1. **Mathematical Inertia Derivation**:
   Write the mathematical formulation for Within-Cluster Sum of Squares (WCSS / Inertia) across $K$ clusters. Explain step-by-step why $WCSS(K)$ is monotonically decreasing with respect to $K$, and why setting $K = N$ yields $WCSS = 0$ while being practically useless.
2. **Silhouette Coefficient Computation**:
   Suppose observation $i$ belongs to Cluster $A$. The mean intra-cluster distance to all other members of Cluster $A$ evaluates to $a(i) = 1.85$. The mean distance from observation $i$ to all points in neighboring Cluster $B$ is $d(i, B) = 4.20$, and to neighboring Cluster $C$ is $d(i, C) = 2.90$.
   - Identify $b(i)$ and state its mathematical definition.
   - Compute the exact Silhouette score $s(i)$ for observation $i$.
   - Interpret whether observation $i$ is well-clustered, on the decision border, or misclassified.
3. **Automated Elbow Detection**:
   Explain how the `kneed.KneeLocator` algorithm programmatically determines the inflection point on a convex decreasing WCSS curve compared to manual visual estimation.

---

### 🧬 Case Study 2: Oncological Gene Expression Microarray via Agglomerative Hierarchical Clustering

**Biomedical Context**:
A computational biology genomics lab analyzes RNA-sequencing expression profiles for $N = 120$ tumor biopsy samples across 500 oncological biomarker genes. The research team aims to discover previously unknown molecular cancer subtypes without imposing a pre-defined cluster count $K$.

#### 📝 Problem Specifications & Deliverables:
1. **Linkage Criteria Comparison**:
   The bioinformaticians evaluate **Single Linkage**, **Complete Linkage**, and **Ward's Linkage**:
   - Contrast the mathematical definitions of Single Linkage vs Complete Linkage.
   - Explain the physiological vulnerability of Single Linkage known as the **Chaining Phenomenon**, and why it frequently joins distinct biological subtypes through stray noisy background expression.
   - Formulate Ward's minimum variance criterion: explain how merging clusters $A$ and $B$ minimizes total within-cluster sum of squares.
2. **Dendrogram Cutting & Optimal K Determination**:
   Suppose the Ward hierarchical agglomerative merge tree yields the following fusion heights:
   - Final merger (Root joining last 2 clusters): Linkage distance $h = 24.5$
   - Preceding merger (joining subclusters into 3 groups): Linkage distance $h = 14.0$
   - Prior merger (joining subclusters into 4 groups): Linkage distance $h = 13.2$
   - Prior merger (joining subclusters into 5 groups): Linkage distance $h = 7.1$
   - Prior merger (joining subclusters into 6 groups): Linkage distance $h = 6.8$
   
   Identify the longest unbroken vertical branch segment not intersected by any horizontal merge bar. Propose the optimal horizontal cut threshold $\theta$, and state the resulting optimal number of cancer subtypes $K$.

---

### 🚗 Case Study 3: Urban Ride-Sharing GPS Hotspot & Anomaly Detection via DBSCAN

**Urban Mobility Context**:
A smart-city ride-hailing platform records 50,000 passenger pickup coordinates $(\text{latitude}, \text{longitude})$ during peak Friday night hours in a metropolitan area. The spatial distribution comprises:
- High-density passenger queues along non-linear, curved waterfront entertainment corridors and winding highway access ramps.
- Circular urban center pickup plazas.
- Random GPS sensor glitches, reflections, and dropped signal outliers scattered across uninhabited forest and water bodies.

#### 📝 Problem Specifications & Deliverables:
1. **Geometric Failure of K-Means**:
   Explain why K-Means clustering fundamentally fails when segmenting curved, non-convex passenger streams (such as the waterfront promenade), and explain how K-Means treats isolated GPS glitch outliers.
2. **DBSCAN Point Classification**:
   Given parameters $\epsilon = 250\text{ meters}$ and $\text{MinPts} = 8$:
   - Define the mathematical condition for a pickup point $p$ to be classified as a **Core Point**.
   - Define the conditions for a point $q$ to be classified as a **Border Point**.
   - Explain how DBSCAN identifies and tags GPS sensor errors, and identify the exact integer label assigned to outliers in scikit-learn.
3. **Density Connectivity & Cluster Expansion**:
   Explain the difference between **Direct Density-Reachability**, **Density-Reachability**, and **Density-Connectivity**. Why does density-connectivity allow DBSCAN to assemble arbitrarily curved, winding clusters of arbitrary lengths?
