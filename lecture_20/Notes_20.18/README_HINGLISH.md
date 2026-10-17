# Notes_20.18: Binomial Distribution [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne **Binomial Distribution** ka formula aur uski 4 conditions blackboard par samjhayi hain: 5 baar coin toss karne par exact 3 baar Head aane ki probability ($5/16 = 0.3125$) ko manual math aur `scipy.stats.binom` dono se solve kiya hai.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Binomial experiment ki 4 zaroori shartein (Bernoulli conditions).
- Formula: $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$.
- 5 Coins toss karne par 3 Heads aane ka blackboard solution ($5/16$).
- Python mein `scipy.stats.binom.pmf()` ka use.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Binomial Ki 4 Shartein:
1. Trials ki sankhya fixed ho ($n = 5$).
2. Har trial ke sirf 2 hi result ho sakte hain: Success (Head) ya Failure (Tail).
3. Success ki probability $p$ hamesha constant rahe ($p = 0.5$).
4. Sabhi trials aapas mein independent hon.

#### 2. Blackboard Calculation:
Maan lijiye $n = 5$ coin tosses hain, aur humein $k = 3$ heads chahiye:

$$
P(X = 3) = \binom{5}{3} (0.5)^3 (0.5)^2
$$

$\binom{5}{3} = \frac{5 \times 4}{2 \times 1} = 10$ combinations.

$$
P(X = 3) = 10 \times \frac{1}{8} \times \frac{1}{4} = \frac{10}{32} = \frac{5}{16} = 0.3125 \quad (31.25\%)
$$

---

### 📊 Blackboard Diagram: 5 Coin Tosses Tree

```mermaid
flowchart LR
    Start["5 Coin Tosses"] --> Comb["10 Different Ways to get 3 Heads<br/>(HHHTT, HHTHT, ...)"]
    Comb --> Math["Har combination ki prob = (1/2)^5 = 1/32"]
    Math --> Res["Total = 10 * (1/32) = 5/16 = 31.25%"]
```

---

### 💻 Python Code Implementation

```python
from scipy.stats import binom

def compute_binomial_probability(n=5, k=3, p=0.5):
    """
    Computes exact Binomial probability P(X = k) for k successes in n Bernoulli trials.
    Demonstrates analytical combination formula and scipy.stats.binom verification.
    
    Parameters:
        n (int): Number of independent trials.
        k (int): Number of successful outcomes.
        p (float): Success probability on a single trial.
        
    Returns:
        dict: Mean, Variance, analytical and scipy PMF probabilities.
    """
    # Mean and Variance formulas: mu = n*p, var = n*p*(1-p)
    mean_val = n * p
    variance_val = n * p * (1 - p)
    
    # Scipy implementation
    prob_k = float(binom.pmf(k, n, p))
    
    return {
        "n_trials": n,
        "k_successes": k,
        "p_single": p,
        "mean_np": mean_val,
        "variance_npq": variance_val,
        "P(X=k)": prob_k,
        "fraction_str": "10 * (1/32) = 5/16 = 0.3125"
    }

# --- Execution & Verification ---
# Shraddha ma'am's coin problem: Toss 5 times, find probability of exactly 3 heads
res = compute_binomial_probability(n=5, k=3, p=0.5)
print(f"Trials n = {res['n_trials']}, Heads k = {res['k_successes']}, p = {res['p_single']}")
print(f"Theoretical Probability: {res['fraction_str']}")
print(f"Scipy binom.pmf result : {res['P(X=k)']:.4f}")
print(f"Mean np = {res['mean_np']}, Variance np(1-p) = {res['variance_npq']:.2f}")

```

---

### 🎯 Key Takeaways:
1. Mean $\mu = n \cdot p$ hota hai (jaise 100 coin toss mein expected 50 heads).
2. Variance $\sigma^2 = n \cdot p \cdot (1 - p)$ hota hai.
