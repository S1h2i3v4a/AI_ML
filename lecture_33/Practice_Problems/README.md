# Day 33: Practice Problems Suite (Case-Based Scenarios)

## Context & Alignment
These practice problems are designed around real-world industry scenarios strictly aligned with the end-to-end unsupervised customer clustering curriculum taught in Day 33. All three case studies reflect actual challenges encountered when building e-commerce segmentation pipelines.

---

## Case Study 1: Feature Transformation & RFM Pipeline Design for E-Commerce Clustering
**Scenario**: You are hired as a Lead ML Engineer by an online subscription platform. The marketing database contains 50,000 raw customer rows with attributes including `Account_Created_Timestamp`, `Birth_Year`, `Monthly_Streaming_Minutes`, `Device_Types` (`Mobile`, `Desktop`, `Tablet`, `SmartTV`), and `Subscription_Status` (`Active_Single`, `Active_Family`, `Paused`, `Cancelled`).
1. Explain mathematically why feeding raw timestamps and raw birth years directly into Euclidean distance metrics:
$$
d(u, v) = \sqrt{\sum_{i=1}^{p} (u_i - v_i)^2}
$$
destroys cluster quality.
2. How should the reference anchor date be established to guarantee reproducibility across automated production retraining cycles?
3. In encoding `Subscription_Status`, a junior data scientist advocates setting `drop_first=True` in `pd.get_dummies` to avoid multicollinearity. Explain why this practice is beneficial in Ordinary Least Squares (OLS) regression but detrimental in geometric clustering.

---

## Case Study 2: Quantitative Hyperparameter Tuning: WCSS Convex Elbow vs Silhouette Width
**Scenario**: An e-commerce engineering team is building an automated model-training pipeline to find the optimal number of customer clusters ($K \in [2, 12]$). The evaluation logs produce the following metrics:

| Number of Clusters ($K$) | WCSS (Inertia) | Silhouette Score |
| :---: | :---: | :---: |
| 2 | 24,500 | 0.38 |
| 3 | 16,800 | 0.42 |
| 4 | 11,200 | 0.45 |
| 5 | 9,900 | 0.41 |
| 6 | 8,900 | 0.39 |
| 7 | 8,100 | 0.36 |
| 8 | 7,400 | 0.34 |

1. Formulate the mathematical objective function of WCSS (Inertia) and explain why WCSS is guaranteed to decrease monotonically as $K \to N$.
2. Define how the `kneed.KneeLocator` algorithm mathematically identifies the optimal inflection point on a convex decreasing curve.
3. Based on the evaluation table above, identify the optimal $K$. Justify your selection using both the rate of change of WCSS ($\Delta \text{WCSS}$) and the silhouette width.

---

## Case Study 3: Cluster Persona Strategy & Marketing ROI Optimization
**Scenario**: Following Agglomerative Hierarchical Clustering ($K=4$, Ward linkage) on customer transaction data, your analytics team extracts the following four-cluster summary:

| Cluster | Size ($N$) | Mean Income | Mean Total Spend | Kids at Home | Web Visits/Mo | Campaign Response Rate |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Alpha** | 4,200 | \$38,500 | \$210 | 1.35 | 6.8 | 6.5% |
| **Beta** | 2,100 | \$74,200 | \$1,280 | 0.42 | 3.4 | 17.2% |
| **Gamma** | 1,800 | \$35,800 | \$155 | 1.40 | 7.1 | 13.8% |
| **Delta** | 1,400 | \$71,900 | \$1,210 | 0.38 | 3.6 | 33.5% |

The Chief Marketing Officer (CMO) has a fixed campaign budget of \$100,000 and needs to maximize overall revenue return.
1. Assign distinct customer behavioral personas to each of the four clusters based on their income, spending, family dependency, and digital interaction.
2. Cluster Delta has fewer members than Cluster Alpha, yet senior management refers to Delta as the "Golden Cluster." Provide quantitative justification for why Delta yields the highest return on investment (ROI).
3. Design a targeted marketing strategy and budget allocation playbook across the four clusters to optimize conversion and customer lifetime value.
