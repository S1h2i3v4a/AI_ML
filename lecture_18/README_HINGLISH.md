# 📊 Lecture 18: Data Visualization (Part 1 — Matplotlib Mastery) [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c.svg)](https://matplotlib.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Main Hub Par Wapas Jayein](../README_HINGLISH.md)

---

## 📌 Module Ka Parichay (Overview)

Lecture 18 me hum **Matplotlib** ke through data visualization ke fundamentals aur intermediate concepts seekhte hain. Is module me human visual perception, graphic integrity, Matplotlib ka object-oriented architecture, multi-line plots, styling, formatting, discrete bar charts, continuous scatter plots, aur composition pie charts shamil hain.

Har subtopic ek separate module me organized hai:
- 📝 **Markdown Notes (`notes.md`)**: Detailed theory, parameter explanation aur best practices.
- 📕 **High-Definition PDF (`notes.pdf`)**: Formatted document jisme textbook LaTeX mathematical formulas aur diagrams hain.
- 💻 **Jupyter Notebook (`.ipynb`)**: Directly runnable Python practice code.

---

## 🗺️ Sub-Topics Navigation

| Sub-Module | Topic Title | Core Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **Notes_18.01** | What is Data Visualization? | Visual perception, exploratory vs explanatory viz, Anscombe's Quartet | [Notes](Notes_18.01/README.md) \| [PDF](Notes_18.01/notes.pdf) \| [Notebook](Notes_18.01/lecture_18_01.ipynb) |
| **Notes_18.02** | How to Plot Data - Basic Structure | Coordinate systems, Data Prep $\to$ Canvas $\to$ Plot $\to$ Decoration $\to$ Render | [Notes](Notes_18.02/README.md) \| [PDF](Notes_18.02/notes.pdf) \| [Notebook](Notes_18.02/lecture_18_02.ipynb) |
| **Notes_18.03** | Introduction to Matplotlib | Matplotlib history, architecture (`backend`, `artist`, `scripting`), Pyplot state machine | [Notes](Notes_18.03/README.md) \| [PDF](Notes_18.03/notes.pdf) \| [Notebook](Notes_18.03/lecture_18_03.ipynb) |
| **Notes_18.04** | Important Plot Methods | `plt.plot()`, `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.grid()`, `plt.show()` | [Notes](Notes_18.04/README.md) \| [PDF](Notes_18.04/notes.pdf) \| [Notebook](Notes_18.04/lecture_18_04.ipynb) |
| **Notes_18.05** | Multiple Datasets on Line Plot | Ek canvas par multiple lines plot karna, legends (`plt.legend`), color aur z-order | [Notes](Notes_18.05/README.md) \| [PDF](Notes_18.05/notes.pdf) \| [Notebook](Notes_18.05/lecture_18_05.ipynb) |
| **Notes_18.06** | Format Strings (`fmt`) | Fast syntax `[marker][line][color]`, jaise `'ro--'`, `'b^:'`, hex styling | [Notes](Notes_18.06/README.md) \| [PDF](Notes_18.06/notes.pdf) \| [Notebook](Notes_18.06/lecture_18_06.ipynb) |
| **Notes_18.07** | Styling & Saving Plots | `figsize`, DPI scaling, vector/raster export via `plt.savefig()` (PNG, SVG, PDF) | [Notes](Notes_18.07/README.md) \| [PDF](Notes_18.07/notes.pdf) \| [Notebook](Notes_18.07/lecture_18_07.ipynb) |
| **Notes_18.08** | Chart Selection Taxonomy | Sahi chart choose karna: Comparison, Distribution, Composition, Relationship | [Notes](Notes_18.08/README.md) \| [PDF](Notes_18.08/notes.pdf) \| [Notebook](Notes_18.08/lecture_18_08.ipynb) |
| **Notes_18.09** | Vertical Bar Charts (`plt.bar`) | Discrete categorical comparison, bar width, alignment, edge styling | [Notes](Notes_18.09/README.md) \| [PDF](Notes_18.09/notes.pdf) \| [Notebook](Notes_18.09/lecture_18_09.ipynb) |
| **Notes_18.10** | Adding Labels to Bars | Bars ke upar exact numbers likhna: `plt.text()` aur `ax.bar_label()` container loop | [Notes](Notes_18.10/README.md) \| [PDF](Notes_18.10/notes.pdf) \| [Notebook](Notes_18.10/lecture_18_10.ipynb) |
| **Notes_18.11** | Grouped Bar Charts | Side-by-side comparative bars, NumPy index offset math (`np.arange()`) | [Notes](Notes_18.11/README.md) \| [PDF](Notes_18.11/notes.pdf) \| [Notebook](Notes_18.11/lecture_18_11.ipynb) |
| **Notes_18.12** | Horizontal Bar Charts (`plt.barh`) | Lambe label names ke liye horizontal bars, axis sorting & inversion | [Notes](Notes_18.12/README.md) \| [PDF](Notes_18.12/notes.pdf) \| [Notebook](Notes_18.12/lecture_18_12.ipynb) |
| **Notes_18.13** | Scatter Plots (`plt.scatter`) | Bivariate correlation, dispersion, clusters, aur outliers detect karna | [Notes](Notes_18.13/README.md) \| [PDF](Notes_18.13/notes.pdf) \| [Notebook](Notes_18.13/lecture_18_13.ipynb) |
| **Notes_18.14** | Advanced Scatter Customizations | 4D visual encoding: Marker size (`s`), colormap (`c`, `cmap`), alpha transparency | [Notes](Notes_18.14/README.md) \| [PDF](Notes_18.14/notes.pdf) \| [Notebook](Notes_18.14/lecture_18_14.ipynb) |
| **Notes_18.15** | Annotations on Scatter Plots | Specific points par callouts/arrows lagana (`plt.annotate`, `arrowprops`, `bbox`) | [Notes](Notes_18.15/README.md) \| [PDF](Notes_18.15/notes.pdf) \| [Notebook](Notes_18.15/lecture_18_15.ipynb) |
| **Notes_18.16** | Multiple Datasets on Scatter Plots | Multi-class categories ko alag-alag color aur marker se represent karna | [Notes](Notes_18.16/README.md) \| [PDF](Notes_18.16/notes.pdf) \| [Notebook](Notes_18.16/lecture_18_16.ipynb) |
| **Notes_18.17** | Pie Charts (`plt.pie`) | Part-to-whole composition, `autopct`, `startangle`, shadow effects | [Notes](Notes_18.17/README.md) \| [PDF](Notes_18.17/notes.pdf) \| [Notebook](Notes_18.17/lecture_18_17.ipynb) |
| **Notes_18.18** | Advanced Pie Charts | Donut charts (center hollow circle), `explode` slices, custom palettes | [Notes](Notes_18.18/README.md) \| [PDF](Notes_18.18/notes.pdf) \| [Notebook](Notes_18.18/lecture_18_18.ipynb) |

---

## 📐 Ganitiya Adhaar (Mathematical Foundations)

### 1. Data-Ink Ratio (Edward Tufte)
Kisi bhi chart ki visual efficiency Edward Tufte ke Data-Ink formula se measure hoti hai:

$$
\boxed{\eta = \frac{\mathcal{I}_{\text{data}}}{\mathcal{I}_{\text{total}}} = 1.0 - \frac{\mathcal{I}_{\text{non-data}}}{\mathcal{I}_{\text{total}}} \in (0, 1]}
$$

jahan:
- $\mathcal{I}_{\text{data}}$: Data information dikhane wali zaroori ink
- $\mathcal{I}_{\text{total}}$: Poore graphic me use hone wali kul ink
- $\mathcal{I}_{\text{non-data}}$: Faltu decorations, chart junk, aur heavy backgrounds

---

### 2. Symmetrical Grouped Bar Coordinate System
$K = 2$ comparative series aur $N$ categories ke liye ($w < \frac{1}{K} = 0.5$):

Base category index $x_i = i$ ($i \in \{0, 1, \dots, N-1\}$) ke dono taraf side-by-side symmetrically bars place karne ka formula:

$$
\begin{cases}
x_{1, i} = x_i - \dfrac{w}{2} \\
x_{2, i} = x_i + \dfrac{w}{2}
\end{cases}
$$

jahan:
- $x_{1, i}$: Series 1 (Budget) ka horizontal center
- $x_{2, i}$: Series 2 (Spend) ka horizontal center
- $w$: Har bar ki uniform width

Category tick mark $t_i$ central symmetry theorem satisfy karta hai:

$$
\boxed{t_i = \frac{x_{1, i} + x_{2, i}}{2} = x_i}
$$

Generalized $K \ge 2$ series ke liye:

$$
\boxed{x_{k, i} = x_i + \left(k - \frac{K - 1}{2}\right) \cdot w \quad \text{for } k \in \{0, 1, \dots, K-1\}}
$$

## 🎯 Practice Problems & Case Studies

Lecture 18 ke concepts ko master karne ke liye [Practice Problems](Practice_Problems/) module solve karein:

- 📁 **[Questions/](Practice_Problems/Questions/)**:
  - `questions.md` | `questions.pdf` | `questions.ipynb`
  - Problem 1: Healthcare Operations Multi-Metric Bar & Line Chart
  - Problem 2: E-Commerce Multi-Touch Attribution 4D Scatter Plot
  - Problem 3: SaaS Executive Boardroom YoY Revenue Dashboard
- 📁 **[Solutions/](Practice_Problems/Solutions/)**:
  - `solutions.md` | `solutions.pdf` | `solutions.ipynb`
  - Industry-standard, fully commented Python solutions aur exported visual figures.
