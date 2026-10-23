# NovaGen Research Labs — Clinical Drug Trial Patient Risk Classification [Hinglish]

[![Project](https://img.shields.io/badge/Project-NovaGen%20Labs-blue.svg)](#)
[![Notebook](https://img.shields.io/badge/Notebook-novagen.ipynb-orange.svg?logo=jupyter&logoColor=white)](novagen.ipynb)
[![Dataset](https://img.shields.io/badge/Dataset-novagen__dataset.csv-green.svg)](novagen_dataset.csv)
[![Assignment PDF](https://img.shields.io/badge/PDF-Assignment5-red.svg)](Supervised%20ML%20_Assignment5.pdf)

---

## 📌 Project Ka Parichay
**NovaGen Research Labs Project** Day 30 ka capstone lab project hai. Isme pharmaceutical company ke clinical trial patients ka data analyze karke patient risk profile classify karni hoti hai.

Is project mein baseline models se shuru karke advanced ensemble techniques (**Random Forest**, **Gradient Boosting**, aur **Voting Classifier**) tak ka complete real-world comparative benchmark implement kiya gaya hai.

---

## 📂 Project Ki Files
- **Jupyter Notebook**: [`novagen.ipynb`](novagen.ipynb) — Ma'am ka complete project notebook.
- **Dataset File**: [`novagen_dataset.csv`](novagen_dataset.csv) — 15 clinical biomarkers wala patient dataset.
- **Assignment Document**: [`Supervised ML _Assignment5.pdf`](Supervised%20ML%20_Assignment5.pdf) — Project ki official problem statement aur instructions.

---

## 🛠️ Step-by-Step Project Pipeline
1. **Data Preprocessing & Scaling**: `StandardScaler` ke zariye clinical measurements ko normalize karna.
2. **Baseline Model**: Regularized `LogisticRegression` se initial accuracy benchmark set karna.
3. **Model 2 (KNN)**: `KNeighborsClassifier` se local patterns check karna.
4. **Model 3 (Random Forest)**: Bagging technique se multiple trees train karna.
5. **Model 4 (Gradient Boosting)**: Sequential residual learning se boosting model fit karna.
6. **Model 5 (Voting Classifier)**: Sabhi models ko combine karke final ensemble prediction banana.
7. **Comparative Results**: Saare models ka precision, recall aur ROC-AUC score compare karna.

---

## 🔗 Lecture References
- **Lecture 30.08**: [Notes_30.08 (XGBoost & NovaGen Lecture)](../Notes_30.08/README_HINGLISH.md)
