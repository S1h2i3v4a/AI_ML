# Lecture 28.09: Decision Tree Classifier Code Walkthrough (Titanic Dataset)

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Video mein ma'am dwara Jupyter Notebook par Titanic dataset (`sns.load_dataset('titanic')`) ka live coding demonstration.
- `SimpleImputer` se `age` (median) aur `embarked` (most_frequent) ke missing values handle karna.
- Categorical features (`sex`, `embarked`) ko numerical mein convert karna.
- Baseline `DecisionTreeClassifier` ko train karke overfitting ka live saboot dekhna (~98% train vs ~77% test).

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Titanic Dataset Load Karna
Video mein ma'am ne Seaborn se direct Titanic dataset load kiya. Target variable hai `survived` (1 = bacha, 0 = doob gaya).
Features chune gaye:
- `pclass`: Passenger class (1, 2, 3)
- `sex`: Gender (male/female)
- `age`: Umra
- `fare`: Ticket ka kiraya
- `embarked`: Boarding port (C, Q, S)

#### 2. Missing Values Handle Karna (`SimpleImputer`)
- `age` column mein kaafi missing values the, jinko ma'am ne `median` strategy se bhara (`SimpleImputer(strategy="median")`).
- `embarked` column mein missing values ko mode yani sabse zyada aane wale port se bhara (`strategy="most_frequent"`).

#### 3. Encoding Karna
Machine learning models text nahi samajhte, isiliye:
- `female -> 0`, `male -> 1`
- `C -> 0`, `Q -> 1`, `S -> 2`

#### 4. Baseline Model Aur Overfitting Ka Live Result
Jab ma'am ne bina kisi restriction ke baseline model train kiya:
- **Training Accuracy**: $\approx 98\%$
- **Testing Accuracy**: $\approx 77.5\%$

Ma'am ne screen par dikhaya ki training score lagbhag 100% hai, lekin testing par score 20% gir gaya! Yeh classic saboot hai ki tree ne training data ko blindly ratt (memorize) liya hai. Isko theek karne ke liye agle lecture mein **Pre-pruning** lagayenge!

---

### 💻 Python Code

```python
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier

def train_titanic_baseline_tree():
    """
    Loads Titanic dataset, imputes missing values, and fits an unpruned
    DecisionTreeClassifier to demonstrate overfit in a real-world pipeline.
    """
    # 1. Load dataset
    df = sns.load_dataset('titanic')
    features = ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']
    X = df[features].copy()
    y = df['survived']

    # 2. Encode categorical variables
    X['sex'] = X['sex'].map({'male': 0, 'female': 1})
    X['embarked'] = X['embarked'].map({'S': 0, 'C': 1, 'Q': 2})

    # 3. Impute missing values
    imputer_age = SimpleImputer(strategy='median')
    X['age'] = imputer_age.fit_transform(X[['age']])

    imputer_emb = SimpleImputer(strategy='most_frequent')
    X['embarked'] = imputer_emb.fit_transform(X[['embarked']])

    # 4. Train-Test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 5. Fit unpruned Decision Tree
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)

    train_acc = clf.score(X_train, y_train)
    test_acc = clf.score(X_test, y_test)

    return clf, train_acc, test_acc

# --- Execute Function ---
tree_model, train_score, test_score = train_titanic_baseline_tree()
print(f"Train Accuracy: {train_score*100:.1f}%")
print(f"Test Accuracy:  {test_score*100:.1f}% (Overfitting Gap: {(train_score - test_score)*100:.1f}%)")
```

---

### 📌 Summary Points
- Unpruned tree Titanic data par severe overfit dikhati hai (98% train vs 77% test).
- Missing values ko `SimpleImputer` se impute kiya jata hai.
- Is overfitting ko solve karne ke liye pruning zaroori hai.
