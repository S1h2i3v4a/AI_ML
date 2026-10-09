# Module 23.08: Best Fit Line Kya Hoti Hai? (Residuals & Ordinary Least Squares)

## 1. Introduction: Best Fit Line Kaise Decide Hoti Hai?

Jab hamare paas 2D data points $(x^{(1)}, y^{(1)}), \dots, (x^{(m)}, y^{(m)})$ hote hain, to hum unke beech se hazaaron straight lines draw kar sakte hain. Lekin in saari lines mein se sabse **best line** kaun si hai?
Ise mathematically decide karne ke liye hum ek objective criteria banate hain jo calculate karta hai ki line data points se kitni close hai.

---

## 2. Residual (Error) Kya Hota Hai?

Har data point $(x^{(i)}, y^{(i)})$ ke liye candidate line ek prediction generate karti hai:

$$
\hat{y}^{(i)} = w x^{(i)} + b
$$

Data point ke actual target $y^{(i)}$ aur predicted target $\hat{y}^{(i)}$ ke beech ke difference ko **residual** ya **error** $e^{(i)}$ kehte hain:

$$
e^{(i)} = y^{(i)} - \hat{y}^{(i)} = y^{(i)} - (w x^{(i)} + b)
$$

### Hum Simple Errors Ka Sum ($\sum e^{(i)}$) Kyu Nahi Lete?
Agar hum sirf raw errors ko add karenge, to jo points line ke upar hain unka error positive hoga aur jo neeche hain unka negative hoga. Ye positive aur negative errors ek dusre ko cancel out kar denge. Result ye hoga ki ek bekaar line ka total error bhi zero aa sakta hai!

### Absolute Error ($\sum |e^{(i)}|$) Kyu Avoid Karte Hain?
Absolute value function $|u|$, zero ($u=0$) par differentiate nahi hota. Calculus mein iska clean analytical derivative nahi nikalta, jisse formula derive karna mushkil ho jata hai.

---

## 3. Ordinary Least Squares (OLS) Ka Principle

Gauss aur Legendre ne iska permanent solution nikala: **Sum of Squared Errors (SSE)** ko minimize karna:

$$
SSE(w, b) = \sum_{i=1}^m \left( e^{(i)} \right)^2 = \sum_{i=1}^m \left( y^{(i)} - (w x^{(i)} + b) \right)^2
$$

### OLS Ki 3 Khaas Baatein:
1. **Always Positive:** Square hone se koi error negative nahi rehta, to cancellation ka khatra zero ho jata hai.
2. **Outliers Ko Strong Penalty:** Chhote error par kam penalty, bade error par square penalty ($4 \to 16$).
3. **Smooth & Differentiable:** Calculus ke derivatives asaani se nikal aate hain aur exact closed-form formula mil jata hai.

---

## 4. Analytical Formula Derivation

Partial derivatives ko zero set karke:

1. **Optimal Intercept:**
$$
b = \bar{y} - w \bar{x}
$$
Iska matlab best fit line hamesha data ke center point centroid $(\bar{x}, \bar{y})$ se hokar gujregi!

2. **Optimal Slope:**
$$
w = \frac{\sum_{i=1}^m (x^{(i)} - \bar{x})(y^{(i)} - \bar{y})}{\sum_{i=1}^m (x^{(i)} - \bar{x})^2} = \frac{\text{Cov}(x, y)}{\text{Var}(x)}
$$
Slope covariance aur variance ka direct ratio hota hai!
