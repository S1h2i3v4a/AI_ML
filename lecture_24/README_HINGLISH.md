# Lecture 24: Advanced Regression, Regularization & Logistic Regression (Hinglish)

AI/ML curriculum ke **Lecture 24** mein aapka swagat hai! Is masterclass mein hum simple linear regression se aage badhkar high-performance regularized models aur probabilistic classification ko master karte hain: **Feature Engineering, Regularization (Lasso, Ridge, ElasticNet)**, aur **Logistic Regression**.

---

## 1. Curriculum Architecture & Subtopic Index

Is pure module ko 15 comprehensive submodules mein divide kiya gaya hai:

| Submodule | Topic | Mukhya Concept | Artifacts |
| :--- | :--- | :--- | :--- |
| [**Notes_24.01**](./Notes_24.01/) | **Feature Engineering: Encoding** | Nominal vs Ordinal data, Label Encoding, One-Hot Encoding | `README.md`, `README_HINGLISH.md`, `lecture_24_01.ipynb` |
| [**Notes_24.02**](./Notes_24.02/) | **Dummy Variable Trap** | Perfect multicollinearity, non-invertible matrix, $K-1$ rule (`drop_first=True`) | `README.md`, `README_HINGLISH.md`, `lecture_24_02.ipynb` |
| [**Notes_24.03**](./Notes_24.03/) | **Other Feature Engineering** | StandardScaler vs MinMaxScaler, Binning, Interaction features ($x_1 \times x_2$) | `README.md`, `README_HINGLISH.md`, `lecture_24_03.ipynb` |
| [**Notes_24.04**](./Notes_24.04/) | **Overfitting (High Variance)** | Noise memorize karna, High Variance, Generalization gap explosion | `README.md`, `README_HINGLISH.md`, `lecture_24_04.ipynb` |
| [**Notes_24.05**](./Notes_24.05/) | **Underfitting (High Bias)** | Model ka bohot simple hona, non-linear pattern na sikh pana | `README.md`, `README_HINGLISH.md`, `lecture_24_05.ipynb` |
| [**Notes_24.06**](./Notes_24.06/) | **Fixing Underfit & Overfit** | Playbook: Regularization lagana, features drop karna, capacity badhana | `README.md`, `README_HINGLISH.md`, `lecture_24_06.ipynb` |
| [**Notes_24.07**](./Notes_24.07/) | **Learning Curves Diagnostics** | Training size $m$ vs loss curves se underfit/overfit pehchanna | `README.md`, `README_HINGLISH.md`, `lecture_24_07.ipynb` |
| [**Notes_24.08**](./Notes_24.08/) | **Lasso Regression (L1)** | $J = MSE + \lambda \|\mathbf{w}\|_1$, Diamond geometry, automatic feature selection | `README.md`, `README_HINGLISH.md`, `lecture_24_08.ipynb` |
| [**Notes_24.09**](./Notes_24.09/) | **Ridge Regression (L2)** | $J = MSE + \frac{\lambda}{2} \|\mathbf{w}\|_2^2$, Closed-form formula $(\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^T \mathbf{y}$ | `README.md`, `README_HINGLISH.md`, `lecture_24_09.ipynb` |
| [**Notes_24.10**](./Notes_24.10/) | **Lasso Implementation & Paths** | `insurance.csv` par scaling, coefficient shrinkage path visualize karna | `README.md`, `README_HINGLISH.md`, `lecture_24_10.ipynb` |
| [**Notes_24.11**](./Notes_24.11/) | **Using LassoCV** | K-Fold Cross Validation se automatic best $\alpha^*$ choose karna | `README.md`, `README_HINGLISH.md`, `lecture_24_11.ipynb` |
| [**Notes_24.12**](./Notes_24.12/) | **ElasticNet Overview** | Hybrid L1 + L2 penalty, `l1_ratio` mixing, correlated feature groups | `README.md`, `README_HINGLISH.md`, `lecture_24_12.ipynb` |
| [**Notes_24.13**](./Notes_24.13/) | **Logistic Regression Intuition** | Odds $\frac{p}{1-p}$, Logit function, Sigmoid curve $\sigma(z) = \frac{1}{1 + e^{-z}}$ | `README.md`, `README_HINGLISH.md`, `lecture_24_13.ipynb` |
| [**Notes_24.14**](./Notes_24.14/) | **Logistic Regression Cost Function**| MLE se Binary Cross-Entropy $J = -\frac{1}{m} \sum [y \ln \hat{y} + (1-y) \ln(1-\hat{y})]$ | `README.md`, `README_HINGLISH.md`, `lecture_24_14.ipynb` |
| [**Notes_24.15**](./Notes_24.15/) | **Classification Code & Metrics** | Real `heart.csv` par Confusion Matrix, Precision, Recall, F1, ROC-AUC | `README.md`, `README_HINGLISH.md`, `lecture_24_15.ipynb` |

---

## 2. Practice Problems Suite

Module ke andar [**`Practice_Problems/`**](./Practice_Problems/) folder mein production case studies included hain:
- **Case 1:** Polynomial Degree Bias-Variance Tradeoff aur Learning Curves.
- **Case 2:** Lasso vs Ridge Regularization Shrinkage Paths.
- **Case 3:** Logistic Regression Decision Boundary, ROC Curve aur Confusion Matrix.
