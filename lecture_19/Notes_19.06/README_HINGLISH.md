# Day 19 - Lecture 19.6: Stack Plots (Area Charts) [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_19_06.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 19 Module Par Wapas Jayein](../README_HINGLISH.md)

---

## 1. Overview & Purpose
A **Stack Plot** (also called a Stacked Area Chart) displays multiple data series stacked on top of each other along a continuous or sequential x-axis (such as time, days, or months).

### Why use a Stack Plot?
- **Part-to-Whole over Time:** While a **Pie Chart** shows part-to-whole for a single static point in time, a **Stack Plot** shows how both the individual parts and the cumulative total evolve over time.
- **Contribution Analysis:** Easily observe which sub-category is growing or shrinking in proportion to the total.
- **Total Magnitude:** The topmost line shows the cumulative total across all series.

---

## 2. Syntax & Parameters

```python
plt.stackplot(
    x,                      # Sequential x-axis (e.g., days, years)
    y1, y2, y3, ...,        # Multiple 1D arrays of equal length representing layers
    labels=['L1', 'L2'],    # Labels for each category
    colors=['c1', 'c2'],    # Fill colors for each layer
    alpha=0.8,              # Transparency
    baseline='zero'         # 'zero' (standard), 'sym' (streamgraph), or 'wiggle'
)
```

---

## 3. Real-World Case Study: Website Traffic Channels

Tracking visitor traffic across days of the week:
- **Direct Traffic:** Users typing the URL directly.
- **Organic Traffic:** Users arriving via search engines (Google, Bing).
- **Social Traffic:** Users arriving from LinkedIn, Twitter, YouTube.

```python
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
direct = [50, 60, 70, 80, 90, 100, 110]
organic = [30, 40, 50, 55, 60, 70, 80]
social = [20, 25, 30, 35, 40, 50, 60]

plt.figure(figsize=(9, 6))
plt.stackplot(days, direct, organic, social, labels=['Direct Traffic', 'Organic Search', 'Social Media'],
              colors=['#4C72B0', '#55A868', '#C44E52'], alpha=0.85)

plt.title("Website Traffic Channels Over a Week", fontsize=14, fontweight="bold")
plt.xlabel("Day of the Week", fontsize=12)
plt.ylabel("Number of Visitors", fontsize=12)
plt.legend(loc='upper left', fontsize=11)
plt.grid(True, linestyle=":", alpha=0.5)
plt.show()
```

---

## 📐 Stack Plot (Area Chart) Ka Ganitiya Sutra

Stack plot cumulative curve ke total area ko $K$ alag-alag components $\{y_1(t), y_2(t), \dots, y_K(t)\}$ me divide karta hai:

Cumulative boundary curves:
$$
\boxed{S_k(t) = \sum_{j=1}^k y_j(t), \quad\text{with } S_0(t) \equiv 0}
$$

Har category ka total net area definite integral ke barabar hota hai:
$$
\boxed{\mathcal{A}_k = \int_{t_0}^{t_1} y_k(t) \, dt = \int_{t_0}^{t_1} [S_k(t) - S_{k-1}(t)] \, dt}
$$

---
## 4. Mukhya Batein (Key Takeaways) & Limitations
- **Readability Caution:** Because layers are stacked on top of each other, only the bottom-most layer has a flat baseline. Higher layers have curved baselines, making it harder to judge exact numerical values of upper layers.
- Limit the number of categories to 3–5. Beyond that, the chart becomes cluttered and hard to interpret.
