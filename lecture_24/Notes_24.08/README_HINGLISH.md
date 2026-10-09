# Module 24.08: Regularization — Lasso Regression (L1 Penalty) (Hinglish)

## 1. Regularization Kya Hota Hai?

Jab model training data ko ratne lagta hai (Overfitting), to uske weights $w_j$ bohot bade ho jate hain.
**Regularization** loss function mein ek extra penalty term jod deta hai jo bade weights par jurmana (penalty) lagata hai:

$$
\text{Total Cost} = \text{MSE Loss} + \lambda \times \text{Complexity Penalty}
$$

Yaha $\lambda$ (alpha) hyperparameter decide karta hai ki kitni penalty lagani hai.

---

## 2. Lasso Regression Ka Formula (L1 Norm)

Lasso Regression weights ke **Absolute Values ka sum** penalty ke roop mein add karta hai:

$$
J(\mathbf{w}, b) = \frac{1}{2m} \sum_{i=1}^m \left( \hat{y}^{(i)} - y^{(i)} \right)^2 + \lambda \sum_{j=1}^p |w_j|
$$

**Khaas Baat:** Intercept $b$ par kabhi penalty nahi lagayi jaati, sirf feature weights $w_1, \dots, w_p$ par lagti hai.

---

## 3. Lasso Features Ko Zero Kyu Kar Deta Hai? (Geometric Reason)

Lasso ki sabse badi superpower hai: **Automatic Feature Selection (Sparsity)**.
Ye bekaar features ke weights ko exactly **0.0** bana deta hai!

### Diamond Shape Ka Logic:
- 2D parameter space mein L1 constraint ($|w_1| + |w_2| \le C$) ek **Diamond** (rhombus) banata hai.
- Is diamond ke chaaron kone seedhe axes par hote hain (jaha $w_1 = 0$ ya $w_2 = 0$ hota hai).
- MSE ke circular/elliptical contours jab is diamond se takraate hain, to 99% cases mein pehla touch diamond ke kisi ek kone (corner) par hi hota hai.
- Is wajah se feature ka weight exactly **zero** ban jata hai aur feature model se automatically drop ho jata hai!
