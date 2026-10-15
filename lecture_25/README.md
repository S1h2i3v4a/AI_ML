# Lecture 25: Classification Fundamentals, Naive Bayes, kNN & Evaluation Pipelines

Welcome to **Lecture 25** of the AI/ML curriculum! This master module covers foundational classification algorithms (**Naive Bayes** and **k-Nearest Neighbors - kNN**), essential data preprocessing (**Standardization vs Normalization**), robust validation workflows (**Train-Val-Test splits, K-Fold & Stratified Cross Validation**), Scikit-Learn **Pipelines**, and rigorous **Classification Evaluation Metrics** (Confusion Matrix, Precision, Recall, Specificity, F1-Score).

---

## 1. Curriculum Architecture & Subtopic Index

The curriculum is structured into **15 comprehensive submodules**:

| Submodule | Video / Topic | Core Mathematical & Practical Concepts | Artifacts |
| :--- | :--- | :--- | :--- |
| [**Notes_25.01**](./Notes_25.01/) | **Standardization & Normalization** | Z-score scaling vs MinMax, distance distortion, mathematical definitions | `README.md`, `README_HINGLISH.md`, `lecture_25_01.ipynb` |
| [**Notes_25.02**](./Notes_25.02/) | **Using StandardScaler** | Sklearn `StandardScaler`, `fit_transform` vs `transform`, data leakage prevention | `README.md`, `README_HINGLISH.md`, `lecture_25_02.ipynb` |
| [**Notes_25.03**](./Notes_25.03/) | **Understanding Confusion Matrix** | True Positive (TP), True Negative (TN), False Positive (FP), False Negative (FN) | `README.md`, `README_HINGLISH.md`, `lecture_25_03.ipynb` |
| [**Notes_25.04**](./Notes_25.04/) | **Classification Evaluation Metrics** | Accuracy, Precision, Recall, Specificity, F1-Score, Class Imbalance dilemma | `README.md`, `README_HINGLISH.md`, `lecture_25_04.ipynb` |
| [**Notes_25.05**](./Notes_25.05/) | **Naive Bayes (Intuition)** | Bayes' Theorem, Prior $P(y)$, Likelihood, Conditional Independence assumption | `README.md`, `README_HINGLISH.md`, `lecture_25_05.ipynb` |
| [**Notes_25.06**](./Notes_25.06/) | **Naive Bayes (Example)** | Step-by-step tabular probability calculation, Zero Frequency problem, Laplace Smoothing | `README.md`, `README_HINGLISH.md`, `lecture_25_06.ipynb` |
| [**Notes_25.07**](./Notes_25.07/) | **Types of Naive Bayes** | GaussianNB (Continuous), MultinomialNB (Word counts), BernoulliNB (Binary) | `README.md`, `README_HINGLISH.md`, `lecture_25_07.ipynb` |
| [**Notes_25.08**](./Notes_25.08/) | **Naive Bayes (Code)** | Sklearn implementation, Text classification, GaussianNB on `heart.csv` | `README.md`, `README_HINGLISH.md`, `lecture_25_08.ipynb` |
| [**Notes_25.09**](./Notes_25.09/) | **kNN - K Nearest Neighbours (Intuition)** | Non-parametric lazy learner, Euclidean & Manhattan metrics, Majority voting | `README.md`, `README_HINGLISH.md`, `lecture_25_09.ipynb` |
| [**Notes_25.10**](./Notes_25.10/) | **kNN (Code)** | Sklearn `KNeighborsClassifier`, feature scaling necessity, distance weights | `README.md`, `README_HINGLISH.md`, `lecture_25_10.ipynb` |
| [**Notes_25.11**](./Notes_25.11/) | **Limitations of kNN** | Curse of Dimensionality, inference latency $\mathcal{O}(N \cdot d)$, memory footprint | `README.md`, `README_HINGLISH.md`, `lecture_25_11.ipynb` |
| [**Notes_25.12**](./Notes_25.12/) | **What is Validation Data?** | Train-Validation-Test partitioning, testing data sanctity, overfitting tuning | `README.md`, `README_HINGLISH.md`, `lecture_25_12.ipynb` |
| [**Notes_25.13**](./Notes_25.13/) | **What is Cross Validation?** | K-Fold, Stratified K-Fold for imbalanced data, variance reduction | `README.md`, `README_HINGLISH.md`, `lecture_25_13.ipynb` |
| [**Notes_25.14**](./Notes_25.14/) | **CV for Hyperparameter Tuning** | `GridSearchCV`, tuning $K$ neighbors and distance weights, validation curve | `README.md`, `README_HINGLISH.md`, `lecture_25_14.ipynb` |
| [**Notes_25.15**](./Notes_25.15/) | **Pipeline in sklearn** | Sklearn `Pipeline`, chained preprocessing & modeling, zero data leakage | `README.md`, `README_HINGLISH.md`, `lecture_25_15.ipynb` |

---

## 2. Practice Problems Suite

Located in the [**`Practice_Problems/`**](./Practice_Problems/) directory are 3 advanced production case studies:
- **Case 1:** Medical Diagnostics Clinical Triaging & Cost-Sensitive Confusion Matrix Optimization.
- **Case 2:** Bayesian Spam Filtering & Gaussian vs Multinomial Naive Bayes with Laplace Smoothing.
- **Case 3:** Metric-Space Nearest Neighbor Classification (kNN), Curse of Dimensionality & Leakage-Free Stratified K-Fold Pipeline.
