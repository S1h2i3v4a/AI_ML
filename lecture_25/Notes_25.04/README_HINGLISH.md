# Notes_25.04: Classification Metrics: Accuracy, Precision, Recall, F1 [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_25_04.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 25 Overview](../README_HINGLISH.md)

---

## 📌 Executive Summary
Accuracy paradox, Precision vs Recall trade-off, aur F1-Score ki zaroorat.

---

## 🎯 Mathematical Formulations

Classification Metric Equations:

$$
\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}
$$

$$
\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}, \qquad \text{Recall (Sensitivity)} = \frac{\text{TP}}{\text{TP} + \text{FN}}
$$

$$
\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2\text{TP}}{2\text{TP} + \text{FP} + \text{FN}}
$$

---

## 💡 Concept Intuition & Key Insights (Desi Style)

### Accuracy Paradox (Accuracy Dhoka Kyu Deti Hai?):
Maan lijiye $1000$ logo mein se sirf $5$ logo ko cancer hai ($99.5\%$ negative class). Agar model bina soche sabhi ko 'Negative' bol de, toh model ki Accuracy $99.5\%$ hogi! Lekin asal mein cancer wale saare $5$ mareez mar jayenge. Isliye Imbalanced data mein Accuracy useless hoti hai.

### Precision vs Recall Kab Use Karein?
- **High Recall Zaroori:** Medical diagnosis (Cancer detection) ya Fraud detection mein. Hum ek bhi positive patient chhod nahi sakte (FN minimize karna hai).
- **High Precision Zaroori:** YouTube recommendations, Spam filters, ya Job applicant screening mein. Agar koi email genuine hai toh woh Spam folder mein nahi jaani chahiye (FP minimize karna hai).

---

## 💻 Python Production Implementation

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

print(f"Accuracy  : {accuracy_score(y_true, y_pred):.4f}")
print(f"Precision : {precision_score(y_true, y_pred):.4f}")
print(f"Recall    : {recall_score(y_true, y_pred):.4f}")
print(f"F1-Score  : {f1_score(y_true, y_pred):.4f}")
```
