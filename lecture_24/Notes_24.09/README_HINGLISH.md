# Module 24.09: Regularization — Ridge Regression (L2 Penalty) (Hinglish)

## 1. Ridge Regression Ka Formula (L2 Norm)

Ridge Regression weights ke **Squares ke sum** par penalty lagata hai:

$$
J(\mathbf{w}, b) = \frac{1}{2m} \sum_{i=1}^m \left( \hat{y}^{(i)} - y^{(i)} \right)^2 + \frac{\lambda}{2} \sum_{j=1}^p w_j^2
$$

Ise mathematics mein **Tikhonov Regularization** ya **Weight Decay** bhi kehte hain.

---

## 2. Closed-Form Analytical Solution (Ridge Normal Equation)

Ridge Regression ka derivative poori tarah smooth hota hai, isliye iska exact formula nikalta hai:

$$
\mathbf{w}_{\text{Ridge}}^* = (\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^T \mathbf{y}
$$

### Multicollinearity Ka Permanent Ilaaj:
Agar data mein columns collinear hon to OLS ka matrix inverse fail ho jata hai. Lekin Ridge mein hum diagonal par $\lambda \mathbf{I}$ add karte hain. Isse matrix **hamesha 100% invertible** ban jata hai!

---

## 3. Ridge vs Lasso Ka Fark (Circle vs Diamond)

- **Lasso (L1):** Diamond shape hota hai, isliye weights ko **exactly 0** kar deta hai (Feature Selection).
- **Ridge (L2):** Smooth Circle shape hota hai, isliye ye weights ko **chhota (shrink)** karta hai lekin kabhi **zero nahi karta**! Saare features model mein rehte hain par unka asar control mein aa jata hai.
