# Lecture 28.12: Decision Tree Regressor (Core Concepts & Mean Prediction)

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Decision Tree Regressor aur Classifier ke beech ka farak.
- Leaf node par prediction kaise aati hai: **Mean / Average ($\bar{y}$)**.
- Regression mein Impurity Metric: Entropy/Gini ke badle **Variance ($\sigma^2$) ya MSE**.
- Video mein board par solve kiya gaya dataset: $x = [1, 2, 3, 4]$ aur $y = [2, 4, 6, 10]$.
- Parent node ka Mean ($\bar{y} = 5.5$) aur Variance ($V_S = 8.75$) nikaalna.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Classifier vs Regressor Mein Farak
- **Classifier**: Target categorical hota hai (Yes/No, Spam/Not Spam). Leaf par majority vote se faisla hota hai.
- **Regressor**: Target continuous number hota hai (Salary, Price, Temperature). Leaf par aane wale sabhi numbers ka **Average (Mean)** output banta hai!

#### 2. Leaf Node Prediction Ka Niyam
Agar kisi leaf node mein 3 points pahunche jinki salary hai ₹30k, ₹40k, aur ₹50k, toh wo leaf kya predict karega?
Un teeno ka average:
$$\hat{y} = \frac{30 + 40 + 50}{3} = 40\text{k}$$

#### 3. Board Par Ki Gayi Calculation

Video mein ma'am ne board par table banayi:

| $x$ | $y$ |
| :--- | :--- |
| 1 | 2 |
| 2 | 4 |
| 3 | 6 |
| 4 | 10 |

**Step 1: Mean ($\bar{y}$) Nikaalna**

$$\bar{y} = \frac{2 + 4 + 6 + 10}{4} = \frac{22}{4} = 5.5$$

**Step 2: Variance ($V_S$) Nikaalna**
Formula:

$$V_S = \frac{1}{n} \sum (y_i - \bar{y})^2$$

Har point ka $(y_i - 5.5)^2$:
- $(2 - 5.5)^2 = (-3.5)^2 = 12.25$
- $(4 - 5.5)^2 = (-1.5)^2 = 2.25$
- $(6 - 5.5)^2 = (0.5)^2 = 0.25$
- $(10 - 5.5)^2 = (4.5)^2 = 20.25$

Sum $= 12.25 + 2.25 + 0.25 + 20.25 = 35.0$.

$$V_S = \frac{35.0}{4} = 8.75$$

Ma'am ne board ke upar circle karke likha: **$V_S = 8.75$**. Yeh hamari initial impurity hai!

---

### 💻 Python Code

```python
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 10])

# Mean
y_mean = np.mean(y)
print("Mean (y_bar):", y_mean)

# Variance
var = np.var(y)
print("Variance (V_S):", var)
```

---

### 📌 Summary Points
- Decision Tree Regressor continuous target values ke liye use hota hai.
- Leaf node ka prediction usme aane wale samples ka mean hota hai.
- Impurity metric variance ($\sigma^2$) ya MSE hota hai.
