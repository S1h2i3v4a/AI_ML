# Module 23.09: Cost Function Kya Hota Hai? (MSE Aur $1/(2m)$ Ka Reason)

## 1. Loss Function vs Cost Function Mein Farq

Machine Learning mein aksar log in dono terms mein confuse hote hain:

```
+--------------------------------------------------------------------------+
| Ek Single Example (x^(i), y^(i))  --->  Loss Function: L(y, \hat{y})      |
| Saare m Training Examples         --->  Cost Function: J(w, b)           |
+--------------------------------------------------------------------------+
```

- **Loss Function:** Sirf ek sample ka error calculate karta hai: $L = \frac{1}{2}(\hat{y}^{(i)} - y^{(i)})^2$.
- **Cost Function:** Poore dataset ke saare errors ka aggregate average calculate karta hai: $J(w, b)$.

---

## 2. Linear Regression Ka Cost Function Formula

Univariate Linear Regression ke liye cost function formula hota hai:

$$
J(w, b) = \frac{1}{2m} \sum_{i=1}^m \left( \hat{y}^{(i)} - y^{(i)} \right)^2 = \frac{1}{2m} \sum_{i=1}^m \left( w x^{(i)} + b - y^{(i)} \right)^2
$$

---

## 3. Formula Mein $\frac{1}{2m}$ Kyu Hota Hai?

### Pehla Reason: $\frac{1}{m}$ (Dataset Size Se Independence)
Agar hum $m$ se divide na karein, to 10 points ka error chhota hoga aur 10 lakh points ka error bahut bada ho jayega. $m$ se divide karne par hume **Average Error per Data Point** milta hai, jo dataset size par depend nahi karta.

### Doosra Reason: $\frac{1}{2}$ (Calculus Ki Simplicity)
Calculus ke power rule ke mutabiq jab hum square term ka derivative nikaalte hain:

$$
\frac{d}{du} \left[ \frac{1}{2} u^2 \right] = \frac{1}{2} \cdot 2u = u
$$

Power 2 neeche aakar $\frac{1}{2}$ se cancel out ho jata hai! Agar $\frac{1}{2}$ na hota, to har gradient update step mein ek extra 2 multiply hota rehta. Constant se multiply ya divide karne se minimum point ki location nahi badalti, isliye $\frac{1}{2}$ math ko clean banane ke liye standard convention hai.
