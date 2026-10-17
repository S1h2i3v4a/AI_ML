# Lecture 28.01: Decision Trees Ka Introduction & Core Intuition

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Decision Tree asal mein kya hota hai aur machine learning mein iska intuition kya hai.
- Video mein ma'am dwara samjhaya gaya Loan Approval wala `if-elif-else` real-life example.
- Tree ke components: Root Node, Internal Node, Branch, aur Leaf Node ka exact matlab.
- Blue dots aur Orange dots ke data partitioning ka visual concept.
- Famous algorithms: CART, ID3, C4.5, aur CHAID.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Decision Tree Asal Mein Kya Hai?
Decision Tree ek aisa supervised machine learning algorithm hai jo feature ke basis par ek ke baad ek simple sawal (if-then questions) pooch kar prediction karta hai.

Jaise hum daily life mein decision lete hain:
- *"Kya bahar barish ho rahi hai?"* $\rightarrow$ Haan $\rightarrow$ *"Kya umbrella hai?"* $\rightarrow$ Haan $\rightarrow$ *"Bahar jao."*
Thik isi tarah machine learning mein decision tree data ko analyze karke rules banata hai.

#### 2. Real-Life Example: Bank Loan Approval
Video mein ma'am ne board par sabse pehle Python code ka simple example likh kar samjhaya:

```python
def check_loan_approval(loan_amt, employed):
    """
    Simple if-else rules se loan approve hoga ya reject:
    - Agar loan 1 Lakh ya zyada hai aur applicant employed hai -> Approved
    - Agar loan 1 Lakh ya zyada hai aur unemployed hai -> Rejected
    - Agar loan 1 Lakh se kam hai -> Seedha Approved
    """
    if loan_amt >= 100000:
        if employed == "Yes":
            return "Loan Approved"
        else:
            return "Loan Rejected"
    else:
        return "Loan Approved"

# --- Function Test Karna ---
faisla = check_loan_approval(loan_amt=150000, employed="Yes")
print("Loan Faisla:", faisla)
```

Jab hum isi logic ko visual diagram mein convert karte hain, toh yeh ek tree ban jata hai:
- Pehle check karo: `loan_amt >= 1 Lakh?`
- Agar condition match hui, toh seedha decision mil gaya.
- Agar condition match nahi hui, toh agla sawal poocho: `employed == 'Yes'?`
- Uske baad aakhri faisla (Yes ya No).

#### 3. Tree Ke Chaar Mukhya Ang (Structural Anatomy)
- **Root Node**: Tree ka sabse pehla aur top node jahan se decision shuru hota hai. Is node mein poora ka poora dataset rehta hai.
- **Internal (Decision) Nodes**: Beech ke nodes jahan conditions check hoti hain (jaise `employed == Yes?`). Yeh data ko do ya zyada hisson mein baant te hain.
- **Branches (Edges)**: Teer (arrows) jo sawal ke javab ko darshate hain (jaise `Yes` branch ya `No` branch).
- **Leaf (Terminal) Nodes**: Tree ke aakhri dabba jahan koi naya sawal nahi poocha jata, balki final prediction (output) milta hai.

#### 4. Data Partitioning Ka Concept (Blue vs Orange Dots)
Video mein ma'am ne blackboard par blue dots (Yes) aur orange dots (No) banakar dikhaya:
- Root node par saare dots mix hote hain (ise hum **impure** ya ashuddh kehte hain).
- Jab tree ek feature (jaise Gender $\rightarrow$ Male / Female) par split karta hai, toh ek taraf zyada blue dots chale jaate hain aur doosri taraf orange dots.
- Tree baar-baar split tab tak karta hai jab tak har ek leaf node bilkul **pure** (sirf blue ya sirf orange) na ho jaye!

#### 5. Prastut Algorithms
1. **CART (Classification and Regression Trees)**: Scikit-learn mein yahi algorithm use hota hai. Yeh binary split (hamesha 2 branches) banata hai.
2. **ID3**: Information Gain aur Entropy par based purana standard algorithm.
3. **C4.5**: ID3 ka advanced version jo continuous data aur pruning ko support karta hai.
4. **CHAID**: Statistics ke Chi-square test par based algorithm.

---

### 💻 Python Code

```python
import numpy as np
from sklearn.tree import DecisionTreeClassifier

def train_and_predict_loan_tree():
    """
    Trains a CART DecisionTreeClassifier on applicant data
    and predicts approval for a new applicant.
    """
    # Feature matrix: [Loan_Amount_in_Lakhs, Employed (1=Yes, 0=No)]
    X = np.array([
        [0.5, 0],
        [0.8, 1],
        [1.5, 1],
        [2.0, 0],
        [3.0, 1]
    ])
    # Target: 1 = Approved, 0 = Rejected
    y = np.array([1, 1, 1, 0, 1])

    # 1. Initialize and fit Decision Tree Classifier
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X, y)

    # 2. Predict for a new applicant: Loan 2.5 Lakh, Unemployed (0)
    new_applicant = [[2.5, 0]]
    prediction = clf.predict(new_applicant)[0]
    decision = "Approved" if prediction == 1 else "Rejected"

    return clf, decision

# --- Function Call & Result ---
model, decision = train_and_predict_loan_tree()
print("Prediction for [2.5L, Unemployed]:", decision)
```

---

### 📌 Summary Points
- Decision Tree simple `if-else` sawalon ki chain par kaam karta hai.
- Root node par saara data hota hai, internal nodes par splits hote hain, aur leaf nodes final output dete hain.
- Scikit-Learn mein default algorithm **CART** use hota hai.
