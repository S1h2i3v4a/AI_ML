# 📈 Lecture 19: Advanced Matplotlib & Seaborn Mastery [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Viz-4c72b0.svg)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Main Hub Par Wapas Jayein](../README_HINGLISH.md)

---

## 📌 Module Ka Parichay (Overview)

Lecture 19 me hum advanced statistical data visualization, object-oriented Matplotlib design, aur high-level statistical library **Seaborn** ke upyog se plots banana seekhte hain. Yeh module raw plotting aur industry-grade Exploratory Data Analysis (EDA) ke beech ke gap ko fill karta hai.

Mukhya vishay:
- **Continuous Distribution Analysis**: Histograms, multi-distribution overlays, aur statistical reference lines.
- **Five-Number Summary & Outlier Detection**: Box plots, Tukey fences, notched median confidence intervals.
- **Modern Object-Oriented Matplotlib**: Explicit `fig, ax = plt.subplots()` design pattern aur multi-panel subplots.
- **High-Level Statistical Graphics with Seaborn**: Relational (`relplot`), Categorical (`catplot`), Distribution (`displot`), aur Correlation Heatmaps.
- **Data Visualization Best Practices**: Edward Tufte ke principles, visual perception hierarchy, aur color accessibility.

---

## 🗺️ Sub-Topics Navigation

| Sub-Module | Topic Title | Core Concepts | Quick Links |
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

## 📐 Ganitiya Adhaar (Mathematical Foundations)

### 1. Optimal Histogram Bin Partitioning
Continuous dataset $X = \{x_1, x_2, \dots, x_n\}$ (range $\Delta X = \max(X) - \min(X)$) ke liye bins calculate karne ke niyam:

1. **Sturges' Rule** (Normal distribution ke liye optimal):

$$
\boxed{k = 1 + \lceil \log_2(n) \rceil}
$$

2. **Freedman-Diaconis Rule** (Skewed data aur outliers ke against robust):

$$
\boxed{h = 2 \cdot \frac{\text{IQR}(X)}{n^{1/3}} \qquad\implies\qquad k = \left\lceil \frac{\Delta X}{h} \right\rceil}
$$

jahan:
- $n$: Sample size
- $h$: Optimal bin width
- $k$: Total bins count
- $\text{IQR}(X) = Q_3 - Q_1$: Interquartile range

---

### 2. Tukey's Five-Number Summary & Outlier Fences
Sorted dataset $X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$ ke liye five-number summary:

$$
\boxed{\text{Summary} = \left( X_{(1)}, \; Q_1, \; Q_2, \; Q_3, \; X_{(n)} \right)}
$$

jahan:
- $Q_1$: First Quartile (25th percentile)
- $Q_2$: Median (50th percentile)
- $Q_3$: Third Quartile (75th percentile)
- $\boxed{\text{IQR} = Q_3 - Q_1}$

Tukey's Outlier Fences $(F_L, F_U)$:

$$
\boxed{F_L = Q_1 - 1.5 \cdot \text{IQR} \qquad\text{aur}\qquad F_U = Q_3 + 1.5 \cdot \text{IQR}}
$$

Outlier rule:

$$
\boxed{\text{Outlier}(x_i) \iff x_i < F_L \quad\lor\quad x_i > F_U}
$$

---

### 3. Univariate Kernel Density Estimation (KDE)
Continuous probability density function $f(x)$ non-parametrically estimate karne ka formula:

$$
\boxed{\hat{f}_h(x) = \frac{1}{n h} \sum_{i=1}^n K\left( \frac{x - x_i}{h} \right)}
$$

jahan $K(u)$ standard Gaussian kernel hai:

$$
\boxed{K(u) = \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}u^2}}
$$

aur bandwidth parameter $h$ Silverman ke formula se optimize hota hai:

$$
\boxed{h_{\text{opt}} = 0.9 \cdot \min\left(s, \; \frac{\text{IQR}}{1.34}\right) \cdot n^{-1/5}}
$$

---

## 🎯 Practice Problems & Case Studies

Lecture 19 ke advanced visualization concepts ko master karne ke liye [Practice Problems](Practice_Problems/) module solve karein:

- 📁 **[Questions/](Practice_Problems/Questions/)**:
  - [Questions README](Practice_Problems/Questions/README_HINGLISH.md) | [questions.pdf](Practice_Problems/Questions/questions.pdf) | [questions.ipynb](Practice_Problems/Questions/questions.ipynb)
  - **Case 1**: Algorithmic E-Commerce Logistics & Delivery Duration Distribution (KDE & Histogram Density)
  - **Case 2**: Multi-Cohort Oncology Clinical Trial Biomarker & Outlier Audit (Notched Box Plots & Violins)
  - **Case 3**: Quantitative Hedge Fund Multi-Asset Risk & Macroeconomic Regime Analysis (Heatmaps & Subplots)
- 📁 **[Solutions/](Practice_Problems/Solutions/)**:
  - [Solutions Guide](Practice_Problems/Solutions/README_HINGLISH.md) | [solutions.pdf](Practice_Problems/Solutions/solutions.pdf) | [solutions.ipynb](Practice_Problems/Solutions/solutions.ipynb)
  - Industry-standard Python solutions, formal mathematical derivations aur generated high-resolution plots.

