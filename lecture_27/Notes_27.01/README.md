# Lecture 27.01: Problem Statement & Credit Risk Fundamentals

## 📌 Executive Summary
Real-world banking case study for SecureTrust Bank, the asymmetric cost of underwriting errors, Type I vs Type II errors, and the business rationale for precision-focused machine learning in loan approvals.

---

## 🏛️ Theoretical Formulation & Mathematical Architecture

### 🏦 SecureTrust Bank Business Problem Statement

In contemporary retail banking and financial institutions, **Credit Risk Underwriting** is the core operational process that determines an institution's solvency and profitability. 

A mid-sized financial company named **SecureTrust Bank** offers personal and home loans across urban and rural regions in India. Every day, hundreds of applicants submit documentation. Historically, SecureTrust Bank relied on a manual underwriting protocol where credit officers inspected paper income proofs, tax filings, and subjective character references.

#### Core Operational Vulnerabilities of Manual Underwriting:
1. **High Latency & Inefficiency**: Turnaround time (TAT) per loan application averaged 5 to 10 business days.
2. **Cognitive Bias & Inconsistency**: Different loan officers in different branches applied disparate heuristic criteria to identical applicant profiles.
3. **The Dual Risk Dilemma**:
   - **Good Customers Wrongly Rejected (Type II Error / False Negative)**: Loss of prime banking relationships and interest income to competitor NBFCs.
   - **High-Risk Borrowers Wrongly Approved (Type I Error / False Positive)**: Direct credit default leading to Non-Performing Assets (NPAs) and capital write-offs.

---

### ⚖️ The Asymmetry of Financial Classification Errors

In traditional machine learning benchmarks (e.g., MNIST digit recognition), all misclassifications carry an identical loss penalty. In financial risk management, the loss matrix is **severely asymmetric**:

```mermaid
flowchart TD
    A["Loan Application Received"] --> B{"Model Decision"}
    B -->|"Predict Approved (y_hat = 1)"| C{"Actual True Status"}
    B -->|"Predict Rejected (y_hat = 0)"| D{"Actual True Status"}
    
    C -->|"Borrower Repays (y = 1)"| E["True Positive (TP)<br/>Reward: Net Interest Margin (+₹50,000)"]
    C -->|"Borrower Defaults (y = 0)"| F["False Positive (FP) - TYPE I ERROR<br/>Severe Loss: Unrecovered Principal (-₹500,000)"]
    
    D -->|"Borrower Defaults (y = 0)"| G["True Negative (TN)<br/>Reward: Loss Avoidance (₹0 / Safe Capital)"]
    D -->|"Borrower Repays (y = 1)"| H["False Negative (FN) - TYPE II ERROR<br/>Mild Loss: Lost Interest Opportunity (-₹20,000)"]
```

#### Mathematical Formulation of Underwriting Utility:
Let $C_{	ext{FP}}$ denote the financial loss incurred from approving a borrower who subsequently defaults, and let $C_{	ext{FN}}$ denote the opportunity loss from rejecting a creditworthy borrower:

$$
	ext{Cost}(	ext{FP}) pprox 	ext{Loan Principal} 	imes 	ext{Loss Given Default (LGD)}
$$

$$
	ext{Cost}(	ext{FN}) pprox 	ext{Loan Principal} 	imes 	ext{Net Interest Margin (NIM)}
$$

In commercial retail banking, typically:

$$
rac{C_{	ext{FP}}}{C_{	ext{FN}}} \in [5, 20]
$$

Because a single default can wipe out the profit margins of 10 to 15 successfully repaid loans, the operational objective function must heavily prioritize **Precision**:

$$
	ext{Precision} = rac{	ext{TP}}{	ext{TP} + 	ext{FP}}
$$

A high-precision underwriting engine guarantees that when the system issues an **Approved** decision, the probability of borrower default is minimized.

---

## 💻 Vectorized Python Implementation

```python
import numpy as np
import pandas as pd

# Financial Utility Matrix simulation
def calculate_underwriting_utility(tp, fp, fn, tn, 
                                   interest_gain=50000.0, 
                                   default_loss=250000.0, 
                                   opportunity_loss=10000.0):
    net_profit = (tp * interest_gain) - (fp * default_loss) - (fn * opportunity_loss)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    return {
        "Net_Profit_INR": net_profit,
        "Precision": precision,
        "Recall": recall
    }

# Benchmark: Model A (Balanced) vs Model B (High Precision)
model_a = calculate_underwriting_utility(tp=80, fp=25, fn=20, tn=75)
model_b = calculate_underwriting_utility(tp=65, fp=5, fn=35, tn=95)

print("Model A (Naive Balanced):", model_a)
print("Model B (High-Precision Guarded):", model_b)
assert model_b["Net_Profit_INR"] > model_a["Net_Profit_INR"], "High-precision underwriting must preserve bank capital!"

```

---

## 🔬 Key Engineering Takeaways & Invariants
1. **Mathematical Grounding**: Every transformation and classification step directly addresses the underlying empirical distribution and financial risk constraints.
2. **Reproducibility**: Clean, leak-free pipeline partitioning guarantees that performance metrics match production operating realities.
3. **Domain Alignment**: Aligning model evaluation with the asymmetric cost of financial errors protects institutional solvency.
