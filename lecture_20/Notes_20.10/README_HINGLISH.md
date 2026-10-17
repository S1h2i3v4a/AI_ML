# Notes_20.10: Conditional Probability [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne **Conditional Probability ($P(A \mid B)$)** ka concept bohot hi intuitive tarike se samjhaya hai: kaise nayi information aane par sample space chhota ho jata hai aur probability update ho jaati hai.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Conditional Probability $P(A \mid B)$ ka matlab kya hai? ("B ho chuka hai, ab A ke hone ke kitne chances hain?").
- Sample space ka shrink (collapse) hona.
- Formula: $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$.
- Dice example: "Pata chala ki even number aaya hai, toh exact 2 aane ke kya chances hain?".

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Sample Space Ka Shrink Hona:
Normally ek 6-sided dice par 2 aane ki probability hoti hai:

$$
P(2) = \frac{1}{6} \approx 16.67\%
$$

Lekin maan lijiye aapke dost ne dice dekha aur aapko ek hint diya: **"Bhai, Even number aaya hai!"**
Ab sample space $\{1, 2, 3, 4, 5, 6\}$ nahi raha! Odd numbers ($1, 3, 5$) eliminate ho gaye.
Naya sample space ban gaya: $B = \{2, 4, 6\}$.
Is naye chote space mein 2 aane ke chances hain:

$$
P(2 \mid \text{Even}) = \frac{1}{3} \approx 33.33\%
$$

Nayi information ne probability ko double kar diya!

#### 2. Mathematical Formula:

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
$$

---

### 📊 Blackboard Diagram: Universe Ka Shrink Hona

```mermaid
flowchart LR
    A["Poora Universe S: {1, 2, 3, 4, 5, 6}"] -->|Condition: Even Number| B["Naya Universe B: {2, 4, 6}"]
    B --> C["A = {2} ki Probability: 1 / 3"]
```

---

### 💻 Python Code Implementation

```python
def compute_conditional_probability(p_intersection, p_given):
    """
    Computes conditional probability P(A | B) = P(A ∩ B) / P(B).
    Demonstrates the restriction of the universal sample space S to conditioning event B.
    
    Parameters:
        p_intersection (float): P(A ∩ B)
        p_given (float): P(B) where P(B) > 0
        
    Returns:
        dict: Calculated conditional probability.
    """
    if p_given <= 0:
        raise ValueError("Conditioning event probability P(B) must be strictly positive.")
        
    p_conditional = p_intersection / p_given
    
    return {
        "P(A ∩ B)": p_intersection,
        "P(B)": p_given,
        "P(A | B)": p_conditional
    }

# --- Execution & Verification ---
# Rolling a die: E = {number is 2}, B = {number is even {2, 4, 6}}
# P(E ∩ B) = P({2}) = 1/6, P(B) = 3/6
res = compute_conditional_probability(p_intersection=1/6, p_given=3/6)
print(f"P(Number is 2 ∩ Even) = {res['P(A ∩ B)']:.4f} (1/6)")
print(f"P(Even)               = {res['P(B)']:.4f} (3/6)")
print(f"P(Number is 2 | Even) = (1/6) / (3/6) = {res['P(A | B)']:.4f} (1/3 = 33.33%)")

```

---

### 🎯 Key Takeaways:
1. $P(A \mid B)$ mein vertical bar `$|$` ka matlab hota hai **"Given that"** (yeh event pehle hi ho chuka hai).
2. Denominator hamesha given event $P(B)$ hota hai kyunki woh hamara naya sample space ban chuka hai.
