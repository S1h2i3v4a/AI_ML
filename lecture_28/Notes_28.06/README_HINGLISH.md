# Lecture 28.06: Information Gain Aur Split Selection

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Information Gain (IG) ka concept: Entropy mein aayi kami (Reduction in entropy).
- Formula: $IG = 	ext{Parent Entropy} - 	ext{Weighted Child Entropy}$.
- Video mein board par solve ki gayi exact calculation:
- Parent $[2y, 4n]$ ki entropy nikaalna ($0.918$).
- `Gender` feature ke liye IG calculate karna ($0.459$).
- `Employed` feature ke IG ($0.8$) se compare karke best split select karna.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Information Gain (IG) Kya Hai?
Jab hum kisi feature par data ko split karte hain, toh impurity kam hoti hai.
> **Information Gain yeh batata hai ki split karne se hamare confusion ya entropy mein kitni kami aayi.**

Jitna zyada Information Gain hoga, wo split utna hi behtar hoga!

#### 2. Information Gain Ka Formula

$$IG = 	ext{Entropy of parent} - 	ext{Weighted entropy of children}$$

$$IG(S, A) = H(S) - \sum rac{|S_v|}{|S|} H(S_v)$$

Yahan child nodes ki entropy ko unke sample size ke hisaab se weight diya jata hai.

#### 3. Board Par Ki Gayi Complete Step-by-Step Calculation

**Step 1: Parent Node Ki Entropy**
Parent node par 6 samples hain: $[2y, 4n]$:
- $p_y = 2/6$, $p_n = 4/6$
- $H(S) = - \left(rac{2}{6}\log_2rac{2}{6} + rac{4}{6}\log_2rac{4}{6}
ight) pprox 0.918$.

**Step 2: Feature 1 (Gender) Par Split Karna**
- Male branch: $[2y, 1n]$ (total 3 samples)
- $H(S_M) = -\left(rac{2}{3}\log_2rac{2}{3} + rac{1}{3}\log_2rac{1}{3}
ight) pprox 0.918$.
- Female branch: $[0y, 3n]$ (total 3 samples, all No $
\rightarrow$ Pure)
- $H(S_F) = 0.0$.

**Step 3: Children Ki Weighted Entropy**
Total samples 6 hain, aur dono branches mein 3-3 samples gaye:

$$	ext{Weighted Entropy} = rac{3}{6} \cdot (0.918) + rac{3}{6} \cdot (0) = 0.459$$

**Step 4: Information Gain Nikaalna**

$$IG(	ext{Gender}) = 0.918 - 0.459 = 0.459$$

**Step 5: Faisla (Decision)**
Ma'am ne board par doosre feature `Employed` ka IG likha:
- $IG(	ext{Employed}) = 0.8$
- $IG(	ext{Gender}) = 0.459$

Kyunki $0.8 > 0.459$, isiliye Decision Tree pehle **`Employed`** feature par split karega!

---

### 💻 Python Code

```python
import numpy as np

def entropy(y, n):
if y == 0 or n == 0:
return 0.0
total = y + n
py = y / total
pn = n / total
return -(py * np.log2(py) + pn * np.log2(pn))

# Parent Entropy
h_parent = entropy(2, 4)

# Children Weighted Entropy
weighted_child = (3/6) * entropy(2, 1) + (3/6) * entropy(0, 3)

# Information Gain
ig = h_parent - weighted_child
print(f"Parent Entropy: {h_parent:.3f}")
print(f"Information Gain (Gender): {ig:.3f}")
```

---

### 📌 Summary Points
- Information Gain reduction in entropy ko measure karta hai.
- Jis feature ka Information Gain sabse zyada hota hai, tree usse hi split karta hai.
