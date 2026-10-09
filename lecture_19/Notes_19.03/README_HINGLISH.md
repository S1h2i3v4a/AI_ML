# Day 19 - Lecture 19.3: Vertical Reference Lines (`plt.axvline`) [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_19_03.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 19 Module Par Wapas Jayein](../README_HINGLISH.md)

---

## 1. Overview & Purpose
In data analysis, histograms show the distribution, but stakeholders need **benchmarks and reference thresholds**. 
For example:
- *What is the pass mark?* (e.g., 33 marks)
- *What is the mean / average score?* ($\mu$)
- *What is the median or 95th percentile?*
- *What are control limits in manufacturing?*

`plt.axvline()` draws an **infinite vertical reference line across the axes** at a specified x-coordinate.

---

## 2. Syntax & Key Parameters

```python
plt.axvline(
    x=0,                     # The x-coordinate where the line will be drawn
    ymin=0, ymax=1,          # Normalized y-span (0 = bottom, 1 = top)
    color='red',             # Line color
    linestyle='--',          # Style: '--' (dashed), '-' (solid), ':' (dotted), '-.' (dashdot)
    linewidth=2,             # Thickness of line
    label='Threshold Name'   # Label for legend
)
```

### Companion Methods:
- `plt.axhline(y, ...)`: Draws horizontal reference line across entire width.
- `plt.axvspan(xmin, xmax, ...)`: Highlights a vertical region (e.g. critical zone).
- `plt.text(x, y, "label")` or `plt.annotate()`: Places descriptive text directly next to the line.

---

## 3. Mathematical Reference Lines

Given a dataset $X = \{x_1, x_2, \dots, x_n\}$:
1. **Sample Mean:**
   $$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$
2. **Standard Deviation Bands:**
   $$\text{Upper: } \bar{x} + \sigma, \quad \text{Lower: } \bar{x} - \sigma$$

Plotting $\bar{x}$ as a vertical dashed line instantly reveals skewness:
- If $\text{Mean} > \text{Median}$, distribution is **positively (right) skewed**.
- If $\text{Mean} < \text{Median}$, distribution is **negatively (left) skewed**.

---

## 4. Code Implementation

```python
import matplotlib.pyplot as plt
import numpy as np

marks = [
    25, 38, 42, 55, 61, 67, 72, 78, 83, 88,
    91, 95, 47, 53, 59, 64, 69, 74, 79, 85,
    92, 97, 33, 45, 58, 62, 71, 76, 81, 89
]
bins = [0, 30, 70, 90, 100]

plt.figure(figsize=(9, 6))
plt.hist(marks, bins=bins, edgecolor="black", color="lightblue")

# 1. Reference line for Passing Marks (33)
plt.axvline(
    x=33,
    color="crimson",
    linestyle="--",
    linewidth=2.5,
    label="Pass Mark (33)"
)

# 2. Reference line for Mean Score
mean_val = np.mean(marks)
plt.axvline(
    x=mean_val,
    color="darkblue",
    linestyle="-.",
    linewidth=2,
    label=f"Mean Mark ({mean_val:.1f})"
)

plt.xlabel("Marks", fontsize=12)
plt.ylabel("Number of Students", fontsize=12)
plt.title("Distribution of Marks of 30 Students with Threshold Lines", fontsize=14, fontweight="bold")
plt.legend(loc="upper left", fontsize=11)
plt.grid(True, linestyle=":", alpha=0.6)
plt.show()
```

---

## 5. Summary & Best Practices
- Always add `label=` to `axvline` and invoke `plt.legend()`.
- Use contrasting styles (e.g. dashed red) so the threshold stands out clearly against the histogram bins.


---

## 📐 Statistical Benchmarks Ka Ganitiya Sutra

Vertical reference lines parametric aur non-parametric metrics mark karne ke liye use hoti hain:

$$
\boxed{\mu = \frac{1}{N} \sum_{i=1}^N x_i \qquad\text{aur}\qquad \sigma = \sqrt{\frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2}}
$$

Normal distribution ke liye **Empirical Rule**:

$$
\begin{aligned}
\Pr(\mu - 1\sigma \le X \le \mu + 1\sigma) &\approx 68.27\% \\
\Pr(\mu - 2\sigma \le X \le \mu + 2\sigma) &\approx 95.45\% \\
\Pr(\mu - 3\sigma \le X \le \mu + 3\sigma) &\approx 99.73\%
\end{aligned}
$$
