# Lecture 28.07: Pruning Decision Trees (Concept & Overfitting)

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Decision Tree overfit kyun hota hai.
- Video mein board par draw kiya gaya $[14y, 1n]$ outlier node ka example.
- Overfitting ki pehchaan: `Training Accuracy >>>> Testing Accuracy`.
- Pruning kya hoti hai aur iska gardener analogy se connection.
- Pre-pruning (early stopping) aur Post-pruning ke beech ka farak.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Decision Tree Overfit Kyun Hota Hai?
Decision tree bohot greedy hota hai. Wo tab tak split karta rehta hai jab tak har ek single data point alag na ho jaye.

Video mein ma'am ne board par ek node draw kiya:
$$[14y, 1n]$$
- Yahan 14 log Yes keh rahe hain aur sirf 1 aadmi No keh raha hai (jo ki ek outlier ya galti ho sakti hai).
- Lekin bina rok-tok ke decision tree is 1 aadmi ke liye ek alag branch aur alag leaf node bana deta hai: $[14y, 0n]$ aur $[0y, 1n]$.
- **Natija**: Tree unnecessarily deep ban jata hai aur noise ko yaad kar leta hai.

#### 2. Overfitting Ki Pehchaan
Ma'am ne board ke upar likha:
$$	ext{Training} \gg 	ext{Testing}$$
- Training data par accuracy $100\%$ aa rahi hoti hai.
- Lekin jab wahi model naye (testing) data par chalta hai, toh accuracy gir kar $70-75\%$ reh jaati hai. Isi ko **Overfitting** kehte hain.

#### 3. Pruning Kya Hai?
Jaise bageeche mein maali (gardener) paudhe ki bekar aur lambi branches ko kaat kar chhota karta hai taaki paudha theek se grow kare, thik waise hi:
> **Pruning wo technique hai jisme hum Decision Tree ki unnecessary branches ko kaat dete hain taaki overfitting kam ho aur model naye data par accha perform kare.**

#### 4. Pruning Ke Do Tareeqe

**1. Pre-pruning (Pehle hi rok dena):**
- Tree ko bohot gehra banne hi mat do.
- Board par ma'am ne ek horizontal line draw ki aur likha: `max_depth = 4`.
- Isse tree 4 level ke baad aage split nahi hoga chahe data pure ho ya na ho.

**2. Post-pruning (Baad mein kaatna):**
- Pehle tree ko poora badhne do (full grow hone do).
- Fir niche se shuru karke dekho ki kaun si branch faltu hai aur usko cut kar do.

---

### 💻 Python Code

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = make_classification(n_samples=500, n_features=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Bina kisi restriction ke tree (Overfit hoga)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

print("Training Score:", model.score(X_train, y_train))
print("Testing Score: ", model.score(X_test, y_test))
```

---

### 📌 Summary Points
- Decision tree outliers ke liye alag branch banakar overfit ho jata hai.
- Pruning unnecessary branches ko hata kar overfitting ko theek karta hai.
- Pre-pruning tree ke badhne ke dauran rokti hai, jabki Post-pruning baad mein cut karti hai.
