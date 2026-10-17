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
import time
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier

def benchmark_gini_vs_entropy(n_samples=50000, random_state=42):
    """
    Benchmarks training runtime of Gini Impurity vs Shannon Entropy
    to demonstrate why Gini is Scikit-Learn's default criterion.
    """
    # 1. Generate large synthetic classification dataset
    X, y = make_classification(
        n_samples=n_samples, n_features=20, n_informative=10, random_state=random_state
    )

    # 2. Measure Gini runtime
    t0 = time.time()
    clf_gini = DecisionTreeClassifier(criterion='gini', random_state=random_state)
    clf_gini.fit(X, y)
    gini_time = time.time() - t0

    # 3. Measure Entropy runtime
    t0 = time.time()
    clf_entropy = DecisionTreeClassifier(criterion='entropy', random_state=random_state)
    clf_entropy.fit(X, y)
    entropy_time = time.time() - t0

    results = {
        'gini_time': gini_time,
        'entropy_time': entropy_time,
        'speedup': entropy_time / gini_time
    }
    return results

# --- Function Call & Output ---
res = benchmark_gini_vs_entropy()
print(f"Gini Impurity Fit Time:  {res['gini_time']:.4f}s")
print(f"Shannon Entropy Fit Time: {res['entropy_time']:.4f}s")
print(f"Gini is {res['speedup']:.2f}x faster!")
```

---

### 📌 Summary Points
- Gini compute karne mein fast hai kyunki isme $\log$ nahi hota.
- Large datasets par hamesha Gini prefer ki jaati hai.
- Scikit-Learn ka default criterion `gini` hota hai.
