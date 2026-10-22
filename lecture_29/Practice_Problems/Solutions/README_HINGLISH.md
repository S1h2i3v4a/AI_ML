# Lecture 29: Practice Problems Suite (Solutions & Mathematical Proofs - Hinglish)
## Supervised Machine Learning (Part 5) — Support Vector Machines & Ensemble Learning

Yeh systems manual Lecture 29 ke sabhi 4 Case Studies aur 8 Algorithmic Challenges ke verified solutions, mathematical derivations, aur benchmark results provide karta hai.

---

## 🩺 Case Study 1: Diabetes Progression Forecaster (Support Vector Regression - SVR)

### 1. Unscaled SVR ka Failure
Jab raw continuous target $y \in [25, 346]$ par default `SVR()` run karte hain:
- Test $R^2$ score sirf **0.1616** aata hai.
- **Wajah**:
  1. Default tube width $\epsilon = 0.1$ target range ($321$ units) ke comparison mein itni choti hai ki lagbhag saare points tube ke bahar gir jaate hain.
  2. Default $C = 1.0$ itne bade errors ($100^2$ scale) ko balance nahi kar paata.

### 2. Dual Scaled Pipeline Implementation
Jab target $y$ ko `StandardScaler` se scale karte hain:
$$y_{\text{scaled}} = \frac{y - \mu_y}{\sigma_y}$$
- Scaled target par SVR fit karke inverse-transform karne par Test $R^2$ score jump karke **0.4884** (RMSE = 52.55) ho jaata hai, jo teacher notebook `svr_implementation_reference.ipynb` se perfectly match karta hai.

### 3. Support Vector Sparsity
- `svr_scaled.support_` inspect karne par:
  - **269 / 309 samples (87.1%)** support vectors bante hain.
  - KKT Complementary Slackness ke rule se jo points tube ke andar hote hain ($|y_i - f(\mathbf{x}_i)| < \epsilon$), unke Lagrange multipliers $\alpha_i = \alpha_i^* = 0$ hote hain. Iska matlab un samples ka final model par zero influence hota hai.

---

## 🚢 Case Study 2: Titanic Survival Modeling aur OOB Validation

### 1. Out-Of-Bag (OOB) Mathematical Derivation (First Principles)
Size $N$ ke dataset se replacement ke saath $N$ draws kiye gaye:
1. Ek single draw mein kisi specific observation $x_i$ ke select NA hone ki probability:
   $$P = 1 - \frac{1}{N}$$
2. Sabhi $N$ draws mein $x_i$ ke ek baar bhi select NA hone ki probability:
   $$P(\text{omitted}) = \left(1 - \frac{1}{N}\right)^N$$
3. Dono taraf natural logarithm lene par:
   $$\ln\left[\left(1 - \frac{1}{N}\right)^N\right] = N \ln\left(1 - \frac{1}{N}\right)$$
4. Taylor series $\ln(1 - u) = -u - \frac{u^2}{2} - \dots$ use karke:
   $$N \left( -\frac{1}{N} - \frac{1}{2N^2} - \dots \right) = -1 - \frac{1}{2N} - \dots$$
5. Limit $N \to \infty$ lene par:
   $$\lim_{N \to \infty} \left(1 - \frac{1}{N}\right)^N = e^{-1} = \frac{1}{e} \approx \mathbf{0.367879 \implies 36.79\%}$$
6. Isliye bootstrap sample mein unique samples include hone ki probability:
   $$1 - \frac{1}{e} \approx \mathbf{0.632121 \implies 63.21\%}$$

### 2. Titanic Dataset Par Empirical Verification
- `RandomForestClassifier(n_estimators=501, oob_score=True, max_depth=4)`:
  - **OOB Score**: **81.44%**.
  - **Held-Out Test Accuracy**: **82.51%**.
  - OOB score bina kisi cross-validation ke unbiased estimate provide karta hai.
- **Top Importances (MDI)**:
  1. `sex_male`: **49.50%**
  2. `fare`: **19.39%**
  3. `pclass`: **15.79%**

---

## 👥 Case Study 3: Wisdom of Crowds aur Ensemble Variance Collapse

### 1. Condorcet's Jury Theorem
Agar individual classifier ki accuracy $p = 0.60$ hai:
- $M = 3$ voters: Majority Accuracy = **64.80%**
- $M = 11$ voters: Majority Accuracy = **75.35%**
- $M = 101$ voters: Majority Accuracy = **97.91%**
$M \to \infty$ par ensemble accuracy 100% ho jaati hai!

### 2. Leo Breiman's Variance Decomposition
$M$ base estimators ke average prediction $\bar{f}$ ka variance:
$$\text{Var}(\bar{f}) = \rho \sigma^2 + \frac{1 - \rho}{M} \sigma^2$$
- $M \to \infty$ hone par term $\frac{1-\rho}{M}\sigma^2 \to 0$ ho jaata hai, aur variance irreducible floor $\rho \sigma^2$ par ruk jaata hai.
- Standard Bagging mein trees correlate rehte hain ($\rho \approx 0.5$).
- Random Forest feature sub-spacing ($\sqrt{D}$) use karke trees ko de-correlate karta hai, jisse $\rho \downarrow 0.1$ ho jaata hai aur variance collapse ho kar minimum ho jaata hai!

### 3. Heterogeneous Bagging Benchmark
- **Decision Tree (High Variance)**:
  - Single Tree: **75.34%** $\to$ Bagged Tree ($M=201$): **78.92%** ($\mathbf{+3.59\%}$ boost!)
- **Logistic Regression (Low Variance)**:
  - Single Model: **78.48%** $\to$ Bagged Model ($M=201$): **78.48%** ($\mathbf{+0.00\%}$ boost)
- **Takeaway**: Bagging unstable high-variance models ko stabilize karti hai, lekin stable low-variance linear models par koi effect nahi karti.

---

## ⚡ Case Study 4: Computational Scaling (LinearSVR vs Kernel SVR)

### 1. Benchmark Results ($N = 5,000$ samples)
- `LinearSVR(dual='auto')` Coordinate Descent: **3.19s**
- `SVR(kernel='linear')` Libsvm SMO: **56.43s**
- **Speedup**: `LinearSVR` Coordinate Descent se **17.7x faster** chali!

### 2. Algorithmic Reasons
1. `LinearSVR` primal objective function par Coordinate Descent chala kar $O(N \cdot D)$ mein solve karti hai.
2. `SVR(kernel='linear')` $N \times N$ Gram matrix aur SMO solver use karti hai jo $O(N^2 \sim N^3)$ time complexity leti hai.
