# 📈 Lecture 19: Advanced Matplotlib & Seaborn Mastery

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Viz-4c72b0.svg)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Main Repository](../README.md)

---

## 📌 Module Overview

Lecture 19 explores advanced statistical data visualization, object-oriented Matplotlib design, and high-level statistical plotting using **Seaborn**. It bridges the gap between raw programmatic plotting and publication-grade exploratory data analysis (EDA).

Key topics include:
- **Continuous Distribution Analysis**: Histograms, multi-distribution overlays, and reference lines.
- **Five-Number Summary & Outlier Detection**: Box plots, Tukey fences, notched confidence intervals.
- **Modern Object-Oriented Matplotlib**: Explicit `fig, ax = plt.subplots()` API and multi-panel figures.
- **High-Level Statistical Graphics with Seaborn**: Relational (`relplot`), Categorical (`catplot`), Distribution (`displot`), and Heatmap matrix correlation.
- **Data Visualization Best Practices**: Edward Tufte principles, visual perception hierarchy, and color accessibility.

---

## 🗺️ Sub-Topic Navigation

| Sub-Module | Topic Title | Core Concepts Covered | Fast Links |
| :--- | :--- | :--- | :--- |
| **Notes_19.01** | Histograms (`plt.hist`) | Continuous distribution, bin count & width, density normalization, skewness | [Notes](Notes_19.01/README.md) \| [PDF](Notes_19.01/notes.pdf) \| [Notebook](Notes_19.01/lecture_19_01.ipynb) |
| **Notes_19.02** | Multiple Datasets on Histogram | Side-by-side vs stacked histograms, overlapping distributions with alpha | [Notes](Notes_19.02/README.md) \| [PDF](Notes_19.02/notes.pdf) \| [Notebook](Notes_19.02/lecture_19_02.ipynb) |
| **Notes_19.03** | Vertical Reference Lines (`plt.axvline`) | Statistical benchmarks: Mean, Median, Mode lines, standard deviation bands | [Notes](Notes_19.03/README.md) \| [PDF](Notes_19.03/notes.pdf) \| [Notebook](Notes_19.03/lecture_19_03.ipynb) |
| **Notes_19.04** | Box Plots (Five-Number Summary) | Tukey's 5-number summary ($Q_1, Q_2, Q_3, \text{IQR}$), $1.5 \times \text{IQR}$ outlier detection | [Notes](Notes_19.04/README.md) \| [PDF](Notes_19.04/notes.pdf) \| [Notebook](Notes_19.04/lecture_19_04.ipynb) |
| **Notes_19.05** | Advanced Box Plot Operations | Notched box plots (median confidence), horizontal orientation, custom flier props | [Notes](Notes_19.05/README.md) \| [PDF](Notes_19.05/notes.pdf) \| [Notebook](Notes_19.05/lecture_19_05.ipynb) |
| **Notes_19.06** | Stack Plots (Area Charts) | Cumulative part-to-whole trends over time via `plt.stackplot()` | [Notes](Notes_19.06/README.md) \| [PDF](Notes_19.06/notes.pdf) \| [Notebook](Notes_19.06/lecture_19_06.ipynb) |
| **Notes_19.07** | Subplots in Matplotlib | Multi-panel figures via `plt.subplot()` and `plt.subplots()`, `tight_layout()` | [Notes](Notes_19.07/README.md) \| [PDF](Notes_19.07/notes.pdf) \| [Notebook](Notes_19.07/lecture_19_07.ipynb) |
| **Notes_19.08** | Modern Matplotlib (Object-Oriented API) | Explicit `fig, ax = plt.subplots()`, axis methods (`ax.set_*()`), cleaner engineering | [Notes](Notes_19.08/README.md) \| [PDF](Notes_19.08/notes.pdf) \| [Notebook](Notes_19.08/lecture_19_08.ipynb) |
| **Notes_19.09** | Practice Task: Weekly Weather Analysis | Multi-axis dual plotting ($Y_1$ temperature line, $Y_2$ precipitation bars) | [Notes](Notes_19.09/README.md) \| [PDF](Notes_19.09/notes.pdf) \| [Notebook](Notes_19.09/lecture_19_09.ipynb) |
| **Notes_19.10** | Introduction to Seaborn | High-level statistical visualization library, themes (`darkgrid`, `whitegrid`), Pandas integration | [Notes](Notes_19.10/README.md) \| [PDF](Notes_19.10/notes.pdf) \| [Notebook](Notes_19.10/lecture_19_10.ipynb) |
| **Notes_19.11** | Creating Plots with Seaborn | Semantic mapping attributes: `x`, `y`, `hue`, `style`, `size`, `palette` | [Notes](Notes_19.11/README.md) \| [PDF](Notes_19.11/notes.pdf) \| [Notebook](Notes_19.11/lecture_19_11.ipynb) |
| **Notes_19.12** | Relational Plots in Seaborn | Figure-level `sns.relplot()`, `sns.scatterplot()`, `sns.lineplot()`, faceting (`col`, `row`) | [Notes](Notes_19.12/README.md) \| [PDF](Notes_19.12/notes.pdf) \| [Notebook](Notes_19.12/lecture_19_12.ipynb) |
| **Notes_19.13** | Categorical Plots in Seaborn | Figure-level `sns.catplot()`, `sns.barplot()` (with CI error bars), `sns.boxplot()`, `violinplot` | [Notes](Notes_19.13/README.md) \| [PDF](Notes_19.13/notes.pdf) \| [Notebook](Notes_19.13/lecture_19_13.ipynb) |
| **Notes_19.14** | Distribution Plots in Seaborn | Figure-level `sns.displot()`, Kernel Density Estimation (`kdeplot`), `histplot`, `rugplot` | [Notes](Notes_19.14/README.md) \| [PDF](Notes_19.14/notes.pdf) \| [Notebook](Notes_19.14/lecture_19_14.ipynb) |
| **Notes_19.15** | Relational & Matrix Plots: Heatmaps | `sns.heatmap()`, correlation matrix (`df.corr()`), `annot=True`, diverging colormaps | [Notes](Notes_19.15/README.md) \| [PDF](Notes_19.15/notes.pdf) \| [Notebook](Notes_19.15/lecture_19_15.ipynb) |
| **Notes_19.16** | Best Practices for Data Visualization | Edward Tufte principles (Data-Ink ratio, chartjunk), color accessibility, chart ethics | [Notes](Notes_19.16/README.md) \| [PDF](Notes_19.16/notes.pdf) \| [Notebook](Notes_19.16/lecture_19_16.ipynb) |

---

## 📐 Mathematical Foundations

### 1. Optimal Histogram Bin Partitioning
For a sample of continuous observations $X = \{x_1, x_2, \dots, x_n\}$ with range $\Delta X = \max(X) - \min(X)$:

1. **Sturges' Rule** (Optimal for Gaussian unimodal distributions):

$$
\boxed{k = 1 + \lceil \log_2(n) \rceil}
$$

2. **Freedman-Diaconis Rule** (Robust against heavy tails, skewness, and outliers):

$$
\boxed{h = 2 \cdot \frac{\text{IQR}(X)}{n^{1/3}} \qquad\implies\qquad k = \left\lceil \frac{\Delta X}{h} \right\rceil}
$$

where:
- $n$: Sample size
- $h$: Optimal bin width
- $k$: Total number of histogram bins
- $\text{IQR}(X) = Q_3 - Q_1$: Interquartile range

---

### 2. Tukey's Five-Number Summary & Outlier Fences
Given ordered sample observations $X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$, the distribution is summarized by:

$$
\boxed{\text{Summary} = \left( X_{(1)}, \; Q_1, \; Q_2, \; Q_3, \; X_{(n)} \right)}
$$

where:
- $Q_1$: 25th percentile (First Quartile)
- $Q_2$: 50th percentile (Sample Median)
- $Q_3$: 75th percentile (Third Quartile)
- $\boxed{\text{IQR} = Q_3 - Q_1}$

Tukey's Outlier Fences $(F_L, F_U)$:

$$
\boxed{F_L = Q_1 - 1.5 \cdot \text{IQR} \qquad\text{and}\qquad F_U = Q_3 + 1.5 \cdot \text{IQR}}
$$

Outlier decision rule:

$$
\boxed{\text{Outlier}(x_i) \iff x_i < F_L \quad\lor\quad x_i > F_U}
$$

---

### 3. Univariate Kernel Density Estimation (KDE)
The continuous probability density function $f(x)$ is estimated non-parametrically as:

$$
\boxed{\hat{f}_h(x) = \frac{1}{n h} \sum_{i=1}^n K\left( \frac{x - x_i}{h} \right)}
$$

where $K(u)$ is the standard Gaussian kernel:

$$
\boxed{K(u) = \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}u^2}}
$$

and $h > 0$ is the smoothing bandwidth parameter, optimized by Silverman's formulation:

$$
\boxed{h_{\text{opt}} = 0.9 \cdot \min\left(s, \; \frac{\text{IQR}}{1.34}\right) \cdot n^{-1/5}}
$$
