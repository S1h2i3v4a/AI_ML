# Day 20 - Lecture 20.18: Binomial Distribution

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](lecture_20_18.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Lecture 20 Module](../README.md)

---

## 1. Overview & Bernoulli Trial Foundation

The **Binomial Distribution** models the exact number of successes $k$ in a fixed sequence of $n$ independent and identically distributed (i.i.d.) **Bernoulli trials**, each with a constant probability of success $p$.

```mermaid
flowchart LR
    A["Bernoulli Trial: Success (p) or Failure (1-p)"] --> B["Repeat n Independent Times"]
    B --> C["Binomial Variable X ~ B(n, p)"]
    C --> D["Count of Total Successes k in {0, 1, ..., n}"]
```

### Necessary Assumptions:
1. Fixed number of trials $n$.
2. Binary outcomes per trial (Success vs Failure).
3. Constant probability of success $p$ across all trials.
4. Independent trials.

---

## 2. Mathematical Formalism

### Probability Mass Function (PMF):
The probability of observing exactly $k$ successes in $n$ trials:

$$
\boxed{P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k} \quad \text{for } k \in \{0, 1, \dots, n\}}
$$

where $\binom{n}{k} = \frac{n!}{k!(n - k)!}$ accounts for all distinct permutation orders.

### Mathematical Derivation of Moments:

#### Expected Value (Mean $\mu$):
Since $X = \sum_{i=1}^n I_i$ where $I_i \sim \text{Bernoulli}(p)$ and $\mathbb{E}[I_i] = p$:

$$
\boxed{\mathbb{E}[X] = \mu = \sum_{i=1}^n \mathbb{E}[I_i] = n \cdot p}
$$

#### Variance ($\sigma^2$):
By independence, covariances vanish:

$$
\boxed{\text{Var}(X) = \sigma^2 = \sum_{i=1}^n \text{Var}(I_i) = n \cdot p \cdot (1 - p)}
$$

$$
\boxed{\sigma = \sqrt{n \cdot p \cdot (1 - p)}}
$$

---

## 3. Real-World Demonstrative Example

A customer conversion model evaluates $n = 5$ website visitors with independent conversion probability $p = 0.50$. What is the probability that exactly $k = 3$ visitors convert?

$$
\boxed{P(X = 3) = \binom{5}{3} (0.5)^3 (0.5)^2 = 10 \cdot (0.125) \cdot (0.25) = \frac{10}{32} = \frac{5}{16} = 0.3125 \quad (31.25\%)}
$$

---

## 4. Python Implementation

```python
from scipy.stats import binom
import numpy as np

n = 5
k = 3
p = 0.5

# 1. PMF calculation
prob_pmf = binom.pmf(k, n, p)
print(f"Scipy PMF P(X = {k} | n={n}, p={p}): {prob_pmf:.4f} (Exact: 5/16 = {5/16:.4f})")

# 2. Cumulative Distribution Function (CDF): P(X <= 3)
prob_cdf = binom.cdf(k, n, p)
print(f"Cumulative P(X <= {k}):               {prob_cdf:.4f}")

# 3. Moments verification
mean_ana = n * p
var_ana = n * p * (1 - p)
print(f"Analytical Mean = {mean_ana:.2f}, Variance = {var_ana:.4f}")
```

---

## 5. Key Takeaways & Interview Points
- **Maximum Variance at $p = 0.5$:** $\text{Var}(X)$ is maximized when outcomes are most uncertain ($p = 0.5$).
- **Normal Approximation:** When $n$ is large and $np \ge 5, n(1-p) \ge 5$, the Binomial distribution converges smoothly to a Gaussian $\mathcal{N}(np, np(1-p))$.
