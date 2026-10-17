# Lecture 28.03: Entropy (Impurity Metric) Aur Uski Calculation

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Entropy ka aasan bhasha mein matlab (Disorder / Uncertainty).
- Claude Shannon ka Entropy formula: $-\sum p_i \log_2(p_i)$.
- Binary classification mein Entropy ki range ($0$ se $1$).
- Video mein board par solve kiya gaya step-by-step example: $[3y, 3n]$ aur $[0y, 3n]$.
- Inverted Parabola curve: $p=0.5$ par peak kyun hota hai.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Entropy Kya Hoti Hai?
Entropy ka seedha matlab hai: **kisi dataset ya dabbe ke andar kitna confusion, disorder ya ashuddhi (impurity) hai.**

- Agar ek bag mein sirf aur sirf red balls hain, toh hum 100% sure hain ki haath daalne par red ball hi niklegi $
\rightarrow$ Zero confusion $
\rightarrow$ **Entropy = 0**.
- Agar bag mein aadhi red aur aadhi blue balls hain, toh sabse zyada confusion hai $
\rightarrow$ Maximum disorder $
\rightarrow$ **Entropy = 1**.

#### 2. Entropy Ka Formula
Dataset $S$ ke liye formula hota hai:

$$E(S) = -\sum_{i=1}^c p_i \log_2(p_i)$$

Jab hamare paas sirf do classes (Yes aur No) hoti hain:

$$E(S) = - p_y \log_2(p_y) - p_n \log_2(p_n)$$

Yahan:
- $p_y$ = Yes aane ki probability (fraction).
- $p_n$ = No aane ki probability (fraction).
- $\log_2$ = Logarithm base 2 (kyunki binary decisions 0 aur 1 hote hain).

#### 3. Board Par Ki Gayi Calculation

**Example 1: Jab 50-50 confusion ho $[3y, 3n]$**
- Total = $3 + 3 = 6$
- $p_y = 3/6 = 0.5$
- $p_n = 3/6 = 0.5$

$$E(S) = - [0.5 \cdot \log_2(0.5)] - [0.5 \cdot \log_2(0.5)]$$

Kyunki $\log_2(0.5) = -1$:

$$E(S) = - [0.5 \cdot (-1)] - [0.5 \cdot (-1)] = 0.5 + 0.5 = 1.0$$

Iska matlab $[3y, 3n]$ par maximum impurity $1.0$ hai!

**Example 2: Jab group bilkul pure ho $[0y, 3n]$**
- $p_y = 0$, $p_n = 3/3 = 1.0$
- $E(S) = - 0 - (1.0 \cdot \log_2 1.0) = 0 - 0 = 0.0$.
- Puri tarah pure node ki entropy **hamesha 0** hoti hai.

#### 4. Inverted Parabola Curve
Video mein ma'am ne board par ulta u-shape curve banaya:
- Jab probability $0$ ya $1$ hoti hai, toh entropy $0$ hoti hai.
- Jab probability $0.5$ hoti hai, toh curve apne peak yani $1.0$ par pahunch jata hai.

---

### 💻 Python Code

```python
import numpy as np

def entropy(y, n):
total = y + n
if total == 0 or y == 0 or n == 0:
return 0.0
py = y / total
pn = n / total
return -(py * np.log2(py) + pn * np.log2(pn))

print("Entropy [3y, 3n]:", entropy(3, 3))
print("Entropy [0y, 3n]:", entropy(0, 3))
print("Entropy [2y, 1n]:", round(entropy(2, 1), 4))
```

---

### 📌 Summary Points
- Entropy uncertainty aur disorder ko 0 se 1 ke scale par naapti hai.
- Pure node ki Entropy = 0, aur 50-50 split ki Entropy = 1.
- Decision tree aise splits choose karta hai jo entropy ko zyada se zyada kam karein.
