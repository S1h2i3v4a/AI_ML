# Lecture 24: Advanced Regression, Regularization & Logistic Regression

Welcome to **Lecture 24** of the AI/ML curriculum. This masterclass bridges classical linear regression to robust regularized models and probabilistic classification, establishing the mathematical foundations, optimization theory, and production implementations of **Feature Engineering, Regularization (Lasso, Ridge, ElasticNet)**, and **Logistic Regression**.

---

## 1. Curriculum Architecture & Subtopic Index

This module is partitioned into 15 comprehensive, self-contained subtopics mapping 1-to-1 with the course lectures:

| Submodule | Topic | Core Focus & Mathematical Concept | Key Artifacts |
| :--- | :--- | :--- | :--- |
| [**Notes_24.01**](./Notes_24.01/) | **Feature Engineering: Encoding** | Nominal vs Ordinal, Label Encoding, One-Hot Encoding orthogonal basis | `README.md`, `README_HINGLISH.md`, `lecture_24_01.ipynb` |
| [**Notes_24.02**](./Notes_24.02/) | **The Dummy Variable Trap** | Perfect multicollinearity, singular matrix $\det(\mathbf{X}^T \mathbf{X}) = 0$, $K-1$ rule | `README.md`, `README_HINGLISH.md`, `lecture_24_02.ipynb` |
| [**Notes_24.03**](./Notes_24.03/) | **Other Feature Engineering Techniques**| Z-score standardization vs MinMax normalization, Binning, Polynomial interactions | `README.md`, `README_HINGLISH.md`, `lecture_24_03.ipynb` |
| [**Notes_24.04**](./Notes_24.04/) | **Overfitting (High Variance)** | Memorizing noise, Bias-Variance decomposition $\text{Bias}^2 + \text{Var} + \sigma^2$, generalization gap | `README.md`, `README_HINGLISH.md`, `lecture_24_04.ipynb` |
| [**Notes_24.05**](./Notes_24.05/) | **Underfitting (High Bias)** | Oversimplified hypothesis space, inability to capture non-linear structure | `README.md`, `README_HINGLISH.md`, `lecture_24_05.ipynb` |
| [**Notes_24.06**](./Notes_24.06/) | **Fixing Underfit & Overfit** | Engineering playbook: Regularization, feature pruning, polynomial expansion | `README.md`, `README_HINGLISH.md`, `lecture_24_06.ipynb` |
| [**Notes_24.07**](./Notes_24.07/) | **Diagnostic Learning Curves** | Training size $m$ vs loss curves, plateau analysis, cross-validation diagnostics | `README.md`, `README_HINGLISH.md`, `lecture_24_07.ipynb` |
| [**Notes_24.08**](./Notes_24.08/) | **Regularization: Lasso (L1)** | $J = MSE + \lambda \|\mathbf{w}\|_1$, geometric diamond constraint, automatic sparsity | `README.md`, `README_HINGLISH.md`, `lecture_24_08.ipynb` |
| [**Notes_24.09**](./Notes_24.09/) | **Regularization: Ridge (L2)** | $J = MSE + \frac{\lambda}{2} \|\mathbf{w}\|_2^2$, Normal Equation $(\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^T \mathbf{y}$ | `README.md`, `README_HINGLISH.md`, `lecture_24_09.ipynb` |
| [**Notes_24.10**](./Notes_24.10/) | **Lasso Implementation & Paths** | Hands-on `insurance.csv`, tracing coefficient shrinkage paths across $\alpha$ | `README.md`, `README_HINGLISH.md`, `lecture_24_10.ipynb` |
| [**Notes_24.11**](./Notes_24.11/) | **Using LassoCV** | K-Fold cross-validated hyperparameter search for optimal regularizer $\alpha^*$ | `README.md`, `README_HINGLISH.md`, `lecture_24_11.ipynb` |
| [**Notes_24.12**](./Notes_24.12/) | **ElasticNet Overview** | Hybrid convex combination $MSE + \alpha [\rho \|\mathbf{w}\|_1 + \frac{1-\rho}{2} \|\mathbf{w}\|_2^2]$, grouping effect | `README.md`, `README_HINGLISH.md`, `lecture_24_12.ipynb` |
| [**Notes_24.13**](./Notes_24.13/) | **Logistic Regression Intuition** | Odds $\frac{p}{1-p}$, Logit $\ln(\text{Odds})$, Sigmoid function $\sigma(z) = \frac{1}{1 + e^{-z}}$ | `README.md`, `README_HINGLISH.md`, `lecture_24_13.ipynb` |
| [**Notes_24.14**](./Notes_24.14/) | **Logistic Regression Cost Function**| MLE derivation of Binary Cross-Entropy $J = -\frac{1}{m} \sum [y \ln \hat{y} + (1-y) \ln(1-\hat{y})]$ | `README.md`, `README_HINGLISH.md`, `lecture_24_14.ipynb` |
| [**Notes_24.15**](./Notes_24.15/) | **Classification Code & Metrics** | Clinical `heart.csv` pipeline, Confusion Matrix, Precision, Recall, F1, ROC-AUC | `README.md`, `README_HINGLISH.md`, `lecture_24_15.ipynb` |

---

## 2. Core Theoretical Mathematical Formulations

### 1. The Regularization Taxonomy

```
                       Regularized Objective Functions
                                      |
         +----------------------------+----------------------------+
         |                                                         |
         v                                                         v
   Lasso Regression (L1)                                     Ridge Regression (L2)
   J = MSE + \lambda \sum |w_j|                              J = MSE + (\lambda / 2) \sum w_j^2
   * Diamond constraint (sharp corners)                      * Spherical constraint (smooth)
   * Drives coefficients strictly to ZERO                    * Shrinks coefficients toward zero
   * Built-in Feature Selection                              * Inverts ill-conditioned matrices
```

### 2. The Logistic Hypothesis & Maximum Likelihood Estimation (MLE)
For binary classification $y \in \{0, 1\}$, the parameterized hypothesis produces calibrated probabilities:

$$
\hat{y} = P(y = 1 \mid \mathbf{x}) = \sigma(\mathbf{w}^T \mathbf{x} + b) = \frac{1}{1 + e^{-(\mathbf{w}^T \mathbf{x} + b)}}
$$

The cost function is the Negative Log-Likelihood of the Bernoulli process:

$$
J(\mathbf{w}, b) = -\frac{1}{m} \sum_{i=1}^m \left[ y^{(i)} \ln \hat{y}^{(i)} + (1 - y^{(i)}) \ln(1 - \hat{y}^{(i)}) \right]
$$

---

## 3. Production Practice Problems & Datasets

Inside [**`Practice_Problems/`**](./Practice_Problems/), you will find:
1. **Case Study 1 (Bias-Variance Tradeoff & Model Complexity):** Polynomial model degree tuning ($d = 1, 3, 14$) and learning curve diagnostics.
2. **Case Study 2 (Regularization Shrinkage Paths):** Comparing Lasso (L1) vs Ridge (L2) coefficient trajectories across $\alpha$ on `insurance.csv`.
3. **Case Study 3 (Logistic Regression Decision Boundary & Clinical Metrics):** Visualizing the Sigmoid decision boundary hyperplane and evaluating clinical diagnostics on `heart.csv` (ROC curve, AUC, Confusion Matrix).
