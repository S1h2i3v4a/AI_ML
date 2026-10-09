# Module 24.15: Logistic Regression Implementation & Evaluation

## 1. End-to-End Classification Pipeline (Heart Disease Dataset)

We execute an end-to-end binary classification model using the clinical `heart.csv` dataset to predict the presence of heart disease ($y \in \{0, 1\}$).

```
+------------------------------------------------------------------------------------+
| 1. Ingestion: Inspect 303 medical records (13 clinical features, target 'target')  |
| 2. Train-Test Split: 80% Train, 20% Test (stratified split)                        |
| 3. Feature Scaling: StandardScaler() on continuous predictors                      |
| 4. Model Training: LogisticRegression(max_iter=1000)                               |
| 5. Evaluation: Confusion Matrix, Precision, Recall, F1-Score, ROC-AUC              |
+------------------------------------------------------------------------------------+
```

---

## 2. The Confusion Matrix

Binary classification evaluation partitions predictions into a $2 \times 2$ contingency matrix:

```
                      Actual Positive (y = 1)        Actual Negative (y = 0)
Predicted Positive       True Positive (TP)             False Positive (FP) (Type I Error)
Predicted Negative       False Negative (FN) (Type II)  True Negative (TN)
```

---

## 3. Core Classification Metrics

### 1. Accuracy
$$
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
$$
- Misleading on imbalanced datasets (e.g., in fraud detection where 99.9% of transactions are legitimate).

### 2. Precision (Positive Predictive Value)
$$
\text{Precision} = \frac{TP}{TP + FP}
$$
- "Out of all patients predicted to have disease, how many actually had it?"
- Critical when False Positives are costly (e.g., Spam detection).

### 3. Recall / Sensitivity (True Positive Rate)
$$
\text{Recall} = \frac{TP}{TP + FN}
$$
- "Out of all patients who genuinely had disease, how many did the model catch?"
- Critical when False Negatives are fatal (e.g., Cancer / Heart disease diagnosis).

### 4. F1-Score (Harmonic Mean)
$$
\text{F1} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
$$
- Penalizes models that achieve high precision at the expense of terrible recall.

### 5. ROC Curve & AUC Score
- **ROC Curve:** Plots True Positive Rate (Recall) vs False Positive Rate ($\text{FPR} = \frac{FP}{FP + TN}$) across all classification thresholds $\tau \in [0, 1]$.
- **AUC (Area Under Curve):** Quantifies ranking discrimination capability ($AUC = 1.0$ is perfect; $0.5$ is random guessing).
