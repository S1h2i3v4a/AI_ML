# Lecture 28.13: Variance Reduction (Formula & Split Selection)

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Variance Reduction (VR) ka concept: Regression mein Information Gain ka roop.
- Formula: $VR = V_S - \text{Weighted Child Variance}$.
- Video mein board par solve kiye gaye dono split cases:
- Case 1 ($x \le 2$): $VR = 6.25$.
- Case 2 ($x \le 3$): $VR = 6.75$.
- Best split threshold ka chunav.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Variance Reduction Kya Hai?
Classification mein hum Information Gain se dekhte the ki entropy kitni kam hui.
Regression mein numbers hote hain, isiliye:
> **Variance Reduction yeh naapta hai ki split karne ke baad data ke variance (bikhrav) mein kitni kami aayi.**

Jitna zyada Variance Reduction hoga, child nodes ke andar numbers apne average ke utne hi paas honge!

#### 2. Formula

$$VR = V_S - \left( \frac{|S_L|}{|S|} V_L + \frac{|S_R|}{|S|} V_R \right)$$

#### 3. Board Par Ki Gayi Calculation ($y = [2, 4, 6, 10]$, $V_S = 8.75$)

**Case 1: Split $x \le 2$ Par**
- Left branch mein 2 points: $[2, 4]$
- Average: $\bar{y}_L = 3$
- Variance: $V_L = 1.0$
- Right branch mein 2 points: $[6, 10]$
- Average: $\bar{y}_R = 8$
- Variance: $V_R = 4.0$
- Children ka weighted variance:
$$\frac{2}{4}(1.0) + \frac{2}{4}(4.0) = 0.5 + 2.0 = 2.5$$
- Variance Reduction:
$$VR_1 = 8.75 - 2.5 = 6.25$$

**Case 2: Split $x \le 3$ Par**
- Left branch mein 3 points: $[2, 4, 6] \r\rightarrow V_L \approx 2.67$
- Right branch mein 1 point: $[10] \r\rightarrow V_R = 0$ (single point ka variance hamesha 0 hota hai)
- Weighted child variance:
$$\frac{3}{4}(2.67) + \frac{1}{4}(0) = 2.0$$
- Variance Reduction:
$$VR_2 = 8.75 - 2.0 = 6.75$$

#### 4. Faisla (Decision)
Kyunki $6.75 > 6.25$, isiliye Decision Tree **Case 2 ($x \le 3$)** ko chunega!

---

### 💻 Python Code

```python
import numpy as np

def calculate_variance_reduction(y_parent, y_left, y_right):
    """
    Calculates Variance Reduction achieved by splitting continuous target y into two child nodes.
    Formula: VR = Var(Parent) - [ (|Left|/|Parent|)*Var(Left) + (|Right|/|Parent|)*Var(Right) ]
    """
    n_p = len(y_parent)
    n_l = len(y_left)
    n_r = len(y_right)

    v_parent = np.var(y_parent)
    v_left = np.var(y_left)
    v_right = np.var(y_right)

    weighted_child_var = (n_l / n_p) * v_left + (n_r / n_p) * v_right
    reduction = v_parent - weighted_child_var
    return reduction

# --- Compare Candidate Splits on Video Example ---
y = np.array([2, 4, 6, 10])

# Split 1: x <= 2 -> Left [2, 4], Right [6, 10]
vr_split1 = calculate_variance_reduction(y, np.array([2, 4]), np.array([6, 10]))

# Split 2: x <= 3 -> Left [2, 4, 6], Right [10]
vr_split2 = calculate_variance_reduction(y, np.array([2, 4, 6]), np.array([10]))

print(f"Variance Reduction (Split 1: x <= 2): {vr_split1:.3f}")
print(f"Variance Reduction (Split 2: x <= 3): {vr_split2:.3f}")
print("Best Split:", "Split 2 (x <= 3)" if vr_split2 > vr_split1 else "Split 1 (x <= 2)")
```

---

### 📌 Summary Points
- Variance Reduction regression trees ka split selection criteria hai.
- Tree wo threshold chunta hai jo target variance ko sabse zyada ghatata hai.
