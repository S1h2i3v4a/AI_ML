# Day 18 - Lecture 18.5: Multiple Datasets on Line Plot

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_05.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Lecture 18 Module](../README.md)

---

## 1. Overview & Purpose
A single line plot shows trend, but comparing two or more series on the same axes enables **comparative performance analysis**:
- How do Oscar Winners compare to Non-Oscar Blockbusters in revenue?
- How does Product A compare to Product B?

---

## 2. Core Concepts & Parameters
To plot multiple lines on the same axes:
1. Call `plt.plot()` sequentially for each dataset.
2. Supply a descriptive **`label`** to each call:
   ```python
   plt.plot(x, y1, label="Oscar Winners")
   plt.plot(x, y2, label="Non-Oscar Winners")
   ```
3. Call **`plt.legend()`** to display the key mapping colors to labels.

### Legend Placement (`loc` parameter):
- `'best'` (default, Matplotlib automatically chooses least overlapping spot)
- `'upper right'`, `'upper left'`, `'lower right'`, `'lower left'`
- `'center'`, `'center left'`, `'center right'`

---

## 3. Code Implementation

```python
import matplotlib.pyplot as plt

years = [2008, 2009, 2010, 2011, 2012]
oscar_revenue = [1005, 170, 427, 133, 232]       # Oscar Winners
non_oscar_revenue = [378, 2788, 829, 185, 275]   # Non-Oscar Blockbusters (Avatar, Inception, etc.)

plt.figure(figsize=(9, 5))
plt.plot(years, oscar_revenue, label="Oscar Winners", marker='o', linewidth=2, color='darkblue')
plt.plot(years, non_oscar_revenue, label="Non-Oscar Winners", marker='s', linewidth=2, color='crimson')

plt.title("Revenue Comparison: Oscar vs Non-Oscar Winners", fontsize=14, fontweight='bold')
plt.xlabel("Years", fontsize=12)
plt.ylabel("Revenue (in $M)", fontsize=12)
plt.legend(loc="upper right", fontsize=11)
plt.grid(True, linestyle=":", alpha=0.6)
plt.show()
```

---

## 4. Key Takeaways
- Without `plt.legend()`, labels defined in `plt.plot(..., label="...")` will not appear on the chart.
- Ensure both datasets share the same x-axis values or are plotted over compatible ranges.
