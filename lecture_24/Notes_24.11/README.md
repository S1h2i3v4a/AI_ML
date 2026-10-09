# Module 24.11: Using LassoCV for Automated Hyperparameter Tuning

## 1. The Challenge of Selecting Optimal $\alpha$

The regularization strength $\alpha$ is a **hyperparameter**—it cannot be learned directly by minimizing the training loss, because minimizing training loss trivially selects $\alpha = 0$ (unregularized OLS).
Determining the optimal $\alpha^*$ requires evaluating generalization error across unseen validation folds via **K-Fold Cross-Validation**.

---

## 2. Algorithmic Mechanics of LassoCV

Scikit-learn's `LassoCV` automates the search across an array of candidate $\alpha$ values using an integrated coordinate descent path algorithm:

```
For each candidate alpha in [alpha_1, alpha_2, ..., alpha_k]:
    For each fold k in K-Fold Cross Validation:
        1. Train Lasso on K-1 folds
        2. Evaluate validation MSE on fold k
    Average the MSE across all K folds -> Mean CV Loss(alpha)

Select alpha* = argmin Mean CV Loss(alpha)
Re-fit Lasso on the ENTIRE training set using alpha*
```

---

## 3. Inspecting the Fitted LassoCV Object

After calling `model.fit(X_train, y_train)`:
- `model.alpha_`: The single optimal regularization strength chosen by cross-validation.
- `model.coef_`: The final feature coefficients learned at `alpha_`.
- `model.mse_path_`: Matrix of shape `(n_alphas, n_folds)` containing validation errors for every fold and candidate parameter.
