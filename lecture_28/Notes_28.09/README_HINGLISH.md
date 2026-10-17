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
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier

# 1. Dataset
df = sns.load_dataset("titanic")

# 2. Imputation
imp_med = SimpleImputer(strategy="median")
df["age"] = imp_med.fit_transform(df[["age"]])

imp_mode = SimpleImputer(strategy="most_frequent")
df["embarked"] = imp_mode.fit_transform(df[["embarked"]]).ravel()

# 3. Encoding
df["sex"] = df["sex"].map({"female": 0, "male": 1})
df["embarked"] = df["embarked"].map({"C": 0, "Q": 1, "S": 2})

X = df[["pclass", "sex", "fare", "embarked", "age"]]
y = df["survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

print(f"Train Acc: {model.score(X_train, y_train):.3f}")
print(f"Test Acc:  {model.score(X_test, y_test):.3f}")
```

---

### 📌 Summary Points
- Unpruned tree Titanic data par severe overfit dikhati hai (98% train vs 77% test).
- Missing values ko `SimpleImputer` se impute kiya jata hai.
- Is overfitting ko solve karne ke liye pruning zaroori hai.
