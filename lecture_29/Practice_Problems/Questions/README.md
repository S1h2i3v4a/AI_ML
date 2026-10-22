# Lecture 29: Practice Problems Suite (Questions)
## Supervised Machine Learning (Part 5) — Support Vector Machines & Ensemble Learning

This problem set tests maximum margin duality, the $\epsilon$-insensitive tube in SVR, mandatory target standardization, Out-Of-Bag (OOB) derivation, and Breiman's double randomness variance reduction. All problems are strictly derived from the concepts taught in Lecture 29.

---

## 🩺 Case Study 1: Diabetes Progression Forecaster (Support Vector Regression - SVR)

### 🎯 Clinical Context & Scenario
A medical study evaluates 442 diabetes patients (`datasets.load_diabetes()`) across 10 continuous physiological predictors:
`age`, `sex`, `bmi`, `bp`, `s1`, `s2`, `s3`, `s4`, `s5`, `s6`.
Target $y$: Quantitative disease progression index measured one year after baseline ($y \in [25, 346]$).

### 📝 Case Study Questions
1. **Unscaled Catastrophic Failure**:
   - Split the data into 70% train and 30% test sets (`random_state=42`).
   - Fit an unscaled `SVR(kernel='rbf', C=10.0, epsilon=0.1)` directly on $X_{\text{train}}$ and $y_{\text{train}}$.
   - Compute train and test $R^2$ scores. Why is the test $R^2$ negative or near zero?
   - Explain mathematically why an RBF kernel $K(\mathbf{x}_i, \mathbf{x}_j) = \exp(-\gamma \|\mathbf{x}_i - \mathbf{x}_j\|^2)$ fails when continuous features have differing scales or when the target scale spans hundreds of units.
2. **Dual Scaling Pipeline Implementation**:
   - Construct a standardized pipeline where:
     - Features $X$ are scaled using `StandardScaler`.
     - Target $y$ is scaled using a separate `StandardScaler`:
       $$y_{\text{scaled}} = \frac{y - \mu_y}{\sigma_y}$$
     - SVR is trained on $(X_{\text{train\_scaled}}, y_{\text{train\_scaled}})$.
     - Predictions $\hat{y}_{\text{scaled}}$ are mapped back to original progression units using:
       $$\hat{y} = \hat{y}_{\text{scaled}} \times \sigma_y + \mu_y$$
   - Evaluate test $R^2$ score and RMSE. Confirm that $R^2 > 0.45$.
3. **5-Fold Cross-Validation GridSearchCV**:
   - Perform a systematic grid search over:
     - $C \in [0.1, 1.0, 10.0, 50.0, 100.0]$
     - $\epsilon \in [0.01, 0.05, 0.1, 0.2, 0.5]$
     - $\gamma \in ['scale', 'auto', 0.01, 0.1, 1.0]$
   - Using 5-fold cross-validation with scoring `r2`.
   - What is the best parameter combination? What is the final test $R^2$ score?
4. **Dual Sparsity & Support Vector Analysis**:
   - In SVR, the dual optimization problem yields Lagrange multipliers $\alpha_i, \alpha_i^* \ge 0$.
   - Inspect `model.support_` (indices of support vectors).
   - What percentage of the training cohort become support vectors?
   - Explain why observations strictly inside the tube ($|y_i - f(\mathbf{x}_i)| < \epsilon$) have $\alpha_i = \alpha_i^* = 0$, meaning they have zero influence on the final regression function.

---

## 🚢 Case Study 2: Titanic Survival Modeling & OOB Validation

### 🎯 Maritime Evacuation Context & Scenario
The Titanic passenger dataset (`sns.load_dataset('titanic')`) contains demographic and cabin attributes for 891 passengers. We select 5 key features: `pclass`, `sex`, `fare`, `embarked`, and `age` to predict binary survival (`survived`).

### 📝 Case Study Questions
1. **First-Principles OOB Mathematical Derivation**:
   - Suppose a bootstrap dataset of size $N$ is drawn from a training set of size $N$ uniformly with replacement.
   - For any specific training sample $x_i$, what is the probability that it is NOT selected in a single random draw?
   - What is the probability that $x_i$ is NOT selected in all $N$ independent draws?
   - Compute the asymptotic limit:
     $$\lim_{N \to \infty} \left(1 - \frac{1}{N}\right)^N$$
     Using the fundamental calculus definition $\lim_{u \to 0} (1 + u)^{1/u} = e$, prove that the exclusion probability converges to:
     $$P(\text{omitted}) = \frac{1}{e} \approx 0.367879 \implies \approx 36.8\%$$
   - Show that the expected proportion of unique training samples included in the bootstrap replicate is $1 - 1/e \approx 63.2\%$.
2. **Production Random Forest & OOB Verification**:
   - Preprocess the Titanic dataset: impute missing values (median for `age`, mode for `embarked`), map categorical features (`sex`, `embarked`), and split 75% train / 25% test (`random_state=42`).
   - Train `RandomForestClassifier(n_estimators=501, oob_score=True, max_depth=4, random_state=42)` on the training set.
   - Compare the internal `rf.oob_score_` against the held-out test set accuracy:
     ```python
     print("OOB Score:", rf.oob_score_ * 100, "%")
     print("Test Accuracy:", accuracy_score(y_test, rf.predict(X_test)) * 100, "%")
     ```
   - Explain why OOB validation serves as a free validation set and why it requires zero data leakage across trees.
3. **MDI Feature Importance**:
   - Extract `rf.feature_importances_`.
   - Which two features exhibit the highest Mean Decrease in Impurity?
   - Relate these importances to the historical "women and children first" maritime evacuation protocol.

---

## 👥 Case Study 3: Wisdom of Crowds & Ensemble Variance Collapse

### 🎯 Theoretical Aggregation Scenario
A fraud detection system deploys $M$ independent weak sensor models to classify suspicious credit transactions. Each sensor model has an individual classification accuracy of $p = 0.60$.

### 📝 Case Study Questions
1. **Condorcet's Jury Theorem Formulation**:
   - For an ensemble of $M$ independent classifiers (where $M$ is an odd number), the majority vote is correct if at least $k = \lfloor M/2 \rfloor + 1$ classifiers are correct.
   - Using the cumulative binomial formula:
     $$P(\text{Majority}) = \sum_{k=\lfloor M/2 \rfloor + 1}^M \binom{M}{k} p^k (1 - p)^{M-k}$$
   - Calculate $P(\text{Majority})$ for $M = 3$, $M = 11$, and $M = 101$.
   - What happens to $P(\text{Majority})$ as $M \to \infty$ if $p > 0.5$? What happens if $p < 0.5$?
2. **Leo Breiman's Variance Decomposition**:
   - Let $f_1, f_2, \dots, f_M$ be $M$ identically distributed base predictors, each with individual prediction variance $\sigma^2$ and average pairwise correlation $\rho \in [0, 1]$.
   - The ensemble prediction is the average $\bar{f} = \frac{1}{M} \sum_{m=1}^M f_m$.
   - Prove that the ensemble variance is:
     $$\text{Var}(\bar{f}) = \rho \sigma^2 + \frac{1 - \rho}{M} \sigma^2$$
   - Evaluate the limit as $M \to \infty$:
     $$\lim_{M \to \infty} \text{Var}(\bar{f}) = \rho \sigma^2$$
   - Explain why standard Bagging (which samples only rows) hits a performance plateau when trees are correlated ($\rho > 0$), and how Random Forest's feature sub-spacing ($\sqrt{D}$) forces $\rho \downarrow$, collapsing the variance asymptote.
3. **Heterogeneous Base Estimator Experiment**:
   - On the Titanic dataset, train two meta-estimators:
     - `BaggingClassifier(base_estimator=DecisionTreeClassifier(), n_estimators=201, random_state=42)`
     - `BaggingClassifier(base_estimator=LogisticRegression(max_iter=1000), n_estimators=201, random_state=42)`
   - Compare single model vs bagged ensemble accuracy for both.
   - Why does bagging unstable, high-variance decision trees produce significant accuracy gains, while bagging stable, low-variance logistic regression yields almost zero improvement?

---

## ⚡ Case Study 4: Computational Scaling & Coordinate Descent (LinearSVR vs Kernel SVR)

### 🎯 Big-Data High-Throughput Scenario
A financial trading firm predicts real-time asset settlement spreads from continuous order book features. As transaction volume scales from $N = 1,000$ to $N = 100,000$, the algorithmic complexity of the solver dictates whether the pipeline runs in real-time or exhausts memory.

### 📝 Case Study Questions
1. **Algorithmic Complexity Analysis**:
   - Explain the difference between:
     - Libsvm (`SVR(kernel='linear')`): Solves the dual Quadratic Programming problem using Sequential Minimal Optimization (SMO), exhibiting $O(N^2 \sim N^3)$ time complexity.
     - Liblinear (`LinearSVR`): Solves the primal or dual problem using Coordinate Descent, exhibiting linear $O(N \cdot D)$ time complexity.
2. **Coordinate Descent Mechanics**:
   - For `LinearSVR(dual=False)`, when is primal optimization preferred over dual optimization?
   - Why is `dual=False` mathematically optimal when the number of samples $N$ exceeds the number of features $D$ ($N > D$)?
3. **Production Decision Matrix**:
   - Create an engineering decision matrix for deploying regression algorithms based on sample size $N$ and feature dimension $D$:
     - $N < 10,000$, non-linear relationships: which model?
     - $N > 50,000$, linear relationships, $N \gg D$: which model?
     - $N > 1,000,000$, streaming out-of-core data: which model?
