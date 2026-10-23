# NovaGen Research Labs — Clinical Drug Trial Toxicity & Patient Outcome Classification

[![Project](https://img.shields.io/badge/Project-NovaGen%20Labs-blue.svg)](#)
[![Notebook](https://img.shields.io/badge/Notebook-novagen.ipynb-orange.svg?logo=jupyter&logoColor=white)](novagen.ipynb)
[![Dataset](https://img.shields.io/badge/Dataset-novagen__dataset.csv-green.svg)](novagen_dataset.csv)
[![Assignment PDF](https://img.shields.io/badge/PDF-Assignment5-red.svg)](Supervised%20ML%20_Assignment5.pdf)

---

## 📌 Project Overview
NovaGen Research Labs conducts clinical drug efficacy and toxicity trials. This capstone project builds an end-to-end supervised machine learning pipeline to classify patient risk profiles and therapeutic response under medication.

The project demonstrates baseline modeling, multi-model benchmarking (**Logistic Regression**, **K-Nearest Neighbors**, **Random Forest**, **Gradient Boosting**), and building a final **Voting Ensemble** to achieve maximum clinical sensitivity and accuracy.

---

## 📂 Project Assets
- **Jupyter Notebook**: [`novagen.ipynb`](novagen.ipynb) — Fully runnable end-to-end benchmark notebook.
- **Dataset**: [`novagen_dataset.csv`](novagen_dataset.csv) — Patient clinical trial observations across 15 biomarkers.
- **Lab Specification**: [`Supervised ML _Assignment5.pdf`](Supervised%20ML%20_Assignment5.pdf) — Complete project guidelines and evaluation criteria.

---

## 🔬 Pipeline Workflow

1. **Exploratory Data Analysis (EDA)**:
   - Inspection of patient demographic, physiological, and chemical biomarker distributions.
   - Handling missing values and feature scaling using `StandardScaler`.
2. **Baseline Model (Logistic Regression with Regularization)**:
   - Establishing baseline precision, recall, and ROC-AUC scores.
3. **Model 2: K-Nearest Neighbors (KNN)**:
   - Evaluating localized non-linear decision boundaries.
4. **Model 3: Random Forest (Bagging Ensemble)**:
   - Decorrelating decision trees to reduce prediction variance.
5. **Model 4: Gradient Boosting (Boosting Ensemble)**:
   - Sequentially correcting pseudo-residuals to optimize patient risk classification.
6. **Model 5: Voting Classifier (Heterogeneous Ensemble)**:
   - Combining Logistic Regression, KNN, Random Forest, and Gradient Boosting via soft confidence voting.
7. **Final Benchmark & Results**:
   - Comprehensive comparative evaluation across models on held-out clinical test cohorts.

---

## 🔗 Referenced In Lectures
- **Lecture 30.08**: [Notes_30.08 (XGBoost & NovaGen Walkthrough)](../Notes_30.08/README.md)
