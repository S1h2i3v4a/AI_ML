# Lecture 28.02: Decision Tree Classifier — Recursive Binary Splitting aur Hunt's Algorithm

## 📌 Executive Summary (Hinglish)
Recursive binary splitting ka algorithmic workflow, Hunt's greedy split algorithm, continuous features ke split candidate thresholds calculate karna, aur leaves par majority voting.

---

### 📋 Is Topic/Section Mein Hum Kya Cover Kar Rahe Hain?
1. Hunt's Algorithm ka top-down greedy recursive workflow.
2. Continuous numerical features par split candidate thresholds $(\theta_i = \frac{x_i + x_{i+1}}{2})$ ka generation.
3. Terminal leaf node par class assignment rule: Plurality Majority Voting $\hat{y} = \arg\max_k \hat{p}_{mk}$.
4. Computational complexity: Training phase $\mathcal{O}(d \cdot m \log m)$ vs Inference phase $\mathcal{O}(\text{depth})$.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**Hunt's Algorithm**: Tree construction root se start hoti hai. Har step par greedy approach se best feature aur best threshold chuna jaata hai jo impurity ko maximum reduce kare.

**Continuous Thresholds**: Kisi continuous feature ke $m$ unique values ko sort karke adjacent values ke midpoints ko test kiya jaata hai. Maximum $m-1$ possible candidate thresholds bante hain.

**Majority Voting**: Kisi leaf node par aane wale samples mein jis class ka count highest hota hai, wahi class pure leaf ka prediction ban jaati hai.

**Computational Complexity**: Training mein sorting ki vajah se $\mathcal{O}(d \cdot m \log m)$ lagta hai, lekin inference ultra-fast $\mathcal{O}(\log m)$ ya $\mathcal{O}(\text{depth})$ hoti hai.

---

## 🏛️ Mathematical Architecture & Detailed Theory

### ⚙️ Hunt's Greedy Recursive Binary Splitting

Decision trees are constructed via **top-down greedy induction**. The general procedure, formalized in **Hunt's Algorithm** and implemented in modern CART, follows this recursive structure:

Let $\mathcal{D}_t$ be the set of training records that reach node $t$:
1. **Purity Base Case**: If all records in $\mathcal{D}_t$ belong to the same class $y_k$, node $t$ is designated a **Leaf Node** predicting class $y_k$.
2. **Greedy Partitioning Step**: If $\mathcal{D}_t$ contains multiple classes, iterate through all $d$ available features $j \in \{1, \dots, d\}$ and all valid candidate thresholds $\theta$.
3. Evaluate the split $(j, \theta)$ that maximizes the **Impurity Reduction**:
   
$$
   \Delta I(t) = I(t) - \left( \frac{|\mathcal{D}_L|}{|\mathcal{D}_t|} I(\mathcal{D}_L) + \frac{|\mathcal{D}_R|}{|\mathcal{D}_t|} I(\mathcal{D}_R) \right)
$$

4. Create child nodes $\mathcal{D}_L = \{\mathbf{x} \in \mathcal{D}_t \mid x_j \le \theta\}$ and $\mathcal{D}_R = \{\mathbf{x} \in \mathcal{D}_t \mid x_j > \theta\}$ and recursively repeat.

---

### 📐 Continuous Threshold Formulation

For a continuous feature $X_j$, sort the unique observed values in ascending order:

$$
x_{(1), j} < x_{(2), j} < \dots < x_{(u), j}
$$

The set of valid split candidates $\Theta_j$ consists of the midpoints between adjacent sorted values:

$$
\boxed{
\theta_i = \frac{x_{(i), j} + x_{(i+1), j}}{2} \quad \text{for } i = 1, 2, \dots, u-1
}
$$

---

### 🗳️ Majority Plurality Leaf Assignment

For any leaf node $m$ containing a subset of samples $\mathcal{D}_m$, the empirical class probability for class $k$ is:

$$
\hat{p}_{mk} = \frac{1}{|\mathcal{D}_m|} \sum_{i \in \mathcal{D}_m} \mathbb{I}(y_i = k)
$$

The deterministic class prediction $\hat{y}_m$ is the plurality winner:

$$
\boxed{
\hat{y}_m = \arg\max_k \hat{p}_{mk}
}
$$

---

## 💻 Python Implementation & Code Example

```python
import numpy as np

def generate_candidate_thresholds(feature_values):
    unique_vals = np.sort(np.unique(feature_values))
    midpoints = (unique_vals[:-1] + unique_vals[1:]) / 2.0
    return midpoints

# Test
sample_feature = np.array([12.5, 5.0, 8.0, 5.0, 15.0])
candidates = generate_candidate_thresholds(sample_feature)
print("Unique Sorted:", np.unique(sample_feature))
print("Split Candidates:", candidates)
assert len(candidates) == len(np.unique(sample_feature)) - 1

```

---

## 🎯 Quick Revision Points (Interview Notes)
- **Scale Invariance**: Decision Trees monotonically invariant hote hain, isliye inme `StandardScaler` mandatory nahi hota.
- **Gini vs Entropy**: Gini speed mein 10x faster hota hai kyunki logarithm computation ki zaroorat nahi padti.
- **Pruning Necessity**: Unconstrained decision tree hamesha overfit karti hai; `min_samples_leaf` aur `ccp_alpha` sabse effective regularizers hain.
