# Lecture 24: Regularization & Logistic Regression — Practice Problems (Hinglish)

Ye practice problem suite aapko first-principles mathematical derivations, numerical optimization, regularization mechanics aur clinical classification ke 3 in-depth engineering case studies solve karne ke liye challenge karti hai.

---

## Case Study 1: Bias-Variance Tradeoff Aur Model Complexity Dynamics

### Context
Ek non-linear physical process ka data generate hota hai:

$$
y = \cos(1.5 \pi x) + \epsilon, \quad \epsilon \sim \mathcal{N}(0, 0.18^2)
$$

### Questions:
1. Polynomial regression ke 3 models ($d = 1, 4, 14$) formulate karein.
2. Vandermonde matrix se teeno models ke parameters calculate karein.
3. Polynomial degree $1$ se $14$ tak Training MSE aur Test MSE calculate karein.
4. U-shaped generalization curve se identify karein ki kaun sa model Underfitting (High Bias) hai, kaun sa Overfitting (High Variance) hai, aur optimal degree $d^*$ kya hai.

---

## Case Study 2: Lasso (L1) vs Ridge (L2) Regularization Paths Aur Sparsity Proof

### Context
8 features ka dataset hai jisme pehle 3 features real hain aur baaki 5 features pure random Gaussian noise hain:

$$
y = 4.5 x_1 - 3.8 x_2 + 2.5 x_3 + 0 \cdot x_4 + \dots + 0 \cdot x_8 + \epsilon
$$

### Questions:
1. Ridge (L2) aur Lasso (L1) ke loss function formulas likhein.
2. Ridge ka closed-form formula $(\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^T \mathbf{y}$ calculate karein.
3. $\lambda \in [10^{-2}, 10^3]$ par dono models ke coefficient shrinkage paths plot karein.
4. Prove karein ki Lasso noise features ($x_4, \dots, x_8$) ko exactly zero ($0.0$) kar deta hai jabki Ridge sirf shrink karta hai par zero nahi karta.

---

## Case Study 3: Logistic Regression Decision Boundary Aur Clinical Metrics (`heart.csv`)

### Context
Heart disease ($y=1$) predict karne ke liye do clinical features use kiye gaye hain: Age ($x_1$) aur Max Heart Rate ($x_2$).

### Questions:
1. Sigmoid hypothesis $\sigma(\mathbf{w}^T \mathbf{x} + b)$ formulate karein.
2. $p = 0.5$ threshold par linear decision boundary line ki equation derive karein.
3. Confusion Matrix construct karke Accuracy, Precision, Recall, Specificity aur F1-Score calculate karein.
4. ROC Curve plot karein aur Area Under Curve (ROC-AUC) score nikaalein.
