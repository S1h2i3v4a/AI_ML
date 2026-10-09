# Day 20 - Lecture 20.14: Random Variables

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](lecture_20_14.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Lecture 20 Module](../README.md)

---

## 1. Formal Mathematical Definition

A **Random Variable** is not a traditional algebraic variable; it is a **mathematical function** that maps outcomes from an abstract sample space $\mathcal{S}$ to real numerical values on the real number line $\mathbb{R}$:

$$
\boxed{X: \mathcal{S} \to \mathbb{R}}
$$

```mermaid
flowchart LR
    S["Sample Space S: {HH, HT, TH, TT}"] -->|Mapping Function X(w)| R["Real Line R: {0, 1, 2}"]
```

---

## 2. Taxonomy: Discrete vs. Continuous Random Variables

| Property | Discrete Random Variable | Continuous Random Variable |
| :--- | :--- | :--- |
| **Possible Values** | Countable set $\{x_1, x_2, \dots\}$ | Continuous uncountably infinite interval $[a, b] \subseteq \mathbb{R}$ |
| **Probability Function** | Probability Mass Function (PMF) $p(x)$ | Probability Density Function (PDF) $f(x)$ |
| **Single-Point Probability** | $P(X = x) \ge 0$ | $P(X = x) \equiv 0$ |
| **Normalization Law** | $\sum_{x} p(x) = 1.0$ | $\int_{-\infty}^\infty f(x) \, dx = 1.0$ |
| **Interval Probability** | $P(a \le X \le b) = \sum_{x=a}^b p(x)$ | $P(a \le X \le b) = \int_a^b f(x) \, dx$ |

---

## 3. The Cumulative Distribution Function (CDF)

The **CDF** $F(x)$ represents the probability that random variable $X$ takes a value less than or equal to $x$, universally defined for both discrete and continuous variables:

$$
\boxed{F(x) = P(X \le x)}
$$

### Fundamental Properties of CDF:
1. **Monotonic Non-Decreasing:** $x_1 < x_2 \implies F(x_1) \le F(x_2)$
2. **Boundary Limits:**

$$
\boxed{\lim_{x \to -\infty} F(x) = 0.0 \qquad\text{and}\qquad \lim_{x \to \infty} F(x) = 1.0}
$$

3. **Relationship to Continuous PDF:**

$$
\boxed{F(x) = \int_{-\infty}^x f(t) \, dt \iff f(x) = \frac{d}{dx} F(x)}
$$

---

## 4. Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

# 1. Discrete Random Variable: Number of Heads in 3 Coin Flips
flips_3 = [0, 1, 2, 3]
pmf_discrete = [1/8, 3/8, 3/8, 1/8]
cdf_discrete = np.cumsum(pmf_discrete)

print("Discrete Variable X = Number of Heads:")
for k, p, c in zip(flips_3, pmf_discrete, cdf_discrete):
    print(f"  k = {k}: PMF P(X={k}) = {p:.3f} | CDF F({k}) = {c:.3f}")

# 2. Continuous Random Variable Simulation
samples = np.random.normal(loc=0, scale=1, size=100_000)
p_between = np.mean((samples >= -1.0) & (samples <= 1.0))
print(f"\nContinuous Variable Z ~ N(0, 1): P(-1 <= Z <= 1) = {p_between:.4f} (Exact: 68.27%)")
```

---

## 5. Key Takeaways & Interview Points
- **Point Probability of Continuous RV is Zero:** For a continuous random variable, $P(X = 3.500000...) = 0$. Probability exists only over finite intervals $[a, b]$.
- **CDF is Universal:** Whether discrete, continuous, or mixed, every random variable has a well-defined CDF bounded in $[0, 1]$.
