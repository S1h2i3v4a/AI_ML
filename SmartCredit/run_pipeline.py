"""
============================================================
SmartCredit — Main Training Pipeline
============================================================
Run this script to execute the complete ML pipeline:
  1. Load raw data
  2. Preprocess & clean
  3. Engineer features
  4. Train all 3 models
  5. Evaluate & generate reports
  6. Save the best model for Streamlit app

Usage:
    cd SmartCredit
    python run_pipeline.py
============================================================
"""

import os
import sys
import warnings

# Ensure UTF-8 output on Windows
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except AttributeError:
    pass

import joblib

warnings.filterwarnings("ignore")

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from data_loader import load_raw_data, get_data_summary
from preprocessing import preprocess_pipeline
from feature_engineering import engineer_all_features
from model_training import split_data, train_all_models
from evaluation import generate_full_report


def main():
    """Execute the complete SmartCredit ML pipeline."""

    # ── Paths ──────────────────────────────────────────────
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    RAW_DATA = os.path.join(BASE_DIR, "data", "raw", "loan_data.csv")
    PROCESSED_DATA = os.path.join(BASE_DIR, "data", "processed", "loan_cleaned.csv")
    MODELS_DIR = os.path.join(BASE_DIR, "models")
    REPORTS_DIR = os.path.join(BASE_DIR, "reports")
    FIGURES_DIR = os.path.join(REPORTS_DIR, "figures")

    os.makedirs(MODELS_DIR, exist_ok=True)
    os.makedirs(FIGURES_DIR, exist_ok=True)

    print("=" * 60)
    print("🏦 SmartCredit — Training Pipeline")
    print("=" * 60)

    # ── Step 1: Load Raw Data ──────────────────────────────
    print("\n📥 Step 1: Loading raw data...")
    df_raw = load_raw_data(RAW_DATA)
    summary = get_data_summary(df_raw)
    print(f"   ✅ Loaded {summary['shape'][0]} rows × {summary['shape'][1]} columns")
    print(f"   ⚠️  Total missing values: {summary['missing_counts'].sum()}")

    # ── Step 2: Preprocess ─────────────────────────────────
    print("\n🧹 Step 2: Preprocessing data...")
    df_clean = preprocess_pipeline(RAW_DATA)
    print(f"   ✅ After cleaning: {df_clean.shape[0]} rows × {df_clean.shape[1]} columns")
    print(f"   ✅ Missing values remaining: {df_clean.isnull().sum().sum()}")

    # ── Step 3: Feature Engineering ────────────────────────
    print("\n⚙️  Step 3: Engineering features...")
    df_features = engineer_all_features(df_clean)
    print(f"   ✅ Feature matrix: {df_features.shape[0]} rows × {df_features.shape[1]} columns")
    print(f"   📋 Feature list: {list(df_features.columns)[:10]}... ({len(df_features.columns)} total)")

    # Save processed data
    df_features.to_csv(PROCESSED_DATA, index=False)
    print(f"   💾 Saved processed data to: {PROCESSED_DATA}")

    # ── Step 4: Train/Test Split ───────────────────────────
    print("\n✂️  Step 4: Splitting data (80/20)...")
    X_train, X_test, y_train, y_test = split_data(df_features, target="Loan_Approved")
    print(f"   ✅ Train set: {X_train.shape[0]} samples")
    print(f"   ✅ Test set:  {X_test.shape[0]} samples")
    print(f"   📊 Target distribution (train): {y_train.value_counts().to_dict()}")

    # Save feature column names for Streamlit app
    feature_columns_path = os.path.join(MODELS_DIR, "feature_columns.joblib")
    joblib.dump(list(X_train.columns), feature_columns_path)
    print(f"   💾 Saved feature columns to: {feature_columns_path}")

    # ── Step 5: Train All Models ───────────────────────────
    print("\n🤖 Step 5: Training models...")
    models = train_all_models(X_train, y_train, save_dir=MODELS_DIR)
    print(f"   ✅ Trained {len(models)} models: {list(models.keys())}")

    # ── Step 6: Evaluate & Report ──────────────────────────
    print("\n📊 Step 6: Evaluating models & generating reports...")
    metrics_df = generate_full_report(
        models_dict=models,
        X_test=X_test,
        y_test=y_test,
        feature_names=list(X_train.columns),
        save_dir=REPORTS_DIR,
    )

    print("\n" + "=" * 60)
    print("📈 MODEL COMPARISON RESULTS")
    print("=" * 60)
    print(metrics_df.to_string(index=True))

    # ── Step 7: Select & Save Best Model ───────────────────
    auc_col = "roc_auc" if "roc_auc" in metrics_df.columns else "ROC_AUC"
    best_model_name = metrics_df[auc_col].idxmax()
    best_model = models[best_model_name]
    best_model_path = os.path.join(MODELS_DIR, "best_model.joblib")
    joblib.dump(best_model, best_model_path)

    # Also save best model name
    joblib.dump(best_model_name, os.path.join(MODELS_DIR, "best_model_name.joblib"))

    print(f"\n🏆 Best Model: {best_model_name} (ROC-AUC = {metrics_df.loc[best_model_name, auc_col]:.4f})")
    print(f"💾 Saved to: {best_model_path}")

    print("\n" + "=" * 60)
    print("✅ PIPELINE COMPLETE!")
    print("=" * 60)
    print(f"\n🚀 Now run the Streamlit app:")
    print(f"   cd SmartCredit")
    print(f"   streamlit run app/app.py")


if __name__ == "__main__":
    main()
