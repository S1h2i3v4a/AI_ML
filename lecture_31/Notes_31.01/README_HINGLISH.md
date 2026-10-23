# Lecture 31.01: Unsupervised Machine Learning Ka Introduction Aur Core Branches [Hinglish]

[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#)
[![Theory](https://img.shields.io/badge/Topic-Theory%20%26%20Math-lightgrey.svg)](#)
[![English Notes](https://img.shields.io/badge/Notes-English-blue.svg)](README.md)
[![English PDF](https://img.shields.io/badge/PDF-English-red.svg)](notes.pdf)
[![Hinglish PDF](https://img.shields.io/badge/PDF-Hinglish-green.svg)](notes_hinglish.pdf)

---

## 📌 Topic Overview
Comprehensive introduction to Unsupervised Machine Learning. Unlike supervised learning, unsupervised learning operates on unlabeled feature sets to discover latent structures, clusters, dimensional reductions, and anomalies.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Supervised Learning ($X, y$) aur Unsupervised Learning (Sirf $X$) ke beech ka basic farak.
- Unsupervised Learning ki 3 Main Branches: **Clustering**, **Dimensionality Reduction**, aur **Anomaly Detection**.
- Ma'am Ka Bank ATM Case Study: Balance aur Cash Withdrawals ke basis par customer segmentation.
- Real-world business applications: Target marketing, fraud detection, aur latent pattern discovery.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation
- **Supervised vs Unsupervised Learning**: Supervised learning mein hamare pass inputs $X$ ke sath target output labels $y$ hote the (jaise Spam/Ham ya House Price). Lekin **Unsupervised Learning** mein koi target label $y$ nahi hota! Model ko sirf input features $X$ diye jaate hain aur use khud data ke andar ke hidden patterns aur groupings dhoondhne hote hain.

- **Pehli Main Branch: Clustering**: Unlabeled data points ko unki similarities ke basis par alag-alag groups (clusters) mein divide karna. Jaise customer segmentation ya document topic classification.

- **Doosri Main Branch: Dimensionality Reduction**: Jab dataset mein bohot saare features (jaise 100+ columns) hote hain, toh unhe 2D ya 3D mein compress karna bina zaroori information khoe (jaise **PCA**, **t-SNE**).

- **Teesri Main Branch: Anomaly Detection**: Normal patterns se alag hatkar aane wale unusual ya fraudulent data points ko pehchanna (jaise Credit Card Fraud ya Server Defect detection).

- **Classroom Bank ATM Example**: Ma'am ne board par bank customer transactions ka example diya jisme do features the: `Feature 1 = Daily Balance` aur `Feature 2 = Cash Withdrawals`. Bank apne customers ko 2 clusters mein segment karta hai: high balance/low withdrawals wale users ko investment offers bhejna, aur low balance/high withdrawals wale users ko personal loan offers bhejna!

- **Pure Theory Lecture**: Is lecture mein ma'am ne conceptual foundations samjhaye hain, isliye is module mein koi code nahi hai.

---

### 📋 Supervised vs Unsupervised Learning Comparison Matrix

| Feature / Dimension | Supervised Machine Learning | Unsupervised Machine Learning |
| :--- | :--- | :--- |
| **Training Data** | Features $X$ + Ground Truth Labels $y$ | Only Features $X$ (Unlabeled Data) |
| **Objective** | Predict label $y$ for unseen sample $x^*$ | Discover hidden patterns, clusters, manifolds |
| **Evaluation** | Ground truth metrics (Accuracy, MSE, ROC-AUC) | Internal geometric metrics (Inertia, Silhouette) |
| **Primary Tasks** | Classification, Regression | Clustering, Dim-Reduction, Anomaly Detection |
| **Feedback Mechanism**| Error feedback via actual label $(y - \hat{y})$ | No external feedback (Self-guided discovery) |

---

### 📊 Unsupervised Machine Learning Taxonomy

```mermaid
flowchart TD
    A["Unsupervised Machine Learning<br/>(Only Inputs X, No Labels y)"] --> B["1. Clustering<br/>(Grouping Similar Data Points)"]
    A --> C["2. Dimensionality Reduction<br/>(Compressing High Dimensions)"]
    A --> D["3. Anomaly Detection<br/>(Detecting Outliers & Fraud)"]
    
    B --> B1["Partitioning: K-Means<br/>Hierarchical: Agglomerative<br/>Density-based: DBSCAN"]
    C --> C1["PCA (Principal Component Analysis)<br/>t-SNE / UMAP"]
    D --> D1["Isolation Forests<br/>One-Class SVM<br/>DBSCAN Noise (-1)"]
```

---

### 🔢 Mathematical Derivation

Data representation in unsupervised learning:

$$
\mathcal{D} = \{ \mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_N \}, \quad \text{where } \mathbf{x}_i \in \mathbb{R}^D
$$

Objective of clustering into $K$ disjoint partitions $\{S_1, S_2, \dots, S_K\}$:

$$
\bigcup_{k=1}^K S_k = \mathcal{D}, \quad S_j \cap S_k = \emptyset \quad (\forall j \neq k)
$$

---

### 📌 Note on Code
Yeh pure conceptual, mathematical, aur blackboard theory lecture hai. Ma'am ne is lecture mein code nahi likha hai, isliye rule ke mutabiq isme koi extra synthetic code add nahi kiya gaya hai.
