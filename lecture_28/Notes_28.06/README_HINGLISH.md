# Lecture 28.06: Information Gain aur Split Selection Mechanics

## 📌 Executive Summary (Hinglish)
Information Gain ka calculation, weighted child node impurity reduction, C4.5 Gain Ratio dwara high-cardinality bias ka mitigation, aur candidate split selection ka complete numerical walkthrough.

---

### 📋 Is Topic/Section Mein Hum Kya Cover Kar Rahe Hain?
1. Information Gain ka mathematical formulation: Parent Impurity minus Weighted Child Impurity.
2. Weighted Child Impurity ka formula: $I(S, A) = \frac{|S_L|}{|S|} I(S_L) + \frac{|S_R|}{|S|} I(S_R)$.
3. High-cardinality bias: Kyun standard Information Gain unique IDs (jaise Customer_ID) ko favor karta hai.
4. C4.5 Gain Ratio: Split Information penalty ka formulation aur implementation.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**Information Gain**: Parent node ki impurity se split ke baad bachi hui weighted child impurity ko subtract karne par Information Gain milta hai: $IG = I_{\text{parent}} - I_{\text{children}}$.

**Weighted Average**: Left child aur right child ki impurities ko unke sample size ke fraction se multiply karke sum kiya jaata hai.

**High-Cardinality Flaw**: Agar kisi feature mein har row ki unique value ho (jaise Roll No ya Customer_ID), toh har leaf pure ($I=0$) ban jaata hai, leading to maximum Information Gain but zero generalization.

**Gain Ratio Fix**: C4.5 algorithm split ki intrinsic information ($SplitInfo$) se divide karke Gain Ratio calculate karta hai, jo excessive branching ko heavily penalize karta hai.

---

## 🏛️ Mathematical Architecture & Detailed Theory

### 💡 Information Gain Mathematical Formulation

Given a parent node dataset $S$ containing $|S|$ samples and a proposed binary split on feature $A$ yielding left child $S_L$ and right child $S_R$:

$$
\boxed{
IG(S, A) = I(S) - \left( \frac{|S_L|}{|S|} I(S_L) + \frac{|S_R|}{|S|} I(S_R) \right)
}
$$

Where $I(\cdot)$ denotes the chosen impurity metric (either Entropy $H$ or Gini $G$).

In information theory, $IG(S, A)$ is equivalent to the **Mutual Information** $I(Y; A)$ between the supervisory target $Y$ and the split attribute $A$.

---

### 🛡️ High-Cardinality Pathology & C4.5 Gain Ratio

If an attribute $A$ possesses many distinct values (e.g., `User_Session_ID`), pure Information Gain will partition the data into $|S|$ singleton leaf nodes:
- Each child node has $|S_v| = 1 \implies I(S_v) = 0$.
- The weighted child impurity drops to $0.0$.
- Information Gain reaches its absolute maximum $IG = I(S)$, causing catastrophic overfitting.

Ross Quinlan's **C4.5 Algorithm** rectifies this pathology by normalizing $IG(S, A)$ by the **Split Information**:

$$
SplitInfo(S, A) = -\sum_{v=1}^V \frac{|S_v|}{|S|} \log_2 \left( \frac{|S_v|}{|S|} \right)
$$

The normalized criterion is the **Gain Ratio**:

$$
\boxed{
GainRatio(S, A) = \frac{IG(S, A)}{SplitInfo(S, A)}
}
$$

Split Information acts as a penalizing regularizer: splits that generate a multitude of uniformly sized small buckets suffer a high $SplitInfo$ denominator, driving the Gain Ratio down.

---

## 💻 Python Implementation & Code Example

```python
import numpy as np

def compute_information_gain(parent_y, left_y, right_y, metric_fn):
    n_p = len(parent_y)
    n_l = len(left_y)
    n_r = len(right_y)
    if n_p == 0 or n_l == 0 or n_r == 0:
        return 0.0

    parent_imp = metric_fn(parent_y)
    weighted_child_imp = (n_l / n_p) * metric_fn(left_y) + (n_r / n_p) * metric_fn(right_y)
    return parent_imp - weighted_child_imp

def gini(labels):
    _, c = np.unique(labels, return_counts=True)
    return 1.0 - np.sum((c / c.sum())**2)

# Test
p_labels = np.array([1, 1, 1, 1, 0, 0, 0, 0]) # 50-50 mix
l_labels = np.array([1, 1, 1, 1])             # perfectly pure
r_labels = np.array([0, 0, 0, 0])             # perfectly pure

ig = compute_information_gain(p_labels, l_labels, r_labels, gini)
print("Information Gain for perfect split:", ig)
assert ig == 0.5, "Perfect binary split of 50-50 mix must yield IG = 0.5 (Gini)"

```

---

## 🎯 Quick Revision Points (Interview Notes)
- **Scale Invariance**: Decision Trees monotonically invariant hote hain, isliye inme `StandardScaler` mandatory nahi hota.
- **Gini vs Entropy**: Gini speed mein 10x faster hota hai kyunki logarithm computation ki zaroorat nahi padti.
- **Pruning Necessity**: Unconstrained decision tree hamesha overfit karti hai; `min_samples_leaf` aur `ccp_alpha` sabse effective regularizers hain.
