# Day 18 - Lecture 18.4: Important Plot Methods

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_04.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Lecture 18 Module](../README.md)

---

## 1. Overview & Conceptual Foundations
Master the primary labeling, scaling, and annotation methods in Matplotlib: title, xlabel, ylabel, xlim, ylim, grid, xticks, and yticks. Proper labeling transforms abstract numbers into self-documenting analytical visualizations.

---

## 2. Visual Architecture & Workflow Diagram

```mermaid
flowchart TD
    A["Raw Plot: plt.plot(X, Y)"] --> B["Add Titles & Labels:<br/>plt.title(), xlabel(), ylabel()"]
    B --> C["Configure Spacing & Limits:<br/>plt.xlim(), plt.ylim()"]
    C --> D["Set Reference Guides:<br/>plt.grid(True)"]
    D --> E["Map Tick Identifiers:<br/>plt.xticks(), plt.yticks()"]
    E --> F["Finished Professional Plot Canvas"]
```

---

## 3. Mathematical & Theoretical Framework

Axis limits define the rectangular viewport subset of $\mathbb{R}^2$:

$$
V = [x_{\min}, x_{\max}] \times [y_{\min}, y_{\max}]
$$

Any data coordinate $(x_i, y_i) \notin V$ is clipped by the rasterizer:

$$
\text{visible}(x_i, y_i) = \begin{cases} 1 & \text{if } x_{\min} \le x_i \le x_{\max} \land y_{\min} \le y_i \le y_{\max} \\ 0 & \text{otherwise} \end{cases}
$$

---

## 4. Structured Implementation & Execution

```python
import matplotlib.pyplot as plt

def create_fully_labeled_plot(years: list, revenue: list, movie_title: str) -> dict:
    """
    Builds a fully labeled, scaled, and gridded plot adhering to professional
    data visualization standards.
    
    Parameters:
    -----------
    years : list of int
        Chronological year indices.
    revenue : list of float
        Revenue generated in Millions USD.
    movie_title : str
        Name of the franchise or focus movie category.
        
    Returns:
    --------
    dict
        Applied axis configuration properties.
    """
    fig, ax = plt.subplots(figsize=(7, 4.5))
    
    # Plot line with custom markers
    ax.plot(years, revenue, marker='o', markersize=7, color='#7570b3', linewidth=2, label="Revenue")
    
    # 1. Labels and Titles
    ax.set_title(f"{movie_title}: Annual Financial Performance", fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel("Release Year", fontsize=11, fontweight='semibold')
    ax.set_ylabel("Box Office Gross ($ Millions)", fontsize=11, fontweight='semibold')
    
    # 2. Axis limits with padding
    y_padding = max(revenue) * 0.15
    ax.set_ylim(0, max(revenue) + y_padding)
    ax.set_xlim(min(years) - 0.5, max(years) + 0.5)
    
    # 3. Ticks and Grids
    ax.set_xticks(years)
    ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.6)
    ax.legend(loc="upper left")
    
    plt.tight_layout()
    plt.show()
    
    return {
        "x_ticks": years,
        "y_limits": (0, max(revenue) + y_padding),
        "total_revenue": sum(revenue)
    }

# Driver execution
years_data = [2008, 2009, 2010, 2011, 2012]
revenue_data = [1005, 170, 427, 133, 232]

config_res = create_fully_labeled_plot(years_data, revenue_data, "Oscar Winners Franchise")
print("Applied Plot Configuration:")
for k, v in config_res.items():
    print(f"  {k}: {v}")
```

---

## 5. Summary & Key Takeaways
- **Self-contained Functional Design**: Implementation is encapsulated into modular functions with explicit inputs, structured outputs, and type hints.
- **Visual Accuracy**: Adheres strictly to Matplotlib's layout management, aesthetic guidelines, and production best practices.
