# Lecture 28.11: Post-Pruning Implementation — Minimal Cost-Complexity Pruning (ccp_alpha)

## 📌 Executive Summary (Hinglish)
Leo Breiman ke Minimal Cost-Complexity Pruning ka mathematical framework, effective alpha sequence extraction, ccp_alpha path traversal, aur optimal alpha identify karna.

---

### 📋 Is Topic/Section Mein Hum Kya Cover Kar Rahe Hain?
1. Minimal Cost-Complexity criterion ka mathematical formula: $R_\alpha(T) = R(T) + \alpha |T|$.
2. `clf.cost_complexity_pruning_path(X, y)` se unique candidate $\alpha$ values extract karna.
3. Subtree collapse dynamics: Jaise-jaise $\alpha$ badhta hai, leaf count $|T|$ monotonically decrease hota hai.
4. Optimal $\alpha^*$ selection: Test generalization F1 score ko maximize karne wala complexity parameter.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**Mathematical Formulation**: Cost-Complexity function $R_\alpha(T) = R(T) + \alpha |T|$ misclassification error $R(T)$ aur tree complexity $|T|$ (total leaves) ko balance karta hai. $\alpha$ L1/L2 regularization ki tarah penalty multiplier hai.

**Effective Alpha Sequence**: CART algorithm mathematically prove karta hai ki ek finite sequence $0 = \alpha_0 < \alpha_1 < \dots < \alpha_k$ exist karti hai jahan tree ke subtrees sequentially collapse hote hain.

**Alpha vs Tree Size**: Jab $\alpha = 0$, tree fully grown rehti hai. Jab $\alpha \to \infty$, poori tree collapse hokar sirf single root node ban jaati hai.

**Optimal Alpha**: Cross-validation se hum wo $\alpha^*$ pick karte hain jahan validation F1 peak par ho aur unnecessary complex branches automatically prune ho chuki hon.

---

## 🏛️ Mathematical Architecture & Detailed Theory

### 📐 Minimal Cost-Complexity Pruning Mathematics

Formulated by Leo Breiman, Jerome Friedman, Richard Olshen, and Charles Stone (1984), **Minimal Cost-Complexity Pruning** defines a parameterized objective function balancing empirical misclassification error with structural tree complexity:

$$
\boxed{
R_\alpha(T) = R(T) + \alpha |T|
}
$$

Where:
- $R(T) = \sum_{t \in \mathcal{L}} R(t) = \sum_{t \in \mathcal{L}} \left( \frac{N_t}{N} I(t) \right)$ is the total unpenalized leaf impurity/error.
- $|T|$ is the number of terminal leaf nodes in subtree $T$.
- $\alpha \ge 0$ is the **complexity parameter** (regularization penalty).

#### Pruning Mechanics:
For each internal node $t$:
1. If node $t$ is collapsed into a single leaf, its error is $R(t)$.
2. If subtree $T_t$ rooted at $t$ is kept, its error is $R(T_t) + \alpha |T_t|$.
3. Subtree $T_t$ and leaf $t$ have identical cost-complexity when:
   
$$
   R(t) + \alpha (1) = R(T_t) + \alpha |T_t| \implies \alpha = \frac{R(t) - R(T_t)}{|T_t| - 1}
$$

This critical value is the **effective alpha** for node $t$. Pruning the node with the smallest effective alpha produces the optimal nested subtree sequence:

$$
T_0 \supset T_1 \supset T_2 \supset \dots \supset \{t_{\text{root}}\}
$$

---

## 💻 Python Implementation & Code Example

```python
from sklearn.tree import DecisionTreeClassifier

# Compute Cost-Complexity Pruning Path
base_clf = DecisionTreeClassifier(random_state=42).fit(X_syn, y_syn)
path = base_clf.cost_complexity_pruning_path(X_syn, y_syn)
ccp_alphas, impurities = path.ccp_alphas, path.impurities

print(f"Total Effective Alphas: {len(ccp_alphas)}")
print("First 3 Alphas: ", np.round(ccp_alphas[:3], 5))
print("Final 3 Alphas: ", np.round(ccp_alphas[-3:], 5))

# Fit with mid-range alpha
pruned_clf = DecisionTreeClassifier(random_state=42, ccp_alpha=ccp_alphas[len(ccp_alphas)//2])
pruned_clf.fit(X_syn, y_syn)
print(f"Unpruned Nodes: {base_clf.tree_.node_count} -> Pruned Nodes: {pruned_clf.tree_.node_count}")
assert pruned_clf.tree_.node_count < base_clf.tree_.node_count

```

---

## 🎯 Quick Revision Points (Interview Notes)
- **Scale Invariance**: Decision Trees monotonically invariant hote hain, isliye inme `StandardScaler` mandatory nahi hota.
- **Gini vs Entropy**: Gini speed mein 10x faster hota hai kyunki logarithm computation ki zaroorat nahi padti.
- **Pruning Necessity**: Unconstrained decision tree hamesha overfit karti hai; `min_samples_leaf` aur `ccp_alpha` sabse effective regularizers hain.
