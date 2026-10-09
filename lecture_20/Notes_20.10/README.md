# Day 20 - Lecture 20.10: Conditional Probability

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](lecture_20_10.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Lecture 20 Module](../README.md)

---

## 1. Overview & Sample Space Reduction

**Conditional Probability** measures the likelihood of an event $A$ occurring given that another event $B$ has already occurred ($P(A \mid B)$). Geometrically, conditioning on event $B$ shrinks the relevant universe from the entire sample space $\mathcal{S}$ down exclusively to the subset $B$.

```mermaid
flowchart LR
    S["Global Universe S"] -->|Condition on B| B["Reduced Sample Space B"]
    B --> A_given_B["Fraction occupied by (A cap B) inside B"]
```

---

## 2. Mathematical Formalism

### Formal Definition:
For any two events $A$ and $B$ where $P(B) > 0$:

$$
\boxed{P(A \mid B) = \frac{P(A \cap B)}{P(B)}}
$$

In a finite uniform discrete sample space with cardinality counting:

$$
\boxed{P(A \mid B) = \frac{|A \cap B|}{|B|}}
$$

### Kolmogorov Axiom Consistency:
Conditional probability is a rigorous probability measure satisfying all three Kolmogorov axioms over the restricted universe $B$:
1. $P(A \mid B) \ge 0$
2. $P(B \mid B) = 1.0$
3. $P(A_1 \cup A_2 \mid B) = P(A_1 \mid B) + P(A_2 \mid B)$ if $A_1 \cap A_2 = \emptyset$.

---

## 3. Real-World Demonstrative Example

A medical dataset contains 1,000 patient records classified by smoking status and cardiovascular disease (CVD):
- Smoker ($B$): 300 patients
- Non-Smoker ($B'$): 700 patients
- Smoker AND Has CVD ($A \cap B$): 90 patients
- Non-Smoker AND Has CVD ($A \cap B'$): 35 patients

What is the probability that a randomly chosen patient has CVD given that they are a smoker?

$$
\boxed{P(\text{CVD} \mid \text{Smoker}) = \frac{P(\text{CVD} \cap \text{Smoker})}{P(\text{Smoker})} = \frac{90 / 1000}{300 / 1000} = \frac{90}{300} = 0.30 \quad (30\%)}
$$

What is the baseline unconditional probability of CVD across the general population?

$$
\boxed{P(\text{CVD}) = \frac{90 + 35}{1000} = \frac{125}{1000} = 0.125 \quad (12.5\%)}
$$

Because $P(\text{CVD} \mid \text{Smoker}) = 0.30 \ne P(\text{CVD}) = 0.125$, smoking and cardiovascular disease are statistically dependent.

---

## 4. Python Implementation

```python
import pandas as pd

# Contingency table representation
data = {
    'CVD_Yes': [90, 35],
    'CVD_No': [210, 665]
}
df = pd.DataFrame(data, index=['Smoker', 'NonSmoker'])

total = df.values.sum()
p_smoker = df.loc['Smoker'].sum() / total
p_cvd_and_smoker = df.loc['Smoker', 'CVD_Yes'] / total

# Conditional Probability P(CVD | Smoker)
p_cvd_given_smoker = p_cvd_and_smoker / p_smoker

print("Contingency Table:\n", df)
print(f"\nP(Smoker):              {p_smoker:.4f}")
print(f"P(CVD and Smoker):      {p_cvd_and_smoker:.4f}")
print(f"P(CVD | Smoker):        {p_cvd_given_smoker:.4f} (Exact: 90/300 = {90/300:.4f})")
```

---

## 5. Key Takeaways & Interview Points
- **Universe Reduction:** Conditioning on $B$ changes the denominator from $|\mathcal{S}|$ to $|B|$.
- **Conditioning vs Intersection:** $P(A \cap B)$ is the probability of both happening in the global universe; $P(A \mid B)$ is the probability of $A$ happening once we already know $B$ is true.
