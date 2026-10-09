# Module 24.13: Logistic Regression — Intuition Aur Sigmoid Function (Hinglish)

## 1. Linear Regression Classification Par Kyu Fail Ho Jata Hai?

Classification mein answer $0$ ya $1$ hota hai. Agar hum Linear Regression $\hat{y} = w x + b$ lagate hain to do bohot badi problems aati hain:
1. **Unbounded Output:** Linear Regression $-\infty$ se $+\infty$ tak koi bhi number de sakta hai. Lekin Probability hamesha $[0, 1]$ ke beech honi chahiye. $\hat{y} = 2.5$ ya $-0.4$ ka koi matlab nahi banta!
2. **Outliers Ka Asar:** Agar door ek outlier aa jaye, to straight line uski taraf jhuk jaati hai aur sahi points ko galat predict karne lagti hai.

---

## 2. Sigmoid Function Ka Mathematical Derivation

Hum linear equation $z = \mathbf{w}^T \mathbf{x} + b$ ko probability $p$ mein convert karte hain:

1. **Odds:** $\frac{p}{1-p}$
2. **Logit (Log-Odds):** $\ln\left(\frac{p}{1-p}\right) = z$
3. **Inversion (Sigmoid):**
$$
p = \sigma(z) = \frac{1}{1 + e^{-z}}
$$

Ye S-shaped curve kisi bhi real number $z \in (-\infty, \infty)$ ko smoothly $0$ aur $1$ ke beech squeeze kar deta hai!

---

## 3. Decision Boundary

Jab probability $\ge 0.5$ hoti hai, to hum class $1$ predict karte hain.
Kyunki $\sigma(z) = 0.5$ tab hota hai jab $z = 0$, isliye decision boundary hoti hai:

$$
\mathbf{w}^T \mathbf{x} + b = 0
$$

Ye feature space mein ek straight line ya hyperplane hoti hai jo dono classes ko alag karti hai!
