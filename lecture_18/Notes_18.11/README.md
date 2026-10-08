# Day 18 - Lecture 18.11: Grouped / Clustered Bar Charts

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_11.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Lecture 18 Module](../README.md)

---

## 1. Overview & The Coordinate Offset Mechanism
When comparing two or more metrics across identical categories (e.g. Oscar vs Non-Oscar movie revenues across years), simply calling `plt.bar()` twice will cause the second set of bars to **overlap directly on top of the first**, hiding the data.

To create a **Grouped (Side-by-Side) Bar Chart**, we must manually calculate horizontal coordinate offsets using **NumPy**:

```mermaid
flowchart TD
    A["Categories: 5 Years"] --> B["Base Indices: x = np.arange(5) = [0, 1, 2, 3, 4]"]
    B --> C["Group 1 Position: x - width/2"]
    B --> D["Group 2 Position: x + width/2"]
    C & D --> E["Replace Numeric Ticks with Year Strings: plt.xticks(x, years)"]
```

---

## 📐 Mathematical Coordinate Formulation (Grouped Bars)

Let $N$ denote the total number of categories, and let $K = 2$ denote two comparative series. Let $x_i = i$ ($i \in \{0, 1, \dots, N-1\}$) represent the baseline categorical coordinates along the axis.

To position two bars of uniform width $w$ symmetrically side-by-side with zero overlap:
$$
\boxed{
\begin{cases}
x_{1, i} = x_i - \dfrac{w}{2} & (\text{Series 1: Budget}) \\
x_{2, i} = x_i + \dfrac{w}{2} & (\text{Series 2: Spend})
\end{cases}
}
$$

The categorical tick label coordinate $t_i$ satisfies the central symmetry theorem:
$$
\boxed{t_i = \frac{x_{1, i} + x_{2, i}}{2} = \frac{\left(x_i - \dfrac{w}{2}\right) + \left(x_i + \dfrac{w}{2}\right)}{2} = x_i}
$$

For generalized $K \ge 2$ comparative series:
$$
\boxed{x_{k, i} = x_i + \left(k - \frac{K - 1}{2}\right) \cdot w \quad \text{for } k \in \{0, 1, \dots, K-1\}}
$$

---

## 3. Code Implementation

```python
import matplotlib.pyplot as plt
import numpy as np

oscar_revenue = [1005, 170, 427, 133, 232]       # Oscar Winners
non_oscar_revenue = [378, 2788, 829, 185, 275]   # Non-Oscar Blockbusters
years = [2008, 2009, 2010, 2011, 2012]

# 1. Generate numerical index array
x = np.arange(len(years))  # array([0, 1, 2, 3, 4])
width = 0.38               # Bar width

plt.figure(figsize=(10, 6))

# 2. Plot both groups with offset positions
plt.bar(x - width/2, oscar_revenue, width=width, label="Oscar Winners", color="#386cb0", edgecolor="black")
plt.bar(x + width/2, non_oscar_revenue, width=width, label="Non-Oscar Blockbusters", color="#fdc086", edgecolor="black")

# 3. Restore categorical x-axis labels
plt.xticks(x, years, fontsize=11)

plt.xlabel("Years", fontsize=12)
plt.ylabel("Revenue (in $M)", fontsize=12)
plt.title("Yearly Revenue: Oscar vs Non-Oscar Winners", fontsize=14, fontweight="bold")
plt.legend(fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
```

---

## 4. Key Takeaways
- Without `plt.xticks(x, years)`, the horizontal axis would display raw indices `[0, 1, 2, 3, 4]` instead of `[2008, 2009, 2010, 2011, 2012]`.
- For 3 groups, offset positions become $x - w$, $x$, and $x + w$ with a narrower width $w \approx 0.25$.
