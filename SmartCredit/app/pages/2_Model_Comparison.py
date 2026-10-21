"""
SmartCredit — Model Performance Comparison
Streamlit page: view metrics, confusion matrices, ROC curves,
and feature importance for all trained models.
"""

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="SmartCredit · Models", page_icon="🤖", layout="wide")
st.title("🤖 Model Performance Comparison")

# ── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
METRICS_PATH = os.path.join(BASE_DIR, "reports", "model_metrics.csv")
FIGURES_DIR = os.path.join(BASE_DIR, "reports", "figures")


# ─────────────────────────────────────────────────────────────────────────────
# Section 1 — Metrics table
# ─────────────────────────────────────────────────────────────────────────────
st.subheader("📋 Metrics Summary")

if os.path.exists(METRICS_PATH):
    metrics_df = pd.read_csv(METRICS_PATH)

    # Highlight best values per numeric column
    def highlight_best(s):
        """Highlight the maximum value in each numeric column."""
        if s.dtype in ("float64", "float32", "int64"):
            is_max = s == s.max()
            return ["background-color: #d4edda" if v else "" for v in is_max]
        return [""] * len(s)

    styled = metrics_df.style.apply(highlight_best, axis=0).format(precision=4)
    st.dataframe(styled, width="stretch", hide_index=True)

    # Quick winner callout
    if "F1_Score" in metrics_df.columns and "Model" in metrics_df.columns:
        best_idx = metrics_df["F1_Score"].idxmax()
        best_model = metrics_df.loc[best_idx, "Model"]
        best_f1 = metrics_df.loc[best_idx, "F1_Score"]
        st.success(f"🏆 **Best model**: {best_model} with F1 Score = {best_f1:.4f}")
else:
    st.info(
        "📂 Metrics file not found at `reports/model_metrics.csv`.  \n"
        "Run the training pipeline first:  \n"
        "```bash\npython run_pipeline.py\n```"
    )

# ─────────────────────────────────────────────────────────────────────────────
# Section 2 — Saved Figures
# ─────────────────────────────────────────────────────────────────────────────
st.divider()
st.subheader("📈 Visual Reports")

if os.path.exists(FIGURES_DIR):
    figure_files = sorted(
        [f for f in os.listdir(FIGURES_DIR) if f.endswith((".png", ".jpg", ".jpeg"))]
    )

    if figure_files:
        # Group figures by type for cleaner display
        confusion_figs = [f for f in figure_files if "confusion" in f.lower()]
        roc_figs = [f for f in figure_files if "roc" in f.lower()]
        importance_figs = [f for f in figure_files if "importance" in f.lower() or "feature" in f.lower()]
        other_figs = [
            f
            for f in figure_files
            if f not in confusion_figs + roc_figs + importance_figs
        ]

        # --- Confusion Matrices ---
        if confusion_figs:
            st.markdown("#### 🔢 Confusion Matrices")
            cols = st.columns(min(len(confusion_figs), 3))
            for i, fig_name in enumerate(confusion_figs):
                fig_path = os.path.join(FIGURES_DIR, fig_name)
                cols[i % len(cols)].image(fig_path, caption=fig_name, width="stretch")

        # --- ROC Curves ---
        if roc_figs:
            st.markdown("#### 📉 ROC Curves")
            cols = st.columns(min(len(roc_figs), 3))
            for i, fig_name in enumerate(roc_figs):
                fig_path = os.path.join(FIGURES_DIR, fig_name)
                cols[i % len(cols)].image(fig_path, caption=fig_name, width="stretch")

        # --- Feature Importance ---
        if importance_figs:
            st.markdown("#### 🌲 Feature Importance")
            cols = st.columns(min(len(importance_figs), 3))
            for i, fig_name in enumerate(importance_figs):
                fig_path = os.path.join(FIGURES_DIR, fig_name)
                cols[i % len(cols)].image(fig_path, caption=fig_name, width="stretch")

        # --- Other figures ---
        if other_figs:
            st.markdown("#### 📊 Additional Figures")
            cols = st.columns(min(len(other_figs), 3))
            for i, fig_name in enumerate(other_figs):
                fig_path = os.path.join(FIGURES_DIR, fig_name)
                cols[i % len(cols)].image(fig_path, caption=fig_name, width="stretch")

    else:
        st.info("No figures found in `reports/figures/`. Train the models to generate visualisations.")
else:
    st.info(
        "📂 Figures directory not found at `reports/figures/`.  \n"
        "Run the training pipeline first:  \n"
        "```bash\npython SmartCredit/src/train.py\n```"
    )
