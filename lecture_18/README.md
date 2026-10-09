# 📊 Lecture 18: Data Visualization (Part 1 — Matplotlib Mastery)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c.svg)](https://matplotlib.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Main Repository](../README.md)

---

## 📌 Module Overview

Lecture 18 covers foundational and intermediate data visualization using **Matplotlib**. It focuses on human visual perception, graphic integrity, the Matplotlib object-oriented architecture, line plots, styling, formatting, discrete bar charts, continuous scatter plots, and composition pie charts.

Every subtopic is organized into an isolated module containing:
- 📝 **Markdown Notes (`notes.md`)**: Comprehensive theory, method parameters, and best practices.
- 📕 **High-Definition PDF (`notes.pdf`)**: Styled document with rendered vector formulas and diagrams.
- 💻 **Jupyter Notebook (`.ipynb`)**: Runnable Python code examples.

---

## 🗺️ Sub-Topic Navigation

| Sub-Module | Topic Title | Core Concepts Covered | Fast Links |
| :--- | :--- | :--- | :--- |
| **Notes_18.01** | What is Data Visualization? | Visual perception, exploratory vs explanatory, Anscombe's Quartet | [Notes](Notes_18.01/README.md) \| [PDF](Notes_18.01/notes.pdf) \| [Notebook](Notes_18.01/lecture_18_01.ipynb) |
| **Notes_18.02** | How to Plot Data - Basic Structure | Coordinate systems, Data Prep $\to$ Canvas $\to$ Plot $\to$ Decoration $\to$ Render | [Notes](Notes_18.02/README.md) \| [PDF](Notes_18.02/notes.pdf) \| [Notebook](Notes_18.02/lecture_18_02.ipynb) |
| **Notes_18.03** | Introduction to Matplotlib | Architecture (`Backend`, `Artist`, `Scripting`), Pyplot state machine vs OO | [Notes](Notes_18.03/README.md) \| [PDF](Notes_18.03/notes.pdf) \| [Notebook](Notes_18.03/lecture_18_03.ipynb) |
| **Notes_18.04** | Important Plot Methods | `plt.plot()`, `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.grid()`, `plt.show()` | [Notes](Notes_18.04/README.md) \| [PDF](Notes_18.04/notes.pdf) \| [Notebook](Notes_18.04/lecture_18_04.ipynb) |
| **Notes_18.05** | Multiple Datasets on Line Plot | Multi-series plotting, legends (`plt.legend`), color differentiation, z-order | [Notes](Notes_18.05/README.md) \| [PDF](Notes_18.05/notes.pdf) \| [Notebook](Notes_18.05/lecture_18_05.ipynb) |
| **Notes_18.06** | Format Strings (`fmt`) | Syntax `[marker][line][color]`, e.g., `'ro--'`, `'b^:'`, hex styling | [Notes](Notes_18.06/README.md) \| [PDF](Notes_18.06/notes.pdf) \| [Notebook](Notes_18.06/lecture_18_06.ipynb) |
| **Notes_18.07** | Styling & Saving Plots | `figsize`, DPI scaling, vector/raster export via `plt.savefig()` (PNG, SVG, PDF) | [Notes](Notes_18.07/README.md) \| [PDF](Notes_18.07/notes.pdf) \| [Notebook](Notes_18.07/lecture_18_07.ipynb) |
| **Notes_18.08** | Chart Selection Taxonomy | Choosing the right chart: Comparison, Distribution, Composition, Relationship | [Notes](Notes_18.08/README.md) \| [PDF](Notes_18.08/notes.pdf) \| [Notebook](Notes_18.08/lecture_18_08.ipynb) |
| **Notes_18.09** | Vertical Bar Charts (`plt.bar`) | Discrete categorical comparison, bar width, alignment, edge styling | [Notes](Notes_18.09/README.md) \| [PDF](Notes_18.09/notes.pdf) \| [Notebook](Notes_18.09/lecture_18_09.ipynb) |
| **Notes_18.10** | Adding Labels to Bars | Direct data labels via `plt.text()` & `ax.bar_label()` container iteration | [Notes](Notes_18.10/README.md) \| [PDF](Notes_18.10/notes.pdf) \| [Notebook](Notes_18.10/lecture_18_10.ipynb) |
| **Notes_18.11** | Grouped Bar Charts | Side-by-side comparative bars, NumPy index offset math (`np.arange()`) | [Notes](Notes_18.11/README.md) \| [PDF](Notes_18.11/notes.pdf) \| [Notebook](Notes_18.11/lecture_18_11.ipynb) |
| **Notes_18.12** | Horizontal Bar Charts (`plt.barh`) | Long categorical labels, axis sorting, horizontal orientation | [Notes](Notes_18.12/README.md) \| [PDF](Notes_18.12/notes.pdf) \| [Notebook](Notes_18.12/lecture_18_12.ipynb) |
| **Notes_18.13** | Scatter Plots (`plt.scatter`) | Bivariate correlation, dispersion, clusters, outliers | [Notes](Notes_18.13/README.md) \| [PDF](Notes_18.13/notes.pdf) \| [Notebook](Notes_18.13/lecture_18_13.ipynb) |
| **Notes_18.14** | Advanced Scatter Customizations | 4D visual encoding: Marker size (`s`), colormap (`c`, `cmap`), alpha transparency | [Notes](Notes_18.14/README.md) \| [PDF](Notes_18.14/notes.pdf) \| [Notebook](Notes_18.14/lecture_18_14.ipynb) |
| **Notes_18.15** | Annotations on Scatter Plots | Specific data callouts (`plt.annotate`, `arrowprops`, `bbox`) | [Notes](Notes_18.15/README.md) \| [PDF](Notes_18.15/notes.pdf) \| [Notebook](Notes_18.15/lecture_18_15.ipynb) |
| **Notes_18.16** | Multiple Datasets on Scatter Plots | Multi-class categories, legend construction, marker variations | [Notes](Notes_18.16/README.md) \| [PDF](Notes_18.16/notes.pdf) \| [Notebook](Notes_18.16/lecture_18_16.ipynb) |
| **Notes_18.17** | Pie Charts (`plt.pie`) | Part-to-whole composition, `autopct`, `startangle`, shadow effects | [Notes](Notes_18.17/README.md) \| [PDF](Notes_18.17/notes.pdf) \| [Notebook](Notes_18.17/lecture_18_17.ipynb) |
| **Notes_18.18** | Advanced Pie Charts | Donut charts (center hollow circle), `explode` slices, custom palettes | [Notes](Notes_18.18/README.md) \| [PDF](Notes_18.18/notes.pdf) \| [Notebook](Notes_18.18/lecture_18_18.ipynb) |

---

## 📐 Mathematical Foundations

### 1. Data-Ink Ratio (Edward Tufte)
The efficiency of a visual graphic is formally measured by Edward Tufte's Data-Ink formulation:

$$
\boxed{\eta = \frac{\mathcal{I}_{\text{data}}}{\mathcal{I}_{\text{total}}} = 1.0 - \frac{\mathcal{I}_{\text{non-data}}}{\mathcal{I}_{\text{total}}} \in (0, 1]}
$$

where:
- $\mathcal{I}_{\text{data}}$: Ink dedicated to displaying non-redundant data information
- $\mathcal{I}_{\text{total}}$: Total ink used across the entire graphic
- $\mathcal{I}_{\text{non-data}}$: Redundant non-data ink (chart junk, excessive gridlines, heavy fills)

---

### 2. Symmetrical Grouped Bar Coordinate System
For $K = 2$ comparative series across $N$ discrete categories with uniform bar width $w < \frac{1}{K} = 0.5$:

Let $x_i = i$ ($i \in \{0, 1, \dots, N-1\}$) denote the baseline category index. The shifted horizontal coordinates $(x_{1, i}, x_{2, i})$ follow the symmetric system:

$$
\begin{cases}
x_{1, i} = x_i - \dfrac{w}{2} \\
x_{2, i} = x_i + \dfrac{w}{2}
\end{cases}
$$

where:
- $x_{1, i}$: Center coordinate for Series 1 (e.g. Budget)
- $x_{2, i}$: Center coordinate for Series 2 (e.g. Spend)
- $w$: Uniform width of each bar

The category tick label location $t_i$ satisfies the central symmetry theorem:

$$
\boxed{t_i = \frac{x_{1, i} + x_{2, i}}{2} = x_i}
$$

For generalized $K \ge 2$ comparative series of uniform width $w$:

$$
\boxed{x_{k, i} = x_i + \left(k - \frac{K - 1}{2}\right) \cdot w \quad \text{for } k \in \{0, 1, \dots, K-1\}}
$$

## 🎯 Practice Problems & Case Studies

To master the concepts of Lecture 18, solve the practical case studies in the [Practice Problems](Practice_Problems/) module:

- 📁 **[Questions/](Practice_Problems/Questions/)**:
  - [Questions README](Practice_Problems/Questions/README.md) | [questions.pdf](Practice_Problems/Questions/questions.pdf) | [questions.ipynb](Practice_Problems/Questions/questions.ipynb)
  - Problem 1: Healthcare Operations Multi-Metric Bar & Line Chart
  - Problem 2: E-Commerce Multi-Touch Attribution 4D Scatter Plot
  - Problem 3: SaaS Executive Boardroom YoY Revenue Dashboard
- 📁 **[Solutions/](Practice_Problems/Solutions/)**:
  - [Solutions Guide](Practice_Problems/Solutions/README.md) | [solutions.pdf](Practice_Problems/Solutions/solutions.pdf) | [solutions.ipynb](Practice_Problems/Solutions/solutions.ipynb)
  - Production-ready, fully commented Python solutions with exported figures.
