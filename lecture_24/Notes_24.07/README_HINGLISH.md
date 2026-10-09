# Module 24.07: Diagnostic Framework — Model Underfit Hai Ya Overfit? (Hinglish)

## 1. Kaise Pata Karein Ki Model Mein Kaun Si Problem Hai?

Sirf ek single accuracy score dekh kar ye nahi pata chal sakta ki model underfit hai ya overfit. Iske liye hum **Learning Curves** plot karte hain.

Learning curve mein hum x-axis par **Training Set Size ($m$)** rakhte hain aur y-axis par **Error (Loss)** plot karte hain.

---

## 2. Learning Curves Ka Analysis

### 1. High Bias (Underfitting) Ka Curve:
- Training error aur Validation error dono bohot jaldi ek **High Plateau** par pahunch kar freeze ho jate hain.
- Dono ke beech ka gap bohot chhota hota hai lekin error bohot high hota hai.
- **Golden Rule:** Is condition mein aur zyada data laane ka **koi fayda nahi** hoga! Kyunki model itna simple hai ki wo aur data handle hi nahi kar sakta. Model ko complex banana padega.

### 2. High Variance (Overfitting) Ka Curve:
- Training error bohot low rehta hai, jabki Validation error upar rehta hai.
- Dono ke beech ek **Bada Generalization Gap** dikhta hai.
- **Golden Rule:** Is condition mein aur zyada training data laane se **fayda hoga**! Validation curve dheere-dheere neeche aayega aur gap kam hoga.

---

## 3. Quick Decision Guide

- **Train Error High + Val Error High:** $\implies$ Underfitting $\implies$ Model complex karein, features badhayein, regularization kam karein.
- **Train Error Low + Val Error High:** $\implies$ Overfitting $\implies$ Regularization lagayein, faltu features drop karein, zyada data collect karein.
- **Train Error Low + Val Error Low:** $\implies$ Perfect Balance $\implies$ Production ready!
