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
- Female branch: $[0y, 3n]$ (total 3 samples, all No $\rightarrow$ Pure)
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

def calculate_entropy(yes_count, no_count):
    """Calculates Shannon Entropy for binary classes."""
    total = yes_count + no_count
    if total == 0 or yes_count == 0 or no_count == 0:
        return 0.0
    p1 = yes_count / total
    p2 = no_count / total
    return -(p1 * np.log2(p1) + p2 * np.log2(p2))

def calculate_information_gain(parent_y, parent_n, left_y, left_n, right_y, right_n):
    """
    Calculates Information Gain achieved by splitting a parent node into two child branches.
    Formula: IG = H(Parent) - [ (|Left|/|Parent|)*H(Left) + (|Right|/|Parent|)*H(Right) ]
    """
    total_parent = parent_y + parent_n
    total_left = left_y + left_n
    total_right = right_y + right_n

    h_parent = calculate_entropy(parent_y, parent_n)
    h_left = calculate_entropy(left_y, left_n)
    h_right = calculate_entropy(right_y, right_n)

    weighted_child_entropy = (total_left / total_parent) * h_left + (total_right / total_parent) * h_right
    info_gain = h_parent - weighted_child_entropy
    return info_gain

# --- Execute Calculation on Classroom Video Example ---
# Parent Node: [2 Yes, 4 No]
parent_entropy = calculate_entropy(2, 4)

# Candidate 1: Split on Gender -> Male [0y, 3n], Female [2y, 1n]
ig_gender = calculate_information_gain(2, 4, 0, 3, 2, 1)

# Candidate 2: Split on Employed -> Employed [2y, 0n], Unemployed [0y, 4n]
ig_employed = calculate_information_gain(2, 4, 2, 0, 0, 4)

print(f"Parent Node Entropy:         {parent_entropy:.3f}")
print(f"Information Gain (Gender):   {ig_gender:.3f}")
print(f"Information Gain (Employed): {ig_employed:.3f}")
print("Best Split Selected:", "Employed" if ig_employed > ig_gender else "Gender")
```

---

### 📌 Summary Points
- Information Gain reduction in entropy ko measure karta hai.
- Jis feature ka Information Gain sabse zyada hota hai, tree usse hi split karta hai.
