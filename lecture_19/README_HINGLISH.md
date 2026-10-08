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
| **Notes_19.01** | Histograms (`plt.hist`) | Continuous distribution, bin count & width, density normalization, skewness | [Notes](Notes_19.01/notes.md) \| [PDF](Notes_19.01/notes.pdf) \| [Notebook](Notes_19.01/lecture_19_01.ipynb) |
| **Notes_19.02** | Multiple Datasets on Histogram | Side-by-side vs stacked histograms, overlapping distributions with alpha | [Notes](Notes_19.02/notes.md) \| [PDF](Notes_19.02/notes.pdf) \| [Notebook](Notes_19.02/lecture_19_02.ipynb) |
| **Notes_19.03** | Vertical Reference Lines (`plt.axvline`) | Statistical benchmarks: Mean, Median, Mode lines, standard deviation bands | [Notes](Notes_19.03/notes.md) \| [PDF](Notes_19.03/notes.pdf) \| [Notebook](Notes_19.03/lecture_19_03.ipynb) |
| **Notes_19.04** | Box Plots (Five-Number Summary) | Tukey's 5-number summary ($Q_1, Q_2, Q_3, \text{IQR}$), $1.5 \times \text{IQR}$ outlier detection | [Notes](Notes_19.04/notes.md) \| [PDF](Notes_19.04/notes.pdf) \| [Notebook](Notes_19.04/lecture_19_04.ipynb) |
| **Notes_19.05** | Advanced Box Plot Operations | Notched box plots (median confidence), horizontal orientation, custom flier props | [Notes](Notes_19.05/notes.md) \| [PDF](Notes_19.05/notes.pdf) \| [Notebook](Notes_19.05/lecture_19_05.ipynb) |
| **Notes_19.06** | Stack Plots (Area Charts) | Cumulative part-to-whole trends over time via `plt.stackplot()` | [Notes](Notes_19.06/notes.md) \| [PDF](Notes_19.06/notes.pdf) \| [Notebook](Notes_19.06/lecture_19_06.ipynb) |
| **Notes_19.07** | Subplots in Matplotlib | Multi-panel figures via `plt.subplot()` and `plt.subplots()`, `tight_layout()` | [Notes](Notes_19.07/notes.md) \| [PDF](Notes_19.07/notes.pdf) \| [Notebook](Notes_19.07/lecture_19_07.ipynb) |
| **Notes_19.08** | Modern Matplotlib (Object-Oriented API) | Explicit `fig, ax = plt.subplots()`, axis methods (`ax.set_*()`), cleaner engineering | [Notes](Notes_19.08/notes.md) \| [PDF](Notes_19.08/notes.pdf) \| [Notebook](Notes_19.08/lecture_19_08.ipynb) |
| **Notes_19.09** | Practice Task: Weekly Weather Analysis | Multi-axis dual plotting ($Y_1$ temperature line, $Y_2$ precipitation bars) | [Notes](Notes_19.09/notes.md) \| [PDF](Notes_19.09/notes.pdf) \| [Notebook](Notes_19.09/lecture_19_09.ipynb) |
| **Notes_19.10** | Introduction to Seaborn | High-level statistical visualization library, themes (`darkgrid`, `whitegrid`), Pandas integration | [Notes](Notes_19.10/notes.md) \| [PDF](Notes_19.10/notes.pdf) \| [Notebook](Notes_19.10/lecture_19_10.ipynb) |
| **Notes_19.11** | Creating Plots with Seaborn | Semantic mapping attributes: `x`, `y`, `hue`, `style`, `size`, `palette` | [Notes](Notes_19.11/notes.md) \| [PDF](Notes_19.11/notes.pdf) \| [Notebook](Notes_19.11/lecture_19_11.ipynb) |
| **Notes_19.12** | Relational Plots in Seaborn | Figure-level `sns.relplot()`, `sns.scatterplot()`, `sns.lineplot()`, faceting (`col`, `row`) | [Notes](Notes_19.12/notes.md) \| [PDF](Notes_19.12/notes.pdf) \| [Notebook](Notes_19.12/lecture_19_12.ipynb) |
| **Notes_19.13** | Categorical Plots in Seaborn | Figure-level `sns.catplot()`, `sns.barplot()` (with CI error bars), `sns.boxplot()`, `violinplot` | [Notes](Notes_19.13/notes.md) \| [PDF](Notes_19.13/notes.pdf) \| [Notebook](Notes_19.13/lecture_19_13.ipynb) |
| **Notes_19.14** | Distribution Plots in Seaborn | Figure-level `sns.displot()`, Kernel Density Estimation (`kdeplot`), `histplot`, `rugplot` | [Notes](Notes_19.14/notes.md) \| [PDF](Notes_19.14/notes.pdf) \| [Notebook](Notes_19.14/lecture_19_14.ipynb) |
| **Notes_19.15** | Relational & Matrix Plots: Heatmaps | `sns.heatmap()`, correlation matrix (`df.corr()`), `annot=True`, diverging colormaps | [Notes](Notes_19.15/notes.md) \| [PDF](Notes_19.15/notes.pdf) \| [Notebook](Notes_19.15/lecture_19_15.ipynb) |
| **Notes_19.16** | Best Practices for Data Visualization | Edward Tufte principles (Data-Ink ratio, chartjunk), color accessibility, chart ethics | [Notes](Notes_19.16/notes.md) \| [PDF](Notes_19.16/notes.pdf) \| [Notebook](Notes_19.16/lecture_19_16.ipynb) |

---

## 📐 Mathematical & Statistical Formulations (Ganitiya Sutra)

### 1. Optimal Histogram Bin Rules

#### Sturges' Formula (Normal Distributions ke liye)
$$\boxed{k = 1 + \lceil \log_2 n \rceil}$$

#### Freedman-Diaconis Rule (Outliers aur Skewness ke against robust)
$$\boxed{\text{Bin Width } h = 2 \cdot \dfrac{\text{IQR}(X)}{n^{1/3}} \quad\implies\quad k = \left\lceil \dfrac{\max(X) - \min(X)}{h} \right\rceil}$$

---

### 2. Tukey's Five-Number Summary & Outlier Detection
Sorted data $X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$ ke liye:
- Median ($Q_2$): 50th percentile.
- First Quartile ($Q_1$): 25th percentile.
- Third Quartile ($Q_3$): 75th percentile.
- Interquartile Range: $\boxed{\text{IQR} = Q_3 - Q_1}$

Outlier boundaries (Tukey's Fences):
$$\boxed{\text{Lower Fence} = Q_1 - 1.5 \times \text{IQR}} \qquad\text{aur}\qquad \boxed{\text{Upper Fence} = Q_3 + 1.5 \times \text{IQR}}$$

Koi bhi value jo $\text{Lower Fence}$ se choti ho ya $\text{Upper Fence}$ se badi ho, usse outlier (flier) mana jata hai.

---

### 3. Univariate Kernel Density Estimation (KDE)
Seaborn ke `sns.kdeplot()` aur `sns.displot(kind='kde')` me continuous distribution ki probability density estimate karne ka mathematical formula:

$$\boxed{\hat{f}_h(x) = \dfrac{1}{n h} \sum_{i=1}^n K\left( \dfrac{x - x_i}{h} \right)}$$

jahan $K(u)$ symmetric Gaussian kernel $K(u) = \dfrac{1}{\sqrt{2\pi}} e^{-u^2/2}$ hai aur $h > 0$ bandwidth smoothing parameter hai.
