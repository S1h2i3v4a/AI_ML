# Lecture 30.04: Gradient Boosting Classifier Ka Code Aur Evaluation Metrics [Hinglish]

[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_30_04.ipynb)
[![English Notes](https://img.shields.io/badge/Notes-English-blue.svg)](README.md)
[![English PDF](https://img.shields.io/badge/PDF-English-red.svg)](notes.pdf)
[![Hinglish PDF](https://img.shields.io/badge/PDF-Hinglish-green.svg)](notes_hinglish.pdf)

---

## 📌 Topic Overview
Practical implementation of GradientBoostingClassifier in scikit-learn. Generating binary classification datasets with make_classification, model training, accuracy evaluation, and classification report analysis.


---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- `make_classification` se binary classification dataset generate karna.
- `GradientBoostingClassifier` ko import aur train karna.
- Model Hyperparameters: `n_estimators=150`, `learning_rate=0.1`, `max_depth=3`.
- `accuracy_score`, **Confusion Matrix**, aur **Classification Report** se evaluate karna.
- Model ki predicted probabilities (`predict_proba`) ka distribution samajhna.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation
- **Classification Dataset**: `make_classification(n_samples=1000, n_features=10, n_informative=5, random_state=42)` se binary target dataset create kiya gaya.

- **Data Splitting**: `test_size=0.3` (30% test set, 70% training set) aur `random_state=42` ke sath split kiya gaya.

- **Classifier Setup**: `GradientBoostingClassifier(n_estimators=150, learning_rate=0.1, max_depth=3, random_state=42)` banaya gaya.

- **Training**: `clf.fit(X_train, y_train)` se sequential boosting stages execute kiye gaye.

- **Accuracy Score**: `accuracy_score(y_test, y_pred)` se model ne test data par high accuracy achieve ki.

- **Classification Report**: Precision, Recall, aur F1-Score inspect karke verify kiya gaya ki dono classes balanced way mein predict ho rahi hain.

---

### 📊 Visual Flowchart / Diagram

```mermaid
flowchart TD
    A["make_classification(1000 samples, 2 classes)"] --> B["Train-Test Split (70/30)"]
    B --> C["GradientBoostingClassifier(n_estimators=150, lr=0.1)"]
    C --> D["Fit on Training Set"]
    D --> E["Predict on Test Set: y_pred & predict_proba"]
    E --> F["Metrics: Accuracy, Precision, Recall, F1-Score"]
```

---

### 🔢 Mathematical Derivation

Classification accuracy score formulation:

$$
\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}
$$

Binary cross-entropy loss evaluated across test samples:

$$
\text{Log-Loss} = -\frac{1}{N} \sum_{i=1}^N \left[ y_i \ln(p_i) + (1 - y_i) \ln(1 - p_i) \right]
$$

---

### 💻 Standalone Python Code & Verification
Iss module ka complete runnable code [Jupyter Notebook](lecture_30_04.ipynb) mein available hai.
