# Module 24.02: Dummy Variable Trap Aur Multicollinearity (Hinglish)

## 1. Dummy Variable Trap Kya Hota Hai?

Jab hum kisi categorical column par One-Hot Encoding lagate hain jisme $K$ categories hain, to agar hum saare $K$ columns retain kar lein, to ek bohot badi mathematical problem create ho jati hai jise **Dummy Variable Trap** kehte hain.

Misaal ke taur par, `Gender` ke do categories hain: `Female` ($D_1$) aur `Male` ($D_2$).
Har row ke liye:

$$
D_1 + D_2 = 1 \implies D_2 = 1 - D_1
$$

Iska matlab $D_2$ ko $D_1$ se directly calculate kiya ja sakta hai. Dono columns mein **Perfect Multicollinearity** (100% linear dependence) hai!

---

## 2. Linear Regression Ka Math Kyu Fail Ho Jata Hai?

Normal Equation ka formula yaad karein:

$$
\mathbf{w}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}
$$

Linear Regression ke feature matrix $\mathbf{X}$ mein pehla column intercept ka hota hai jisme saari values $1$ hoti hain:
$$
\mathbf{x}_0 = \mathbf{D}_1 + \mathbf{D}_2
$$

Kyunki do columns ko jodkar teesra column ban raha hai:
- Matrix $\mathbf{X}$ linearly dependent ho jati hai.
- Determinant $\det(\mathbf{X}^T \mathbf{X}) = 0$ ban jata hai.
- Matrix **Singular** (non-invertible) ho jati hai, yaani iska inverse $(\mathbf{X}^T \mathbf{X})^{-1}$ nikaalna impossible ho jata hai!
- Computer mein weights ki value infinite ($+\infty / -\infty$) blast ho sakti hai.

---

## 3. Solution: $K-1$ Rule (`drop_first=True`)

Is problem ko solve karne ka golden rule hai: **Hamesha ek column drop karein!**

Agar kisi categorical feature ke $K$ options hain, to sirf $K-1$ columns banayein:
- Pandas mein: `pd.get_dummies(df, drop_first=True)`
- Jo column drop hota hai, use **Reference / Baseline** category kehte hain.
- Jab bache hue saare dummy columns $0$ hote hain, to model us baseline category ka prediction intercept $b$ ke through karta hai!
