# Day 18 - Lecture 18.18: Advanced Customizations on Pie Charts [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_18.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 18 Module Par Wapas Jayein](../README_HINGLISH.md)

---

## 1. Overview & Visual Emphasis Techniques
Standard flat pie charts can look plain. Matplotlib allows rich customizations to **emphasize specific categories**, improve aesthetics, and control borders:
- **`explode`:** Pulls a specific slice outward from the pie center.
- **`shadow=True`:** Adds depth and drop-shadow styling.
- **`startangle`:** Rotates the pie so the primary slice begins at a specific angle (e.g. $90^\circ$ top or $180^\circ$).
- **`wedgeprops`:** Controls border width, edgecolor, and fill transparency.

---

## 2. Advanced Parameters & Wedgeprops

```python
wedgeprops = {
    'edgecolor': 'black',    # Border outline color
    'linewidth': 1.5,        # Outline thickness
    'linestyle': '--',       # Dashed border
    'fill': True             # Whether to fill slice
}
```

### Explode Offset Vector:
An array of floats of equal length to categories, where each value represents the fractional radius offset:
```python
# Pulls only the 4th slice ("R&D") outward by 20% of radius:
explode = [0, 0, 0, 0.2, 0]
```

---

## 3. Code Implementation

```python
import matplotlib.pyplot as plt

expenses = ["Salaries", "Rent", "Marketing", "R&D", "Miscellaneous"]
amounts = [500, 150, 120, 100, 50]

# Explode the 4th category ("R&D")
explode = [0, 0, 0, 0.15, 0]
colors = ["#4e79a7", "#f28e2b", "#e15759", "#76b7b2", "#59a14f"]

plt.figure(figsize=(8, 8))
plt.pie(
    amounts,
    labels=expenses,
    autopct='%1.1f%%',
    explode=explode,
    shadow=True,
    startangle=90,          # Starts highest slice at 12 o'clock position
    colors=colors,
    wedgeprops={"edgecolor": "black", "linewidth": 1.2}
)

plt.title("Budget Distribution with Exploded Slice (R&D) & Shadow", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()

# Donut Chart Concept using wedgeprops
plt.figure(figsize=(7, 7))
plt.pie(
    amounts,
    labels=expenses,
    autopct='%1.1f%%',
    pctdistance=0.75,
    colors=colors,
    wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2)  # width < 1 creates donut hole!
)
plt.title("Modern Donut Chart (Budget Breakdown)", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()
```

---

## 4. Mukhya Batein (Key Takeaways)
- Setting `wedgeprops=dict(width=0.4)` automatically turns a pie chart into a modern **Donut Chart**, which is widely preferred in corporate dashboards because the empty center can display the total budget ($920K).
- Use `startangle=90` so the largest slice starts at 12 o'clock and rotates clockwise.
