# Module 24.11: LassoCV Se Automatic Hyperparameter Tuning (Hinglish)

## 1. Best $\alpha$ Kaise Choose Karein?

Regularization parameter $\alpha$ (alpha) model khud se training loss minimize karke nahi seekh sakta, kyunki agar model se poochoge to wo bolega $\alpha = 0$ rakho taaki training error zero rahe.
Isliye best $\alpha$ dhoondhne ke liye hum **K-Fold Cross-Validation** use karte hain.

---

## 2. LassoCV Kaise Kaam Karta Hai?

Scikit-learn ka `LassoCV` candidate alphas ki list par automatically 5-fold cross validation chalata hai:
- Har alpha par validation error nikaalta hai.
- Jis alpha par average test error sabse kam aata hai, use **Best Alpha (`model.alpha_`)** declare kar deta hai.
- Aur phir poore training data par us best alpha se final model train kar deta hai!
