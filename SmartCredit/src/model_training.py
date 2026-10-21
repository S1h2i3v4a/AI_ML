"""
model_training.py — Model training utilities for SmartCredit.

Supports Logistic Regression, Decision Tree (with cost-complexity pruning),
and Random Forest classifiers.  Includes helpers for train/test splitting
and model persistence via joblib.
"""

import os

import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


# ---------------------------------------------------------------------------
# Data splitting
# ---------------------------------------------------------------------------

def split_data(
    df: pd.DataFrame,
    target: str = "Loan_Approved",
    test_size: float = 0.2,
    random_state: int = 42,
):
    """
    Split the DataFrame into training and test sets.

    Parameters
    ----------
    df : pd.DataFrame
        Feature-engineered DataFrame (must include the target column).
    target : str
        Name of the target column.
    test_size : float
        Fraction of data reserved for testing.
    random_state : int
        Random seed for reproducibility.

    Returns
    -------
    X_train, X_test, y_train, y_test : tuple of array-like
    """
    X = df.drop(columns=[target])
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    print(f"Train set: {X_train.shape[0]} samples")
    print(f"Test  set: {X_test.shape[0]} samples")
    print(f"Target distribution (train):\n{y_train.value_counts(normalize=True).to_string()}")
    return X_train, X_test, y_train, y_test


# ---------------------------------------------------------------------------
# Logistic Regression
# ---------------------------------------------------------------------------

def train_logistic_regression(X_train, y_train):
    """
    Train a Logistic Regression classifier.

    Uses ``class_weight='balanced'`` to handle class imbalance and
    ``max_iter=1000`` for convergence.

    Returns
    -------
    LogisticRegression
        Fitted model.
    """
    model = LogisticRegression(
        class_weight="balanced",
        max_iter=1000,
        random_state=42,
    )
    model.fit(X_train, y_train)
    train_acc = model.score(X_train, y_train)
    print(f"Logistic Regression — training accuracy: {train_acc:.4f}")
    return model


# ---------------------------------------------------------------------------
# Decision Tree with cost-complexity pruning
# ---------------------------------------------------------------------------

def train_decision_tree(X_train, y_train):
    """
    Train a Decision Tree classifier with cost-complexity pruning.

    Procedure
    ---------
    1. Fit a full (unpruned) tree to obtain the effective-alpha path.
    2. Evaluate each candidate ``ccp_alpha`` via 5-fold cross-validation.
    3. Retrain a final tree using the ``ccp_alpha`` that maximises mean CV
       accuracy.

    Returns
    -------
    DecisionTreeClassifier
        Pruned, fitted model.
    """
    # Step 1: fit a full tree to get the ccp_alpha path
    full_tree = DecisionTreeClassifier(
        class_weight="balanced", random_state=42
    )
    full_tree.fit(X_train, y_train)

    path = full_tree.cost_complexity_pruning_path(X_train, y_train)
    ccp_alphas = [a for a in path.ccp_alphas if a >= 0]
    if len(ccp_alphas) > 20:
        step = len(ccp_alphas) // 20
        ccp_alphas = ccp_alphas[::step]

    # Step 2: cross-validate each alpha
    best_alpha = 0.0
    best_score = 0.0
    for alpha in ccp_alphas:
        dt = DecisionTreeClassifier(
            ccp_alpha=alpha, class_weight="balanced", random_state=42
        )
        scores = cross_val_score(dt, X_train, y_train, cv=5, scoring="accuracy")
        mean_score = scores.mean()
        if mean_score > best_score:
            best_score = mean_score
            best_alpha = alpha

    print(f"Decision Tree — best ccp_alpha: {best_alpha:.6f}  "
          f"(CV accuracy: {best_score:.4f})")

    # Step 3: retrain with optimal alpha
    model = DecisionTreeClassifier(
        ccp_alpha=best_alpha, class_weight="balanced", random_state=42
    )
    model.fit(X_train, y_train)
    train_acc = model.score(X_train, y_train)
    print(f"Decision Tree — training accuracy: {train_acc:.4f}")
    return model


# ---------------------------------------------------------------------------
# Random Forest
# ---------------------------------------------------------------------------

def train_random_forest(X_train, y_train):
    """
    Train a Random Forest classifier.

    Uses 200 estimators with ``class_weight='balanced'``.

    Returns
    -------
    RandomForestClassifier
        Fitted model.
    """
    model = RandomForestClassifier(
        n_estimators=200,
        class_weight="balanced",
        random_state=42,
    )
    model.fit(X_train, y_train)
    train_acc = model.score(X_train, y_train)
    print(f"Random Forest — training accuracy: {train_acc:.4f}")
    return model


# ---------------------------------------------------------------------------
# Model persistence
# ---------------------------------------------------------------------------

def save_model(model, filepath: str) -> None:
    """Save a fitted model to disk using joblib."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    joblib.dump(model, filepath)
    print(f"Model saved → {filepath}")


def load_model(filepath: str):
    """Load a previously saved model from disk."""
    model = joblib.load(filepath)
    print(f"Model loaded ← {filepath}")
    return model


# ---------------------------------------------------------------------------
# Train-all orchestrator
# ---------------------------------------------------------------------------

def train_all_models(X_train, y_train, save_dir: str) -> dict:
    """
    Train all three models, save them to ``save_dir``, and return a dict.

    Parameters
    ----------
    X_train, y_train : array-like
        Training data and labels.
    save_dir : str
        Directory where ``.pkl`` model files will be saved.

    Returns
    -------
    dict
        ``{'Logistic Regression': model, 'Decision Tree': model,
           'Random Forest': model}``
    """
    os.makedirs(save_dir, exist_ok=True)
    models = {}

    print("\n--- Logistic Regression ---")
    lr = train_logistic_regression(X_train, y_train)
    save_model(lr, os.path.join(save_dir, "logistic_regression.pkl"))
    models["Logistic Regression"] = lr

    print("\n--- Decision Tree ---")
    dt = train_decision_tree(X_train, y_train)
    save_model(dt, os.path.join(save_dir, "decision_tree.pkl"))
    models["Decision Tree"] = dt

    print("\n--- Random Forest ---")
    rf = train_random_forest(X_train, y_train)
    save_model(rf, os.path.join(save_dir, "random_forest.pkl"))
    models["Random Forest"] = rf

    print(f"\nAll models trained and saved to: {save_dir}")
    return models
