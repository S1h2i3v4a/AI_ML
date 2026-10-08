# Day 18 - Lecture 18.4: Important Plot Methods [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_04.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 18 Module Par Wapas Jayein](../README_HINGLISH.md)

---

## 1. Overview & Core Functions
To turn raw lines into meaningful figures, Matplotlib provides essential helper methods that label, scale, and display the plot:

| Method | Purpose |
| :--- | :--- |
| `plt.plot(x, y)` | Draws line plots and markers connecting coordinates |
| `plt.title("...")` | Sets the main title centered above the plot |
| `plt.xlabel("...")` | Sets descriptive label for the horizontal axis |
| `plt.ylabel("...")` | Sets descriptive label for the vertical axis |
| `plt.grid(True)` | Displays grid lines to facilitate reading exact values |
| `plt.xlim(min, max)` | Sets manual boundaries for the X-axis |
| `plt.ylim(min, max)` | Sets manual boundaries for the Y-axis |
| `plt.show()` | Flushes and renders the figure to the screen / notebook |

---

## 2. Practical Case Study: Oscar Winner Revenues

Tracking the box office revenue of Academy Award (Oscar) Best Picture winners:
- 2008: *The Dark Knight* ($1005M)
- 2009: *The Hurt Locker* ($170M)
- 2010: *The King's Speech* ($427M)
- 2011: *The Artist* ($133M)
- 2012: *Argo* ($232M)

```python
import matplotlib.pyplot as plt

oscar_years = [2008, 2009, 2010, 2011, 2012]
oscar_revenue = [1005, 170, 427, 133, 232]  # in $M

plt.figure(figsize=(8, 5))
plt.plot(oscar_years, oscar_revenue)

# Adding labels and title
plt.title("Oscar Years vs Revenue (in $M)", fontsize=14, fontweight='bold')
plt.xlabel("Years", fontsize=12)
plt.ylabel("Revenue (in $M)", fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()
```

---

## 3. Mukhya Batein (Key Takeaways)
- Without `xlabel` and `ylabel`, a chart is uninterpretable to stakeholders. Always include units (e.g. `(in $M)` or `(in kg)`).
- Calling `plt.show()` tells Matplotlib that figure definition is finished and ready for display.


---

## 📐 Piecewise Linear Spline aur Arc Length Ka Ganitiya Sutra

Line plot ordered discrete samples $D = \{(x_0, y_0), (x_1, y_1), \dots, (x_{n-1}, y_{n-1})\}$ ke beech linear interpolation ke zariye continuous curve banata hai:

$$
\boxed{\mathcal{L}(x) = y_i + \frac{y_{i+1} - y_i}{x_{i+1} - x_i}(x - x_i), \quad \forall x \in [x_i, x_{i+1}]}
$$

Poore line plot ka total Euclidean curve length $S$:
$$
\boxed{S = \sum_{i=0}^{n-2} \sqrt{(x_{i+1} - x_i)^2 + (y_{i+1} - y_i)^2}}
$$
