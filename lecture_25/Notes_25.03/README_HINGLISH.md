# Notes_25.03: Confusion Matrix Ko Samjhein (TP, TN, FP, FN) [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_25_03.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 25 Overview](../README_HINGLISH.md)

---

## 📌 Executive Summary
Binary classification ki Confusion Matrix, Type I aur Type II errors ka intuition.

---

## 🎯 Mathematical Formulations

Confusion Matrix Table:

$$
\begin{array}{c|cc}
& \text{Predicted Negative (0)} & \text{Predicted Positive (1)} \\
\hline
\text{Actual Negative (0)} & \text{True Negative (TN)} & \text{False Positive (FP) [Type I Error]} \\
\text{Actual Positive (1)} & \text{False Negative (FN) [Type II Error]} & \text{True Positive (TP)}
\end{array}
$$

---

## 💡 Concept Intuition & Key Insights (Desi Style)

### 4 Outcomes Ka Desi Matlab:
1. **True Positive (TP):** Mareez ko bimaari thi, aur model ne bhi bola bimaari hai (Sahi pakda!).
2. **True Negative (TN):** Insaan bilkul healthy tha, aur model ne bola healthy hai (Sahi chhora!).
3. **False Positive (FP - Type I Error):** Insaan healthy tha, lekin model ne jhootha alarm baja diya ki bimaari hai.
4. **False Negative (FN - Type II Error):** Mareez ko bimaari thi, lekin model ne bol diya ki healthy hai. (Medical field mein yeh sabse zyada deadly aur khatarnak error hota hai!).

---

## 💻 Python Production Implementation

```python
from sklearn.metrics import confusion_matrix
import numpy as np

y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])
y_pred = np.array([1, 0, 1, 0, 0, 1, 1, 0, 1, 0])

cm = confusion_matrix(y_true, y_pred)
tn, fp, fn, tp = cm.ravel()

print("Confusion Matrix:\n", cm)
print(f"TP: {tp}, TN: {tn}, FP: {fp}, FN: {fn}")
```
