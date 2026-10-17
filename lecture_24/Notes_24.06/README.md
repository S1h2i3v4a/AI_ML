# Lecture 24.06: How to Fix Underfitting & Overfitting

## 📌 Topic Overview
In this lecture, Shraddha ma'am presents the practical **Machine Learning Playbook** for resolving Underfitting and Overfitting in real-world tabular projects.

---

## 🏛️ The Remediation Playbook

```mermaid
flowchart TD
    Issue["Diagnostic Check"] --> Under["Underfitting (High Bias)<br/>Model is too simple!"]
    Issue --> Over["Overfitting (High Variance)<br/>Model is memorizing noise!"]

    Under --> U1["Add Polynomial / Interaction Features"]
    Under --> U2["Increase Model Capacity (More layers / trees)"]
    Under --> U3["Decrease Regularization Penalty (Lower λ)"]

    Over --> O1["Collect More Training Data"]
    Over --> O2["Apply Regularization (L1 Lasso / L2 Ridge)"]
    Over --> O3["Feature Selection: Drop Noisy Predictors"]
    Over --> O4["Prune Complexity (Lower degree / tree depth)"]
```

---

## 💻 Python Implementation

```python
def get_remedies_for_fit_issues():
    """
    Returns the comprehensive engineering playbook to cure
    Underfitting (High Bias) and Overfitting (High Variance).
    """
    remedies = {
        'Fixing Underfitting (High Bias)': [
            "Increase model complexity (e.g., use polynomial degree 2 or 3 instead of linear)",
            "Engineer more informative features and domain interaction terms",
            "Reduce regularization strength (decrease lambda / alpha)",
            "Train longer or optimize training convergence"
        ],
        'Fixing Overfitting (High Variance)': [
            "Collect more training data (dilutes random noise memorization)",
            "Apply Regularization: L1 Lasso (feature sparsity) or L2 Ridge (weight shrinkage)",
            "Reduce model complexity (prune trees, lower polynomial degree)",
            "Perform Feature Selection to drop noisy, irrelevant features",
            "Use K-Fold Cross Validation and early stopping"
        ]
    }
    return remedies

# --- Function Call & Testing ---
playbook = get_remedies_for_fit_issues()
for problem, solutions in playbook.items():
    print(f"=== {problem} ===")
    for sol in solutions:
        print(f" * {sol}")
    print()
```

---

## 🔑 Key Takeaways
1. To fix underfitting: make the model more expressive and feed it richer features.
2. To fix overfitting: constrain the model's freedom via regularization and data expansion.
