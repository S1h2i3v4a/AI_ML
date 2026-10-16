# Lecture 28.09: Decision Tree Classifier Implementation in Scikit-Learn

## 📌 Executive Summary (Hinglish)
Scikit-Learn DecisionTreeClassifier ka hands-on implementation, parameter configuration, imbalanced data par class_weight='balanced', aur plot_tree se structure visualization.

---

### 📋 Is Topic/Section Mein Hum Kya Cover Kar Rahe Hain?
1. `DecisionTreeClassifier` class ka initialization aur parameter tuning.
2. `class_weight='balanced'` se imbalanced target classes ko inversely weight karna.
3. Tree attributes (`tree_.node_count`, `tree_.max_depth`, `feature_importances_`) ko introspect karna.
4. `plot_tree` aur `export_text` se tree architecture visualize karna.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**API Implementation**: `from sklearn.tree import DecisionTreeClassifier` se estimator initialize karke `fit()` aur `predict()` call karte hain.

**Class Imbalance Handling**: E-commerce ya banking datasets mein positive class kam hoti hai. `class_weight='balanced'` minority class ke samples ko higher penalty deta hai.

**Feature Importance**: Decision Tree har feature ke split se hone wale total Information Gain ko aggregate karke normalize karta hai, jisse feature importance array $\sum f_j = 1$ milta hai.

**Tree Visualization**: `sklearn.tree.plot_tree` se decision nodes, thresholds, impurity values aur sample counts ka graphical flowchart draw kiya ja sakta hai.

---

## 🏛️ Mathematical Architecture & Detailed Theory

### 💻 Scikit-Learn DecisionTreeClassifier Architecture

Scikit-Learn's `DecisionTreeClassifier` is an optimized Cython implementation of the CART (Classification and Regression Trees) algorithm supporting both dense and sparse float32 arrays.

#### Mathematical Feature Importance Formulation:
The importance of feature $j$ is calculated as the sum over all internal nodes $t$ split on feature $j$, weighted by the fraction of samples reaching node $t$:

$$
\boxed{
\text{Imp}(j) = \sum_{t \in \text{Nodes}: \text{split}(t) = j} \left( \frac{N_t}{N} \Delta I(t) \right)
}
$$

The scores are then normalized to sum to $1.0$:

$$
\text{Normalized Imp}(j) = \frac{\text{Imp}(j)}{\sum_{k=1}^d \text{Imp}(k)}
$$

---

## 💻 Python Implementation & Code Example

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# Fit sample classifier
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_syn, y_syn)

# Introspect attributes
print(f"Total Nodes: {clf.tree_.node_count}")
print(f"Max Depth:   {clf.tree_.max_depth}")
print(f"Feature Importances: {clf.feature_importances_}")

# Text tree visualization
tree_rules = export_text(clf, feature_names=[f"Feature_{i}" for i in range(5)])
print("
--- Tree Architecture ---")
print(tree_rules[:300], "...")

```

---

## 🎯 Quick Revision Points (Interview Notes)
- **Scale Invariance**: Decision Trees monotonically invariant hote hain, isliye inme `StandardScaler` mandatory nahi hota.
- **Gini vs Entropy**: Gini speed mein 10x faster hota hai kyunki logarithm computation ki zaroorat nahi padti.
- **Pruning Necessity**: Unconstrained decision tree hamesha overfit karti hai; `min_samples_leaf` aur `ccp_alpha` sabse effective regularizers hain.
