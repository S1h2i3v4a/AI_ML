# Lecture 28.11: Post-Pruning Implementation (Cost-Complexity ccp_alpha)

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Post-pruning ka concept aur Cost-Complexity formula: $R_\alpha(T) = R(T) + \alpha |T|$.
- Scikit-Learn ka `cost_complexity_pruning_path()` function kaise candidate alphas nikaalta hai.
- Video mein ma'am dwara likha gaya code: `for alpha in ccp_alphas: ... tree.append((model, acc))`.
- Test accuracy ke basis par optimal `ccp_alpha` chunna.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Cost-Complexity Pruning Ka Mathematical Formula
Post-pruning mein hum tree ke size (number of leaves) par penalty lagate hain:

$$R_\alpha(T) = R(T) + \alpha |T|$$

Yahan:
- $R(T)$ = Training data par tree ka error.
- $|T|$ = Tree ke total leaf nodes ki sankhya (complexity).
- $\alpha$ (`ccp_alpha`) = Penalty parameter.
- Agar $\alpha = 0$ hai, toh koi penalty nahi hai (unpruned tree).
- Jaise-jaise $\alpha$ badhta hai, badi trees par penalty lagti hai aur wo prune hokar choti hoti jaati hain.

#### 2. Video Mein Coding Walkthrough
Ma'am ne video mein step-by-step code likha:

**Step 1: Pruning Path Nikaalna**
```python
# Unconstrained tree se pruning path nikalna
path = model.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas = path.ccp_alphas
```
Yeh function candidate alpha values ki list return karta hai.

**Step 2: Har Alpha Par Model Train Karna**
```python
# Har candidate alpha par model train karke test score record karna
tree = []
for alpha in ccp_alphas:
    model = DecisionTreeClassifier(random_state=42, ccp_alpha=alpha)
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    tree.append((model, acc, alpha))
```

**Step 3: Best Alpha Chunna**
Ma'am ne test accuracy check ki aur wo model pick kiya jahan test score sabse zyada tha.

#### 3. Train vs Test Accuracy Ka Behaviour
- Jaise-jaise alpha badhta hai, training accuracy thodi kam hoti hai (kyunki tree memorize nahi kar raha).
- Lekin testing accuracy pehle improve hoti hai, peak par pahunchti hai, aur fir bohot zyada pruning karne par girne lagti hai. Sweet-spot wahi peak hai!

---

### 💻 Python Code

```python
import numpy as np
from sklearn.tree import DecisionTreeClassifier

def find_optimal_ccp_alpha(X_train, y_train, X_test, y_test):
    """
    Cost-Complexity Pruning ka optimal alpha dhoondhne wala function:
    - Step 1: Base tree se pruning path (candidate alphas) nikalta hai.
    - Step 2: Har alpha par tree train karke test accuracy check karta hai.
    - Step 3: Best alpha, best score aur best model return karta hai.
    """
    # 1. Pruning path nikalna
    base_tree = DecisionTreeClassifier(random_state=42)
    path = base_tree.cost_complexity_pruning_path(X_train, y_train)
    alphas = path.ccp_alphas

    # 2. Candidate alphas par iterate karke evaluate karna
    best_alpha = 0.0
    best_score = 0.0
    best_model = None

    for alpha in alphas:
        clf = DecisionTreeClassifier(random_state=42, ccp_alpha=alpha)
        clf.fit(X_train, y_train)
        score = clf.score(X_test, y_test)
        
        # Highest accuracy wala alpha track karna
        if score > best_score:
            best_score = score
            best_alpha = alpha
            best_model = clf

    # 3. Best results return karna
    return best_alpha, best_score, best_model

# --- Function Call & Testing ---
# best_alpha, best_score, pruned_tree = find_optimal_ccp_alpha(X_train, y_train, X_test, y_test)
# print(f"Best ccp_alpha:       {best_alpha:.5f}")
# print(f"Optimized Test Score: {best_score:.4f}")
```

---

### 📌 Summary Points
- Post-pruning poori tree banne ke baad bottom se branches cut karti hai.
- `ccp_alpha` parameter tree ke size par penalty lagata hai.
- Best alpha wahi hota hai jahan test accuracy sabse zyada ho.
