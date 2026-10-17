# Lecture 28.05: Entropy vs Gini Impurity (Detailed Comparison)

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Entropy aur Gini Impurity ke beech ka practical difference.
- Slide par dikhayi gayi 5-point comparison table (Speed, Split Behaviour, Dataset Size, etc.).
- Video ka golden rule: Small dataset vs Large dataset mein kya chunein.
- Scikit-Learn mein default criterion kaun sa hota hai.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Comparison Table (Video Slide Ke Hisaab Se)

| Parameter | Entropy | Gini Impurity |
| :--- | :--- | :--- |
| **Training Speed** | Thoda slow hota hai kyunki isme $\log_2$ ki calculation karni padti hai. | **Kaafi tez** hota hai kyunki isme sirf simple square aur minus hota hai. |
| **Split Behaviour** | Balanced splits banata hai (dono branches lagbhag barabar size ki hoti hain). | Dominant class ko jaldi alag karke fast splits banata hai. |
| **Dataset Size** | Chhote datasets ke liye theek hai. | **Bade datasets** ke liye recommended hai. |
| **Sensitivity** | Class probabilities ke chhote badlaav par zyada sensitive hota hai. | Chhote badlaav par kam sensitive hota hai. |
| **Industry Standard** | Theory aur ID3/C4.5 mein use hota hai. | **Scikit-Learn ka default** parameter hai (`criterion='gini'`). |

#### 2. Golden Rule: Kab Kaun Sa Use Karein?
Video mein ma'am ne board ke kone mein short rule likha:
- `small dataset -> Entropy (log)`
- `large dataset -> G.I`

**Kyun?** 
Agar dataset mein 10 lakh rows hain, toh har possible split par log calculate karna CPU ko slow kar deta hai. Gini bina log ke turant square nikaal kar decision le leta hai, isiliye Scikit-Learn ne Gini ko apna default rakha hai.

#### 3. Kya Accuracy Mein Koi Bada Farak Padta Hai?
Practically **nahi**! 100 mein se 98 datasets par Entropy aur Gini lagbhag identical accuracy dete hain, kyunki dono curves ka curvature lagbhag same hota hai.

---

### 💻 Python Code

```python
from sklearn.tree import DecisionTreeClassifier

# Gini use karne ka tarika (Default)
model_gini = DecisionTreeClassifier(criterion="gini", random_state=42)

# Entropy use karne ka tarika
model_entropy = DecisionTreeClassifier(criterion="entropy", random_state=42)
```

---

### 📌 Summary Points
- Gini compute karne mein fast hai kyunki isme $\log$ nahi hota.
- Large datasets par hamesha Gini prefer ki jaati hai.
- Scikit-Learn ka default criterion `gini` hota hai.
