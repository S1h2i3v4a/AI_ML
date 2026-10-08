# Day 18 - Lecture 18.17: Pie Charts (`plt.pie`) [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_17.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 18 Module Par Wapas Jayein](../README_HINGLISH.md)

---

## 1. Overview & Mathematical Definition
A **Pie Chart** is a circular graphic divided into slices to illustrate numerical proportions of a whole (100%).
- Each slice represents a category.
- The arc length, central angle, and area of each slice are proportional to the quantity it represents.

### Central Angle Formulation:
$$\theta_i = 360^\circ \times \frac{y_i}{\sum_{j=1}^{K} y_j}$$

### Percentage of Total:
$$\%_i = 100\% \times \frac{y_i}{\sum_{j=1}^{K} y_j}$$

---

## 2. Syntax & Parameters

```python
plt.pie(
    x,                      # Slice magnitudes (array of values)
    labels=None,            # Sequence of strings providing labels for each slice
    autopct='%1.1f%%',      # String or function used to format slice value percentages
    colors=None,            # List of color codes for slices
    startangle=0,           # Counter-clockwise rotation angle from the x-axis
    explode=None,           # Fractional radius offset to pull slices outwards
    shadow=False            # Draw a 3D drop shadow beneath pie
)
```

---

## 3. Code Implementation: Corporate Expense Breakdown

```python
import matplotlib.pyplot as plt

expenses = ["Salaries", "Rent", "Marketing", "R&D", "Miscellaneous"]
amounts = [500, 150, 120, 100, 50]  # Total = $920K

colors = ["#4C72B0", "#55A868", "#C44E52", "#8172B2", "#CCB974"]

plt.figure(figsize=(7, 7))
plt.pie(
    amounts,
    labels=expenses,
    autopct='%1.1f%%',      # Displays percentage formatted to 1 decimal place
    colors=colors,
    startangle=140
)

plt.title("Company Budget Allocation by Expense Category", fontsize=14, fontweight="bold")
plt.show()
```

---

## 📐 Pie Chart Ke Circular Sector Ka Ganitiya Sutra

Non-negative values $V = \{v_1, v_2, \dots, v_n\}$ jinka total sum $V_{\text{total}} = \sum_{j=1}^n v_j$ hai, har category slice $i$ ka central angle aur percentage:

$$
\boxed{\theta_i = 360^\circ \times \frac{v_i}{\sum_{j=1}^n v_j} \qquad\text{aur}\qquad p_i = \frac{v_i}{\sum_{j=1}^n v_j} \times 100\%}
$$

Conservation niyam:
$$
\boxed{\sum_{i=1}^n \theta_i = 360^\circ \qquad\text{aur}\qquad \sum_{i=1}^n p_i = 100\%}
$$

Radius $R$ wale circular sector ka arc length $L_i$ aur area $A_i$:
$$
\boxed{L_i = R \cdot \left(\frac{\pi \theta_i}{180^\circ}\right) \qquad\text{aur}\qquad A_i = \frac{1}{2} R^2 \left(\frac{\pi \theta_i}{180^\circ}\right) = \pi R^2 \cdot \frac{p_i}{100}}
$$

---
## 4. Mukhya Batein (Key Takeaways) & Limitations
- **When to Use:** Part-to-whole relationships with **few categories (3 to 5 max)**.
- **When NOT to Use:** When comparing more than 6 categories, or comparing two categories of similar sizes (e.g. 24% vs 26%). The human brain is poor at estimating angles and areas compared to estimating lengths in bar charts.
