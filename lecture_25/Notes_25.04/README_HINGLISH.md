# Notes_25.04: Classification Ke Evaluation Metrics [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne sikhaya hai ki sirf Accuracy par bharosa kyu nahi karna chahiye, aur **Precision**, **Recall**, aur **F1 Score** ke formulas aur unki real-life importance kya hai.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Accuracy ka formula aur imbalanced data mein iski kamzori.
- Precision ka matlab aur spam detection example.
- Recall (Sensitivity) ka matlab aur cancer detection example.
- F1 Score: Harmonic mean kyu use karte hain.
- Precision vs Recall tradeoff: Kab kisse prioritize karein?

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Accuracy (Overall Sahi Faisle)
- **Formula**:

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

- **Problem**: Maan lijiye 100 logon mein se 99 swasth hain aur 1 ko cancer hai. Agar model aankh band karke sabko "Healthy" bol de, toh bhi uski Accuracy **99%** aayegi! Lekin usne us ek cancer mareez ko marne ke liye chhod diya. Isliye accuracy dhokha de sakti hai.

#### 2. Precision (Galti Na Karne Ki Shuddhata)
- **Formula**:

$$\text{Precision} = \frac{TP}{TP + FP}$$

- **Sawal**: *"Jab model ne 'Positive' bola, toh wo kitni baar sach mein sahi tha?"*
- **Kahan Zaroori Hai?**: Jahan **False Positive (Type 1)** bohot costly ho. Jaise Spam Detection: Agar bank ka OTP ya job offer letter galti se spam mein chala gaya toh user ka bohot bada nuksaan ho jayega!

#### 3. Recall / Sensitivity (Pakadne Ki Shamta)
- **Formula**:

$$\text{Recall} = \frac{TP}{TP + FN}$$

- **Sawal**: *"Total bimari wale logon mein se model ne kitne logon ko pakad liya?"*
- **Kahan Zaroori Hai?**: Jahan **False Negative (Type 2)** jaanleva ho. Jaise Cancer Detection ya Fire Alarm: Chahe do normal logon ko test ke liye dubara bula lo (FP), lekin ek bhi cancer patient chhootna nahi chahiye (FN zero hona chahiye!).

#### 4. F1 Score (Dono Ka Santulan)
- **Formula**:

$$\text{F1 Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

- Precision aur Recall ka **Harmonic Mean** hota hai. Yeh tab use hota hai jab humein Precision aur Recall dono achha chahiye ho.

---

### 📊 Visual Flowchart: Kab Kisko Chunein?

```mermaid
flowchart TD
    QBusiness Problem Kya Hai?
    Q -->|"Spam Filter / Loan Approval<br/>False Positive se bacho!"| P["Prioritize PRECISION"]
    Q -->|"Medical Diagnosis / Fraud Detection<br/>False Negative se bacho!"| R["Prioritize RECALL"]
    P --> F["Dono ka balance: F1 Score"]
    R --> F
```

---

### 💻 Python Code

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_classification_performance(y_true, y_pred):
    """
    Computes all standard classification metrics:
    - Accuracy:  Overall correctness
    - Precision: Confidence when predicting positive (Minimizes FP)
    - Recall:    Ability to capture all actual positives (Minimizes FN)
    - F1-Score:  Harmonic mean of Precision and Recall
    """
    acc  = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec  = recall_score(y_true, y_pred, zero_division=0)
    f1   = f1_score(y_true, y_pred, zero_division=0)

    results = {
        'accuracy':  float(acc),
        'precision': float(prec),
        'recall':    float(rec),
        'f1_score':  float(f1)
    }
    return results

# --- Function Call & Testing ---
# Real-world scenario: Imbalanced medical test
y_actual    = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
y_predicted = [0, 0, 0, 0, 0, 1, 0, 0, 1, 1]

metrics = evaluate_classification_performance(y_actual, y_predicted)
print(f"Accuracy:  {metrics['accuracy']:.3f}")
print(f"Precision: {metrics['precision']:.3f} (When model says Positive, it is right 66.7% of the time)")
print(f"Recall:    {metrics['recall']:.3f} (Model caught 66.7% of actual disease cases)")
print(f"F1-Score:  {metrics['f1_score']:.3f}")
```

---

### 📌 Summary Points
- Imbalanced data mein accuracy ke bajaye F1-score dekhein.
- False Positive se bachna ho toh **Precision** badhao.
- False Negative se bachna ho toh **Recall** badhao.
