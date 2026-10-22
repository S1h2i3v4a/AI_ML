# Lecture 28: Practice Problems Suite (Questions - Hinglish)
## Supervised Machine Learning (Part 4) — Decision Trees

Yeh problem set Decision Trees ke mathematical foundations, impurity calculation, threshold optimization, C4.5 gain ratio regularization, variance reduction, aur cost-complexity pruning par structured case-based questions provide karta hai. Sabhi questions strictly Lecture 28 ke syllabus par based hain.

---

## 🛒 Case Study 1: E-Commerce Visitor Purchase Conversion (ShopSmart Dataset)

### 🎯 Business Context & Scenario
ShopSmart ek e-commerce platform hai jisme 12,330 visitor clickstream records hain (`shop_smart_ecommerce.csv`). Dataset mein 18 features hain:
- Numerical features: `Administrative_Duration`, `Informational_Duration`, `ProductRelated_Duration`, `BounceRates`, `ExitRates`, `PageValues`.
- Categorical features: `Month`, `OperatingSystems`, `Browser`, `Region`, `TrafficType`, `VisitorType`, `Weekend`.
- Target: `Revenue` (Boolean: `True` agar visitor ne khareedari ki, `False` agar session abandon kiya; ~15.4% positive rate).

### 📝 Case Study Questions
1. **Unconstrained Tree ki Overfitting**: Training set par unconstrained `DecisionTreeClassifier(random_state=42)` fit karein. Model ki depth (`get_depth()`) aur leaf count (`get_n_leaves()`) check karein. Training accuracy aur test F1-score compare karein. Explain karein ki jab `min_samples_leaf=1` hota hai toh tree training noise ko memorize kyun kar leta hai?
2. **Pre-Pruning Grid Search**: Ek `GridSearchCV` pipeline banayein jisme testing parameters hon:
   - `max_depth` $\in [3, 5, 8, 12]$
   - `min_samples_leaf` $\in [5, 10, 20, 50]$
   - `min_impurity_decrease` $\in [0.0, 0.001, 0.005]$
   Scoring metric `f1` use karke 5-fold Stratified CV run karein aur optimal parameters bataiye.
3. **Minimal Cost-Complexity Post-Pruning**: Scikit-learn ke `cost_complexity_pruning_path(X_train, y_train)` function se effective alphas (`ccp_alphas`) nikaalein:
   - Alphas ke sequence par alag-alag trees train karein.
   - Nodes count vs $\alpha$ aur test F1-score vs $\alpha$ plot karein.
   - F1 benchmark > 0.55 beat karne wala optimal $\alpha_{\text{opt}}$ identify karein.
4. **Production Decision Rules**: Optimal tree ke top rules ko `export_text` function se print karein. Root node par konsa feature split ho raha hai aur kis threshold par? Business perspective se `PageValues` itna important kyun hai?

---

## 🏥 Case Study 2: Hospital Emergency Triage aur High-Cardinality ID Failure (C4.5 Gain Ratio)

### 🎯 Clinical Context & Scenario
Ek emergency hospital ward mein 100 incoming patients ka triage data hai:
- Target: `Emergency_Admit` (60 positive / admit, 40 negative / discharge).
- Features:
  - `Patient_ID`: Unique integer $1, 2, \dots, 100$.
  - `Heart_Rate_High`: Binary (50 high: 45 admit, 5 discharge; 50 normal: 15 admit, 35 discharge).
  - `Oxygen_Sat_Low`: Binary (40 low: 38 admit, 2 discharge; 60 normal: 22 admit, 38 discharge).

### 📝 Case Study Questions
1. **Parent Node ki Shannon Entropy**: Parent node $S$ ki Shannon Entropy calculate karein:
   $$H(S) = - \sum_{k=1}^K p_k \log_2(p_k)$$
   $p_1 = 0.60$ aur $p_2 = 0.40$ ke liye step-by-step answer nikalein.
2. **Patient_ID vs Clinical Features ka Information Gain**:
   - Agar hum `Patient_ID` par split karte hain (100 leaves, har leaf mein 1 patient), toh child entropy $H(S, \text{Patient\_ID})$ kya hogi? Information Gain $IG(S, \text{Patient\_ID})$ kitna aayega?
   - `Heart_Rate_High` feature ka weighted child entropy aur Information Gain calculate karein.
   - ID3/Hunt's greedy algorithm kis feature ko root chunega? Medical treatment ke liye yeh kitna bada disaster hai?
3. **C4.5 Split Information Penalty**:
   - `Patient_ID` ke liye C4.5 Split Information formula evaluate karein:
     $$SplitInfo(S, \text{Patient\_ID}) = - \sum_{v=1}^{100} \frac{1}{100} \log_2\left(\frac{1}{100}\right) = \log_2(100) \approx 6.6439\text{ bits}$$
   - Gain Ratio calculate karein:
     $$GR(S, \text{Patient\_ID}) = \frac{IG(S, \text{Patient\_ID})}{SplitInfo(S, \text{Patient\_ID})}$$
   - `Heart_Rate_High` ka $SplitInfo$ aur $GR$ calculate karein.
   - Prove karein ki C4.5 Gain Ratio high-cardinality ID features ko disqualify kyun kar deta hai.
4. **Pure NumPy Implementation**: Pure NumPy mein `ShannonEntropyCalculator` aur `GainRatioOptimizer` classes banayein jisme $0 \log_2 0 \equiv 0$ boundary condition properly handled ho.

---

## 🏙️ Case Study 3: Property Valuation Engine (Regression Trees & Variance Reduction)

### 🎯 Real Estate Context & Scenario
Ek property valuation model 8 calibration flats ke monthly rent $y$ (in thousands of INR) ko area $x$ (in sq ft) ke basis par predict kar raha hai:
```plaintext
Property Index:     [ 1,    2,    3,    4,    5,    6,    7,    8   ]
Area (sq ft):       [ 600,  800,  950,  1100, 1300, 1500, 1800, 2200]
Monthly Rent (kINR):[ 18.0, 22.0, 25.0, 28.0, 36.0, 40.0, 48.0, 55.0]
```

### 📝 Case Study Questions
1. **Parent Node ki Variance**: Sabhi 8 flats ke rent ka sample variance $I_{\text{MSE}}(S)$ calculate karein:
   $$I_{\text{MSE}}(S) = \frac{1}{|S|} \sum_{i=1}^{|S|} (y_i - \bar{y})^2$$
2. **Candidate Split Evaluation**:
   - Midpoint candidate threshold $\theta = 1200\text{ sq ft}$ par split evaluate karein:
     - Left partition $S_L$: Area $\le 1200$ (rents: 18, 22, 25, 28).
     - Right partition $S_R$: Area $> 1200$ (rents: 36, 40, 48, 55).
   - $\bar{y}_L$, $\text{Var}(S_L)$, $\bar{y}_R$, $\text{Var}(S_R)$ compute karein.
   - Variance Reduction calculate karein:
     $$\Delta \text{Var} = \text{Var}(S) - \left[\frac{|S_L|}{|S|}\text{Var}(S_L) + \frac{|S_R|}{|S|}\text{Var}(S_R)\right]$$
3. **Continuous Split Finder**: Pure NumPy mein `ContinuousSplitFinder` class likhein jo midpoints $\theta_i = \frac{x_i + x_{i+1}}{2}$ test karke maximum variance reduction aur best threshold locate kare.
4. **Outlier Sensitivity (MSE vs MAE Criterion)**: Agar property 8 ek luxury penthouse ho jiska rent $180.0\text{ kINR}$ ho jaye, toh MSE criterion (mean prediction) drastically distort kyun hota hai, jabki MAE criterion (median prediction) stable kyun rehta hai?

---

## 📐 Case Study 4: Mathematical Equivalence (Gini Impurity vs Shannon Entropy)

### 🎯 Theoretical Formulation & Derivation
1. **Taylor Series Expansion**:
   Prove karein ki $\ln(u)$ ka Taylor series around 1 hota hai:
   $$\ln(u) = (u - 1) - \frac{(u - 1)^2}{2} + \dots$$
   $u = p_k$ rakh kar prove karein ki first-order approximation se:
   $$H(S) \approx \frac{1}{\ln 2} G(S)$$
2. **Numerical Bounds Comparison**:
   Binary balanced distribution ($p = 0.5$) ke liye $H(0.5)$ aur $G(0.5)$ compare karein. Curve $\frac{1}{2} H(p)$ aur $G(p)$ ke concordance ko explain karein.
3. **Pure NumPy Gini Evaluator**:
   Pure NumPy mein `GiniImpurityEvaluator` implement karein jo weighted split impurity calculate kare.
4. **Scikit-Learn Default Invariant**:
   Scikit-learn by default Gini impurity kyun use karta hai? Computational complexity analyze karein (simple multiplication vs transcendental base-2 log calculations).
