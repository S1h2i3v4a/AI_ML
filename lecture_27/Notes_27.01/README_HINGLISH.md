# Notes_27.01: Problem Statement Aur Credit Risk Ke Fundamentals [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne **CreditWise Loan Approval System** minor project ka business background samjhaya hai: Bank loan approval mein **Type 1** aur **Type 2** errors ka kitna bada financial impact hota hai aur Precision kyu zaroori hai.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- SecureTrust Bank ka real-world business case.
- Manual loan verification ki kamzoriyan.
- **Type I Error** (Defaulter ko loan dena) vs **Type II Error** (Achhe customer ko reject karna).
- Banking mein Accuracy ke bajaye **Precision** ko kyu priority di jaati hai.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. SecureTrust Bank Ki Problem:
Pehle bank ke officers haath se document verify karte the, jisme 5 se 10 din lagte the. Humein ek aisa automated machine learning model banana hai jo instant aur accurate faisla le sake.

#### 2. Dono Galtiyon Ka Asar (Asymmetric Loss):
1. **False Positive (Type 1 Error)**:
   - Kisi aise insaan ko loan pass kar diya jo paise le kar bhaag gaya (Default kar gaya).
   - **Nuksaan**: Bank ka poora mool-dhan (principal amount) doob gaya (₹1,00,000 se ₹10,00,000 tak ka nuksaan!).
2. **False Negative (Type 2 Error)**:
   - Kisi imandar customer ko galti se reject kar diya.
   - **Nuksaan**: Sirf us loan ka byaj (interest) nahi mila (₹5,000 se ₹10,000 ka nuksaan).

Kyunki False Positive 10 se 20 guna zyada nuksaandeh hota hai, isliye banking models mein **Precision** ko sabse pehle dekha jata hai!

---

### 📊 Visual Flowchart: Loan Approval Ki Asymmetric Risk

```mermaid
flowchart TD
    A["Loan Application Aayi"] --> BModel Ka Faisla
    B -->|"Approved Bol Diya"| CAsal Mein Kya Hua?
    B -->|"Reject Bol Diya"| DAsal Mein Kya Hua?

    C -->|"Paisa Wapas Diya"| TP["True Positive (Faayda)"]
    C -->|"DEFAULTER Nikla!"| FP["False Positive (Type 1)<br/>BOHOT BADA NUKSAAN: Poora Principal Doob Gaya!"]

    D -->|"Defaulter Tha"| TN["True Negative (Bach Gaye)"]
    D -->|"Achha Customer Tha"| FN["False Negative (Type 2)<br/>Chhota Nuksaan: Sirf Interest Miss Hua"]
```

---

### 💻 Python Code

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

### 📌 Summary Points
- Banking mein False Positive sabse bada khatra hai.
- Is project ka main goal **Precision maximize karna** hai.
