# Notes_25.07: Naive Bayes Ke Types (Gaussian, Multinomial, Bernoulli) [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne Naive Bayes ke teen alag-alag roop samjhaye hain: **GaussianNB**, **MultinomialNB**, aur **BernoulliNB**, aur bataya hai ki kis dataset ke liye kaunsa model chunna chahiye.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Gaussian Naive Bayes kab lagate hain (Continuous numbers).
- Multinomial Naive Bayes kab lagate hain (Word counts / Text NLP).
- Bernoulli Naive Bayes kab lagate hain (Binary 0 ya 1 features).
- Sahi model choose karne ka decision tree.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Gaussian Naive Bayes (`GaussianNB`):
- **Features**: Continuous decimal numbers (jaise Age = 25.5, Salary = ₹50,000, Temperature = 36.8°C).
- **Logic**: Yeh assume karta hai ki data ek normal bell-curve (Gaussian distribution) banata hai. Har feature ka mean ($\mu$) aur variance ($\sigma^2$) calculate kiya jata hai.

#### 2. Multinomial Naive Bayes (`MultinomialNB`):
- **Features**: Count data (jaise kisi article mein word "cricket" 5 baar aaya, "match" 3 baar aaya).
- **Logic**: NLP (Natural Language Processing) aur document classification ke liye sabse famous model.

#### 3. Bernoulli Naive Bayes (`BernoulliNB`):
- **Features**: Binary 0 ya 1 (jaise email mein word "Offer" hai = 1, nahi hai = 0).
- **Logic**: Chhote text messages (jaise SMS spam detection) mein jahan word kitni baar aaya usse zyada yeh matter karta hai ki word mojood hai ya nahi.

---

### 📊 Visual Flowchart: Model Selection Guide

```mermaid
flowchart TD
    A["Aapka Data Kaisa Hai?"] --> BFeature Check
    B -->|"Continuous Decimal (Age, Salary)"| C["GaussianNB"]
    B -->|"Word Frequency Count (5 baar, 10 baar)"| D["MultinomialNB"]
    B -->|"Sirf Yes/No ya 0/1 (Word Present?)"| E["BernoulliNB"]
```

---

### 💻 Python Code

```python
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

def select_naive_bayes_model(feature_type):
    """
    Selects and initializes the appropriate Naive Bayes variant:
    - 'continuous' -> GaussianNB (Bell curve, mean & variance)
    - 'counts'     -> MultinomialNB (Word frequencies, discrete counts)
    - 'binary'     -> BernoulliNB (Presence/absence 0 or 1)
    """
    if feature_type == 'continuous':
        model = GaussianNB()
        desc = "GaussianNB: Continuous real-valued features following Normal Distribution."
    elif feature_type == 'counts':
        model = MultinomialNB()
        desc = "MultinomialNB: Discrete integer count data (e.g., Bag-of-Words in NLP)."
    elif feature_type == 'binary':
        model = BernoulliNB()
        desc = "BernoulliNB: Binary boolean features (e.g., word present=1, absent=0)."
    else:
        raise ValueError(f"Unknown feature type: {feature_type}")

    return model, desc

# --- Function Call & Testing ---
for f_type in ['continuous', 'counts', 'binary']:
    clf, description = select_naive_bayes_model(f_type)
    print(f"[{f_type.upper()}] => {clf.__class__.__name__}")
    print(f"  Usage: {description}")
```

---

### 📌 Summary Points
- Sahi data type ke liye sahi Naive Bayes choose karna zaroori hai.
- Numbers ke liye **Gaussian**, Word counts ke liye **Multinomial**, aur 0/1 ke liye **Bernoulli**.
