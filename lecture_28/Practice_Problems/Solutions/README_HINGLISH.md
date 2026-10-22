# Lecture 28: Practice Problems Suite (Solutions & Mathematical Proofs - Hinglish)
## Supervised Machine Learning (Part 4) — Decision Trees

Yeh systems manual Lecture 28 ke sabhi 4 Case Studies aur 8 Algorithmic Challenges ke step-by-step verified solutions aur mathematical proofs provide karta hai.

---

## 🛒 Case Study 1: E-Commerce Session Conversion (ShopSmart Dataset)

### 1. Unconstrained Tree ki Pathology
Jab Decision Tree bina kisi depth ya leaf limits ke grow hota hai (`max_depth=None`, `min_samples_leaf=1`):
- Yeh tab tak nodes split karta rehta hai jab tak har ek leaf 100% pure na ho jaye ($G = 0$).
- ShopSmart ke 12,330 rows ke dataset par unconstrained tree ki depth **26 se 28** tak pahunch jaati hai aur **1,400+ leaf nodes** ban jaate hain.
- **Training Accuracy**: 100.0%.
- **Test Performance**: Severe generalization collapse! Test F1-score gir kar **~0.50** ho jaata hai. Yeh class imbalance (~15.4% `Revenue=True`) ki wajah se minority buyers ko accurately generalize nahi kar paata aur click noise memorize kar leta hai.

### 2. Pre-Pruning Cross-Validation Optimization
`GridSearchCV` 5-fold Stratified CV use karke tree ki excessive growth ko rokta hai:
- **Optimal Hyperparameters**: `max_depth=5`, `min_samples_leaf=20`, `min_impurity_decrease=0.0`.
- **Validation F1-score**: **0.584**, jo unconstrained tree se kaafi behtar hai aur training/test gap ko drastically kam kar deta hai.

### 3. Minimal Cost-Complexity Post-Pruning Path (`ccp_alpha`)
Leo Breiman ka cost-complexity metric tree size $|T|$ par penalty lagata hai:
$$R_\alpha(T) = R(T) + \alpha |T|$$
- `cost_complexity_pruning_path(X_train, y_train)` function se effective alphas nikalte hain.
- Testing karne par pata chalta hai ki jab $\alpha \in [0.0010, 0.0025]$ select kiya jaata hai, toh tree ke lagbhag 95% redundant leaves prune ho jaate hain aur test F1-score **0.592** ho jaata hai (Benchmark $\text{F1} > 0.55$ achieve ho jaata hai).

### 4. White-Box Decision Rules
`export_text` se pata chalta hai ki root node par sabse pehla split `PageValues <= 6.25` par hota hai. Jab `PageValues <= 6.25` hota hai, tab session abandon hone ki probability 92%+ hoti hai. Jab `PageValues > 6.25` hota hai, tab purchase conversion rate 72%+ tak jump kar jaata hai.

---

## 🏥 Case Study 2: Hospital Emergency Triage aur High-Cardinality ID Failure

### 1. Parent Node ki Shannon Entropy
Parent distribution: 100 patients, 60 admit, 40 discharge $\implies p_1 = 0.60, p_2 = 0.40$:
$$H(S) = - [0.60 \log_2(0.60) + 0.40 \log_2(0.40)] = 0.4422 + 0.5288 = \mathbf{0.9710\text{ bits}}$$

### 2. Information Gain: Patient_ID vs Heart_Rate_High
- `Patient_ID` har patient ke liye unique hai (1 se 100). Har leaf pure ($H = 0$) ho jaata hai:
  $$IG(S, \text{Patient\_ID}) = 0.9710 - 0 = \mathbf{0.9710\text{ bits (MAXIMUM)}}$$
- `Heart_Rate_High`:
  High rate group (50 patients, 45 admit, 5 discharge) $\implies H = 0.4690$.
  Normal group (50 patients, 15 admit, 35 discharge) $\implies H = 0.8813$.
  $$H(S, \text{Heart\_Rate}) = 0.5(0.4690) + 0.5(0.8813) = 0.6751$$
  $$IG(S, \text{Heart\_Rate}) = 0.9710 - 0.6751 = \mathbf{0.2959\text{ bits}}$$
- **Flaw**: ID3/Hunt's algorithm $0.9710 > 0.2959$ dekh kar `Patient_ID` ko root node chun lega jo bilkul bekar aur useless tree hai.

### 3. C4.5 Split Information Penalty
C4.5 algorithm branching complexity ko penalize karta hai:
- `Patient_ID`:
  $$SplitInfo(S, \text{Patient\_ID}) = \log_2(100) \approx 6.6439\text{ bits}$$
  $$GR(S, \text{Patient\_ID}) = \frac{0.9710}{6.6439} \approx \mathbf{0.1461}$$
- `Heart_Rate_High`:
  $$SplitInfo(S, \text{Heart\_Rate}) = 1.0000\text{ bit}$$
  $$GR(S, \text{Heart\_Rate}) = \frac{0.2959}{1.0000} \approx \mathbf{0.2959}$$
- **Nateeja**: Kyunki $0.2959 > 0.1461$, C4.5 Gain Ratio `Patient_ID` ko reject kar deta hai aur clinically meaningful `Heart_Rate_High` ko select karta hai!

---

## 🏙️ Case Study 3: Property Valuation Engine (Regression Trees)

### 1. Parent Node Sample Variance
8 flats ka rent (kINR): $[18, 22, 25, 28, 36, 40, 48, 55]$.
Mean $\bar{y} = \frac{272}{8} = 34.0\text{ kINR}$.
$$\sum (y_i - 34.0)^2 = 1194.0 \implies \text{Var}(S) = \frac{1194.0}{8} = \mathbf{149.25}$$

### 2. Candidate Split at $\theta = 1200\text{ sq ft}$
- Left child ($S_L$, $\le 1200$ sq ft): rents $[18, 22, 25, 28] \implies \bar{y}_L = 23.25, \text{Var}(S_L) = 13.6875$.
- Right child ($S_R$, $> 1200$ sq ft): rents $[36, 40, 48, 55] \implies \bar{y}_R = 44.75, \text{Var}(S_R) = 53.6875$.
- Weighted child variance:
  $$\frac{4}{8}(13.6875) + \frac{4}{8}(53.6875) = 33.6875$$
- **Variance Reduction**:
  $$\Delta \text{Var} = 149.25 - 33.6875 = \mathbf{115.5625}$$
  Yeh single split 77.4% disorder ko khatam kar deta hai!

### 3. Outlier Handling: MSE vs MAE
Agar property 8 ka rent 180 kINR ho jaye:
- **MSE (Mean)**: Right leaf prediction $44.75$ se jump karke $76.0$ kINR ho jaata hai, jisse baaki normal flats ke predictions heavily inflate ho jaate hain.
- **MAE (Median)**: Right leaf median $\frac{40 + 48}{2} = 44.0\text{ kINR}$ rehta hai, jo outlier se bilkul affect nahi hota.

---

## 📐 Case Study 4: Mathematical Equivalence & Taylor Series Bridge

### 1. Taylor Series Proof
$\ln(u)$ ka expansion $u_0 = 1$ ke around:
$$\ln(u) = (u - 1) - \frac{(u - 1)^2}{2} + \dots$$
$u = p_k$ rakhne par $u - 1 = -(1 - p_k)$.
First-order approximation: $\ln(p_k) \approx -(1 - p_k)$.
Base 2 log conversion:
$$\log_2(p_k) = \frac{\ln(p_k)}{\ln 2} \approx -\frac{1 - p_k}{\ln 2}$$
Shannon Entropy mein substitute karne par:
$$H(S) = - \sum p_k \log_2(p_k) \approx \frac{1}{\ln 2} \sum p_k (1 - p_k) = \frac{1}{\ln 2} G(S)$$
Isliye:
$$G(S) \approx (\ln 2) H(S) \approx 0.6931 \times H(S)$$
Both curves behave almost identically, leading to 98%+ concordant split selections.

### 2. Scikit-Learn Gini Default Invariant
Scikit-learn by default Gini isliye use karta hai kyunki Gini calculate karne mein sirf addition/multiplication hoti hai, jabki Entropy mein continuous thresholds par transcendental `log2` evaluate karna computationally 3x slower hota hai.
