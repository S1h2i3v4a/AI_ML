# Day 19 - Lecture 19.15: Relational & Matrix Plots - Heatmaps [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_19_15.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 19 Module Par Wapas Jayein](../README_HINGLISH.md)

---

## 1. Overview & Purpose
A **Heatmap** represents 2D tabular or matrix data where individual values are encoded as **color variations**.
Primary use cases in Machine Learning and Data Science:
1. **Correlation Matrix:** Detecting multi-collinearity and linear relationships between feature columns.
2. **Pivot Tables & Cross-Tabulations:** Analyzing interactions between two categorical dimensions (e.g., Passengers across Years and Months).
3. **Confusion Matrices:** Evaluating classification model performance.

---

## 2. Pivot Tables & Matrix Transformation

Raw time-series data often comes in "long form":
| year | month | passengers |
| :--- | :--- | :--- |
| 1949 | Jan | 112 |
| 1949 | Feb | 118 |

To plot a heatmap, we must reshape it into "wide/matrix form" using Pandas **`.pivot()`**:
```python
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")
```
$$\begin{matrix} & 1949 & 1950 & \dots & 1960 \\ \text{Jan} & 112 & 115 & \dots & 417 \\ \text{Feb} & 118 & 126 & \dots & 391 \end{matrix}$$

---

## 3. Key Parameters of `sns.heatmap()`

```python
sns.heatmap(
    data,                # 2D rectangular dataset (DataFrame or 2D array)
    annot=True,          # If True, prints numerical values inside each cell
    fmt="d",             # Format string: "d" for integer, ".2f" for 2 decimals
    cmap="coolwarm",     # Colormap ('viridis', 'coolwarm', 'YlGnBu', 'magma')
    linewidths=0.5,      # Width of lines separating each cell
    cbar=True            # Show colorbar legend
)
```

---

## 4. Code Implementation

```python
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Pivot Table Heatmap: Flight Passengers
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

plt.figure(figsize=(11, 7))
sns.heatmap(
    flights_pivot,
    cmap="YlGnBu",
    annot=True,
    fmt="d",
    linewidths=0.5
)
plt.title("Monthly Airline Passengers from 1949 to 1960", fontsize=15, fontweight="bold")
plt.xlabel("Year", fontsize=12)
plt.ylabel("Month", fontsize=12)
plt.tight_layout()
plt.show()

# 2. Correlation Matrix Heatmap: Tips Dataset
tips = sns.load_dataset("tips")
# Select only numeric columns for correlation
numeric_tips = tips.select_dtypes(include=['float64', 'int64'])
corr_matrix = numeric_tips.corr()

plt.figure(figsize=(7, 5))
sns.heatmap(
    corr_matrix,
    cmap="coolwarm",
    annot=True,
    fmt=".2f",
    vmin=-1, vmax=1,
    center=0,
    square=True
)
plt.title("Correlation Matrix (Tips Dataset)", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()
```

---

## 5. Mukhya Batein (Key Takeaways)
- **Diverging vs. Sequential Colormaps:**
  - For **Correlations** (ranging from $-1$ to $+1$), use a **diverging colormap** like `coolwarm` with `center=0`.
  - For **Magnitudes / Counts** (ranging from $0$ to large values), use a **sequential colormap** like `YlGnBu` or `viridis`.
- Always set `fmt="d"` for integers and `fmt=".2f"` for floats; otherwise, scientific notation will clutter cells.


---

## 📐 Correlation Matrix Ka Ganitiya Sutra

Matrix $\mathbf{X} \in \mathbb{R}^{n \times p}$ ke $p$ variables ke beech pairwise correlation matrix $\mathbf{R} \in \mathbb{R}^{p \times p}$ ka formula:

$$
\boxed{r_{jk} = \frac{\sum_{i=1}^n (x_{ij} - \bar{x}_j)(x_{ik} - \bar{x}_k)}{\sqrt{\sum_{i=1}^n (x_{ij} - \bar{x}_j)^2} \sqrt{\sum_{i=1}^n (x_{ik} - \bar{x}_k)^2}} \in [-1, +1]}
$$

Correlation Matrix Ki Properties:
1. **Symmetric**: $\mathbf{R} = \mathbf{R}^T$ kyunki $r_{jk} = r_{kj}$.
2. **Main Diagonal**: $r_{jj} = 1.0$ (har variable ka khud ke sath correlation 1 hota hai).
3. **Positive Semi-Definite**: $\mathbf{z}^T \mathbf{R} \mathbf{z} \ge 0$.
