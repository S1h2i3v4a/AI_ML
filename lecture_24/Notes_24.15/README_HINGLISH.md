# Notes_24.15: Logistic Regression Implementation Aur Evaluation [Hinglish]

## 📌 Topic Overview
Is final lecture mein Shraddha ma'am ne **Heart Disease Dataset** (`heart.csv`) par Logistic Regression ka complete live implementation karke dikhaya hai: scaling se lekar model training aur Confusion Matrix evaluation tak.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- `heart.csv` par Logistic Regression lagana.
- `StandardScaler` lagana kyu zaroori hai?
- Accuracy, Precision, Recall, aur F1-Score ka report.
- Confusion Matrix ka analysis.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Scaling Kyu Zaroori Thi?
Dataset mein `chol` (Cholesterol) 250-300 ke beech tha aur baaki features chhotey the. Agar scaling na karein, toh Gradient Descent cholesterol ke hisab se bhaagne lagega. `StandardScaler` lagane ke baad model ki accuracy turant jump ho gayi!

#### 2. Medical Data Mein Recall Ka Mahatva:
Medical testing mein kisi bimaar aadmi ko galti se "Healthy" bol dena (False Negative) jaanleva ho sakta hai! Isliye ma'am ne samjhaya ki sirf Accuracy mat dekho, **Recall aur Confusion Matrix** dekhna sabse zaroori hai.

---

### 📊 Visual Flowchart: Pipeline

```mermaid
flowchart LR
    A["heart.csv"] --> B["StandardScaler"]
    B --> C["Logistic Regression fit()"]
    C --> D["Confusion Matrix & Recall"]
```

---

### 💻 Python Code

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def train_heart_disease_classifier(data_path=None):
    """
    Trains and evaluates a Logistic Regression classifier on Heart Disease dataset
    as demonstrated by Shraddha ma'am in video lecture 24.15.
    
    Includes StandardScaler preprocessing, train-test split, and classification metrics.
    """
    if data_path and os.path.exists(data_path):
        df = pd.read_csv(data_path)
    else:
        # Fallback synthetic heart dataset
        np.random.seed(42)
        n = 250
        df = pd.DataFrame({
            'age': np.random.randint(30, 75, size=n),
            'chol': np.random.uniform(150, 350, size=n),
            'trestbps': np.random.uniform(100, 180, size=n),
            'thalach': np.random.uniform(80, 200, size=n),
            'target': np.zeros(n, dtype=int)
        })
        # Probability depends on age and cholesterol
        z = 0.05 * df['age'] + 0.02 * df['chol'] - 0.03 * df['thalach'] - 1.5
        prob = 1.0 / (1.0 + np.exp(-z))
        df['target'] = (prob > 0.5).astype(int)

    X = df.drop(columns=['target'])
    y = df['target']

    # 1. Train-test split (80/20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    # 2. Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 3. Fit Logistic Regression
    clf = LogisticRegression(random_state=42)
    clf.fit(X_train_scaled, y_train)

    # 4. Predict & Evaluate
    y_pred = clf.predict(X_test_scaled)

    metrics = {
        'accuracy': float(accuracy_score(y_test, y_pred)),
        'precision': float(precision_score(y_test, y_pred, zero_division=0)),
        'recall': float(recall_score(y_test, y_pred, zero_division=0)),
        'f1_score': float(f1_score(y_test, y_pred, zero_division=0)),
        'confusion_matrix': confusion_matrix(y_test, y_pred).tolist()
    }
    return metrics

# --- Function Call & Testing ---
eval_res = train_heart_disease_classifier()
print(f"Heart Disease Classifier Results:")
print(f"  Accuracy : {eval_res['accuracy']*100:.2f}%")
print(f"  Precision: {eval_res['precision']*100:.2f}%")
print(f"  Recall   : {eval_res['recall']*100:.2f}%")
print(f"  F1-Score : {eval_res['f1_score']:.4f}")
print("Confusion Matrix:")
print(" ", eval_res['confusion_matrix'])
```

---

### 📌 Summary Points
- Logistic Regression se pehle features ko scale karein.
- Medical prediction mein Recall aur Confusion Matrix sabse zaroori hote hain.
