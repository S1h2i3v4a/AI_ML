# Notes_25.08: Scikit-Learn Mein Naive Bayes Ka Code [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne Python aur Scikit-Learn mein **GaussianNB** model ko train aur evaluate karne ka live code likh kar dikhaya hai.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Scikit-Learn se `GaussianNB` kaise import aur initialize karte hain.
- `model.fit()` aur `model.predict()` ka standard workflow.
- Continuous features par Naive Bayes ka prediction check karna.
- Classification Report (Precision, Recall, F1) ko interpret karna.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. GaussianNB Ki Khasiyat
- Is model mein koi heavy hyperparameters tune nahi karne padte.
- Yeh train hone mein bohot tezi se kaam karta hai kyunki iska `fit()` step sirf features ka mean aur variance calculate karta hai.

#### 2. Workflow:
1. Data ko train aur test mein split karo (`train_test_split`).
2. Model ka object banao: `model = GaussianNB()`.
3. Train karo: `model.fit(X_train, y_train)`.
4. Test par predictions nikaalo: `y_pred = model.predict(X_test)`.

---

### 💻 Python Code

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

def train_and_evaluate_gaussian_nb():
    """
    Trains a GaussianNB classifier on a classification dataset,
    evaluates its performance, and returns metrics.
    """
    # 1. Synthetic continuous feature dataset
    X, y = make_classification(
        n_samples=500, n_features=6, n_informative=4, random_state=42
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 2. Fit Gaussian Naive Bayes
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)

    # 3. Evaluate
    y_pred = gnb.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    return gnb, acc, report

# --- Function Call & Testing ---
model, accuracy, metrics_report = train_and_evaluate_gaussian_nb()
print(f"GaussianNB Accuracy: {accuracy*100:.1f}%")
print("Classification Report:")
print(metrics_report)
```

---

### 📌 Summary Points
- GaussianNB fast aur robust baseline classifier hai.
- Iska execution time almost instant hota hai.
