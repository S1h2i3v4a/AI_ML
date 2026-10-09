# Module 24.15: Hands-On Logistic Regression Aur Evaluation Metrics (Hinglish)

## 1. Heart Disease Dataset Par Complete Pipeline

Is module mein hum real-world medical `heart.csv` dataset par heart disease ($0$ ya $1$) predict karne ke liye complete classification pipeline banate hain:
1. Data loading aur class balance check karna.
2. Train/Test split (80-20).
3. `StandardScaler` se features scale karna.
4. `LogisticRegression` train karna.
5. Saare metrics (Confusion Matrix, Precision, Recall, F1, ROC-AUC) calculate karna.

---

## 2. Confusion Matrix

- **True Positive (TP):** Bimari thi aur model ne bimari pakad li.
- **True Negative (TN):** Swasth tha aur model ne swasth bataya.
- **False Positive (FP - Type I Error):** Swasth vyakti ko bimar bata diya.
- **False Negative (FN - Type II Error):** Bimar vyakti ko swasth bata diya (Medical mein ye sabse khatarnak error hota hai!).

---

## 3. Classification Ke Sabse Zaroori Metrics

1. **Accuracy:** Total sahi predictions ka percentage.
2. **Precision:** $\frac{TP}{TP + FP}$ — Model ne jinhe bimar kaha unme se kitne sach mein bimar the?
3. **Recall:** $\frac{TP}{TP + FN}$ — Asal bimar logo mein se model kitno ko pehchan paya? (Medical mein Recall sabse important hota hai taaki koi patient miss na ho).
4. **F1-Score:** Precision aur Recall ka harmonic mean.
5. **ROC-AUC Score:** Model ki overall ranking ability (1.0 = Perfect, 0.5 = Tukka/Random).
