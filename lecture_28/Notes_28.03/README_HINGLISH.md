# Lecture 28.03: Entropy as an Impurity Metric — Shannon Information Theory

## 📌 Executive Summary (Hinglish)
Claude Shannon ki Information Theory par based Entropy ka formulation, bits of surprise, entropy curve ki mathematical properties, aur decision trees mein node impurity measure karna.

---

### 📋 Is Topic/Section Mein Hum Kya Cover Kar Rahe Hain?
1. Claude Shannon ka Information Theory framework: Surprise / Uncertainty ka measurement.
2. Shannon Entropy ka mathematical formula: $H(S) = -\sum_{k=1}^K p_k \log_2 p_k$.
3. Entropy ke core boundaries: Pure node par $H=0$ (zero surprise) aur uniform mix par maximum entropy $\log_2 K$.
4. Binary classification case mein Entropy curve ki symmetry aur concavity.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**Information Theory**: Agar koi event certain hai ($p=1$), toh usme zero new information hoti hai. Agar event highly uncertain hai ($p=0.5$), toh usme maximum information / surprise hoti hai.

**Formula Mechanics**: $H(S) = -\sum p_k \log_2 p_k$. Log base 2 use karne se information 'bits' mein measure hoti hai.

**Boundaries**: Agar kisi leaf node par saare samples Class 1 ke hain, toh $H = -(1 \log_2 1) = 0$. Agar 50% Class 0 aur 50% Class 1 hain, toh $H = -(0.5 \log_2 0.5 + 0.5 \log_2 0.5) = 1.0$ bit.

**Mathematical Concavity**: Entropy ek strictly concave function hai jiska maximum center $p=0.5$ par hota hai.

---

## 🏛️ Mathematical Architecture & Detailed Theory

### 💡 Shannon Information Theory Foundations

In 1948, Claude Shannon established mathematical information theory by defining the **Self-Information** (or surprisal) of observing an event with probability $P(E)$:

$$
I(E) = -\log_2 P(E) = \log_2 \left( rac{1}{P(E)} ight)
$$

The base-2 logarithm quantifies information in **bits**:
- An event with $P(E) = 1.0$ yields $I(E) = 0$ bits (no surprise).
- An event with $P(E) = 0.5$ yields $I(E) = 1$ bit (equivalent to a fair coin flip).

---

### 📐 Shannon Entropy Formulation for Node Impurity

For a dataset partition $S$ containing samples across $K$ discrete classes with empirical proportions $p_1, p_2, \dots, p_K$ (where $\sum_{k=1}^K p_k = 1$ and $0 \log_2 0 \equiv 0$):

$$
\boxed{
H(S) = -\sum_{k=1}^K p_k \log_2(p_k)
}
$$

#### Mathematical Invariants of Entropy:
1. **Non-Negativity**: $H(S) \ge 0$ for all valid probability vectors.
2. **Absolute Purity (Minimum)**:
   
$$
   H(S) = 0 \iff \exists k 	ext{ such that } p_k = 1 	ext{ and } p_{j \neq k} = 0
$$

3. **Maximum Disorder (Uniform Uncertainty)**:
   
$$
   H(S) = \log_2(K) \iff p_1 = p_2 = \dots = p_K = \frac{1}{K}
$$

For a binary classification problem ($K=2$ with positive class proportion $p$):

$$
H(p) = -p \log_2(p) - (1-p) \log_2(1-p)
$$

The function achieves its global maximum $H(0.5) = 1.0$ bit at equal mixture.

---

## 💻 Python Implementation & Code Example

```python
import numpy as np

def calculate_entropy(labels):
    _, counts = np.unique(labels, return_counts=True)
    probs = counts / counts.sum()
    # Zero probability safe mask
    probs = probs[probs > 0]
    return -np.sum(probs * np.log2(probs))

# Test
pure_labels = np.array([1, 1, 1, 1, 1])
mixed_labels = np.array([0, 1, 0, 1, 0, 1])

print("Pure Node Entropy: ", calculate_entropy(pure_labels))
print("50-50 Node Entropy:", calculate_entropy(mixed_labels))
assert calculate_entropy(pure_labels) == 0.0
assert calculate_entropy(mixed_labels) == 1.0

```

---

## 🎯 Quick Revision Points (Interview Notes)
- **Scale Invariance**: Decision Trees monotonically invariant hote hain, isliye inme `StandardScaler` mandatory nahi hota.
- **Gini vs Entropy**: Gini speed mein 10x faster hota hai kyunki logarithm computation ki zaroorat nahi padti.
- **Pruning Necessity**: Unconstrained decision tree hamesha overfit karti hai; `min_samples_leaf` aur `ccp_alpha` sabse effective regularizers hain.
