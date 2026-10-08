# Day 19 - Lecture 19.12: Relational Plots in Seaborn (`relplot`, `scatterplot`, `lineplot`) [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_19_12.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 19 Module Par Wapas Jayein](../README_HINGLISH.md)

---

## 1. Overview & Purpose
**Relational Plots** are designed to visualize the **relationship between two or more continuous numerical variables**.
Seaborn provides two primary relational plot types:
1. **Scatter Plot (`sns.scatterplot`):** Ideal when each row represents an independent observation. Shows correlation, clusters, and spread.
2. **Line Plot (`sns.lineplot`):** Ideal when the $x$-axis represents a continuous, ordered progression (e.g. time, year, sequence). Automatically performs **aggregation and confidence interval estimation** for multiple measurements at each $x$.

---

## 2. Automatic Aggregation & Confidence Intervals

When multiple records exist for a single $x$ value (e.g., monthly passenger records across multiple years):
- `sns.lineplot()` computes the **mean** line:
  $$\bar{y}_x = \frac{1}{m} \sum_{j=1}^{m} y_{x, j}$$
- It draws a **shaded band** around the line representing the **95% Confidence Interval (CI)** (by default using bootstrapping) or Standard Deviation:
  ```python
  sns.lineplot(data=df, x='year', y='passengers', errorbar='ci') # 95% CI
  sns.lineplot(data=df, x='year', y='passengers', errorbar='sd') # Standard Deviation
  sns.lineplot(data=df, x='year', y='passengers', errorbar=None) # No band
  ```

---

## 3. Code Implementation

```python
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Scatter Plot on tips dataset
tips = sns.load_dataset("tips")

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="time",
    palette="Dark2",
    s=70,
    alpha=0.85
)
plt.title("Scatter Plot: Total Bill vs Tip (Colored by Lunch / Dinner)", fontsize=13, fontweight="bold")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()

# 2. Line Plot with Aggregation on flights dataset
flights = sns.load_dataset("flights")

plt.figure(figsize=(9, 5))
sns.lineplot(
    data=flights,
    x="year",
    y="passengers",
    color="navy",
    marker="o",
    errorbar="sd"  # Shows standard deviation across months
)
plt.title("Annual Flight Passengers Trend (Aggregated Across Months with SD)", fontsize=13, fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Number of Passengers")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
```

---

## 📐 Grammar of Graphics Semantic Mapping Ka Ganitiya Sutra

Seaborn statistical attributes ko visual dimensions par formal aesthetic mapping $\Phi$ se bind karta hai:

$$
\boxed{\Phi: \mathcal{D}_1 \times \mathcal{D}_2 \times \mathcal{D}_3 \to \mathbb{R}^2 \times \mathcal{C} \times \mathcal{S}}
$$

jahan data columns simultaneously spatial position $(x, y)$, color hue $\mathcal{C}$, aur marker style $\mathcal{S}$ me encode hote hain.

---
## 4. Mukhya Batein (Key Takeaways) & Best Practices
- Use **`sns.scatterplot`** to spot bivariate correlation and non-linear patterns.
- Use **`sns.lineplot`** whenever $x$ represents time series or sequential tracking.
- The shaded area in `lineplot` is not an error in your code—it represents the statistical variance across sub-samples!
