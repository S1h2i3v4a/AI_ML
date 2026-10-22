# Lecture 29: Practice Problems Suite (Solutions & Mathematical Proofs)
## Supervised Machine Learning (Part 5) — Support Vector Machines & Ensemble Learning

This manual provides verified production solutions, mathematical derivations, and systems walkthroughs for all 4 Case Studies and 8 Algorithmic Challenges in Lecture 29.

---

## 🩺 Case Study 1: Diabetes Progression Forecaster (Support Vector Regression - SVR)

### 1. Unscaled Failure Analysis
When default `SVR()` is fitted directly on the Diabetes dataset with raw continuous target $y \in [25, 346]$:
- Test $R^2$ score is only **0.1616** (almost no predictive power).
- **Mathematical Root Cause**:
  1. The SVR loss function is $L_\epsilon(y, f(\mathbf{x})) = \max(0, |y - f(\mathbf{x})| - \epsilon)$. With default $\epsilon = 0.1$, the tube width is tiny ($\pm 0.1$) compared to the range of $y$ ($321$ units), forcing virtually all data points outside the tube and saturating the slack variables $\xi_i, \xi_i^*$.
  2. The default regularization parameter $C = 1.0$ is completely inadequate to balance the penalty term $C \sum (\xi_i + \xi_i^*)$ when errors are on the order of $100^2$.

### 2. Dual Scaled Pipeline Implementation
Standardizing the target $y$ via `StandardScaler`:
$$y_{\text{scaled}} = \frac{y - \mu_y}{\sigma_y}$$
- After scaling, $y_{\text{scaled}}$ has zero mean and unit variance.
- Test $R^2$ score jumps from **0.1616 to 0.4884** (RMSE = 52.55 progression units), matching the teacher's reference benchmark in `svr_implementation_reference.ipynb`.

### 3. Support Vector Sparsity
- Inspecting `svr_scaled.support_`:
  - Exactly **269 out of 309 training samples (87.1%)** act as support vectors.
  - **Karush-Kuhn-Tucker (KKT) Complementary Slackness**:
    $$\alpha_i (|y_i - f(\mathbf{x}_i)| - \epsilon - \xi_i) = 0$$
    For any observation strictly inside the $\epsilon$-tube ($|y_i - f(\mathbf{x}_i)| < \epsilon$), the slack variable is zero ($\xi_i = 0$), forcing the Lagrange multiplier $\alpha_i = 0$. Hence, non-support vectors exert **zero influence** on the regression function $f(\mathbf{x}) = \sum (\alpha_i - \alpha_i^*) K(\mathbf{x}_i, \mathbf{x}) + b$.

---

## 🚢 Case Study 2: Titanic Survival Modeling & OOB Validation

### 1. First-Principles OOB Mathematical Derivation
Let a training dataset contain $N$ observations. A bootstrap sample of size $N$ is drawn with replacement:
1. In any single random selection, the probability of selecting a specific observation $x_i$ is $\frac{1}{N}$.
2. The probability of NOT selecting $x_i$ in that single draw is:
   $$P(\text{not selected in 1 draw}) = 1 - \frac{1}{N}$$
3. Because draws are independent, the probability that $x_i$ is omitted in all $N$ draws is:
   $$P(\text{omitted in all } N \text{ draws}) = \left(1 - \frac{1}{N}\right)^N$$
4. Taking the natural logarithm:
   $$\ln\left[\left(1 - \frac{1}{N}\right)^N\right] = N \ln\left(1 - \frac{1}{N}\right)$$
5. Using the Taylor series expansion $\ln(1 - u) = -u - \frac{u^2}{2} - \dots$ for $u = \frac{1}{N}$:
   $$N \ln\left(1 - \frac{1}{N}\right) = N \left( - \frac{1}{N} - \frac{1}{2N^2} - \dots \right) = -1 - \frac{1}{2N} - \dots$$
6. Taking the limit as $N \to \infty$:
   $$\lim_{N \to \infty} N \ln\left(1 - \frac{1}{N}\right) = -1 \implies \lim_{N \to \infty} \left(1 - \frac{1}{N}\right)^N = e^{-1} = \frac{1}{e}$$
   $$\frac{1}{e} \approx \mathbf{0.367879 \implies 36.79\%}$$
7. Consequently, the proportion of unique samples included in each bootstrap sample is:
   $$1 - \frac{1}{e} \approx \mathbf{0.632121 \implies 63.21\%}$$

### 2. Empirical Verification on Titanic Dataset
- Training `RandomForestClassifier(n_estimators=501, oob_score=True, max_depth=4)`:
  - **OOB Score**: **81.44%**.
  - **Held-Out Test Accuracy**: **82.51%**.
  - The discrepancy between OOB validation and independent test accuracy is less than **1.07%**, confirming that OOB evaluation provides an unbiased generalization estimate without requiring cross-validation.
- **Top Feature Importances (MDI)**:
  1. `sex_male`: **49.50%**
  2. `fare`: **19.39%**
  3. `pclass`: **15.79%**
  This accurately reflects the historical protocol prioritizing female passengers and premium cabin ticket holders.

---

## 👥 Case Study 3: Wisdom of Crowds & Ensemble Variance Collapse

### 1. Condorcet's Jury Theorem
For $M$ independent classifiers with individual competence $p = 0.60$:
$$P(\text{Majority}) = \sum_{k=\lfloor M/2 \rfloor + 1}^M \binom{M}{k} p^k (1 - p)^{M-k}$$
- For $M = 3$ (majority $\ge 2$):
  $$P(\text{Maj}) = \binom{3}{2}(0.6)^2(0.4) + \binom{3}{3}(0.6)^3 = 3(0.36)(0.4) + 0.216 = 0.432 + 0.216 = \mathbf{64.80\%}$$
- For $M = 11$ (majority $\ge 6$):
  $$P(\text{Maj}) = \mathbf{75.35\%}$$
- For $M = 101$ (majority $\ge 51$):
  $$P(\text{Maj}) = \mathbf{97.91\%}$$
As $M \to \infty$, $P(\text{Majority}) \to \mathbf{100.0\%}$ when $p > 0.50$.

### 2. Leo Breiman's Variance Decomposition
For $M$ estimators each with variance $\sigma^2$ and pairwise correlation $\rho$:
$$\bar{f} = \frac{1}{M}\sum_{m=1}^M f_m$$
$$\text{Var}(\bar{f}) = \frac{1}{M^2} \left[ \sum_{m=1}^M \text{Var}(f_m) + \sum_{j \neq k} \text{Cov}(f_j, f_k) \right]$$
Since $\text{Cov}(f_j, f_k) = \rho \sigma^2$ for $M(M-1)$ off-diagonal terms:
$$\text{Var}(\bar{f}) = \frac{1}{M^2} [M \sigma^2 + M(M - 1) \rho \sigma^2] = \frac{\sigma^2}{M} + \frac{M - 1}{M}\rho \sigma^2 = \mathbf{\rho \sigma^2 + \frac{1 - \rho}{M} \sigma^2}$$
- As $M \to \infty$, $\frac{1-\rho}{M}\sigma^2 \to 0$, leaving an irreducible asymptote $\rho \sigma^2$.
- In standard Bagging, base trees split on the same dominant features, keeping $\rho$ high ($\rho \approx 0.4 - 0.6$).
- In Random Forests, Leo Breiman introduced **feature sub-spacing** (selecting only $\sqrt{D}$ features at each split). This de-correlates the trees, forcing $\rho \downarrow 0.1$, collapsing the variance asymptote.

### 3. Heterogeneous Bagging Benchmark
- **Decision Tree (High-Variance Base Learner)**:
  - Single Tree: **75.34%**
  - Bagged Tree ($M=201$): **78.92%** ($\mathbf{+3.59\%}$ boost)
- **Logistic Regression (Low-Variance Base Learner)**:
  - Single Model: **78.48%**
  - Bagged Model ($M=201$): **78.48%** ($\mathbf{+0.00\%}$ boost)
- **Takeaway**: Bagging is a variance reduction technique. It delivers dramatic gains on unstable learners with high variance, but cannot improve low-variance, bias-constrained linear models.

---

## ⚡ Case Study 4: Computational Scaling Analysis (LinearSVR vs Kernel SVR)

### 1. Benchmark Results ($N = 5,000$ samples, $D = 20$ features)
- `LinearSVR(dual='auto')` via Liblinear Coordinate Descent: **3.1936s**
- `SVR(kernel='linear')` via Libsvm SMO Quadratic Programming: **56.4293s**
- **Speedup Ratio**: `LinearSVR` is **17.7x faster**!

### 2. Algorithmic Solver Dynamics
1. **Liblinear (`LinearSVR`)**: Optimizes the primal objective directly using Coordinate Descent ($O(N \cdot D)$ iterations). Each update requires only dot products in feature space, requiring no kernel matrix storage.
2. **Libsvm (`SVR`)**: Formulates the dual problem requiring an $N \times N$ Gram matrix. Even with chunking, SMO repeatedly searches for violating pairs across $N$ dual variables, scaling as $O(N^2 \sim N^3)$.

### 3. Production Deployment Matrix

| Dataset Regime | Recommended Algorithm | Solver Engine | Computational Complexity |
| :--- | :--- | :--- | :--- |
| $N < 10,000$, Non-Linear | `SVR(kernel='rbf')` | Libsvm (SMO) | $O(N^2 \cdot D)$ memory / time |
| $N > 50,000$, Linear, $N \gg D$ | `LinearSVR(dual=False)` | Liblinear (Coordinate Descent) | $O(N \cdot D)$ linear runtime |
| $N > 1,000,000$, Streaming | `SGDRegressor(loss='epsilon_insensitive')` | Pure SGD (First-Order Gradient) | $O(N \cdot D)$, online learning |
