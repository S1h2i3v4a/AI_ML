# Lecture 28: Practice Problems Suite (Questions)
## Supervised Machine Learning (Part 4) — Decision Trees

This problem set tests algorithmic impurity formulation, continuous threshold search, C4.5 gain ratio regularization, variance reduction, and minimal cost-complexity pruning. All problems are strictly derived from the concepts taught in Lecture 28.

---

## 🛒 Case Study 1: E-Commerce Session Conversion & Cart Abandonment (ShopSmart Dataset)

### 🎯 Business Context & Scenario
ShopSmart is an e-commerce platform processing clickstream logs across 12,330 visitor sessions (`shop_smart_ecommerce.csv`). The dataset contains 18 features capturing visitor engagement metrics:
- Continuous engagement metrics: `Administrative_Duration`, `Informational_Duration`, `ProductRelated_Duration`, `BounceRates`, `ExitRates`, `PageValues`.
- Calendar and structural metrics: `SpecialDay`, `Month`, `OperatingSystems`, `Browser`, `Region`, `TrafficType`, `VisitorType`, `Weekend`.
- Target: `Revenue` (Boolean: `True` if purchase completed, `False` if session abandoned; ~15.4% positive rate).

### 📝 Case Study Questions
1. **Unconstrained Pathology Analysis**: Fit an unconstrained `DecisionTreeClassifier(random_state=42)` on the training set (80/20 train/test split). Inspect `model.get_depth()` and `model.get_n_leaves()`. Compare training accuracy and test F1-score. Explain why an unconstrained tree overfits and memorizes noise when `min_samples_leaf=1`.
2. **Pre-Pruning Grid Search**: Construct a `GridSearchCV` pipeline testing:
   - `max_depth` $\in [3, 5, 8, 12]$
   - `min_samples_leaf` $\in [5, 10, 20, 50]$
   - `min_impurity_decrease` $\in [0.0, 0.001, 0.005]$
   Using 5-fold Stratified Cross-Validation with scoring `f1`. What are the optimal pre-pruning parameters?
3. **Minimal Cost-Complexity Post-Pruning**: Compute the cost-complexity pruning path using `cost_complexity_pruning_path(X_train, y_train)`:
   - Extract the effective alphas sequence `ccp_alphas` and corresponding impurities `impurities`.
   - Train a decision tree for each alpha in a subsampled sequence of 20 alpha values.
   - Plot number of nodes vs $\alpha$ and test F1-score vs $\alpha$.
   - Identify the optimal $\alpha_{\text{opt}}$ that hits the benchmark $\text{F1} > 0.55$.
4. **Production Rule Extraction**: Extract the top decision rules of the optimal pruned tree using `export_text`. What is the primary splitting feature at the root node, and what is its threshold? Explain why `PageValues` dominates the split from a business perspective.

---

## 🏥 Case Study 2: Emergency Room Triage & High-Cardinality ID Pathology (C4.5 Gain Ratio)

### 🎯 Clinical Context & Scenario
A regional hospital evaluates emergency triage intake for 100 incoming patients:
- Target: `Emergency_Admit` (60 positive, 40 negative).
- Features:
  - `Patient_ID`: Unique integer $1, 2, \dots, 100$.
  - `Heart_Rate_High`: Binary indicator (50 patients high: 45 admitted, 5 discharged; 50 patients normal: 15 admitted, 35 discharged).
  - `Oxygen_Sat_Low`: Binary indicator (40 patients low: 38 admitted, 2 discharged; 60 patients normal: 22 admitted, 38 discharged).

### 📝 Case Study Questions
1. **Parent Node Entropy**: Calculate the Shannon Entropy $H(S)$ of the parent node $S$ in bits. Formula:
   $$H(S) = - \sum_{k=1}^K p_k \log_2(p_k)$$
   Show work for $p_1 = 0.60$ and $p_2 = 0.40$.
2. **Information Gain of Patient_ID vs Clinical Features**:
   - Compute the weighted child entropy if we split on `Patient_ID` (100 leaves, each with 1 patient). What is $H(S, \text{Patient\_ID})$? What is $IG(S, \text{Patient\_ID})$?
   - Compute the weighted child entropy for `Heart_Rate_High` and its Information Gain $IG(S, \text{Heart\_Rate\_High})$.
   - Which feature would ID3/Hunt's algorithm choose as root? Why is this catastrophic for clinical deployment?
3. **C4.5 Split Information Penalty**:
   - Compute the C4.5 Split Information for `Patient_ID`:
     $$SplitInfo(S, \text{Patient\_ID}) = - \sum_{v=1}^{100} \frac{1}{100} \log_2\left(\frac{1}{100}\right) = \log_2(100) \approx 6.6439\text{ bits}$$
   - Compute the Gain Ratio:
     $$GR(S, \text{Patient\_ID}) = \frac{IG(S, \text{Patient\_ID})}{SplitInfo(S, \text{Patient\_ID})}$$
   - Compute $SplitInfo(S, \text{Heart\_Rate\_High})$ and its Gain Ratio $GR(S, \text{Heart\_Rate\_High})$.
   - Prove that C4.5 Gain Ratio successfully prevents the tree from picking `Patient_ID`.
4. **Algorithmic Implementation**:
   - Implement `ShannonEntropyCalculator` in pure NumPy handling the $0 \log_2 0 \equiv 0$ boundary.
   - Implement `GainRatioOptimizer` computing $IG$, $SplitInfo$, and $GR$.

---

## 🏙️ Case Study 3: Property Valuation Engine (Regression Trees & Variance Reduction)

### 🎯 Real Estate Context & Scenario
A property appraisal algorithm evaluates continuous monthly rental valuations $y$ (in thousands of INR) for 8 calibration apartments based on area $x$ (in sq ft):
```plaintext
Property Index:     [ 1,    2,    3,    4,    5,    6,    7,    8   ]
Area (sq ft):       [ 600,  800,  950,  1100, 1300, 1500, 1800, 2200]
Monthly Rent (kINR):[ 18.0, 22.0, 25.0, 28.0, 36.0, 40.0, 48.0, 55.0]
```

### 📝 Case Study Questions
1. **Parent Node Variance**: Calculate the total sample variance $I_{\text{MSE}}(S)$ of the 8 monthly rental values:
   $$I_{\text{MSE}}(S) = \frac{1}{|S|} \sum_{i=1}^{|S|} (y_i - \bar{y})^2$$
2. **Midpoint Split Candidate Evaluation**:
   - Evaluate candidate threshold $\theta = 1200\text{ sq ft}$ (between 1100 and 1300):
     - Left partition $S_L$: properties with Area $\le 1200$ (rents: 18, 22, 25, 28).
     - Right partition $S_R$: properties with Area $> 1200$ (rents: 36, 40, 48, 55).
   - Compute $\bar{y}_L$, $\text{Var}(S_L)$, $\bar{y}_R$, $\text{Var}(S_R)$.
   - Calculate the Variance Reduction:
     $$\Delta \text{Var} = \text{Var}(S) - \left[\frac{|S_L|}{|S|}\text{Var}(S_L) + \frac{|S_R|}{|S|}\text{Var}(S_R)\right]$$
3. **Algorithmic Split Optimizer**: Write a Python/NumPy class `ContinuousSplitFinder` that automatically sorts the continuous feature, generates all candidate midpoints $\theta_i = \frac{x_i + x_{i+1}}{2}$, and returns the optimal threshold $\theta^*$ and peak variance reduction.
4. **Outlier Sensitivity (MSE vs MAE Criterion)**: Suppose property 8 is a luxury penthouse with monthly rent $180.0\text{ kINR}$ instead of $55.0$. Explain why the MSE criterion (which predicts the local mean $\bar{y}$) shifts drastically, whereas the MAE criterion (which predicts the local median) remains robust.

---

## 📐 Case Study 4: Mathematical Equivalence & Taylor Series Bridge (Gini vs Entropy)

### 🎯 Theoretical Formulation & Derivation
1. **Taylor Series Expansion**:
   Prove that the Taylor series of the natural logarithm around 1 is:
   $$\ln(u) = (u - 1) - \frac{(u - 1)^2}{2} + \dots$$
   Substitute $u = p_k$ so that $u - 1 = -(1 - p_k)$. Show that keeping the first-order term yields:
   $$\ln(p_k) \approx -(1 - p_k)$$
   Using $\log_2(p_k) = \frac{\ln(p_k)}{\ln(2)}$, show that:
   $$H(S) = - \sum_{k=1}^K p_k \log_2(p_k) \approx \frac{1}{\ln 2} \sum_{k=1}^K p_k (1 - p_k) = \frac{1}{\ln 2} G(S)$$
2. **Numerical Alignment**:
   Calculate the maximum value of $H(S)$ and $G(S)$ for a balanced binary distribution ($p = 0.5$).
   Show that $G(0.5) = 0.50$ and $\frac{1}{2 \ln 2} \approx 0.721$. Explain why the binary curves $\frac{1}{2} H(p)$ and $G(p)$ are almost indistinguishable across the entire interval $p \in [0, 1]$.
3. **Pure NumPy Gini Evaluator**:
   Implement `GiniImpurityEvaluator` in pure NumPy. Verify that:
   - A pure array returns $0.0$.
   - A 50/50 binary array returns $0.50$.
   - A uniform 4-class array returns $0.75$.
4. **Production Decision Invariant**:
   Why does scikit-learn's `DecisionTreeClassifier` default to `criterion='gini'`? Analyze computational complexity: Gini uses simple floating-point multiplications and subtractions, whereas Entropy requires transcendent $\log_2$ evaluations on every candidate split of every continuous feature.
