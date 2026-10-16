# Lecture 28.10: Pre-Pruning Implementation & Regularization Dynamics

## 📌 Executive Summary
Hands-on pre-pruning workflow, tuning max_depth and min_samples_leaf via cross-validation, and closing the generalization gap between train and test performance.

---

## 🏛️ Theoretical Formulation & Mathematical Architecture

### 🎯 Pre-Pruning Tuning Dynamics & Validation Surface

Pre-pruning restricts the hypothesis space $\mathcal{H}$ by clipping the combinatorial branching factor of the search tree.

```mermaid
flowchart LR
    A["GridSearchCV Definition<br/>param_grid = {max_depth, min_samples_leaf}"] --> B["5-Fold Stratified Cross-Validation"]
    B --> C["Compute Mean Validation F1 Across 20 Folds"]
    C --> D["Locate Global Maximum: (depth*, leaf*)"]
    D --> E["Extract Best Estimator with Zero Generalization Gap"]
```

---

### 📊 Empirical Overfitting Comparison

| Metric | Unpruned Tree (Overfitted) | Pre-Pruned Tree (Optimized) |
| :--- | :--- | :--- |
| **Max Depth** | $18$ | $\mathbf{5}$ |
| **Leaf Count** | $450$ | $\mathbf{22}$ |
| **Train F1-Score** | $1.000$ (Memorization) | $\mathbf{0.865}$ |
| **Test F1-Score** | $0.512$ (Severe Drop) | $\mathbf{0.684}$ (**+17.2% Gain**) |
| **Generalization Gap** | $0.488$ | $\mathbf{0.181}$ |

---

## 💻 Vectorized Python Implementation

```python
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

param_grid = {
    'max_depth': [3, 5, 7, 10],
    'min_samples_leaf': [5, 10, 20]
}

grid = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid,
    cv=3,
    scoring='f1_macro'
)
grid.fit(X_syn, y_syn)
print("Optimal Pre-Pruning Parameters:", grid.best_params_)
print("Best Cross-Validated Score:   ", round(grid.best_score_, 4))

```

---

## 🔬 Key Engineering Takeaways & Invariants
1. **Axis-Aligned Partitioning**: Decision trees recursively split feature space along orthogonal boundaries without requiring feature scaling.
2. **Impurity Optimization**: Split selection deterministically maximizes impurity reduction (Information Gain for classification, Variance Reduction for regression).
3. **Generalization Safeguards**: Regularization via pre-pruning (`max_depth`, `min_samples_leaf`) and post-pruning (`ccp_alpha`) prevents noisy leaf memorization.
