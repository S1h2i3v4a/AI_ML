# Lecture 29: Practice Problems Suite (Questions - Hinglish)
## Supervised Machine Learning (Part 5) — Support Vector Machines & Ensemble Learning

Yeh problem set Support Vector Machines (SVM), Support Vector Regression (SVR) ki $\epsilon$-insensitive tube, dual target scaling, Out-Of-Bag (OOB) derivation, aur Breiman's double randomness variance reduction par structured case-based questions provide karta hai. Sabhi questions strictly Lecture 29 ke syllabus par based hain.

---

## 🩺 Case Study 1: Diabetes Progression Forecaster (Support Vector Regression - SVR)

### 🎯 Clinical Context & Scenario
Scikit-learn ka official Diabetes dataset (`datasets.load_diabetes()`) 442 patients ke 10 continuous physiological predictors (`age`, `sex`, `bmi`, `bp`, `s1`, `s2`, `s3`, `s4`, `s5`, `s6`) provide karta hai. Target $y$ ek saal baad measurable disease progression index hai ($y \in [25, 346]$).

### 📝 Case Study Questions
1. **Unscaled Model ka Failure**:
   - Data ko 70% train aur 30% test sets mein divide karein (`random_state=42`).
   - Bina scaling ke direct $X_{\text{train}}$ aur $y_{\text{train}}$ par `SVR(kernel='rbf', C=10.0, epsilon=0.1)` fit karein.
   - Train aur test $R^2$ scores calculate karein. Test $R^2$ negative ya near zero kyun aata hai?
   - RBF kernel formula $K(\mathbf{x}_i, \mathbf{x}_j) = \exp(-\gamma \|\mathbf{x}_i - \mathbf{x}_j\|^2)$ ke context mein explain karein ki unscaled data par distance metric kaise distort ho jaata hai.
2. **Dual Scaling Pipeline Implementation**:
   - Ek aisi pipeline banayein jisme:
     - Features $X$ ko `StandardScaler` se scale kiya jaye.
     - Continuous target $y$ ko bhi ek alag `StandardScaler` se scale kiya jaye:
       $$y_{\text{scaled}} = \frac{y - \mu_y}{\sigma_y}$$
     - SVR ko scaled data par train kiya jaye.
     - Predictions ko inverse-transform karke wapas original units mein laya jaye:
       $$\hat{y} = \hat{y}_{\text{scaled}} \times \sigma_y + \mu_y$$
   - Test $R^2$ score aur RMSE report karein. Verify karein ki $R^2 > 0.45$ achieve ho raha hai.
3. **5-Fold Cross-Validation GridSearchCV**:
   - Systematic grid search run karein:
     - $C \in [0.1, 1.0, 10.0, 50.0, 100.0]$
     - $\epsilon \in [0.01, 0.05, 0.1, 0.2, 0.5]$
     - $\gamma \in ['scale', 'auto', 0.01, 0.1, 1.0]$
   - 5-fold CV use karke best hyperparameter combination aur final test $R^2$ score determine karein.
4. **Dual Sparsity aur Support Vector Analysis**:
   - `model.support_` inspect karein.
   - Training cohort ke kitne percent patients support vectors bane?
   - Explain karein ki jo points tube ke andar hote hain ($|y_i - f(\mathbf{x}_i)| < \epsilon$), unke Lagrange multipliers zero ($\alpha_i = \alpha_i^* = 0$) kyun hote hain aur final regression equation par unka koi asar kyun nahi hota.

---

## 🚢 Case Study 2: Titanic Survival Modeling aur OOB Validation

### 🎯 Maritime Context & Scenario
Titanic passenger dataset (`sns.load_dataset('titanic')`) 891 passengers ka record provide karta hai. Hum 5 features (`pclass`, `sex`, `fare`, `embarked`, `age`) select karte hain target `survived` ko predict karne ke liye.

### 📝 Case Study Questions
1. **OOB Mathematical Derivation (First Principles)**:
   - Maan lijiye size $N$ ke dataset se $N$ samples uniformly with replacement draw kiye jaate hain.
   - Ek single draw mein kisi specific sample $x_i$ ke select NA hone ki probability kya hai?
   - Sabhi $N$ independent draws mein $x_i$ ke ek baar bhi select NA hone ki probability kya hogi?
   - Asymptotic limit calculate karein:
     $$\lim_{N \to \infty} \left(1 - \frac{1}{N}\right)^N$$
     Calculus ke fundamental definition $\lim_{u \to 0} (1 + u)^{1/u} = e$ ka use karke prove karein ki:
     $$P(\text{omitted}) = \frac{1}{e} \approx 0.367879 \implies \approx 36.8\%$$
   - Prove karein ki har bootstrap sample mein expected unique samples $1 - 1/e \approx 63.2\%$ hote hain.
2. **Production Random Forest aur OOB Verification**:
   - Missing values impute karein (`age` ke liye median, `embarked` ke liye mode), categorical features encode karein, aur 75/25 split karein (`random_state=42`).
   - `RandomForestClassifier(n_estimators=501, oob_score=True, max_depth=4, random_state=42)` train karein.
   - Model ke internal `rf.oob_score_` ko held-out test accuracy se compare karein:
     ```python
     print("OOB Score:", rf.oob_score_ * 100, "%")
     print("Test Accuracy:", accuracy_score(y_test, rf.predict(X_test)) * 100, "%")
     ```
   - Explain karein ki OOB score bina kisi validation split ke unbiased accuracy estimate kaise de deta hai.
3. **MDI Feature Importance**:
   - `rf.feature_importances_` nikaalein.
   - Top 2 features konse hain aur historical "women and children first" evacuation rule se inka kya relation hai?

---

## 👥 Case Study 3: Wisdom of Crowds aur Ensemble Variance Collapse

### 🎯 Theoretical Scenario
Ek credit fraud detection engine $M$ independent weak sensor models ko aggregate karta hai. Har model ki accuracy $p = 0.60$ hai.

### 📝 Case Study Questions
1. **Condorcet's Jury Theorem Formulation**:
   - $M$ independent classifiers (odd $M$) ke majority vote ke sahi hone ki probability binomial formula se calculate karein:
     $$P(\text{Majority}) = \sum_{k=\lfloor M/2 \rfloor + 1}^M \binom{M}{k} p^k (1 - p)^{M-k}$$
   - $M = 3$, $M = 11$, aur $M = 101$ ke liye $P(\text{Majority})$ calculate karein.
   - Prove karein ki agar $p > 0.5$ ho toh $M \to \infty$ par accuracy 100% ki taraf badhti hai.
2. **Leo Breiman's Variance Decomposition**:
   - $M$ base models ke average prediction $\bar{f}$ ka variance hota hai:
     $$\text{Var}(\bar{f}) = \rho \sigma^2 + \frac{1 - \rho}{M} \sigma^2$$
   - Prove karein ki $M \to \infty$ par variance $\rho \sigma^2$ par ruk jaata hai.
   - Explain karein ki standard Bagging mein correlation $\rho > 0$ rehta hai isliye variance plateau kar jaata hai, jabki Random Forest feature bagging ($\sqrt{D}$) se $\rho$ ko force karke neeche le aata hai aur variance collapse ho jaata hai.
3. **Heterogeneous Base Estimator Experiment**:
   - Titanic dataset par do meta-estimators train karein ($M = 201$):
     - `BaggingClassifier(base_estimator=DecisionTreeClassifier())`
     - `BaggingClassifier(base_estimator=LogisticRegression(max_iter=1000))`
   - Explain karein ki high-variance Decision Trees par bagging se massive boost kyun milta hai, jabki low-variance Logistic Regression par koi improvement kyun nahi hoti.

---

## ⚡ Case Study 4: Computational Scaling & Coordinate Descent (LinearSVR vs Kernel SVR)

### 🎯 Scenario
Financial order book transactions $N = 1,000$ se $N = 100,000$ par scale ho rahi hain.

### 📝 Case Study Questions
1. **Algorithmic Time Complexity**:
   - Libsvm (`SVR(kernel='linear')`) quadratic-cubic time ($O(N^2 \sim N^3)$) kyun leti hai?
   - Liblinear (`LinearSVR`) Coordinate Descent use karke linear time ($O(N \cdot D)$) mein kaise execute ho jaati hai?
2. **Primal vs Dual Coordinate Descent**:
   - `LinearSVR(dual=False)` kab prefer kiya jaata hai? Prove karein ki jab samples features se zyada hon ($N > D$), tab primal formulation memory aur speed dono mein superior hoti hai.
3. **Decision Matrix**:
   - Small non-linear dataset ($N < 10,000$): konsa model?
   - Large linear dataset ($N > 50,000$, $N \gg D$): konsa model?
   - Massive streaming data ($N > 1,000,000$): konsa model?
