"""
test_pipeline.py — Unit and integration tests for SmartCredit.

Run with:
    pytest tests/
or:
    python -m unittest tests/test_pipeline.py
"""

import os
import sys
import unittest
import numpy as np
import pandas as pd
import joblib

# Add src to path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(BASE_DIR, "src"))

from data_loader import load_raw_data, get_data_summary
from preprocessing import handle_missing_values, encode_target
from feature_engineering import create_income_features, create_credit_tiers, create_risk_flags


class TestSmartCreditPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw_data_path = os.path.join(BASE_DIR, "data", "raw", "loan_data.csv")
        cls.model_path = os.path.join(BASE_DIR, "models", "best_model.joblib")
        cls.feature_cols_path = os.path.join(BASE_DIR, "models", "feature_columns.joblib")

    def test_01_data_loader(self):
        """Test that data loads properly and returns expected columns."""
        df = load_raw_data(self.raw_data_path)
        self.assertGreater(df.shape[0], 500, "Dataset should have at least 500 rows.")
        self.assertIn("Loan_Approved", df.columns, "Target column must exist.")

        summary = get_data_summary(df)
        self.assertIn("shape", summary)
        self.assertIn("missing_counts", summary)

    def test_02_missing_values_handling(self):
        """Test that handle_missing_values leaves 0 missing values."""
        df = load_raw_data(self.raw_data_path)
        df_clean = handle_missing_values(df)
        self.assertEqual(df_clean.isnull().sum().sum(), 0, "No NaNs should remain after cleaning.")
        self.assertEqual(len(df_clean), 950, "50 rows with null target should be dropped.")

    def test_03_target_encoding(self):
        """Test target encoding maps Yes->1 and No->0."""
        df = pd.DataFrame({"Loan_Approved": ["Yes", "No", "Yes", "No"]})
        df_enc = encode_target(df)
        self.assertListEqual(df_enc["Loan_Approved"].tolist(), [1, 0, 1, 0])

    def test_04_feature_engineering_income(self):
        """Test income feature derivations."""
        df = pd.DataFrame({
            "Applicant_Income": [10000.0, 5000.0],
            "Coapplicant_Income": [2000.0, 0.0],
            "Loan_Amount": [24000.0, 10000.0],
        })
        df_feat = create_income_features(df)
        self.assertIn("total_income", df_feat.columns)
        self.assertIn("income_loan_ratio", df_feat.columns)
        self.assertAlmostEqual(df_feat.loc[0, "total_income"], 12000.0)
        self.assertAlmostEqual(df_feat.loc[0, "income_loan_ratio"], 0.5)

    def test_05_feature_engineering_credit_tiers(self):
        """Test credit score tier categorization."""
        df = pd.DataFrame({"Credit_Score": [500, 600, 700, 800]})
        df_tiers = create_credit_tiers(df)
        expected = ["Poor", "Fair", "Good", "Excellent"]
        self.assertListEqual(list(df_tiers["credit_tier"]), expected)

    def test_06_saved_model_and_prediction(self):
        """Test that saved model can make valid predictions on sample feature vector."""
        self.assertTrue(os.path.exists(self.model_path), "Model file must exist.")
        self.assertTrue(os.path.exists(self.feature_cols_path), "Feature columns file must exist.")

        model = joblib.load(self.model_path)
        feature_cols = joblib.load(self.feature_cols_path)

        # Create a single zeroed sample with correct columns
        sample_df = pd.DataFrame([np.zeros(len(feature_cols))], columns=feature_cols)

        pred = model.predict(sample_df)
        self.assertIn(pred[0], [0, 1], "Prediction must be 0 (No) or 1 (Yes).")

        if hasattr(model, "predict_proba"):
            prob = model.predict_proba(sample_df)
            self.assertEqual(prob.shape, (1, 2), "Probabilities should have 2 classes.")
            self.assertAlmostEqual(prob.sum(), 1.0, places=4)


if __name__ == "__main__":
    unittest.main()
