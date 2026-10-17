# Lecture 28.08: Common Pruning Rules & Scikit-Learn Hyperparameters

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Video mein ma'am dwara Scikit-Learn documentation ko open karke explain kiye gaye mukhya parameters.
- `max_depth`, `min_samples_split`, aur `min_samples_leaf` ka practical matlab.
- `class_weight="balanced"` kab aur kyun use karte hain.
- `ccp_alpha` parameter ka role Minimal Cost-Complexity Pruning mein.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Video Mein Documentation Walkthrough
Video mein ma'am ne browser khol kar Scikit-Learn ke `DecisionTreeClassifier` page se direct samjhaya ki overfitting rokne ke liye library mein kaun-kaun se options diye gaye hain.

#### 2. Mukhya Pre-Pruning Parameters

##### A. `max_depth` (Tree Ki Lambai Par Rok)
- Default: `None` (Tree tab tak badhti rehti hai jab tak har leaf pure na ho jaye).
- **Practical Use**: Isko `3`, `4`, ya `5` set kar do. Isse tree kisi bhi branch ko 4 level se zyada gehra nahi le jayega. Yeh sabse popular aur aasan tareeqa hai overfitting rokne ka.

##### B. `min_samples_split` (Split Hone Ke Liye Minimum Log)
- Default: `2`.
- **Practical Use**: Agar hum ise `min_samples_split=10` set kar dein, toh agar kisi dabbe mein 9 ya usse kam samples bache hain, toh model use aage divide karne se inkaar kar dega.

##### C. `min_samples_leaf` (Leaf Node Mein Kam Se Kam Kitne Samples Hon)
- Default: `1`.
- **Practical Use**: Pichhle lecture mein humne dekha tha ki 1 outlier ke liye tree alag branch bana deta tha. Agar hum `min_samples_leaf=5` kar dein, toh aisi koi branch ban hi nahi sakti jisme 5 se kam samples hon! Yeh boundary ko smooth karta hai.

#### 3. `class_weight="balanced"` (Imbalanced Data Ke Liye)
Agar dataset mein 90% log Loan Reject wale hain aur sirf 10% Approve wale, toh tree majority class ki taraf jhuk jata hai. `class_weight="balanced"` likhne se model minority class ko zyada weight dekar balance kar deta hai.

#### 4. `ccp_alpha` (Post-Pruning Ka Parameter)
- Default: `0.0`.
- Yeh **Minimal Cost-Complexity Pruning** ke liye use hota hai. Jaise-jaise alpha badhta hai, kamzor branches cut hoti jaati hain.

---

### 💻 Python Code

```python
from sklearn.tree import DecisionTreeClassifier

# Overfitting se safe Decision Tree
model = DecisionTreeClassifier(
max_depth=4,
min_samples_split=10,
min_samples_leaf=5,
class_weight="balanced",
random_state=42
)
print("Configured Model:", model)
```

---

### 📌 Summary Points
- `max_depth` tree ki gehrai ko limit karta hai.
- `min_samples_leaf` kisi single outlier ke liye alag leaf banne se rokta hai.
- `class_weight="balanced"` imbalanced datasets par model ko bias hone se bachata hai.
