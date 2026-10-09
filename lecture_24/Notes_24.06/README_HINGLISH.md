# Module 24.06: Underfitting Aur Overfitting Ko Fix Kaise Karein? (Hinglish)

## 1. Problem Ko Pehchanna Aur Fix Karna

Machine learning model ko production-ready banane ke liye hume High Bias aur High Variance ke beech ka perfect balance banana hota hai:

---

## 2. Underfitting Ko Fix Karne Ke Upay (High Bias Solutions)

Agar model Underfit ho raha hai (Training error bohot zyada hai):

1. **Model Ki Complexity Badhayein:** Simple linear model ki jagah Polynomial regression ya Tree models use karein.
2. **Naye Features Add Karein:** Domain features, non-linear powers ($x^2$), ya interactions ($x_1 \times x_2$) add karein.
3. **Regularization Kam Karein:** Agar Lasso ya Ridge use kar rahe hain to $\lambda$ (alpha) ki penalty value kam karein taaki weights ko azaadi mile.
4. **Zyada Epochs / Iterations Chalayein:** Agar Gradient Descent jaldi ruk gaya hai to iterations badhayein.

---

## 3. Overfitting Ko Fix Karne Ke Upay (High Variance Solutions)

Agar model Overfit ho raha hai (Training mein 99% accuracy lekin Test par fail):

1. **Regularization Lagayein:** L1 (Lasso) ya L2 (Ridge) penalty add karein jo weights ko control mein rakhti hai.
2. **Aur Zyada Training Data Layein:** Zyada data aane se model noise ko ratne ke bajaye general pattern seekhne lagta hai.
3. **Useless Features Drop Karein:** Faltu columns hatayein ya PCA laga kar dimensionality kam karein.
4. **Model Ko Simplify Karein:** Polynomial degree 10 se ghata kar degree 2 ya 3 karein.
5. **Cross-Validation Use Karein:** K-Fold cross validation lagayein taaki evaluation reliable ho.
