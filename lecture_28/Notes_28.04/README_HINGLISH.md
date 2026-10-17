# Lecture 28.04: Gini Impurity (Formula, Calculation & Range)

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Gini Impurity kya hai aur iska naam Corrado Gini ke naam par kyun pada.
- Gini Impurity ka mathematical formula: $1 - \sum (p_i)^2$.
- Binary classification mein Gini ki maximum value $0.5$ kyun hoti hai.
- Video mein board par solve kiya gaya step-by-step example: $[3n, 3y]$ aur $[0n, 3y]$.
- Entropy curve (peak 1.0) aur Gini curve (peak 0.5) ka visual comparison.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Gini Impurity Asal Mein Kya Hai?
Gini Impurity Italian statistician **Corrado Gini** ke naam par rakha gaya metric hai.
Yeh measure karta hai:
> Agar hum dataset se randomly ek point uthayein aur usko random label de dein, toh uske galat classify (misclassify) hone ki probability kitni hai.

#### 2. Gini Impurity Ka Formula
Har ek class $i$ ke liye:

$$GI = 1 - \sum_{i=1}^c (p_i)^2$$

Agar sirf 2 classes (Yes aur No) hain:

$$GI = 1 - (p_y^2 + p_n^2)$$

Yahan koi logarithm ($\log$) nahi hota, sirf probability ka square karna hota hai! Isi wajah se yeh compute karne mein bohot tez hota hai.

#### 3. Binary Classification Mein Range ($0$ Se $0.5$)
- **Minimum Value = 0.0**: Jab saare points ek hi class ke hon (pure leaf).
- **Maximum Value = 0.5**: Jab aadhi Yes aur aadhi No hon ($p_y = 0.5, p_n = 0.5$):

$$GI = 1 - (0.5^2 + 0.5^2) = 1 - (0.25 + 0.25) = 1 - 0.5 = 0.5$$

> **Dhyan Dein**: Entropy maximum **1.0** tak jaati hai, lekin Gini Impurity binary case mein maximum **0.5** tak hi jaati hai!

#### 4. Board Par Solve Kiye Gaye Examples

**Example 1: Mixed Node $[3n, 3y]$**
- Total = 6, $p_y = 3/6 = 0.5, p_n = 3/6 = 0.5$
- $GI = 1 - (0.5^2 + 0.5^2) = 1 - 0.5 = 0.5$.

**Example 2: Pure Node $[0n, 3y]$**
- Total = 3, $p_y = 1.0, p_n = 0.0$
- $GI = 1 - (1.0^2 + 0^2) = 1 - 1 = 0.0$.

#### 5. Graph Comparison: Entropy vs Gini
Video mein ma'am ne dono curves ko ek hi graph par draw karke dikhaya:
- Orange curve = Entropy (peak 1.0 par)
- Blue curve = Gini Impurity (peak 0.5 par)
Dono curves ka shape lagbhag ek jaisa (parabolic) hota hai, isiliye dono metrics lagbhag 98% cases mein ek hi feature split ko best batate hain.

---

### 💻 Python Code

```python
def calculate_gini_impurity(yes_count, no_count):
    """
    Calculates Gini Impurity for a binary classification node.
    Formula: GI(S) = 1 - (p_yes^2 + p_no^2)
    
    Returns:
        float: Gini value in range [0.0 (Pure), 0.5 (Maximum Impurity)]
    """
    total = yes_count + no_count
    if total == 0:
        return 0.0

    p_yes = yes_count / total
    p_no = no_count / total

    gini = 1.0 - (p_yes**2 + p_no**2)
    return gini

# --- Function Call & Verification ---
print("Gini [3 Yes, 3 No]:", calculate_gini_impurity(3, 3))  # 0.5 (Maximum Impurity)
print("Gini [0 Yes, 3 No]:", calculate_gini_impurity(0, 3))  # 0.0 (Pure node)
print("Gini [2 Yes, 4 No]:", round(calculate_gini_impurity(2, 4), 3))  # 0.444
```

---

### 📌 Summary Points
- Gini Impurity ka formula $1 - \sum p_i^2$ hota hai.
- Binary classification mein Gini 0 se 0.5 ke beech rehti hai.
- Isme logarithm na hone ki wajah se yeh Entropy se tez calculate hoti hai.
