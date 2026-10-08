# Day 18 - Lecture 18.10: Adding Labels to Bars (`plt.text`)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_10.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Lecture 18 Module](../README.md)

---

## 1. Overview & Purpose
While bar heights give a visual comparison, viewers frequently need the **exact numerical value** without having to trace their eyes horizontally to the Y-axis. Adding direct value labels on top of each bar drastically improves readability.

---

## 2. Syntax & Mechanics: `plt.text()`

```python
plt.text(
    x,                      # X coordinate (center of the bar)
    y,                      # Y coordinate (top of bar + offset)
    s,                      # String text to display
    ha='center',            # Horizontal alignment: 'center', 'left', 'right'
    va='bottom',            # Vertical alignment: 'bottom', 'top', 'center'
    fontsize=10,            # Text font size
    fontweight='bold'       # Font weight
)
```

### The Problem of Top Clipping & `plt.ylim()`:
If a bar has height 1005 and your Y-axis tops out at 1005, putting text at `y = 1005 + 20` will push the text outside the canvas boundary!
**Solution:** Always expand the upper Y-limit using:
```python
plt.ylim(0, max(revenue) + 200)
```

---

## 3. Code Implementation

```python
import matplotlib.pyplot as plt

years = [2008, 2009, 2010, 2011, 2012]
revenue = [1005, 170, 427, 133, 232]  # in $M

plt.figure(figsize=(8, 5))
plt.bar(years, revenue, color="purple", width=0.55, edgecolor="black")

# Add numerical values above each bar
for i in range(len(revenue)):
    plt.text(
        x=years[i],
        y=revenue[i] + 25,          # Offset above the bar top
        s=f"${revenue[i]}M",        # Formatted string
        ha="center",                # Horizontally centered
        fontweight="bold"
    )

# Add top padding so the highest label is not clipped
plt.ylim(0, max(revenue) + 180)

plt.xlabel("Years", fontsize=12)
plt.ylabel("Revenue (in $M)", fontsize=12)
plt.title("Yearly Revenue of Movies with Value Labels", fontsize=14, fontweight="bold")
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.show()
```

---

## 📐 Bar Label Coordinate Geometry & Padding Offset

Direct data labeling places numerical callouts directly above each bar without requiring gridline tracing. The centroid coordinate $(x_{\text{label}}, y_{\text{label}})$ for bar $i$ is given by:

$$
\boxed{x_{\text{label}, i} = x_i \qquad\text{and}\qquad y_{\text{label}, i} = y_i + \delta}
$$

where vertical offset $\delta$ is computed proportionally from the global range:
$$
\boxed{\delta = \epsilon \cdot \max_{0 \le j < N}(y_j), \quad \epsilon \in [0.01, 0.03]}
$$

---
## 4. Key Takeaways
- Always pair direct data labels with `plt.ylim()` to guarantee adequate headroom.
- In modern Matplotlib (v3.4+), `plt.bar_label()` is also available as an automatic alternative.
