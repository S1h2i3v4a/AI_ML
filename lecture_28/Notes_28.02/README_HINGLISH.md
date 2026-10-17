# Lecture 28.02: Decision Tree Classifier Aur Recursive Splitting

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Video mein ma'am dwara samjhaya gaya 6 applicants ka Credit Score aur Employment dataset.
- Root node par target distribution $[3y, 3n]$ ka matlab.
- Decision Tree ke do sabse bade sawal: Feature selection aur Degree of purity.
- `Credit Score` par pehla split karne par Low, Med, High branches ka behaviour.
- Pure (homogeneous) aur Impure (heterogeneous) nodes ke beech ka antar.
- Impure node par recursive split kaise perform hota hai.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Blackboard Ka 6-Applicant Dataset
Video mein ma'am ne board par ek table banayi thi:

| Credit Score | Employed | Loan Approved |
| :--- | :--- | :--- |
| Low | No | No |
| Low | Yes | No |
| Medium | Yes | Yes |
| High | Yes | Yes |
| Medium | No | No |
| High | No | Yes |

Root node par total 6 applicants hain:
- 3 logon ka Loan Approve hua (Yes)
- 3 logon ka Loan Reject hua (No)
- Isko ma'am ne board par likha: **$[3y, 3n]$** (yani 50-50 confusion, maximum impurity).

#### 2. Decision Tree Classifier Ke Do Mukhya Sawal
Jab bhi model train hota hai, uske samne 2 main challenges hote hain:
1. **Feature selection for split**: Pehle kis feature se sawal poochein? `Credit Score` se ya `Employed` se?
2. **Degree of purity of a split**: Split karne ke baad bache hue groups kitne saaf (pure) hue hain, yeh kaise measure karein?

#### 3. Step 1: `Credit Score` Par Split Karke Dekhna
Jab hum root node $[3y, 3n]$ ko `Credit Score` par divide karte hain:
- **Low Credit Score**: Yahan 2 applicants aate hain, dono ka loan reject hai $\rightarrow [0y, 2n]$. Yeh **100% Pure** hai! Yahan aur koi sawal poochne ki zaroorat nahi hai, seedha prediction `No` hoga.
- **High Credit Score**: Yahan 2 applicants aate hain, dono ka loan approve hai $\rightarrow [2y, 0n]$. Yeh bhi **100% Pure** hai! Seedha prediction `Yes` hoga.
- **Medium Credit Score**: Yahan 2 applicants aate hain, jisme 1 ka Yes hai aur 1 ka No $\rightarrow [1y, 1n]$. Yeh **Impure** hai, kyunki yahan 50% chance Yes ka hai aur 50% No ka.

#### 4. Step 2: Recursive Splitting (Impure Node Ko Dobara Baantna)
Ab Medium Credit Score wale dabbe mein confusion hai, isliye hum is node ko fir se split karte hain agle feature `Employed?` par:
- Agar `Employed == Yes` $\rightarrow [1y, 0n]$ (Pure $\rightarrow$ Loan Approved).
- Agar `Employed == No` $\rightarrow [0y, 1n]$ (Pure $\rightarrow$ Loan Rejected).

Ab saari branches pure leaf nodes tak pahunch gayi hain!

---

### 💻 Python Code

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

def build_credit_score_tree():
    """
    Builds a DecisionTreeClassifier on the exact 6-applicant classroom dataset
    and returns the learned recursive splitting rules.
    """
    # 1. Dataset: Credit_Score (0: Low, 1: Medium, 2: High), Employed (0: No, 1: Yes)
    data = {
        'Credit_Score': [0, 0, 1, 2, 1, 2],
        'Employed':     [0, 1, 1, 1, 0, 0],
        'Loan_Approved': [0, 0, 1, 1, 0, 1]
    }
    df = pd.DataFrame(data)

    X = df[['Credit_Score', 'Employed']]
    y = df['Loan_Approved']

    # 2. Train Decision Tree using Entropy criterion
    clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
    clf.fit(X, y)

    # 3. Export text rules
    rules = export_text(clf, feature_names=['Credit_Score', 'Employed'])
    return clf, rules

# --- Function Call & Output ---
tree_model, decision_rules = build_credit_score_tree()
print("Learned Decision Rules:\n")
print(decision_rules)
```

---

### 📌 Summary Points
- Node pure tab hota hai jab usme saare samples sirf ek hi class ke hote hain.
- Impure node par tree rukta nahi hai, balki agle feature se dobara split (recursive splitting) karta hai.
- Final prediction hamesha leaf node ke majority class ke hisaab se hota hai.
