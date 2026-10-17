# Day 18 - Lecture 18.3: Introduction to Matplotlib [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_03.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 18 Module Par Wapas Jayein](../README_HINGLISH.md)

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Matplotlib ka historical origin (John D. Hunter, 2003) aur Python scientific stack me iska role.
- Stateful API (`pyplot`) vs Object-Oriented API (`fig, ax = plt.subplots()`).
- Matplotlib Canvas Hierarchy: Figure, Axes, Axis, Ticks aur Artists ka clear model.
- Best practices: Production scripts aur multi-plot workflows me OO interface kyu preferred hai.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

- **Matplotlib Origin**: John Hunter ne ise MATLAB ke plotting workflow ko Python me replicate karne ke liye banaya tha. Isiliye isme direct MATLAB-like global state commands (`plt.plot`, `plt.title`) exist karti hain.

- **Figure vs Axes**: Sabse common confusion: `Figure` poora canvas/window hota hai jo final image hold karta hai. `Axes` woh actual bounding box ya subplot hota hai jisme coordinate axes, data lines aur tick labels draw hote hain. Ek Figure me multiple Axes ho sakte hain!

- **Artists Hierarchy**: Matplotlib me har visible component ek 'Artist' hota hai—text, line, rectangle, spines, ticks, legend sab Artist tree ka part hote hain.

- **Stateful vs OO Interface**: Quick exploratory scripts me `plt.plot()` convenient hai, lekin reusable production functions aur complex dashboards me `fig, ax = plt.subplots()` use karna modular aur collision-free hota hai.

---

## 2. Visual Architecture & Workflow Diagram

```mermaid
classDiagram
    class Figure {
        +canvas
        +subplots()
        +savefig()
        +suptitle()
    }
    class Axes {
        +xaxis: Axis
        +yaxis: Axis
        +plot()
        +scatter()
        +bar()
        +set_title()
        +set_xlabel()
    }
    class Axis {
        +set_ticks()
        +set_ticklabels()
        +set_lim()
    }
    class Artist {
        +Line2D
        +Rectangle
        +Text
    }
    Figure "1" *-- "many" Axes : contains
    Axes "1" *-- "2" Axis : contains
    Axes "1" *-- "many" Artist : renders
```

---

## 3. Mathematical & Theoretical Framework

The mathematical projection from user data coordinates $(x, y) \in \mathbb{R}^2$ to device screen pixels $(p_x, p_y) \in \mathbb{Z}^2$ is governed by affine transformations:

$$
\begin{pmatrix} p_x \\ p_y \\ 1 \end{pmatrix} = \mathbf{T}_{\text{display}} \cdot \mathbf{T}_{\text{axes}} \cdot \mathbf{T}_{\text{data}} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}
$$

where each transformation matrix $\mathbf{T}$ scales and translates coordinate spaces linearly.

---

## 4. Structured Implementation & Execution

```python
import matplotlib.pyplot as plt

def demonstrate_matplotlib_architecture() -> dict:
    """
    Demonstrates Matplotlib's Object-Oriented architecture by creating
    a Figure with multiple explicit Axes subplots.
    
    Returns:
    --------
    dict
        Architecture properties of the Figure and Axes instances.
    """
    # Explicit OO creation of Figure and 2 Axes
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    x_vals = [1, 2, 3, 4, 5]
    y1_vals = [10, 20, 15, 30, 25]
    y2_vals = [100, 400, 900, 1600, 2500]
    
    # Subplot 1 (Linear Scale)
    ax1.plot(x_vals, y1_vals, color='#1f77b4', marker='o', linewidth=2)
    ax1.set_title("Subplot 1: Linear Metric (Axes 1)", fontsize=11, fontweight='bold')
    ax1.set_xlabel("Iterations (X)")
    ax1.set_ylabel("Linear Units (Y1)")
    ax1.grid(True, linestyle='--', alpha=0.5)
    
    # Subplot 2 (Quadratic Scale)
    ax2.plot(x_vals, y2_vals, color='#2ca02c', marker='^', linewidth=2)
    ax2.set_title("Subplot 2: Quadratic Metric (Axes 2)", fontsize=11, fontweight='bold')
    ax2.set_xlabel("Iterations (X)")
    ax2.set_ylabel("Squared Units (Y2)")
    ax2.grid(True, linestyle='--', alpha=0.5)
    
    fig.suptitle("Matplotlib Hierarchy: 1 Figure Holding 2 Independent Axes", fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    return {
        "figure_size_inches": fig.get_size_inches().tolist(),
        "figure_dpi": fig.dpi,
        "total_axes_count": len(fig.axes),
        "axes_titles": [ax.get_title() for ax in fig.axes]
    }

# Driver execution
arch_info = demonstrate_matplotlib_architecture()
print("Matplotlib Architectural Hierarchy Info:")
for k, v in arch_info.items():
    print(f"  {k}: {v}")
```

---

## 5. Mukhya Batein (Key Takeaways) & Summary
- Code ko modular function ke roop me likha gaya hai jisme clear shuruat (`def`), docstrings, error handling, aur ending (`return`) maujood hai.
- Video lectures me ma'am dwara sikhaye gaye real movie box-office datasets aur syntax parameters ko exact follow kiya gaya hai.
