# Lecture 24: Regularization & Logistic Regression — Practice Problem Suite

This production practice problem suite challenges you to apply first-principles mathematical derivations, numerical optimization, regularization mechanics, and clinical classification evaluation across 3 in-depth engineering case studies.

---

## Case Study 1: The Bias-Variance Tradeoff & Model Complexity Dynamics

### Theoretical Context
A continuous physical process generates observations governed by the non-linear relationship:

$$
y = \cos(1.5 \pi x) + \epsilon, \quad \epsilon \sim \mathcal{N}(0, \sigma^2)
$$

Where $x \in [0, 1]$ and noise standard deviation $\sigma = 0.18$. We collect an empirical training set of $m = 25$ noisy observations.

### Problem Statements:
1. **Hypothesis Formulation:** Formulate polynomial regression hypotheses of degree $d \in \{1, 4, 14\}$:
   $$
   \hat{y} = \sum_{k=0}^d w_k x^k
   $$
2. **Analytical Ordinary Least Squares:** Solve the Vandermonde matrix normal equations to compute parameters $\mathbf{w}$ for each degree.
3. **Generalization Diagnostics:** Compute both the empirical Training Mean Squared Error and Test Generalization Error on an independent grid of 200 points across degrees $d \in [1, 14]$.
4. **Bias-Variance Identification:** Identify which degree exhibits High Bias (Underfitting), which exhibits High Variance (Overfitting), and determine the optimal complexity $d^*$ minimizing expected test risk.

---

## Case Study 2: Lasso (L1) vs. Ridge (L2) Regularization Paths & Sparsity Proof

### Theoretical Context
Consider a high-dimensional feature matrix $\mathbf{X} \in \mathbb{R}^{m \times 8}$ ($m = 120$) where only the first 3 features possess true causal relationships with target $y$, while features $x_4, \dots, x_8$ are pure standard Gaussian noise columns:

$$
y = 4.5 x_1 - 3.8 x_2 + 2.5 x_3 + 0 \cdot x_4 + \dots + 0 \cdot x_8 + \epsilon
$$

### Problem Statements:
1. **Regularized Objectives:** Formulate the objective loss functions for Ridge (L2) and Lasso (L1):
   $$
   J_{\text{Ridge}}(\mathbf{w}) = \frac{1}{2m} \|\mathbf{X} \mathbf{w} - \mathbf{y}\|_2^2 + \frac{\lambda}{2} \|\mathbf{w}\|_2^2
   $$
   $$
   J_{\text{Lasso}}(\mathbf{w}) = \frac{1}{2m} \|\mathbf{X} \mathbf{w} - \mathbf{y}\|_2^2 + \lambda \|\mathbf{w}\|_1
   $$
2. **Ridge Analytical Solution:** Express and compute the Ridge closed-form solution $(\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^T \mathbf{y}$ across logarithmic penalties $\lambda \in [10^{-2}, 10^3]$.
3. **Lasso Coordinate Descent:** Trace the Lasso parameter shrinkage trajectory across the same penalty domain.
4. **Sparsity & Selection Proof:** Demonstrate empirically why Lasso sets the weights of noise variables $x_4, \dots, x_8$ strictly to zero ($w_j = 0.0$), while Ridge retains non-zero asymptotic magnitudes.

---

## Case Study 3: Logistic Regression Decision Boundary & Clinical Diagnostics on `heart.csv`

### Theoretical Context
A clinical cardiology department seeks to predict whether a patient has coronary heart disease ($y = 1$) or is healthy ($y = 0$) using standardized biometric indicators: Age ($x_1$) and Maximum Heart Rate Achieved ($x_2$).

### Problem Statements:
1. **The Logit & Sigmoid Hypothesis:** Formulate the probabilistic prediction:
   $$
   P(y = 1 \mid \mathbf{x}) = \sigma(\mathbf{w}^T \mathbf{x} + b) = \frac{1}{1 + e^{- (w_1 x_1 + w_2 x_2 + b)}}
   $$
2. **Decision Boundary Geometry:** Derive the mathematical equation of the linear decision boundary corresponding to the standard probability threshold $\tau = 0.5$.
3. **Contingency Evaluation:** Given test predictions, construct the $2 \times 2$ Confusion Matrix and compute:
   - Accuracy
   - Precision (Positive Predictive Value)
   - Recall / Sensitivity (True Positive Rate)
   - Specificity (True Negative Rate)
   - F1-Score (Harmonic Mean)
4. **ROC & Discrimination:** Derive the Receiver Operating Characteristic (ROC) curve across varying classification thresholds and compute the Area Under Curve (ROC-AUC).
