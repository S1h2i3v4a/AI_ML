# Day 19 - Lecture 19.5: Advanced Operations on Box Plots

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_19_05.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Lecture 19 Module](../README.md)

---

## 1. Overview & Purpose
Standard box plots can be significantly customized to provide richer statistical insight and better presentation aesthetics. This lecture covers:
- **Horizontal Box Plots** (`vert=False`)
- **Displaying the Mean Marker** (`showmeans=True`, `meanline=True`)
- **Customizing Whiskers** (`whis` parameter)
- **Comparing Multiple Groups** with custom labels

---

## 2. Advanced Parameters of `plt.boxplot()`

```python
plt.boxplot(
    x,                      # Dataset or list of datasets: [group1, group2, ...]
    vert=True,              # If False, plots horizontally (useful when category names are long)
    showmeans=True,         # If True, plots a marker for the mean
    meanline=True,          # If True with showmeans=True, renders mean as a dotted line across box
    whis=1.5,               # Whisker multiplier (e.g. 1.5, 2.0, or percentiles [5, 95])
    patch_artist=True,      # If True, fills boxes with color (allows facecolor styling)
    notch=False,            # If True, creates notched box to visually test median significance
    tick_labels=['A', 'B']  # Labels for each dataset (formerly `labels`)
)
```

---

## 3. Comparing Mean vs. Median in Box Plots
When `showmeans=True`:
- The **solid line** inside the box is the **Median ($Q_2$)**.
- The **green triangle or dashed line** is the **Arithmetic Mean ($\mu$)**.
- If Mean $\approx$ Median: Distribution is symmetric.
- If Mean is noticeably to the right (higher) than Median: Right-skewed (driven by high outliers).

---

## 4. Code Implementation

```python
import matplotlib.pyplot as plt
import numpy as np

# 1. Horizontal Box Plot with Mean line
data = [7, 8, 5, 6, 9, 4, 10, 12, 15]

plt.figure(figsize=(8, 4))
plt.boxplot(data, vert=False, showmeans=True, meanline=True, whis=2.0)
plt.title("Horizontal Box Plot with Mean Line & Extended Whiskers (whis=2.0)", fontsize=13, fontweight="bold")
plt.xlabel("Values", fontsize=11)
plt.grid(True, linestyle=":", alpha=0.6)
plt.show()

# 2. Comparing Multiple Datasets
np.random.seed(42)
group1 = np.random.normal(50, 10, 100)
group2 = np.random.normal(60, 15, 100)

plt.figure(figsize=(8, 5))
box = plt.boxplot([group1, group2], tick_labels=["Group 1", "Group 2"], patch_artist=True, showmeans=True)

# Styling individual boxes
colors = ['lightsteelblue', 'lightcoral']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.title("Comparison Between Two Groups", fontsize=14, fontweight="bold")
plt.ylabel("Score / Performance Metric", fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
```

---

## 5. Key Takeaways
- `vert=False` is especially helpful when dealing with lengthy category names to prevent label overlap.
- Setting `patch_artist=True` converts the wireframe box into a filled polygon, enabling company branding colors.


---

## 📐 Notched Box Plot Median Confidence Interval

Notched box plots provide a visual hypothesis test for comparing medians across groups. The 95% confidence interval notch around median $Q_2$ is derived as:

$$
\boxed{\text{Notch} = Q_2 \pm 1.57 \cdot \frac{\text{IQR}}{\sqrt{n}}}
$$

**Decision Rule**: If the notches of two comparative box plots do not overlap, their true medians differ at an approximate 95% statistical confidence level ($\alpha = 0.05$):

$$
\boxed{\text{Notch}_A \cap \text{Notch}_B = \emptyset \implies \text{Medians differ significantly}}
$$
