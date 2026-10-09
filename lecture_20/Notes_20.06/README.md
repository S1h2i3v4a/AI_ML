# Day 20 - Lecture 20.6: The Complementary Rule

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_20_06.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Lecture 20 Module](../README.md)

---

## 1. Overview & Conceptual Architecture

The **Complementary Rule** is one of the most powerful analytical shortcuts in probability calculus and computational engineering. For any event $A$, its complement $A'$ (or $A^c$) consists of all outcomes in the sample space $\mathcal{S}$ that are not in $A$.

```mermaid
flowchart LR
    S["Sample Space S (P = 1.0)"] --> A["Event A (Probability P(A))"]
    S --> A_prime["Complement A' (Probability 1 - P(A))"]
    A -.->|Disjoint & Exhaustive| A_prime
```

### Strategic Value in Machine Learning:
When calculating the probability of a complex compound event involves dozens of permutations, evaluating its complement is often a trivial single-step calculation:

$$
oxed{P(	ext{At least one success}) = 1 - P(	ext{Zero successes})}
$$

---

## 2. Mathematical Formalism & Theorems

By definition, an event $A$ and its complement $A'$ form a binary partition of the sample space:

$$
oxed{A \cap A' = \emptyset \qquad	ext{and}\qquad A \cup A' = \mathcal{S}}
$$

Applying Kolmogorov's Axioms 2 and 3:

$$
oxed{P(A \cup A') = P(A) + P(A') = P(\mathcal{S}) = 1.0}
$$

Rearranging yields the canonical **Complement Rule**:

$$
oxed{P(A') = 1 - P(A) \iff P(A) = 1 - P(A')}
$$

### De Morgan's Laws for Probabilities:
For any two events $A$ and $B$:

$$
oxed{(A \cup B)' = A' \cap B' \implies P(A \cup B) = 1 - P(A' \cap B')}
$$

$$
oxed{(A \cap B)' = A' \cup B' \implies P(A \cap B) = 1 - P(A' \cup B')}
$$

---

## 3. Real-World Case: "At Least One" Failure Problem

Consider an AI server cluster with $n = 10$ independent GPUs. Each GPU has an independent daily failure probability $p = 0.05$. What is the probability that **at least one** GPU fails today?

- Direct calculation: Summing $P(X = 1) + P(X = 2) + \dots + P(X = 10)$ across 10 combinatorial terms.
- Complementary calculation:
  Let $A = 	ext{"At least one GPU fails"}$.
  Then $A' = 	ext{"Zero GPUs fail"}$.
  Since all GPUs are independent, $P(	ext{GPU safe}) = 1 - 0.05 = 0.95$.

$$
oxed{P(A') = (0.95)^{10} pprox 0.5987}
$$

$$
oxed{P(A) = 1 - P(A') = 1 - 0.5987 = 0.4013 \quad (40.13\%)}
$$

---

## 4. Python Implementation

```python
import numpy as np

n_gpus = 10
p_fail = 0.05
p_safe = 1 - p_fail

# Analytical Complement Rule
p_zero_fails = p_safe ** n_gpus
p_at_least_one = 1.0 - p_zero_fails

print(f"Single GPU Failure Rate: {p_fail * 100:.1f}%")
print(f"P(Zero GPU Failures):    {p_zero_fails:.4f}")
print(f"P(At Least 1 Failure):   {p_at_least_one:.4f} ({p_at_least_one * 100:.2f}%)")

# Monte Carlo Verification (1,000,000 simulations)
simulations = np.random.binomial(n=n_gpus, p=p_fail, size=1_000_000)
empirical_at_least_one = np.mean(simulations >= 1)
print(f"Monte Carlo Empirical:   {empirical_at_least_one:.4f}")
```

---

## 5. Key Takeaways & Interview Points
- **The "At Least One" Trigger:** Whenever an interview question or problem asks for "at least one", immediately consider using the complement rule $1 - P(	ext{None})$.
- **Computational Simplicity:** Complement calculation reduces an exponential combinatorial summation into a single product.
