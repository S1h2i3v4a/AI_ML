# Lecture 28.03: Entropy as an Impurity Metric

## 📌 Topic Overview
To automate feature selection, a Decision Tree needs a mathematical formula to quantify impurity and disorder. That formula is **Entropy**. In this lecture, we study the theoretical formula, its range, and the exact step-by-step blackboard calculation.

---

## 📐 Mathematical Definition of Entropy
**Entropy** originated in physics (thermodynamics) and information theory (Claude Shannon). In Machine Learning:
> **Entropy measures the impurity, disorder, or uncertainty in a given dataset $S$.**

The formula for a dataset with $c$ classes is:

$$E(S) = -\sum_{i=1}^c p_i \log_2(p_i)$$

Where:
- $p_i$ is the proportion (probability) of class $i$ in sample set $S$.
- $\log_2$ is logarithm base 2.

For a binary classification task (classes `Yes` and `No`):

$$E(S) = - p_{	ext{yes}} \log_2(p_{	ext{yes}}) - p_{	ext{no}} \log_2(p_{	ext{no}})$$

---

## 📈 Range and Inverted Parabola Curve
For binary classification:
- **Minimum Value = 0**: When the node is 100% pure (all `Yes` or all `No`). There is zero uncertainty!
- **Maximum Value = 1**: When there is a 50-50 split ($p_{	ext{yes}} = 0.5$, $p_{	ext{no}} = 0.5$). There is maximum uncertainty!

```
Entropy E(S)
1.0 +         .-'-.
|       .'     '.
|      /         \
0.5 +     /           \
|    /             \
|   /               \
0.0 +--+-----------------+--
0        0.5      1    Probability (p)
```

At $p=0$ and $p=1$, entropy drops to $0$. At $p=0.5$, entropy peaks at $1.0$.

---

## 🧮 Step-by-Step Numerical Example from Video
In the video, the instructor works out the following calculation on the blackboard:

### Given Node:
$S = [3y, 3n]$ (3 Yes and 3 No, total samples = 6).

$$p_{	ext{yes}} = rac{3}{6} = rac{1}{2} = 0.5$$

$$p_{	ext{no}} = rac{3}{6} = rac{1}{2} = 0.5$$

Applying the formula:

$$E(S) = - \left( rac{1}{2} \cdot \log_2 rac{1}{2} 
ight) - \left( rac{1}{2} \cdot \log_2 rac{1}{2} 
ight)$$

Recall that $\log_2(0.5) = \log_2(2^{-1}) = -1$:

$$E(S) = - \left( rac{1}{2} \cdot (-1) 
ight) - \left( rac{1}{2} \cdot (-1) 
ight) = rac{1}{2} + rac{1}{2} = 1.0$$

### Completely Pure Node:
For a node $S_{	ext{pure}} = [0y, 3n]$ (all 3 samples are No):
- $p_{	ext{yes}} = 0$, $p_{	ext{no}} = 1$.
- By convention, $0 \cdot \log_2(0) = 0$.
- $E(S_{	ext{pure}}) = - 0 - (1 \cdot \log_2 1) = 0 - 0 = 0.0$.

---

## 💻 Python Implementation

```python
import numpy as np

def calculate_entropy(y_count, n_count):
total = y_count + n_count
if total == 0:
return 0.0
p_y = y_count / total
p_n = n_count / total

term_y = p_y * np.log2(p_y) if p_y > 0 else 0
term_n = p_n * np.log2(p_n) if p_n > 0 else 0

return -(term_y + term_n)

print("Entropy of [3y, 3n] (50-50):", calculate_entropy(3, 3))
print("Entropy of [0y, 3n] (Pure): ", calculate_entropy(0, 3))
print("Entropy of [2y, 1n]:        ", round(calculate_entropy(2, 1), 4))
```

---

## 🔑 Key Takeaways
1. Entropy measures disorder or unpredictability.
2. For binary classification, Entropy is bounded between $0$ (pure) and $1$ (maximum uncertainty).
3. The lower the entropy of a node, the better and cleaner that subset is.
