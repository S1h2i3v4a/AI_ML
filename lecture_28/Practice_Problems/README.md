# 🌲 Lecture 28: Practice Problems & Systems Engineering Suite
## Supervised Machine Learning (Part 4) — Decision Trees

Welcome to the **Practice Problems & Systems Engineering Suite** for **Lecture 28**! This laboratory suite is strictly aligned with the Lecture 28 syllabus covering recursive binary splitting (Hunt's algorithm / CART), information-theoretic impurity metrics (Shannon Entropy, Gini Impurity), Taylor series mathematical equivalence, C4.5 Information Gain Ratio regularization, pre-pruning (`max_depth`, `min_samples_leaf`), Leo Breiman's Minimal Cost-Complexity post-pruning (`ccp_alpha`), Decision Tree Regressors with Variance Reduction, and the end-to-end **ShopSmart E-Commerce Purchase Prediction Project** (12,330 sessions, meeting F1 benchmark > 0.55).

---

## 🌐 Language Navigation
- **English Master Documentation**: [`README.md`](README.md)
- **हिंदी / Hinglish Master Documentation**: [`README_HINGLISH.md`](README_HINGLISH.md)

---

## 📂 Suite Architecture

```plaintext
lecture_28/Practice_Problems/
├── README.md                           # Master English Suite Overview
├── README_HINGLISH.md                  # Master Hinglish Suite Overview
├── Questions/
│   ├── README.md                       # Complete Case-Based Problem Statements (English)
│   ├── README_HINGLISH.md              # Case-Based Problem Statements (Hinglish)
│   ├── questions.pdf                   # Printable Problem Manual
│   └── questions.ipynb                 # Interactive Starter Jupyter Notebook
└── Solutions/
    ├── README.md                       # Production Solutions & Mathematical Proofs (English)
    ├── README_HINGLISH.md              # Production Solutions & Mathematical Proofs (Hinglish)
    ├── solutions.pdf                   # Master Solutions Systems Manual
    ├── solutions.ipynb                 # Fully Executed Master Solutions Notebook
    ├── case1_entropy_vs_gini_impurity_curve.png           # 300 DPI Impurity Metrics Comparison
    ├── case2_cost_complexity_pruning_ccp_alpha_path.png   # 300 DPI Minimal Cost-Complexity Path
    └── case3_decision_tree_depth_overfitting_frontier.png # 300 DPI Depth vs Overfitting Frontier
```

---

## 🔬 Systems Engineering Case Studies (Industrial Scenarios)

### 🛒 Case Study 1: E-Commerce Visitor Purchase Conversion & Generalization Frontier (ShopSmart Dataset)
- **Dataset Context**: `shop_smart_ecommerce.csv` containing 12,330 visitor clickstream records across 18 behavioral features (`PageValues`, `BounceRates`, `ExitRates`, `ProductRelated_Duration`, `Month`, `VisitorType`).
- **Core Challenge**: An unconstrained decision tree memorizes all 12,330 paths (training accuracy 100%, depth 26+), leading to disastrous test F1-score collapse on minority purchasers (`Revenue=True`, ~15% class imbalance).
- **Engineering Task**:
  1. Build a pre-pruned cross-validation baseline (`max_depth`, `min_samples_leaf`).
  2. Compute the exact Minimal Cost-Complexity pruning path ($R_\alpha(T) = R(T) + \alpha |T|$) using `cost_complexity_pruning_path`.
  3. Locate the optimal effective $\alpha_{\text{opt}}$ that maximizes held-out test F1-score (> 0.55).
  4. Extract human-interpretable white-box IF-THEN rules using `export_text`.

### 🏥 Case Study 2: Emergency Department Triage & High-Cardinality ID Failure (C4.5 Gain Ratio)
- **Clinical Context**: Emergency room patient admission dataset where triage features include `Patient_ID` (100% unique), `Heart_Rate_High`, and `Oxygen_Sat_Low`, predicting `Emergency_Admit`.
- **Core Challenge**: Standard Information Gain ($IG$) greedily selects `Patient_ID` as the root node ($IG \to H(S)$), creating $N$ pure single-patient leaf nodes with zero generalization capacity.
- **Engineering Task**:
  1. Calculate Shannon Entropy $H(S)$ of the parent node with 60 admitted and 40 discharged patients.
  2. Prove mathematically why $IG(S, \text{Patient\_ID}) = H(S) - 0 = H(S)$ maximizes standard information gain.
  3. Calculate C4.5 Split Information $SplitInfo(S, \text{Patient\_ID}) = \log_2(N)$ and prove how the Gain Ratio $GR = \frac{IG}{SplitInfo} \to \frac{H(S)}{\log_2(N)} \approx 0$ completely eliminates this pathology.
  4. Implement pure vectorized NumPy `ShannonEntropyCalculator` and `GainRatioOptimizer`.

### 🏙️ Case Study 3: Municipal Property Valuation & Rental Appraisal (Regression Trees & Variance Reduction)
- **Real Estate Context**: Valuation engine predicting continuous monthly rental price $y$ from square footage, bedroom count, and transit distance.
- **Core Challenge**: Partition continuous feature space into orthogonal hyper-rectangles $R_m$ where leaf prediction is the constant mean $\hat{c}_m = \frac{1}{|R_m|} \sum_{i \in R_m} y_i$.
- **Engineering Task**:
  1. Calculate parent node variance $I_{\text{MSE}}(S) = \frac{1}{|S|}\sum (y_i - \bar{y})^2$ for an 8-property calibration set.
  2. Evaluate candidate midpoint split thresholds $\theta_i = \frac{x_i + x_{i+1}}{2}$ and compute Variance Reduction $\Delta \text{Var}$.
  3. Implement `ContinuousSplitFinder` in pure NumPy.
  4. Analyze outlier sensitivity: Compare MSE criterion (mean prediction) vs MAE criterion (median prediction) when luxury penthouses distort the local sample mean.

### 📐 Case Study 4: First-Principles Mathematical Bridge (Gini Impurity vs Shannon Entropy)
- **Theoretical Context**: Mathematical comparison of disorder metrics across binary probability $p \in [0, 1]$.
- **Core Challenge**: Why does scikit-learn default to `criterion='gini'` over `'entropy'`?
- **Engineering Task**:
  1. Prove Taylor series expansion $\ln(p_k) = \ln(1 - (1-p_k)) \approx -(1-p_k)$, showing $H(S) \approx \frac{1}{\ln 2} G(S)$.
  2. Implement pure NumPy `GiniImpurityEvaluator` with weighted child impurity evaluation.
  3. Quantify computational throughput: Explain why avoiding transcendent base-2 logarithm computations makes Gini ~3x faster in recursive CART splits.

---

## 📋 Problem Suite Inventory

| Problem ID | Category & Focus | Algorithmic Paradigm | Mathematical Invariant | Syllabus Link |
| :--- | :--- | :--- | :--- | :--- |
| **Problem 01** | Pure NumPy Shannon Entropy | Information Theory | $H(S) = -\sum p_k \log_2 p_k$, with $0 \log_2 0 \equiv 0$ | Notes 28.03 |
| **Problem 02** | Pure NumPy Gini Impurity | Misclassification Probability | $G(S) = 1 - \sum p_k^2$, binary $2p(1-p)$ | Notes 28.04 |
| **Problem 03** | Continuous Feature Split Finder | Midpoint Threshold Search | $\theta_i = \frac{x_i + x_{i+1}}{2}$, $\max \Delta G$ | Notes 28.02 |
| **Problem 04** | C4.5 Information Gain Ratio | High-Cardinality Regularizer | $GR = \frac{IG(S, A)}{SplitInfo(S, A)}$, $\epsilon = 10^{-12}$ | Notes 28.06 |
| **Problem 05** | Regression Tree Variance Split | Continuous Impurity Drop | $\Delta \text{Var} = \text{Var}(S) - \sum \frac{\|S_v\|}{\|S\|}\text{Var}(S_v)$ | Notes 28.12, 28.13 |
| **Problem 06** | Cost-Complexity Pruning Path | Breiman's Post-Pruning | $R_\alpha(T) = R(T) + \alpha \|T\|$, monotonic leaves | Notes 28.11 |
| **Problem 07** | Pre-Pruning Cross-Validation | Structural Regularization | `max_depth`, `min_samples_leaf`, Stratified K-Fold | Notes 28.08, 28.10 |
| **Problem 08** | ShopSmart Purchase Pipeline | Industrial Production ML | End-to-end ColumnTransformer + Tree, F1 > 0.55 | Assignment Brief |
