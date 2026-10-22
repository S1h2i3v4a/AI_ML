# Notes_30.02: Gradient Boosting Classifier Intuition
## Supervised Machine Learning (Part 6) — Boosting & Advanced Ensembles

### 📌 Conceptual Summary
Adapting gradient boosting to binary classification. Target $y \in \{0, 1\}$. The model operates in log-odds space $F(x) = \ln\left(\frac{p(x)}{1 - p(x)}\right)$. The probability is modeled via the sigmoid link $p(x) = \sigma(F(x)) = \frac{1}{1 + e^{-F(x)}}$. Under binary cross-entropy loss $L(y, F) = -y F + \ln(1 + e^F)$, the negative gradient is $r_{im} = y_i - p_{m-1}(x_i)$. Base trees fit these probability residuals, and leaf values are updated using Newton-Raphson approximation $\gamma_{jm} = \frac{\sum_{x_i \in R_{jm}} r_{im}}{\sum_{x_i \in R_{jm}} p_{m-1}(x_i)(1 - p_{m-1}(x_i))}$.

---

### 🛠️ Key Mathematical Formulations
- **Ensemble Hypothesis**: Sequential accumulation or weighted meta-combination.
- **Regularization**: Shrinkage learning rate, tree depth constraints, and out-of-fold validation.

---

### 💻 Code Artifacts & Reference Implementations
- Master Notebook: [`lecture_30.ipynb`](../novagen.ipynb)
- Interactive Heterogeneous Suite: [`ensemble_heterogenous.ipynb`](../ensemble_heterogenous.ipynb)
