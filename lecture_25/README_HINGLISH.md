# Lecture 25: Classification Fundamentals, Naive Bayes, kNN & Evaluation Pipelines [Hinglish]

AI/ML curriculum ke **Lecture 25** mein aapka swagat hai! Is comprehensive module mein hum machine learning ke do sabse intuitive aur foundational classification algorithms (**Naive Bayes** aur **k-Nearest Neighbours - kNN**), unki data preprocessing requirements (**Standardization vs Normalization**), model validation techniques (**Train-Validation-Test, K-Fold Cross Validation**), Scikit-Learn **Pipelines**, aur rigorous **Classification Evaluation Metrics** (Confusion Matrix, Precision, Recall, F1-Score) ko master karenge.

---

## 1. Curriculum Architecture & Subtopic Index

Is pure module ko **15 structured submodules** mein divide kiya gaya hai:

| Submodule | Video / Topic | Mukhya Concepts | Artifacts |
| :--- | :--- | :--- | :--- |
| [**Notes_25.01**](./Notes_25.01/) | **Standardization & Normalization** | Z-score scaling vs MinMax, distance distortion, mathematical definitions | `README.md`, `README_HINGLISH.md`, `lecture_25_01.ipynb` |
| [**Notes_25.02**](./Notes_25.02/) | **Using StandardScaler** | Sklearn `StandardScaler`, `fit_transform` vs `transform`, data leakage prevention | `README.md`, `README_HINGLISH.md`, `lecture_25_02.ipynb` |
| [**Notes_25.03**](./Notes_25.03/) | **Understanding Confusion Matrix** | True Positive (TP), True Negative (TN), False Positive (FP), False Negative (FN) | `README.md`, `README_HINGLISH.md`, `lecture_25_03.ipynb` |
| [**Notes_25.04**](./Notes_25.04/) | **Classification Evaluation Metrics** | Accuracy, Precision, Recall, Specificity, F1-Score, Class Imbalance dilemma | `README.md`, `README_HINGLISH.md`, `lecture_25_04.ipynb` |
| [**Notes_25.05**](./Notes_25.05/) | **Naive Bayes (Intuition)** | Bayes' Theorem, Prior $P(y)$, Likelihood, Conditional Independence assumption | `README.md`, `README_HINGLISH.md`, `lecture_25_05.ipynb` |
| [**Notes_25.06**](./Notes_25.06/) | **Naive Bayes (Example)** | Step-by-step tabular probability calculation, Zero Frequency problem, Laplace Smoothing | `README.md`, `README_HINGLISH.md`, `lecture_25_06.ipynb` |
| [**Notes_25.07**](./Notes_25.07/) | **Types of Naive Bayes** | GaussianNB (Continuous), MultinomialNB (Word counts), BernoulliNB (Binary) | `README.md`, `README_HINGLISH.md`, `lecture_25_07.ipynb` |
| [**Notes_25.08**](./Notes_25.08/) | **Naive Bayes (Code)** | Sklearn implementation, Text classification, GaussianNB on `heart.csv` | `README.md`, `README_HINGLISH.md`, `lecture_25_08.ipynb` |
| [**Notes_25.09**](./Notes_25.09/) | **kNN - K Nearest Neighbours (Intuition)** | Non-parametric lazy learner, Euclidean & Manhattan metrics, Majority voting | [Notes](./Notes_25.09/README.md) \| [Hinglish](./Notes_25.09/README_HINGLISH.md) \| [PDF](./Notes_25.09/notes.pdf) \| [Hinglish PDF](./Notes_25.09/notes_hinglish.pdf) \| [Notebook](./Notes_25.09/lecture_25_09.ipynb) |
| [**Notes_25.10**](./Notes_25.10/) | **kNN (Code)** | Sklearn `KNeighborsClassifier`, feature scaling necessity, distance weights | [Notes](./Notes_25.10/README.md) \| [Hinglish](./Notes_25.10/README_HINGLISH.md) \| [PDF](./Notes_25.10/notes.pdf) \| [Hinglish PDF](./Notes_25.10/notes_hinglish.pdf) \| [Notebook](./Notes_25.10/lecture_25_10.ipynb) |
| [**Notes_25.11**](./Notes_25.11/) | **Limitations of kNN** | Curse of Dimensionality, inference latency $\mathcal{O}(N \cdot d)$, memory footprint | `README.md`, `README_HINGLISH.md`, `lecture_25_11.ipynb` |
| [**Notes_25.12**](./Notes_25.12/) | **What is Validation Data?** | Train-Validation-Test partitioning, testing data sanctity, overfitting tuning | `README.md`, `README_HINGLISH.md`, `lecture_25_12.ipynb` |
| [**Notes_25.13**](./Notes_25.13/) | **What is Cross Validation?** | K-Fold, Stratified K-Fold for imbalanced data, variance reduction | `README.md`, `README_HINGLISH.md`, `lecture_25_13.ipynb` |
| [**Notes_25.14**](./Notes_25.14/) | **CV for Hyperparameter Tuning** | `GridSearchCV`, tuning $K$ neighbors and distance weights, validation curve | `README.md`, `README_HINGLISH.md`, `lecture_25_14.ipynb` |
| [**Notes_25.15**](./Notes_25.15/) | **Pipeline in sklearn** | Sklearn `Pipeline`, chained preprocessing & modeling, zero data leakage | `README.md`, `README_HINGLISH.md`, `lecture_25_15.ipynb` |

---

## 2. Practice Problems Suite

Module ke andar [**`Practice_Problems/`**](./Practice_Problems/) folder mein 3 advanced production case studies included hain:
- **Case 1:** Medical Diagnostics Clinical Triaging & Cost-Sensitive Confusion Matrix Optimization.
- **Case 2:** Bayesian Spam Filtering & Gaussian vs Multinomial Naive Bayes with Laplace Smoothing.
- **Case 3:** Metric-Space Nearest Neighbor Classification (kNN), Curse of Dimensionality & Leakage-Free Stratified K-Fold Pipeline.
