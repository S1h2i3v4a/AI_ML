# Lecture 27.01: Problem Statement & Credit Risk Fundamentals

## 📌 Topic Overview
In this lecture, Shraddha ma'am introduces the **CreditWise Loan Approval System** minor project for **SecureTrust Bank**, detailing the business challenges of credit underwriting and why financial classification requires prioritizing **Precision** over raw Accuracy.

---

## 🏛️ Business Context: SecureTrust Bank
A retail financial institution receives hundreds of daily loan applications for personal and home loans. 
Historically, human credit officers evaluated applications manually. This created two critical vulnerabilities:
1. **High Turnaround Time (TAT)**: 5 to 10 days per decision.
2. **Asymmetric Error Costs**:
   - **Type I Error (False Positive)**: Approving an applicant who defaults $\rightarrow$ **Severe principal loss (₹1,00,000+)**.
   - **Type II Error (False Negative)**: Rejecting a creditworthy applicant $\rightarrow$ **Mild lost interest opportunity (₹10,000)**.

---

## 📊 Visual Diagram: Asymmetric Financial Risk

```mermaid
flowchart TD
    A["Loan Application Received"] --> BModel Decision
    B -->|"Predict Approved (1)"| CActual Borrower Status
    B -->|"Predict Rejected (0)"| DActual Borrower Status

    C -->|"Borrower Repays"| TP["True Positive (TP)<br/>Reward: Net Interest Margin"]
    C -->|"Borrower DEFAULTS!"| FP["False Positive (FP) - TYPE 1 ERROR<br/>CRITICAL LOSS: Lost Principal (10x worse!)"]

    D -->|"Borrower Defaults"| TN["True Negative (TN)<br/>Safe Avoidance"]
    D -->|"Borrower Repays"| FN["False Negative (FN) - TYPE 2 ERROR<br/>Minor Opportunity Loss: Lost Interest"]
```

---

## 💻 Python Implementation

```python
def calculate_loan_portfolio_loss(n_fp, n_fn, principal_loss=100000, interest_loss=10000):
    """
    Demonstrates Asymmetric Financial Loss in Loan Underwriting:
    - False Positive (Type I): Bank approves a defaulter -> Loses entire principal (e.g. Rs 1,00,000)
    - False Negative (Type II): Bank rejects a good borrower -> Loses opportunity interest margin (e.g. Rs 10,000)
    
    False Positives are 10x more costly, explaining why banks prioritize Precision over Accuracy!
    """
    total_fp_loss = n_fp * principal_loss
    total_fn_loss = n_fn * interest_loss
    total_financial_loss = total_fp_loss + total_fn_loss
    
    results = {
        'total_loss': total_financial_loss,
        'fp_loss_ratio': total_fp_loss / (total_financial_loss + 1e-9)
    }
    return results

# --- Function Call & Testing ---
# Suppose 10 defaulters were approved (FP) and 20 good borrowers rejected (FN)
loss_report = calculate_loan_portfolio_loss(n_fp=10, n_fn=20)
print(f"Total Portfolio Loss: Rs {loss_report['total_loss']:,}")
print(f"Loss Driven by False Positives: {loss_report['fp_loss_ratio']*100:.1f}%")
```

---

## 🔑 Key Takeaways
1. In retail lending, False Positives are catastrophic Non-Performing Assets (NPAs).
2. Because of this asymmetry, the CreditWise system optimizes primarily for **Precision**.
