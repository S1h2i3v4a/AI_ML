# Day 18 - Lecture 18.9: Vertical Bar Charts (`plt.bar`)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_09.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Lecture 18 Module](../README.md)

---

## 1. Overview & Conceptual Foundations
Detailed study of vertical bar charts using plt.bar(). Learn how bar heights map discrete categorical metrics, how to adjust bar widths, assign custom colors, and manage vertical headroom using plt.ylim().

---

## 2. Visual Architecture & Workflow Diagram

```mermaid
flowchart LR
    A["Categorical Domain:<br/>Years = [2008, 2009, 2010, 2011, 2012]"] --> B["Heights Array:<br/>Revenue = [1005, 170, 427, 133, 232]"]
    B --> C["Render Vertical Rectangles:<br/>plt.bar(years, revenue, color='purple')"]
    C --> D["Set Ceiling Buffer:<br/>plt.ylim(0, max(revenue) + 200)"]
    D --> E["Clean Categorical Bar Chart"]
```

---

## 3. Mathematical & Theoretical Framework

A vertical bar chart renders disjoint geometric rectangles for each category $i$:

$$
R_i = [x_i - \frac{w}{2}, x_i + \frac{w}{2}] \times [0, h_i]
$$

where $w$ is the bar width (default $w = 0.8$) and $h_i$ is the quantitative metric for category $i$.

---

## 4. Structured Implementation & Execution

```python
import matplotlib.pyplot as plt

def render_vertical_bar_chart(categories: list, values: list, bar_color: str = "#7b3294", top_margin_ratio: float = 0.2) -> dict:
    """
    Renders a standard vertical bar chart with controlled bar widths, custom colors,
    and upper padding headroom.
    
    Parameters:
    -----------
    categories : list
        Category labels or discrete time markers.
    values : list of float
        Numerical values determining vertical bar heights.
    bar_color : str
        Hex color or CSS color name for bars.
    top_margin_ratio : float
        Fraction of max value to add as top padding.
        
    Returns:
    --------
    dict
        Computed bar metrics and applied ceiling limit.
    """
    fig, ax = plt.subplots(figsize=(7, 4.5))
    
    # Plot vertical bars
    bars = ax.bar(categories, values, color=bar_color, width=0.6, edgecolor='black', linewidth=0.8)
    
    ax.set_title("Yearly Revenue of Movies (Vertical Bar Chart)", fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel("Release Years", fontsize=11)
    ax.set_ylabel("Revenue ($ Millions)", fontsize=11)
    
    # Calculate upper headroom limit
    max_val = max(values)
    upper_limit = max_val + (max_val * top_margin_ratio)
    ax.set_ylim(0, upper_limit)
    
    ax.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
    
    return {
        "categories_plotted": categories,
        "max_bar_height": max_val,
        "configured_ylim": (0, upper_limit),
        "total_volume": sum(values)
    }

# Lecture Data
years = [2008, 2009, 2010, 2011, 2012]
revenue = [1005, 170, 427, 133, 232]

bar_res = render_vertical_bar_chart(years, revenue)
print("Vertical Bar Chart Execution Results:")
for k, v in bar_res.items():
    print(f"  {k}: {v}")
```

---

## 5. Summary & Key Takeaways
- **Self-contained Functional Design**: Implementation is encapsulated into modular functions with explicit inputs, structured outputs, and type hints.
- **Visual Accuracy**: Adheres strictly to Matplotlib's layout management, aesthetic guidelines, and production best practices.
