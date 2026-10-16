# Lecture 28.08: Common Pruning Rules aur Hyperparameter Regularization

## 📌 Executive Summary (Hinglish)
Scikit-Learn DecisionTreeClassifier ke regularizing hyperparameters ka deep dive: max_depth, min_samples_split, min_samples_leaf, max_leaf_nodes, aur min_impurity_decrease.

---

### 📋 Is Topic/Section Mein Hum Kya Cover Kar Rahe Hain?
1. `max_depth`: Tree ke maximum vertical growth ko constrain karna.
2. `min_samples_split`: Split attempt karne ke liye minimum sample threshold.
3. `min_samples_leaf`: Terminal leaves mein minimum sample support guarantee karna.
4. `max_leaf_nodes` aur `min_impurity_decrease` ka mathematical impact.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**max_depth**: Yeh sabse direct hyperparameter hai jo root se kisi bhi leaf tak ke maximum steps ko limit karta hai. Depth 4-6 aksar tabular data ke liye sweet spot hota hai.

**min_samples_split**: Agar kisi node mein 20 se kam samples hain, toh aage split karne se mana kar deta hai. Yeh small noisy subsets par branching rokta hai.

**min_samples_leaf**: Yeh guarantee karta hai ki banne wale left aur right child dono mein kam se kam $N$ samples ho. Yeh single-sample outlier leaves ko completely ban kar deta hai.

**min_impurity_decrease**: Split tabhi accept hoga jab Information Gain kisi threshold $\epsilon$ se zyada ho, minor statistical fluctuations ko ignore karke.

---

## 🏛️ Mathematical Architecture & Detailed Theory

### 🛠️ Scikit-Learn Pre-Pruning Hyperparameters

To enforce regularized inductive bias, Scikit-Learn provides five core structural hyperparameter constraints:

| Hyperparameter | Mathematical Definition | Default | Typical Tuned Range | Engineering Impact |
| :--- | :--- | :--- | :--- | :--- |
| `max_depth` | $\max \{ \text{depth}(m) \mid m \in \mathcal{L} \} \le d_{\max}$ | `None` (unbounded) | $[3, 10]$ | Hard ceiling on hierarchy depth; drastically cuts variance |
| `min_samples_split` | $|\mathcal{D}_t| \ge s_{\min}$ to attempt split | `2` | $[10, 100]$ | Prevents splitting small, statistically unreliable sample subsets |
| `min_samples_leaf` | $\min(|\mathcal{D}_L|, |\mathcal{D}_R|) \ge l_{\min}$ | `1` | $[5, 50]$ | **Highest impact**: guarantees statistical support at all terminal leaves |
| `max_leaf_nodes` | $|\mathcal{L}| \le L_{\max}$ | `None` | $[10, 64]$ | Best-first tree growth; bounds overall capacity |
| `min_impurity_decrease` | $\Delta I(t) \ge \tau_{\min}$ | `0.0` | $[10^{-4}, 10^{-2}]$ | Rejects splits that provide negligible information gain |

---

### 🛡️ Why `min_samples_leaf` is Superior to `min_samples_split`

Consider a node with 20 samples (`min_samples_split=20`):
- A split producing $|\mathcal{D}_L| = 19$ and $|\mathcal{D}_R| = 1$ is valid under `min_samples_split=20`.
- However, $|\mathcal{D}_R| = 1$ is a dangerous single-sample leaf that memorizes noise.
- Setting `min_samples_leaf=10` forces both children to contain at least 10 samples, instantly disqualifying asymmetric noise splits.

---

## 💻 Python Implementation & Code Example

```python
from sklearn.tree import DecisionTreeClassifier

# Regularized Tree using Pre-Pruning Hyperparameters
regularized_tree = DecisionTreeClassifier(
    max_depth=5,
    min_samples_split=20,
    min_samples_leaf=10,
    random_state=42
)

# Fits with strict structural safeguards
regularized_tree.fit(X_syn, y_syn)
print("Regularized Tree Depth:     ", regularized_tree.get_depth())
print("Regularized Leaf Count:     ", regularized_tree.get_n_leaves())
assert regularized_tree.get_depth() <= 5, "Depth constraint must be strictly respected"

```

---

## 🎯 Quick Revision Points (Interview Notes)
- **Scale Invariance**: Decision Trees monotonically invariant hote hain, isliye inme `StandardScaler` mandatory nahi hota.
- **Gini vs Entropy**: Gini speed mein 10x faster hota hai kyunki logarithm computation ki zaroorat nahi padti.
- **Pruning Necessity**: Unconstrained decision tree hamesha overfit karti hai; `min_samples_leaf` aur `ccp_alpha` sabse effective regularizers hain.
