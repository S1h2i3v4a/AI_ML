"""
evaluation.py — Model evaluation and reporting for SmartCredit.

Produces classification metrics, comparison tables, confusion-matrix plots,
ROC curves, feature-importance charts, and a consolidated CSV report.
"""

import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    roc_curve,
    confusion_matrix,
    ConfusionMatrixDisplay,
)

# Global plot style
plt.style.use("seaborn-v0_8-whitegrid")


# ---------------------------------------------------------------------------
# Single-model classification report
# ---------------------------------------------------------------------------

def get_classification_report(model, X_test, y_test, model_name: str) -> dict:
    """
    Compute classification metrics for a single model.

    Parameters
    ----------
    model : estimator
        Fitted sklearn-compatible classifier.
    X_test, y_test : array-like
        Test features and true labels.
    model_name : str
        Human-readable name (used as a label in reports).

    Returns
    -------
    dict
        Keys: model_name, accuracy, precision, recall, f1, roc_auc.
    """
    y_pred = model.predict(X_test)

    # Probabilities for ROC-AUC (use positive class)
    if hasattr(model, "predict_proba"):
        y_prob = model.predict_proba(X_test)[:, 1]
        auc = roc_auc_score(y_test, y_prob)
    else:
        auc = None

    report = {
        "model_name": model_name,
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, zero_division=0),
        "recall": recall_score(y_test, y_pred, zero_division=0),
        "f1": f1_score(y_test, y_pred, zero_division=0),
        "roc_auc": auc,
    }
    return report


# ---------------------------------------------------------------------------
# Multi-model comparison
# ---------------------------------------------------------------------------

def compare_models(models_dict: dict, X_test, y_test) -> pd.DataFrame:
    """
    Compare multiple models and return a tidy DataFrame of metrics.

    Parameters
    ----------
    models_dict : dict
        ``{model_name: fitted_model, ...}``
    X_test, y_test : array-like

    Returns
    -------
    pd.DataFrame
        One row per model with columns: model_name, accuracy, precision,
        recall, f1, roc_auc.
    """
    rows = []
    for name, model in models_dict.items():
        rows.append(get_classification_report(model, X_test, y_test, name))
    comparison_df = pd.DataFrame(rows).set_index("model_name")
    print("\nModel Comparison:")
    print(comparison_df.to_string())
    return comparison_df


# ---------------------------------------------------------------------------
# Confusion matrices
# ---------------------------------------------------------------------------

def plot_confusion_matrices(
    models_dict: dict, X_test, y_test, save_dir: str
) -> None:
    """
    Plot confusion matrices for all models in a 1×3 subplot grid and save
    the figure as a PNG.

    Parameters
    ----------
    models_dict : dict
    X_test, y_test : array-like
    save_dir : str
        Directory where the image will be saved.
    """
    os.makedirs(save_dir, exist_ok=True)

    n_models = len(models_dict)
    fig, axes = plt.subplots(1, n_models, figsize=(6 * n_models, 5))

    # Handle single-model edge case
    if n_models == 1:
        axes = [axes]

    for ax, (name, model) in zip(axes, models_dict.items()):
        y_pred = model.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["No", "Yes"])
        disp.plot(ax=ax, cmap="Blues", colorbar=False)
        ax.set_title(name, fontsize=13, fontweight="bold")

    fig.suptitle("Confusion Matrices", fontsize=15, fontweight="bold", y=1.02)
    filepath = os.path.join(save_dir, "confusion_matrices.png")
    fig.savefig(filepath, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Confusion matrices saved → {filepath}")


# ---------------------------------------------------------------------------
# ROC curves
# ---------------------------------------------------------------------------

def plot_roc_curves(
    models_dict: dict, X_test, y_test, save_dir: str
) -> None:
    """
    Overlay ROC curves for all models on a single plot and save the figure.

    Parameters
    ----------
    models_dict : dict
    X_test, y_test : array-like
    save_dir : str
    """
    os.makedirs(save_dir, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 6))

    for name, model in models_dict.items():
        if hasattr(model, "predict_proba"):
            y_prob = model.predict_proba(X_test)[:, 1]
            fpr, tpr, _ = roc_curve(y_test, y_prob)
            auc = roc_auc_score(y_test, y_prob)
            ax.plot(fpr, tpr, linewidth=2, label=f"{name} (AUC = {auc:.3f})")

    # Diagonal reference line
    ax.plot([0, 1], [0, 1], "k--", linewidth=1, label="Random (AUC = 0.500)")

    ax.set_xlabel("False Positive Rate", fontsize=12)
    ax.set_ylabel("True Positive Rate", fontsize=12)
    ax.set_title("ROC Curves", fontsize=15, fontweight="bold")
    ax.legend(loc="lower right", fontsize=10)

    filepath = os.path.join(save_dir, "roc_curves.png")
    fig.savefig(filepath, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"ROC curves saved → {filepath}")


# ---------------------------------------------------------------------------
# Feature importance
# ---------------------------------------------------------------------------

def plot_feature_importance(
    model,
    feature_names: list,
    top_n: int = 10,
    save_dir: str = None,
) -> None:
    """
    Plot a horizontal bar chart of the top N most important features.

    Works with any model exposing ``feature_importances_`` (tree-based) or
    ``coef_`` (linear models).

    Parameters
    ----------
    model : estimator
    feature_names : list
    top_n : int
    save_dir : str or None
        If provided, save the figure to this directory.
    """
    # Extract importances
    if hasattr(model, "feature_importances_"):
        importances = model.feature_importances_
    elif hasattr(model, "coef_"):
        importances = np.abs(model.coef_).flatten()
    else:
        print("Model does not expose feature importances.")
        return

    feat_imp = pd.Series(importances, index=feature_names).sort_values(ascending=True)
    feat_imp = feat_imp.tail(top_n)

    fig, ax = plt.subplots(figsize=(8, max(4, top_n * 0.45)))
    feat_imp.plot.barh(ax=ax, color="steelblue", edgecolor="black")
    ax.set_xlabel("Importance", fontsize=12)
    ax.set_title(f"Top {top_n} Feature Importances", fontsize=14, fontweight="bold")

    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        filepath = os.path.join(save_dir, "feature_importance.png")
        fig.savefig(filepath, dpi=300, bbox_inches="tight")
        print(f"Feature importance plot saved → {filepath}")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Full evaluation report
# ---------------------------------------------------------------------------

def generate_full_report(
    models_dict: dict,
    X_test,
    y_test,
    feature_names: list,
    save_dir: str,
) -> pd.DataFrame:
    """
    Run the complete evaluation suite and save all outputs.

    Outputs
    -------
    - ``model_comparison.csv``    : metrics table
    - ``confusion_matrices.png``  : side-by-side confusion matrices
    - ``roc_curves.png``          : overlaid ROC curves
    - ``feature_importance.png``  : bar chart (using the last model in dict)

    Parameters
    ----------
    models_dict : dict
    X_test, y_test : array-like
    feature_names : list
    save_dir : str

    Returns
    -------
    pd.DataFrame
        Model comparison DataFrame.
    """
    os.makedirs(save_dir, exist_ok=True)

    print("=" * 60)
    print("FULL EVALUATION REPORT")
    print("=" * 60)

    # 1. Comparison table
    print("\n[1/4] Computing classification metrics...")
    comparison_df = compare_models(models_dict, X_test, y_test)
    csv_path = os.path.join(save_dir, "model_comparison.csv")
    comparison_df.to_csv(csv_path)
    print(f"Metrics saved → {csv_path}")

    # Also save model_metrics.csv with capitalized columns for Streamlit UI
    metrics_formatted = comparison_df.reset_index().rename(columns={
        "model_name": "Model",
        "accuracy": "Accuracy",
        "precision": "Precision",
        "recall": "Recall",
        "f1": "F1_Score",
        "roc_auc": "ROC_AUC",
    })
    metrics_formatted_path = os.path.join(save_dir, "model_metrics.csv")
    metrics_formatted.to_csv(metrics_formatted_path, index=False)
    print(f"Streamlit metrics saved → {metrics_formatted_path}")

    # Figures directory
    fig_dir = os.path.join(save_dir, "figures")
    os.makedirs(fig_dir, exist_ok=True)

    # 2. Confusion matrices
    print("\n[2/4] Plotting confusion matrices...")
    plot_confusion_matrices(models_dict, X_test, y_test, save_dir)
    plot_confusion_matrices(models_dict, X_test, y_test, fig_dir)

    # 3. ROC curves
    print("\n[3/4] Plotting ROC curves...")
    plot_roc_curves(models_dict, X_test, y_test, save_dir)
    plot_roc_curves(models_dict, X_test, y_test, fig_dir)

    # 4. Feature importance (use Random Forest if available, else last model)
    print("\n[4/4] Plotting feature importance...")
    fi_model = models_dict.get("Random Forest", list(models_dict.values())[-1])
    plot_feature_importance(fi_model, feature_names, top_n=10, save_dir=save_dir)
    plot_feature_importance(fi_model, feature_names, top_n=10, save_dir=fig_dir)

    print("\n" + "=" * 60)
    print(f"All evaluation artefacts saved to: {save_dir}")
    print("=" * 60)
    return comparison_df
