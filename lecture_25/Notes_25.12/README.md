# Notes_25.12: What is Validation Data?

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_25_12.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Lecture 25 Overview](../README.md)

---

## 📌 Executive Summary
Train-Validation-Test 3-way split, hyperparameter tuning without test set contamination.

---

## 🎯 Mathematical Formulations

Three-Way Data Partition Architecture:

$$
\mathcal{D} = \mathcal{D}_{\text{train}} \cup \mathcal{D}_{\text{val}} \cup \mathcal{D}_{\text{test}}, \qquad \mathcal{D}_{\text{train}} \cap \mathcal{D}_{\text{val}} = \emptyset, \; \mathcal{D}_{\text{val}} \cap \mathcal{D}_{\text{test}} = \emptyset
$$

Standard Split Ratios:

$$
\text{Train: } 60-70\%, \qquad \text{Validation: } 15-20\%, \qquad \text{Test: } 15-20\%
$$

---

## 💡 Conceptual Principles & Architecture

### Test Set Ko Chhuna Mana Hai!
- **Training Data:** Model ke weights aur parameters ko train karne ke liye.
- **Validation Data:** Hyperparameters tune karne ke liye (jaise kNN mein best $K$ choose karna, Decision tree ki depth tune karna).
- **Test Data:** Final unbiased evaluation report card. Test data par kabhi koi parameter ya hyperparameter tune nahi kiya jata!

---

## 💻 Python Production Implementation

```python
from sklearn.model_selection import train_test_split
import numpy as np

X = np.random.randn(1000, 10)
y = np.random.randint(0, 2, 1000)

# Step 1: Split into Train (70%) and Temp (30%)
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, random_state=42)

# Step 2: Split Temp into Validation (15%) and Test (15%)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42)

print(f"Train Shape: {X_train.shape}, Val Shape: {X_val.shape}, Test Shape: {X_test.shape}")
```
