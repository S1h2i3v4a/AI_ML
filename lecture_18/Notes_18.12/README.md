# Day 18 - Lecture 18.12: Horizontal Bar Charts (`plt.barh`)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_12.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Lecture 18 Module](../README.md)

---

## 1. Overview & When to Use Horizontal Bars
When category names are long (e.g. movie titles like *"The Hurt Locker"*, *"Slumdog Millionaire"*), vertical bar charts force labels to collide, overlap, or require severe 90° rotation that strains human neck reading.

**Horizontal Bar Charts (`plt.barh`)** solve this by placing categories on the **Y-axis** and numerical values on the **X-axis**, giving unlimited horizontal room for lengthy labels.

---

## 2. Syntax & Inversion of Axes

```python
plt.barh(
    y,                      # Categorical labels on vertical axis
    width,                  # Length of horizontal bars (the numeric values)
    height=0.8,             # Vertical thickness of bars
    color='steelblue',      # Color
    edgecolor='black'       # Border outline
)
```

> [!NOTE]
> In `plt.bar()`, the numerical values go into `height=`.
> In `plt.barh()`, the numerical values go into `width=`, because bars extend horizontally!

---

## 3. Code Implementation

```python
import matplotlib.pyplot as plt

oscar_movies = [
    "The Dark Knight", 
    "The Hurt Locker", 
    "The King's Speech", 
    "The Artist", 
    "Argo"
]
oscar_revenue = [1005, 170, 427, 133, 232]  # in $M

plt.figure(figsize=(9, 5))
plt.barh(oscar_movies, oscar_revenue, color="teal", edgecolor="black", height=0.6)

plt.title("Box Office Revenue for Oscar Best Picture Winners", fontsize=14, fontweight="bold")
plt.xlabel("Revenue (in $ Millions)", fontsize=12)
plt.ylabel("Movie Title", fontsize=12)
plt.grid(axis='x', linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()
```

---

## 📐 Horizontal & Stacked Bar Chart Geometry

For horizontal bar charts, the coordinate axes transpose roles. The bounding box for category $i$ with length $x_i$ and bar thickness $h$ is:

$$
\boxed{\mathcal{R}_i = [0, \; x_i] \times \left[ y_i - \frac{h}{2}, \; y_i + \frac{h}{2} \right]}
$$

For stacked bar charts with $K$ components, each segment rests on the cumulative sum of preceding layers:

$$
\boxed{y_{k, i}^{(\text{bottom})} = \sum_{j=1}^{k-1} h_{j, i} \qquad\text{and}\qquad y_{k, i}^{(\text{top})} = \sum_{j=1}^k h_{j, i}}
$$

---

## 4. Key Takeaways
- Use `plt.barh` whenever you have $\ge 7$ categories or when category strings exceed 10 characters.
- Invert the y-axis if desired (`plt.gca().invert_yaxis()`) to display the highest ranked category at the very top.
