# 🧠 AI & Machine Learning Masterclass

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Viz-4c72b0.svg)](https://seaborn.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Actively%20Maintained-success.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md)

A comprehensive, organized, and production-grade knowledge repository covering the complete **Artificial Intelligence & Machine Learning Journey (Lectures 00 to 60)**.

Each lecture module contains:
- 📝 **Structured Markdown Notes (`notes.md`)**: In-depth theoretical concepts, mathematical formulas, syntax breakdowns, and best practices.
- 📕 **High-Definition PDFs (`notes.pdf`)**: Formatted documents with rendered KaTeX formulas, tables, and Mermaid architecture diagrams for offline study.
- 💻 **Hands-On Jupyter Notebooks (`.ipynb`)**: Clean, reproducible, self-contained Python implementations with production-ready code examples.
- 📊 **Original Visuals & Diagrams**: High-clarity, code-generated diagrams and visual reference sheets.

---

## 📂 Repository Architecture

```plaintext
AI-ML/
├── .gitignore
├── README.md
├── lecture_00/                   # Course Orientation & Environment Setup
├── lecture_01/ ... lecture_17/   # (Foundations, Python & Numerical Computing)
├── lecture_18/                   # Data Visualization (Part 1 - Matplotlib Fundamentals)
│   ├── Notes_18.01/ to 18.18/    # Sub-topics with notes.md, notes.pdf, .ipynb
│   ├── Practice_Problems/        # Case Studies & Challenges (Questions & Solutions)
│   │   ├── Questions/            # questions.md, questions.pdf, questions.ipynb
│   │   └── Solutions/            # solutions.md, solutions.pdf, solutions.ipynb
├── lecture_19/                   # Data Visualization (Part 2 - Advanced Matplotlib & Seaborn)
│   ├── Notes_19.01/ to 19.16/    # Sub-topics with notes.md, notes.pdf, .ipynb, diagrams
│   └── reference_materials/      # Cheatsheets, slide notes & sample notebooks
├── lecture_20/                   # Mathematics for AI (Part 1 - Probability Theory)
│   ├── Notes_20.01/ to 20.20/    # Sub-topics with README.md, notes.pdf, .ipynb
│   └── Practice_Problems/        # Industry Case Studies (Questions & Solutions)
├── lecture_21/                   # Mathematics for AI (Part 2 - Linear Algebra Mastery)
│   ├── Notes_21.01/ to 21.15/    # Sub-topics with README.md, notes.pdf, .ipynb
│   └── Practice_Problems/        # Industry Case Studies (Questions & Solutions)
├── lecture_22/                   # Mathematics for AI (Part 3 - Calculus Mastery)
│   ├── Notes_22.01/ to 22.09/    # Sub-topics with README.md, notes.pdf, .ipynb
│   └── Practice_Problems/        # Industry Case Studies (Questions & Solutions)
└── lecture_23/ ... lecture_60/   # (Machine Learning, Deep Learning, NLP & Deployment)
```

---

## 📊 Detailed Module Breakdown

### 🎨 Day 18: Data Visualization (Part 1 — Matplotlib Mastery)
*Module Guides:* [📖 English Guide](lecture_18/README.md) \| [हिंदी / Hinglish Guide](lecture_18/README_HINGLISH.md)

Focuses on data visualization theory, the anatomy of plots, and core 2D plotting with **Matplotlib**.

| Lecture | Topic Title | Core Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **18.01** | What is Data Visualization? | Visual perception, exploratory vs explanatory, Anscombe's Quartet | [Notes](lecture_18/Notes_18.01/README.md) \| [PDF](lecture_18/Notes_18.01/notes.pdf) \| [Notebook](lecture_18/Notes_18.01/lecture_18_01.ipynb) |
| **18.02** | How to Plot Data - Basic Structure | Coordinate systems, Data Prep $\to$ Canvas $\to$ Plot $\to$ Decoration $\to$ Render | [Notes](lecture_18/Notes_18.02/README.md) \| [PDF](lecture_18/Notes_18.02/notes.pdf) \| [Notebook](lecture_18/Notes_18.02/lecture_18_02.ipynb) |
| **18.03** | Introduction to Matplotlib | Matplotlib history, architecture (`backend`, `artist`, `scripting`), Pyplot interface | [Notes](lecture_18/Notes_18.03/README.md) \| [PDF](lecture_18/Notes_18.03/notes.pdf) \| [Notebook](lecture_18/Notes_18.03/lecture_18_03.ipynb) |
| **18.04** | Important Plot Methods | `plt.plot()`, `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.grid()`, `plt.show()` | [Notes](lecture_18/Notes_18.04/README.md) \| [PDF](lecture_18/Notes_18.04/notes.pdf) \| [Notebook](lecture_18/Notes_18.04/lecture_18_04.ipynb) |
| **18.05** | Multiple Datasets on Line Plot | Multi-series plotting, legends (`plt.legend`), color differentiation, z-order | [Notes](lecture_18/Notes_18.05/README.md) \| [PDF](lecture_18/Notes_18.05/notes.pdf) \| [Notebook](lecture_18/Notes_18.05/lecture_18_05.ipynb) |
| **18.06** | Format Strings (`fmt`) | Fast syntax `[marker][line][color]`, e.g., `'ro--'`, `'b^:'`, hex colors | [Notes](lecture_18/Notes_18.06/README.md) \| [PDF](lecture_18/Notes_18.06/notes.pdf) \| [Notebook](lecture_18/Notes_18.06/lecture_18_06.ipynb) |
| **18.07** | Styling & Saving Plots | Figure sizing (`figsize`), DPI scaling, `plt.savefig()` (PNG, SVG, PDF), styling themes | [Notes](lecture_18/Notes_18.07/README.md) \| [PDF](lecture_18/Notes_18.07/notes.pdf) \| [Notebook](lecture_18/Notes_18.07/lecture_18_07.ipynb) |
| **18.08** | Chart Selection Taxonomy | Choosing the right chart: Comparison, Distribution, Composition, Relationship | [Notes](lecture_18/Notes_18.08/README.md) \| [PDF](lecture_18/Notes_18.08/notes.pdf) \| [Notebook](lecture_18/Notes_18.08/lecture_18_08.ipynb) |
| **18.09** | Vertical Bar Charts (`plt.bar`) | Categorical discrete comparison, bar width, alignment, edge styling | [Notes](lecture_18/Notes_18.09/README.md) \| [PDF](lecture_18/Notes_18.09/notes.pdf) \| [Notebook](lecture_18/Notes_18.09/lecture_18_09.ipynb) |
| **18.10** | Adding Labels to Bars | Direct data labels via `plt.text()` & `ax.bar_label()` container iteration | [Notes](lecture_18/Notes_18.10/README.md) \| [PDF](lecture_18/Notes_18.10/notes.pdf) \| [Notebook](lecture_18/Notes_18.10/lecture_18_10.ipynb) |
| **18.11** | Grouped Bar Charts | Offset indexing with NumPy `np.arange()`, width offset calculations | [Notes](lecture_18/Notes_18.11/README.md) \| [PDF](lecture_18/Notes_18.11/notes.pdf) \| [Notebook](lecture_18/Notes_18.11/lecture_18_11.ipynb) |
| **18.12** | Horizontal Bar Charts (`plt.barh`) | Long categorical labels, ranking, inverted axis sorting | [Notes](lecture_18/Notes_18.12/README.md) \| [PDF](lecture_18/Notes_18.12/notes.pdf) \| [Notebook](lecture_18/Notes_18.12/lecture_18_12.ipynb) |
| **18.13** | Scatter Plots (`plt.scatter`) | Bivariate relationships, correlation, scatter vs line performance | [Notes](lecture_18/Notes_18.13/README.md) \| [PDF](lecture_18/Notes_18.13/notes.pdf) \| [Notebook](lecture_18/Notes_18.13/lecture_18_13.ipynb) |
| **18.14** | Advanced Scatter Customizations | 4D visual encoding: Marker size (`s`), color mapping (`c`, `cmap`), alpha transparency | [Notes](lecture_18/Notes_18.14/README.md) \| [PDF](lecture_18/Notes_18.14/notes.pdf) \| [Notebook](lecture_18/Notes_18.14/lecture_18_14.ipynb) |
| **18.15** | Annotations on Scatter Plots | Point labeling via `plt.annotate()`, bounding boxes, arrows (`arrowprops`) | [Notes](lecture_18/Notes_18.15/README.md) \| [PDF](lecture_18/Notes_18.15/notes.pdf) \| [Notebook](lecture_18/Notes_18.15/lecture_18_15.ipynb) |
| **18.16** | Multiple Datasets on Scatter Plots | Multi-class scatter plots, category-wise legend separation | [Notes](lecture_18/Notes_18.16/README.md) \| [PDF](lecture_18/Notes_18.16/notes.pdf) \| [Notebook](lecture_18/Notes_18.16/lecture_18_16.ipynb) |
| **18.17** | Pie Charts (`plt.pie`) | Composition plotting, `autopct`, `startangle`, shadow, limitations | [Notes](lecture_18/Notes_18.17/README.md) \| [PDF](lecture_18/Notes_18.17/notes.pdf) \| [Notebook](lecture_18/Notes_18.17/lecture_18_17.ipynb) |
| **18.18** | Advanced Pie Charts | Donut charts (center circle wedge), `explode` slices, custom palettes | [Notes](lecture_18/Notes_18.18/README.md) \| [PDF](lecture_18/Notes_18.18/notes.pdf) \| [Notebook](lecture_18/Notes_18.18/lecture_18_18.ipynb) |


> [!TIP]
> **🧪 Day 18 Comprehensive Case Studies & Practice Problem Set:**  
> *Module Guides:* [📖 English Guide](lecture_18/Practice_Problems/README.md) \| [हिंदी / Hinglish Guide](lecture_18/Practice_Problems/README_HINGLISH.md)  
> - 📝 **Problem Statements:** [Questions](lecture_18/Practice_Problems/Questions/README.md) \| [questions.pdf](lecture_18/Practice_Problems/Questions/questions.pdf) \| [Starter Notebook](lecture_18/Practice_Problems/Questions/questions.ipynb)
> - 💡 **Complete Solutions:** [Solutions](lecture_18/Practice_Problems/Solutions/README.md) \| [solutions.pdf](lecture_18/Practice_Problems/Solutions/solutions.pdf) \| [Executed Notebook](lecture_18/Practice_Problems/Solutions/solutions.ipynb)

---

### 📈 Day 19: Data Visualization (Part 2 — Advanced Matplotlib & Seaborn)
*Module Guides:* [📖 English Guide](lecture_19/README.md) \| [हिंदी / Hinglish Guide](lecture_19/README_HINGLISH.md)

Advanced statistical visualizations, distributions, five-number summary, object-oriented Matplotlib API, and high-level **Seaborn** statistical graphics.

| Lecture | Topic Title | Core Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **19.01** | Histograms (`plt.hist`) | Continuous distribution, bin count & width, density normalization, skewness | [Notes](lecture_19/Notes_19.01/README.md) \| [PDF](lecture_19/Notes_19.01/notes.pdf) \| [Notebook](lecture_19/Notes_19.01/lecture_19_01.ipynb) |
| **19.02** | Multiple Datasets on Histogram | Side-by-side vs stacked histograms, overlapping distributions with alpha | [Notes](lecture_19/Notes_19.02/README.md) \| [PDF](lecture_19/Notes_19.02/notes.pdf) \| [Notebook](lecture_19/Notes_19.02/lecture_19_02.ipynb) |
| **19.03** | Vertical Reference Lines (`plt.axvline`) | Statistical threshold benchmarks: Mean, Median, Mode lines & annotations | [Notes](lecture_19/Notes_19.03/README.md) \| [PDF](lecture_19/Notes_19.03/notes.pdf) \| [Notebook](lecture_19/Notes_19.03/lecture_19_03.ipynb) |
| **19.04** | Box Plots (Five-Number Summary) | Tukey's 5-number summary ($Q_1, Q_2, Q_3, \text{IQR}$), $1.5 \times \text{IQR}$ outlier detection | [Notes](lecture_19/Notes_19.04/README.md) \| [PDF](lecture_19/Notes_19.04/notes.pdf) \| [Notebook](lecture_19/Notes_19.04/lecture_19_04.ipynb) |
| **19.05** | Advanced Box Plot Operations | Notched box plots (median confidence), horizontal orientation, custom flier props | [Notes](lecture_19/Notes_19.05/README.md) \| [PDF](lecture_19/Notes_19.05/notes.pdf) \| [Notebook](lecture_19/Notes_19.05/lecture_19_05.ipynb) |
| **19.06** | Stack Plots (Area Charts) | Cumulative part-to-whole trends over time via `plt.stackplot()` | [Notes](lecture_19/Notes_19.06/README.md) \| [PDF](lecture_19/Notes_19.06/notes.pdf) \| [Notebook](lecture_19/Notes_19.06/lecture_19_06.ipynb) |
| **19.07** | Subplots in Matplotlib | Multi-panel figures via `plt.subplot()` and `plt.subplots()`, `tight_layout()` | [Notes](lecture_19/Notes_19.07/README.md) \| [PDF](lecture_19/Notes_19.07/notes.pdf) \| [Notebook](lecture_19/Notes_19.07/lecture_19_07.ipynb) |
| **19.08** | Modern Matplotlib (Object-Oriented API) | Explicit `fig, ax = plt.subplots()`, axis methods (`ax.set_*()`), cleaner engineering | [Notes](lecture_19/Notes_19.08/README.md) \| [PDF](lecture_19/Notes_19.08/notes.pdf) \| [Notebook](lecture_19/Notes_19.08/lecture_19_08.ipynb) |
| **19.09** | Practice Task: Weekly Weather Analysis | Multi-axis dual plotting ($Y_1$ temperature line, $Y_2$ precipitation bars) | [Notes](lecture_19/Notes_19.09/README.md) \| [PDF](lecture_19/Notes_19.09/notes.pdf) \| [Notebook](lecture_19/Notes_19.09/lecture_19_09.ipynb) |
| **19.10** | Introduction to Seaborn | High-level statistical visualization library, themes (`darkgrid`, `whitegrid`), Pandas integration | [Notes](lecture_19/Notes_19.10/README.md) \| [PDF](lecture_19/Notes_19.10/notes.pdf) \| [Notebook](lecture_19/Notes_19.10/lecture_19_10.ipynb) |
| **19.11** | Creating Plots with Seaborn | Semantic mapping attributes: `x`, `y`, `hue`, `style`, `size`, `palette` | [Notes](lecture_19/Notes_19.11/README.md) \| [PDF](lecture_19/Notes_19.11/notes.pdf) \| [Notebook](lecture_19/Notes_19.11/lecture_19_11.ipynb) |
| **19.12** | Relational Plots in Seaborn | Figure-level `sns.relplot()`, `sns.scatterplot()`, `sns.lineplot()`, faceting (`col`, `row`) | [Notes](lecture_19/Notes_19.12/README.md) \| [PDF](lecture_19/Notes_19.12/notes.pdf) \| [Notebook](lecture_19/Notes_19.12/lecture_19_12.ipynb) |
| **19.13** | Categorical Plots in Seaborn | Figure-level `sns.catplot()`, `sns.barplot()` (with CI error bars), `sns.boxplot()`, `violinplot` | [Notes](lecture_19/Notes_19.13/README.md) \| [PDF](lecture_19/Notes_19.13/notes.pdf) \| [Notebook](lecture_19/Notes_19.13/lecture_19_13.ipynb) |
| **19.14** | Distribution Plots in Seaborn | Figure-level `sns.displot()`, Kernel Density Estimation (`kdeplot`), `histplot`, `rugplot` | [Notes](lecture_19/Notes_19.14/README.md) \| [PDF](lecture_19/Notes_19.14/notes.pdf) \| [Notebook](lecture_19/Notes_19.14/lecture_19_14.ipynb) |
| **19.15** | Relational & Matrix Plots: Heatmaps | `sns.heatmap()`, correlation matrix (`df.corr()`), `annot=True`, diverging colormaps | [Notes](lecture_19/Notes_19.15/README.md) \| [PDF](lecture_19/Notes_19.15/notes.pdf) \| [Notebook](lecture_19/Notes_19.15/lecture_19_15.ipynb) |
| **19.16** | Best Practices for Data Visualization | Edward Tufte principles (Data-Ink ratio, chartjunk), color accessibility, chart ethics | [Notes](lecture_19/Notes_19.16/README.md) \| [PDF](lecture_19/Notes_19.16/notes.pdf) \| [Notebook](lecture_19/Notes_19.16/lecture_19_16.ipynb) |


> [!TIP]
> **🧪 Day 19 Comprehensive Case Studies & Practice Problem Set:**  
> *Module Guides:* [📖 English Guide](lecture_19/Practice_Problems/README.md) \| [हिंदी / Hinglish Guide](lecture_19/Practice_Problems/README_HINGLISH.md)  
> - 📝 **Problem Statements:** [Questions](lecture_19/Practice_Problems/Questions/README.md) \| [questions.pdf](lecture_19/Practice_Problems/Questions/questions.pdf) \| [Starter Notebook](lecture_19/Practice_Problems/Questions/questions.ipynb)
> - 💡 **Complete Solutions:** [Solutions](lecture_19/Practice_Problems/Solutions/README.md) \| [solutions.pdf](lecture_19/Practice_Problems/Solutions/solutions.pdf) \| [Executed Notebook](lecture_19/Practice_Problems/Solutions/solutions.ipynb)

### 🎲 Day 20: Mathematics for AI (Part 1 — Probability Theory)
*Module Guides:* [📖 English Guide](lecture_20/README.md) | [हिंदी / Hinglish Guide](lecture_20/README_HINGLISH.md)

Rigorous mathematical foundations of probability for AI & Machine Learning: Kolmogorov axioms, conditional probability, Bayes' Theorem, random variables, expectation, variance, and parametric distributions (Binomial, Uniform, Gaussian).

| Lecture | Topic Title | Core Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **20.01** | Math for AI & Why Probability Matters | Uncertainty quantification, MLE, cross-entropy, generative modeling | [Notes](lecture_20/Notes_20.01/README.md) \| [PDF](lecture_20/Notes_20.01/notes.pdf) \| [Notebook](lecture_20/Notes_20.01/lecture_20_01.ipynb) |
| **20.02** | Core Foundations of Probability | Random experiments, sample space, events, Kolmogorov's 3 axioms | [Notes](lecture_20/Notes_20.02/README.md) \| [PDF](lecture_20/Notes_20.02/notes.pdf) \| [Notebook](lecture_20/Notes_20.02/lecture_20_02.ipynb) |
| **20.03** | Classical vs. Empirical Probability | Theoretical symmetry, frequentist relative frequency, Law of Large Numbers | [Notes](lecture_20/Notes_20.03/README.md) \| [PDF](lecture_20/Notes_20.03/notes.pdf) \| [Notebook](lecture_20/Notes_20.03/lecture_20_03.ipynb) |
| **20.04** | Foundation Probability Practice Problems | Combinatorics, permutations $P(n,k)$, combinations $C(n,k)$, counting rules | [Notes](lecture_20/Notes_20.04/README.md) \| [PDF](lecture_20/Notes_20.04/notes.pdf) \| [Notebook](lecture_20/Notes_20.04/lecture_20_04.ipynb) |
| **20.05** | Types of Events | Mutually exclusive vs independent events, exhaustive events, partitions | [Notes](lecture_20/Notes_20.05/README.md) \| [PDF](lecture_20/Notes_20.05/notes.pdf) \| [Notebook](lecture_20/Notes_20.05/lecture_20_05.ipynb) |
| **20.06** | The Complementary Rule | Complement $P(A') = 1 - P(A)$, De Morgan's laws, at-least-one calculations | [Notes](lecture_20/Notes_20.06/README.md) \| [PDF](lecture_20/Notes_20.06/notes.pdf) \| [Notebook](lecture_20/Notes_20.06/lecture_20_06.ipynb) |
| **20.07** | The Addition Rule of Probability | General addition rule, double-counting correction, inclusion-exclusion | [Notes](lecture_20/Notes_20.07/README.md) \| [PDF](lecture_20/Notes_20.07/notes.pdf) \| [Notebook](lecture_20/Notes_20.07/lecture_20_07.ipynb) |
| **20.08** | The Multiplication Rule of Probability | Joint intersection, dependent vs independent, probability chain rule | [Notes](lecture_20/Notes_20.08/README.md) \| [PDF](lecture_20/Notes_20.08/notes.pdf) \| [Notebook](lecture_20/Notes_20.08/lecture_20_08.ipynb) |
| **20.09** | Probability Rules Practice Problems | Series vs parallel system reliability, fault tolerance, urn problems | [Notes](lecture_20/Notes_20.09/README.md) \| [PDF](lecture_20/Notes_20.09/notes.pdf) \| [Notebook](lecture_20/Notes_20.09/lecture_20_09.ipynb) |
| **20.10** | Conditional Probability | Reduced sample space, $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$, contingency tables | [Notes](lecture_20/Notes_20.10/README.md) \| [PDF](lecture_20/Notes_20.10/notes.pdf) \| [Notebook](lecture_20/Notes_20.10/lecture_20_10.ipynb) |
| **20.11** | The Law of Total Probability | Sample space partition, marginalization, total defect calculations | [Notes](lecture_20/Notes_20.11/README.md) \| [PDF](lecture_20/Notes_20.11/notes.pdf) \| [Notebook](lecture_20/Notes_20.11/lecture_20_11.ipynb) |
| **20.12** | Bayes' Theorem | Prior, likelihood, marginal evidence, posterior belief updating | [Notes](lecture_20/Notes_20.12/README.md) \| [PDF](lecture_20/Notes_20.12/notes.pdf) \| [Notebook](lecture_20/Notes_20.12/lecture_20_12.ipynb) |
| **20.13** | Bayes' Theorem Practice Problems | Medical diagnosis paradox, base rate fallacy, false positives in AI | [Notes](lecture_20/Notes_20.13/README.md) \| [PDF](lecture_20/Notes_20.13/notes.pdf) \| [Notebook](lecture_20/Notes_20.13/lecture_20_13.ipynb) |
| **20.14** | Random Variables | Mapping $X: \mathcal{S} \to \mathbb{R}$, discrete vs continuous, PMF, PDF, CDF | [Notes](lecture_20/Notes_20.14/README.md) \| [PDF](lecture_20/Notes_20.14/notes.pdf) \| [Notebook](lecture_20/Notes_20.14/lecture_20_14.ipynb) |
| **20.15** | Mean, Median & Mode | Expected value $\mathbb{E}[X]$, linearity of expectation, skewness impact | [Notes](lecture_20/Notes_20.15/README.md) \| [PDF](lecture_20/Notes_20.15/notes.pdf) \| [Notebook](lecture_20/Notes_20.15/lecture_20_15.ipynb) |
| **20.16** | Variance & Standard Deviation | Dispersion $\text{Var}(X) = \mathbb{E}[(X-\mu)^2]$, shortcut $\mathbb{E}[X^2] - (\mathbb{E}[X])^2$ | [Notes](lecture_20/Notes_20.16/README.md) \| [PDF](lecture_20/Notes_20.16/notes.pdf) \| [Notebook](lecture_20/Notes_20.16/lecture_20_16.ipynb) |
| **20.17** | Probability Distributions & its Types | Discrete vs continuous families, PMF/PDF properties, AI loss mapping | [Notes](lecture_20/Notes_20.17/README.md) \| [PDF](lecture_20/Notes_20.17/notes.pdf) \| [Notebook](lecture_20/Notes_20.17/lecture_20_17.ipynb) |
| **20.18** | Binomial Distribution | Bernoulli trials, PMF $\binom{n}{k} p^k (1-p)^{n-k}$, mean $np$, variance $np(1-p)$ | [Notes](lecture_20/Notes_20.18/README.md) \| [PDF](lecture_20/Notes_20.18/notes.pdf) \| [Notebook](lecture_20/Notes_20.18/lecture_20_18.ipynb) |
| **20.19** | Uniform Distribution | Constant density $\mathcal{U}(a, b)$, PDF $\frac{1}{b-a}$, mean $\frac{a+b}{2}$, variance $\frac{(b-a)^2}{12}$ | [Notes](lecture_20/Notes_20.19/README.md) \| [PDF](lecture_20/Notes_20.19/notes.pdf) \| [Notebook](lecture_20/Notes_20.19/lecture_20_19.ipynb) |
| **20.20** | Normal Distribution | Bell curve PDF, 68-95-99.7 rule, Z-score standardization, CLT connection | [Notes](lecture_20/Notes_20.20/README.md) \| [PDF](lecture_20/Notes_20.20/notes.pdf) \| [Notebook](lecture_20/Notes_20.20/lecture_20_20.ipynb) |


> [!TIP]
> **🧪 Day 20 Comprehensive Case Studies & Practice Problem Set:**  
> *Module Guides:* [📖 English Guide](lecture_20/Practice_Problems/README.md) | [हिंदी / Hinglish Guide](lecture_20/Practice_Problems/README_HINGLISH.md)  
> - 📝 **Problem Statements:** [Questions](lecture_20/Practice_Problems/Questions/README.md) | [questions.pdf](lecture_20/Practice_Problems/Questions/questions.pdf) | [Starter Notebook](lecture_20/Practice_Problems/Questions/questions.ipynb)
> - 💡 **Complete Solutions:** [Solutions](lecture_20/Practice_Problems/Solutions/README.md) | [solutions.pdf](lecture_20/Practice_Problems/Solutions/solutions.pdf) | [Executed Notebook](lecture_20/Practice_Problems/Solutions/solutions.ipynb)

### 📐 Day 21: Mathematics for AI (Part 2 — Linear Algebra Mastery)
*Module Guides:* [📖 English Guide](lecture_21/README.md) | [हिंदी / Hinglish Guide](lecture_21/README_HINGLISH.md)

Rigorous mathematical foundations of Linear Algebra for AI, Machine Learning & Deep Learning: Vectors, matrices, tensors, inner products, norms, span, basis, rank, determinants, Gaussian elimination, Moore-Penrose pseudo-inverses, Gram-Schmidt orthogonalization, QR decomposition, eigenvalues, eigenvectors, symmetric spectral theorem, Singular Value Decomposition (SVD), PCA, and Deep Learning attention mechanisms (LoRA).

| Lecture | Topic Title | Core Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **21.01** | Vectors, Scalars, Matrices & Tensors | Tensor rank hierarchy (0D to 4D), row/column vectors, batch tensors | [Notes](lecture_21/Notes_21.01/README.md) \| [PDF](lecture_21/Notes_21.01/notes.pdf) \| [Notebook](lecture_21/Notes_21.01/lecture_21_01.ipynb) |
| **21.02** | Vector Operations & Geometric Intuition | Vector addition, scalar multiplication, $\ell_1$ & $\ell_2$ norms, cosine similarity | [Notes](lecture_21/Notes_21.02/README.md) \| [PDF](lecture_21/Notes_21.02/notes.pdf) \| [Notebook](lecture_21/Notes_21.02/lecture_21_02.ipynb) |
| **21.03** | Matrix Operations & Special Matrices | Addition, scaling, transposes, symmetric, diagonal, identity, orthogonal matrices | [Notes](lecture_21/Notes_21.03/README.md) \| [PDF](lecture_21/Notes_21.03/notes.pdf) \| [Notebook](lecture_21/Notes_21.03/lecture_21_03.ipynb) |
| **21.04** | Matrix Multiplication & AI Forward Passes | Dot products vs outer products, linear composition, batch gemm $\mathcal{O}(mnp)$ | [Notes](lecture_21/Notes_21.04/README.md) \| [PDF](lecture_21/Notes_21.04/notes.pdf) \| [Notebook](lecture_21/Notes_21.04/lecture_21_04.ipynb) |
| **21.05** | Linear Combinations, Span & Basis | Linear combinations, span subspaces, linear independence, canonical basis | [Notes](lecture_21/Notes_21.05/README.md) \| [PDF](lecture_21/Notes_21.05/notes.pdf) \| [Notebook](lecture_21/Notes_21.05/lecture_21_05.ipynb) |
| **21.06** | Linear Independence & Matrix Rank | Row/column rank, rank-nullity theorem, full rank vs rank deficiency | [Notes](lecture_21/Notes_21.06/README.md) \| [PDF](lecture_21/Notes_21.06/notes.pdf) \| [Notebook](lecture_21/Notes_21.06/lecture_21_06.ipynb) |
| **21.07** | Determinants & Geometric Singularity | Oriented volume scaling, Laplace expansion, invertibility criterion $\det(A) \ne 0$ | [Notes](lecture_21/Notes_21.07/README.md) \| [PDF](lecture_21/Notes_21.07/notes.pdf) \| [Notebook](lecture_21/Notes_21.07/lecture_21_07.ipynb) |
| **21.08** | Systems of Linear Equations & Gaussian Elimination | Augmented matrix, forward elimination, back-substitution, REF & RREF | [Notes](lecture_21/Notes_21.08/README.md) \| [PDF](lecture_21/Notes_21.08/notes.pdf) \| [Notebook](lecture_21/Notes_21.08/lecture_21_08.ipynb) |
| **21.09** | Matrix Inverses & Moore-Penrose Pseudo-Inverse | Gauss-Jordan inversion, overdetermined systems, pseudo-inverse $A^+$, Least Squares | [Notes](lecture_21/Notes_21.09/README.md) \| [PDF](lecture_21/Notes_21.09/notes.pdf) \| [Notebook](lecture_21/Notes_21.09/lecture_21_09.ipynb) |
| **21.10** | Orthogonality, Orthonormality & Projections | Orthogonal projections, Gram-Schmidt orthogonalization, QR decomposition | [Notes](lecture_21/Notes_21.10/README.md) \| [PDF](lecture_21/Notes_21.10/notes.pdf) \| [Notebook](lecture_21/Notes_21.10/lecture_21_10.ipynb) |
| **21.11** | Eigenvalues & Eigenvectors | Invariant directions, characteristic equation $\det(A - \lambda I) = 0$, eigenspaces | [Notes](lecture_21/Notes_21.11/README.md) \| [PDF](lecture_21/Notes_21.11/notes.pdf) \| [Notebook](lecture_21/Notes_21.11/lecture_21_11.ipynb) |
| **21.12** | Diagonalization & Spectral Theorem | Modal matrix $P$, similarity transformation $A = P \Lambda P^{-1}$, symmetric spectral theorem | [Notes](lecture_21/Notes_21.12/README.md) \| [PDF](lecture_21/Notes_21.12/notes.pdf) \| [Notebook](lecture_21/Notes_21.12/lecture_21_12.ipynb) |
| **21.13** | Singular Value Decomposition (SVD) | Rectangular factorization $A = U \Sigma V^T$, Eckart-Young low-rank theorem | [Notes](lecture_21/Notes_21.13/README.md) \| [PDF](lecture_21/Notes_21.13/notes.pdf) \| [Notebook](lecture_21/Notes_21.13/lecture_21_13.ipynb) |
| **21.14** | Principal Component Analysis (PCA) via Linear Algebra | Covariance matrix $\mathbf{\Sigma}$, spectral projection, scree plot, dimensionality reduction | [Notes](lecture_21/Notes_21.14/README.md) \| [PDF](lecture_21/Notes_21.14/notes.pdf) \| [Notebook](lecture_21/Notes_21.14/lecture_21_14.ipynb) |
| **21.15** | Linear Algebra in Deep Learning & Attention | Dense layers, im2col gemm convolution, Transformer Scaled Dot-Product Attention, LoRA | [Notes](lecture_21/Notes_21.15/README.md) \| [PDF](lecture_21/Notes_21.15/notes.pdf) \| [Notebook](lecture_21/Notes_21.15/lecture_21_15.ipynb) |

> [!TIP]
> **🧪 Day 21 Comprehensive Case Studies & Practice Problem Set:**  
> *Module Guides:* [📖 English Guide](lecture_21/Practice_Problems/README.md) | [हिंदी / Hinglish Guide](lecture_21/Practice_Problems/README_HINGLISH.md)  
> - 📝 **Problem Statements:** [Questions](lecture_21/Practice_Problems/Questions/README.md) | [questions.pdf](lecture_21/Practice_Problems/Questions/questions.pdf) | [Starter Notebook](lecture_21/Practice_Problems/Questions/questions.ipynb)
> - 💡 **Complete Solutions:** [Solutions](lecture_21/Practice_Problems/Solutions/README.md) | [solutions.pdf](lecture_21/Practice_Problems/Solutions/solutions.pdf) | [Executed Notebook](lecture_21/Practice_Problems/Solutions/solutions.ipynb)

### 📉 Day 22: Mathematics for AI (Part 3 — Calculus Mastery)
*Module Guides:* [📖 English Guide](lecture_22/README.md) | [हिंदी / Hinglish Guide](lecture_22/README_HINGLISH.md)

Rigorous mathematical foundations of Calculus for AI, Machine Learning & Deep Learning: Functions, composite functions, function arithmetic, vertical/horizontal transformations, limit definition of derivative, differentiation rules, activation derivatives (Sigmoid, Tanh, ReLU), critical points, concavity tests, and Gradient Descent optimization.

| Lecture | Topic Title | Core Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **22.01** | Introduction to Calculus for AI & Continuous Change | Continuous change, differential vs integral, parameter sensitivity, loss minimization | [Notes](lecture_22/Notes_22.01/README.md) \| [PDF](lecture_22/Notes_22.01/notes.pdf) \| [Notebook](lecture_22/Notes_22.01/lecture_22_01.ipynb) |
| **22.02** | Mathematical Functions & Real-World Transformations | Domain, codomain, range, root functions, sinusoids, exponentials, logs in AI | [Notes](lecture_22/Notes_22.02/README.md) \| [PDF](lecture_22/Notes_22.02/notes.pdf) \| [Notebook](lecture_22/Notes_22.02/lecture_22_02.ipynb) |
| **22.03** | Composite Functions & Deep Neural Architectures | Function composition $(f \circ g)(x)$, nested deep neural network forward pass, non-commutativity | [Notes](lecture_22/Notes_22.03/README.md) \| [PDF](lecture_22/Notes_22.03/notes.pdf) \| [Notebook](lecture_22/Notes_22.03/lecture_22_03.ipynb) |
| **22.04** | Operations on Functions: Scalar Multiplication & Addition | Vertical stretch, compression, shift, reflection, linear combinations, residual connections | [Notes](lecture_22/Notes_22.04/README.md) \| [PDF](lecture_22/Notes_22.04/notes.pdf) \| [Notebook](lecture_22/Notes_22.04/lecture_22_04.ipynb) |
| **22.05** | Input Transformations: Scaling & Shifts | Horizontal shifts, horizontal scaling, affine input maps ($z = w x + b$), standardization | [Notes](lecture_22/Notes_22.05/README.md) \| [PDF](lecture_22/Notes_22.05/notes.pdf) \| [Notebook](lecture_22/Notes_22.05/lecture_22_05.ipynb) |
| **22.06** | Differentiation & Instantaneous Rate of Change | Secant to tangent limit, derivative definition, first-principles proofs, Taylor linear approximation | [Notes](lecture_22/Notes_22.06/README.md) \| [PDF](lecture_22/Notes_22.06/notes.pdf) \| [Notebook](lecture_22/Notes_22.06/lecture_22_06.ipynb) |
| **22.07** | Differentiation Rules & Activation Derivatives | Power, product, quotient, chain rule. Derivations of Sigmoid, Tanh, ReLU derivatives | [Notes](lecture_22/Notes_22.07/README.md) \| [PDF](lecture_22/Notes_22.07/notes.pdf) \| [Notebook](lecture_22/Notes_22.07/lecture_22_07.ipynb) |
| **22.08** | Finding Minima & Maxima | Critical points, First & Second Derivative Tests, concavity, Gradient Descent algorithm | [Notes](lecture_22/Notes_22.08/README.md) \| [PDF](lecture_22/Notes_22.08/notes.pdf) \| [Notebook](lecture_22/Notes_22.08/lecture_22_08.ipynb) |
| **22.09** | Calculus Optimization Practice Problem | Analytical derivation of $f(x) = x^3 - 6x^2 + 9x$, critical points, double derivative test, extrema | [Notes](lecture_22/Notes_22.09/README.md) \| [PDF](lecture_22/Notes_22.09/notes.pdf) \| [Notebook](lecture_22/Notes_22.09/lecture_22_09.ipynb) |

> [!TIP]
> **🧪 Day 22 Comprehensive Case Studies & Practice Problem Set:**  
> *Module Guides:* [📖 English Guide](lecture_22/Practice_Problems/README.md) | [हिंदी / Hinglish Guide](lecture_22/Practice_Problems/README_HINGLISH.md)  
> - 📝 **Problem Statements:** [Questions](lecture_22/Practice_Problems/Questions/README.md) | [questions.pdf](lecture_22/Practice_Problems/Questions/questions.pdf) | [Starter Notebook](lecture_22/Practice_Problems/Questions/questions.ipynb)
> - 💡 **Complete Solutions:** [Solutions](lecture_22/Practice_Problems/Solutions/README.md) | [solutions.pdf](lecture_22/Practice_Problems/Solutions/solutions.pdf) | [Executed Notebook](lecture_22/Practice_Problems/Solutions/solutions.ipynb)

---

### 🤖 Day 23: Machine Learning & Linear Regression Foundations
*Module Guides:* [📖 English Guide](lecture_23/README.md) | [हिंदी / Hinglish Guide](lecture_23/README_HINGLISH.md)

Rigorous theoretical foundations of Supervised Machine Learning and **Linear Regression**: Arthur Samuel & Tom Mitchell definitions, ML paradigms, Supervised ML workflow, Generalization error & Bias-Variance tradeoff, Regression vs Classification, Scikit-Learn API architecture (Estimators, Transformers, Predictors), Linear Hypothesis line & hyperplane geometry, Ordinary Least Squares (OLS) residual derivation, Mean Squared Error (MSE) cost function, strict convexity & contour geometry, Vectorized Gradient Descent optimization, learning rate dynamics, analytical Normal Equation vs numerical solvers, end-to-end `insurance.csv` implementation, and comprehensive evaluation metrics (MAE, MSE, RMSE, $R^2$, and degrees-of-freedom Adjusted $R^2$).

| Lecture | Topic Title | Core Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **23.01** | Introduction to Machine Learning | Arthur Samuel & Tom Mitchell definitions $E, T, P$; ML paradigms taxonomy | [Notes](lecture_23/Notes_23.01/README.md) \| [PDF](lecture_23/Notes_23.01/notes.pdf) \| [Notebook](lecture_23/Notes_23.01/lecture_23_01.ipynb) |
| **23.02** | Types of ML: Supervised Learning | Labeled datasets $\mathcal{D} = \{(\mathbf{x}^{(i)}, y^{(i)})\}$, target mapping $f: \mathcal{X} \to \mathcal{Y}$ | [Notes](lecture_23/Notes_23.02/README.md) \| [PDF](lecture_23/Notes_23.02/notes.pdf) \| [Notebook](lecture_23/Notes_23.02/lecture_23_02.ipynb) |
| **23.03** | Types of ML: Unsupervised & Reinforcement Learning | Latent structure discovery, PCA, K-Means clustering, MDP $(S, A, P, R, \gamma)$ | [Notes](lecture_23/Notes_23.03/README.md) \| [PDF](lecture_23/Notes_23.03/notes.pdf) \| [Notebook](lecture_23/Notes_23.03/lecture_23_03.ipynb) |
| **23.04** | Supervised ML Workflow & Components | Data splits, generalization error, Bias-Variance tradeoff, Overfitting vs Underfitting | [Notes](lecture_23/Notes_23.04/README.md) \| [PDF](lecture_23/Notes_23.04/notes.pdf) \| [Notebook](lecture_23/Notes_23.04/lecture_23_04.ipynb) |
| **23.05** | Regression vs. Classification Tasks | Continuous targets vs discrete labels, MSE vs Cross-Entropy loss | [Notes](lecture_23/Notes_23.05/README.md) \| [PDF](lecture_23/Notes_23.05/notes.pdf) \| [Notebook](lecture_23/Notes_23.05/lecture_23_05.ipynb) |
| **23.06** | Introduction to Scikit-Learn | API design principles: Estimators, Transformers, Predictors, Uniform interface | [Notes](lecture_23/Notes_23.06/README.md) \| [PDF](lecture_23/Notes_23.06/notes.pdf) \| [Notebook](lecture_23/Notes_23.06/lecture_23_06.ipynb) |
| **23.07** | Starting with Linear Regression | Linear hypothesis $\hat{y} = \mathbf{w}^T \mathbf{x} + b$, geometric hyperplane intuition | [Notes](lecture_23/Notes_23.07/README.md) \| [PDF](lecture_23/Notes_23.07/notes.pdf) \| [Notebook](lecture_23/Notes_23.07/lecture_23_07.ipynb) |
| **23.08** | What is the Best Fit Line? | Residuals $e_i = y_i - \hat{y}_i$, Ordinary Least Squares (OLS), covariance/variance formula | [Notes](lecture_23/Notes_23.08/README.md) \| [PDF](lecture_23/Notes_23.08/notes.pdf) \| [Notebook](lecture_23/Notes_23.08/lecture_23_08.ipynb) |
| **23.09** | What is the Cost Function? | Mean Squared Error (MSE), mathematical justification for the $\frac{1}{2m}$ factor | [Notes](lecture_23/Notes_23.09/README.md) \| [PDF](lecture_23/Notes_23.09/notes.pdf) \| [Notebook](lecture_23/Notes_23.09/lecture_23_09.ipynb) |
| **23.10** | Understanding the Cost Function Curve | Convexity, positive definite Hessian $\mathbf{H}$, 1D parabola vs 3D paraboloid contours | [Notes](lecture_23/Notes_23.10/README.md) \| [PDF](lecture_23/Notes_23.10/notes.pdf) \| [Notebook](lecture_23/Notes_23.10/lecture_23_10.ipynb) |
| **23.11** | Gradient Descent in Linear Regression | Partial derivatives $\nabla J$, simultaneous update rule, learning rate $\alpha$ dynamics | [Notes](lecture_23/Notes_23.11/README.md) \| [PDF](lecture_23/Notes_23.11/notes.pdf) \| [Notebook](lecture_23/Notes_23.11/lecture_23_11.ipynb) |
| **23.12** | Summary of Linear Regression Foundations | Normal Equation $\mathbf{w}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$ vs Gradient Descent comparison | [Notes](lecture_23/Notes_23.12/README.md) \| [PDF](lecture_23/Notes_23.12/notes.pdf) \| [Notebook](lecture_23/Notes_23.12/lecture_23_12.ipynb) |
| **23.13** | Linear Regression Hands-On Pipeline | End-to-end `insurance.csv` implementation, categorical encoding, scikit-learn training | [Notes](lecture_23/Notes_23.13/README.md) \| [PDF](lecture_23/Notes_23.13/notes.pdf) \| [Notebook](lecture_23/Notes_23.13/lecture_23_13.ipynb) |
| **23.14** | Evaluation Metrics for Regression | MAE, MSE, RMSE, $R^2$, and degrees-of-freedom Adjusted $R^2$ penalty | [Notes](lecture_23/Notes_23.14/README.md) \| [PDF](lecture_23/Notes_23.14/notes.pdf) \| [Notebook](lecture_23/Notes_23.14/lecture_23_14.ipynb) |

> [!TIP]
> **🧪 Day 23 Comprehensive Case Studies & Practice Problem Set:**  
> *Module Guides:* [📖 English Guide](lecture_23/Practice_Problems/README.md) | [हिंदी / Hinglish Guide](lecture_23/Practice_Problems/README_HINGLISH.md)  
> - 📝 **Problem Statements:** [Questions](lecture_23/Practice_Problems/Questions/README.md) | [questions.pdf](lecture_23/Practice_Problems/Questions/questions.pdf) | [Starter Notebook](lecture_23/Practice_Problems/Questions/lecture_23_questions.ipynb)
> - 💡 **Complete Solutions:** [Solutions](lecture_23/Practice_Problems/Solutions/README.md) | [solutions.pdf](lecture_23/Practice_Problems/Solutions/solutions.pdf) | [Executed Notebook](lecture_23/Practice_Problems/Solutions/lecture_23_solutions.ipynb)

---

### 🧠 Day 24: Advanced Regression, Regularization & Logistic Regression
*Module Guides:* [📖 English Guide](lecture_24/README.md) | [हिंदी / Hinglish Guide](lecture_24/README_HINGLISH.md)

Bridging classical regression to high-performance regularized models and probabilistic classification: Categorical feature encoding (Nominal vs Ordinal, One-Hot orthogonal basis), the Dummy Variable Trap & perfect multicollinearity, Feature scaling (StandardScaler, MinMaxScaler, RobustScaler), Discretization & Interaction polynomials, the Bias-Variance tradeoff decomposition ($\text{Bias}^2 + \text{Var} + \sigma^2$), Overfitting vs Underfitting mathematical anatomy, systematic mitigation playbook, diagnostic Learning Curves ($m$ vs loss), L1 Regularization (Lasso) diamond geometry & automatic feature selection, L2 Regularization (Ridge / Tikhonov) circular geometry & analytical Normal Equation, Lasso Regularization paths & LassoCV hyperparameter search, ElasticNet hybrid grouping effect, Logistic Regression Odds & Log-odds Logit, Sigmoid activation $\sigma(z) = \frac{1}{1 + e^{-z}}$, linear decision boundary hyperplane, Maximum Likelihood Estimation (MLE) derivation of Binary Cross-Entropy (Log Loss), gradient updates, clinical `heart.csv` pipeline, Confusion Matrix, and comprehensive classification metrics (Accuracy, Precision, Recall, F1-Score, ROC-AUC).

| Lecture | Topic Title | Core Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **24.01** | Feature Engineering: Encoding | Nominal vs Ordinal, Label Encoding, One-Hot Encoding orthogonal basis | [Notes](lecture_24/Notes_24.01/README.md) \| [PDF](lecture_24/Notes_24.01/notes.pdf) \| [Notebook](lecture_24/Notes_24.01/lecture_24_01.ipynb) |
| **24.02** | The Dummy Variable Trap | Perfect multicollinearity, singular matrix $\det(\mathbf{X}^T \mathbf{X}) = 0$, $K-1$ rule | [Notes](lecture_24/Notes_24.02/README.md) \| [PDF](lecture_24/Notes_24.02/notes.pdf) \| [Notebook](lecture_24/Notes_24.02/lecture_24_02.ipynb) |
| **24.03** | Other Feature Engineering Techniques | Z-score standardization vs MinMax normalization, Binning, Polynomial interactions | [Notes](lecture_24/Notes_24.03/README.md) \| [PDF](lecture_24/Notes_24.03/notes.pdf) \| [Notebook](lecture_24/Notes_24.03/lecture_24_03.ipynb) |
| **24.04** | Overfitting (High Variance) | Memorizing noise, Bias-Variance decomposition $\text{Bias}^2 + \text{Var} + \sigma^2$, generalization gap | [Notes](lecture_24/Notes_24.04/README.md) \| [PDF](lecture_24/Notes_24.04/notes.pdf) \| [Notebook](lecture_24/Notes_24.04/lecture_24_04.ipynb) |
| **24.05** | Underfitting (High Bias) | Oversimplified hypothesis space, inability to capture non-linear structure | [Notes](lecture_24/Notes_24.05/README.md) \| [PDF](lecture_24/Notes_24.05/notes.pdf) \| [Notebook](lecture_24/Notes_24.05/lecture_24_05.ipynb) |
| **24.06** | Fixing Underfit & Overfit | Engineering playbook: Regularization, feature pruning, polynomial expansion | [Notes](lecture_24/Notes_24.06/README.md) \| [PDF](lecture_24/Notes_24.06/notes.pdf) \| [Notebook](lecture_24/Notes_24.06/lecture_24_06.ipynb) |
| **24.07** | Diagnostic Learning Curves | Training size $m$ vs loss curves, plateau analysis, cross-validation diagnostics | [Notes](lecture_24/Notes_24.07/README.md) \| [PDF](lecture_24/Notes_24.07/notes.pdf) \| [Notebook](lecture_24/Notes_24.07/lecture_24_07.ipynb) |
| **24.08** | Regularization: Lasso (L1) | $J = MSE + \lambda \|\mathbf{w}\|_1$, geometric diamond constraint, automatic sparsity | [Notes](lecture_24/Notes_24.08/README.md) \| [PDF](lecture_24/Notes_24.08/notes.pdf) \| [Notebook](lecture_24/Notes_24.08/lecture_24_08.ipynb) |
| **24.09** | Regularization: Ridge (L2) | $J = MSE + \frac{\lambda}{2} \|\mathbf{w}\|_2^2$, Normal Equation $(\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^T \mathbf{y}$ | [Notes](lecture_24/Notes_24.09/README.md) \| [PDF](lecture_24/Notes_24.09/notes.pdf) \| [Notebook](lecture_24/Notes_24.09/lecture_24_09.ipynb) |
| **24.10** | Lasso Implementation & Paths | Hands-on `insurance.csv`, tracing coefficient shrinkage paths across $\alpha$ | [Notes](lecture_24/Notes_24.10/README.md) \| [PDF](lecture_24/Notes_24.10/notes.pdf) \| [Notebook](lecture_24/Notes_24.10/lecture_24_10.ipynb) |
| **24.11** | Using LassoCV | K-Fold cross-validated hyperparameter search for optimal regularizer $\alpha^*$ | [Notes](lecture_24/Notes_24.11/README.md) \| [PDF](lecture_24/Notes_24.11/notes.pdf) \| [Notebook](lecture_24/Notes_24.11/lecture_24_11.ipynb) |
| **24.12** | ElasticNet Overview | Hybrid convex combination $MSE + \alpha [\rho \|\mathbf{w}\|_1 + \frac{1-\rho}{2} \|\mathbf{w}\|_2^2]$, grouping effect | [Notes](lecture_24/Notes_24.12/README.md) \| [PDF](lecture_24/Notes_24.12/notes.pdf) \| [Notebook](lecture_24/Notes_24.12/lecture_24_12.ipynb) |
| **24.13** | Logistic Regression Intuition | Odds $\frac{p}{1-p}$, Logit $\ln(\text{Odds})$, Sigmoid function $\sigma(z) = \frac{1}{1 + e^{-z}}$ | [Notes](lecture_24/Notes_24.13/README.md) \| [PDF](lecture_24/Notes_24.13/notes.pdf) \| [Notebook](lecture_24/Notes_24.13/lecture_24_13.ipynb) |
| **24.14** | Logistic Regression Cost Function | MLE derivation of Binary Cross-Entropy $J = -\frac{1}{m} \sum [y \ln \hat{y} + (1-y) \ln(1-\hat{y})]$ | [Notes](lecture_24/Notes_24.14/README.md) \| [PDF](lecture_24/Notes_24.14/notes.pdf) \| [Notebook](lecture_24/Notes_24.14/lecture_24_14.ipynb) |
| **24.15** | Classification Code & Metrics | Clinical `heart.csv` pipeline, Confusion Matrix, Precision, Recall, F1, ROC-AUC | [Notes](lecture_24/Notes_24.15/README.md) \| [PDF](lecture_24/Notes_24.15/notes.pdf) \| [Notebook](lecture_24/Notes_24.15/lecture_24_15.ipynb) |

> [!TIP]
> **🧪 Day 24 Comprehensive Case Studies & Practice Problem Set:**  
> *Module Guides:* [📖 English Guide](lecture_24/Practice_Problems/README.md) | [हिंदी / Hinglish Guide](lecture_24/Practice_Problems/README_HINGLISH.md)  
> - 📝 **Problem Statements:** [Questions](lecture_24/Practice_Problems/Questions/README.md) | [questions.pdf](lecture_24/Practice_Problems/Questions/questions.pdf) | [Starter Notebook](lecture_24/Practice_Problems/Questions/lecture_24_questions.ipynb)
> - 💡 **Complete Solutions:** [Solutions](lecture_24/Practice_Problems/Solutions/README.md) | [solutions.pdf](lecture_24/Practice_Problems/Solutions/solutions.pdf) | [Executed Notebook](lecture_24/Practice_Problems/Solutions/lecture_24_solutions.ipynb)

---

## 📐 Mathematical Formulations & Statistical Expressions

The mathematical formulations across these visualization modules adhere to formal academic and textbook definitions:

### 1. Data-Ink Principle (Tufte Formulation)
The efficiency of a visual graphic is formally measured by the **Data-Ink Ratio** $\eta$:

$$
\boxed{
\eta = \frac{\mathcal{I}_{\text{data}}}{\mathcal{I}_{\text{total}}} = 1.0 - \frac{\mathcal{I}_{\text{non-data}}}{\mathcal{I}_{\text{total}}}
}
$$

where $\mathcal{I}_{\text{data}}$ represents informative data-ink, $\mathcal{I}_{\text{total}}$ represents total graphic ink, and $\eta \in (0, 1]$.

---

### 2. Grouped Bar Clustered Coordinate Mathematics
For $K = 2$ comparative series across $N$ discrete categories with bar width constraint $w < \frac{1}{K} = 0.5$:

Let the baseline category coordinate be $x_i = i$ for $i \in \{0, 1, \dots, N-1\}$. The shifted bar coordinates $(y_{1, i}, y_{2, i})$ follow the symmetric piecewise system:

$$
\begin{cases}
y_{1, i} = x_i - \dfrac{w}{2} \\
y_{2, i} = x_i + \dfrac{w}{2}
\end{cases}
$$

where $y_{1, i}$ denotes the center coordinate for Series 1 (Budget) and $y_{2, i}$ denotes the center coordinate for Series 2 (Spend).

The category label tick mark $t_i$ satisfies the central symmetry theorem:

$$
\boxed{t_i = \frac{y_{1, i} + y_{2, i}}{2} = x_i}
$$

---

### 3. Tukey's Five-Number Summary & Box Plot Outlier Fences
Given an ordered sample $\mathcal{D} = \{x_{(1)}, x_{(2)}, \dots, x_{(n)}\}$, the Interquartile Range ($\text{IQR}$) and whisker fences are defined as:

$$
\boxed{\text{IQR} = Q_3 - Q_1}
$$

$$
\boxed{F_L = Q_1 - 1.5 \cdot \text{IQR} \qquad\text{and}\qquad F_U = Q_3 + 1.5 \cdot \text{IQR}}
$$

$$
\boxed{\mathcal{O} = \left\{ x_i \in \mathcal{D} \;\middle|\; x_i < F_L \;\lor\; x_i > F_U \right\}}
$$

---

### 4. Histogram Bin Estimation Models
For continuous feature distribution partitioning:

- **Sturges' Rule** (Normal distributions):

$$
  k = \left\lceil 1 + \log_2(n) \right\rceil
$$

- **Freedman-Diaconis Rule** (Robust against outliers):

$$
  h = 2 \cdot \frac{\text{IQR}}{\sqrt[3]{n}}, \qquad k = \left\lceil \frac{\max(x) - \min(x)}{h} \right\rceil
$$

Where $n$ is total sample count, $h$ is optimal bin width, and $k$ is the total bin count.

---

## 🗺️ 60-Day Curriculum Roadmap

The repository is structured to take a learner from foundational mathematics and Python programming to cutting-edge AI architectures and real-world deployment:

```mermaid
flowchart LR
    A["Lectures 01-15<br/>Python & Math Foundations"] --> B["Lectures 16-25<br/>Data Analysis & Visualization"]
    B --> C["Lectures 26-40<br/>Classical Machine Learning"]
    C --> D["Lectures 41-52<br/>Deep Learning & Computer Vision"]
    D --> E["Lectures 53-60<br/>NLP, LLMs & MLOps Deployment"]
```

- **Lectures 01 – 15**: Python Programming, Linear Algebra, Calculus, NumPy, and Data Manipulation.
- **Lectures 16 – 25**: Exploratory Data Analysis (EDA), Advanced Pandas, Matplotlib, Seaborn, Feature Engineering.
- **Lectures 26 – 40**: Supervised & Unsupervised Machine Learning (Linear/Logistic Regression, Decision Trees, Random Forests, XGBoost, Clustering, PCA).
- **Lectures 41 – 52**: Deep Learning Foundations (Neural Networks, Backpropagation, PyTorch/TensorFlow, CNNs, Transfer Learning).
- **Lectures 53 – 60**: Natural Language Processing (RNNs, Transformers, Attention Mechanism, LLM Fine-Tuning, MLOps, CI/CD & Model Deployment).

---

## ⚡ Quickstart & Setup Guide

### 1. Clone the Repository
```bash
git clone https://github.com/S1h2i3v4a/AI_ML.git
cd AI_ML
```

### 2. Environment Setup
Create and activate an isolated virtual environment:
```bash
# Using conda
conda create -n aiml python=3.10 -y
conda activate aiml

# Or using venv
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install numpy pandas matplotlib seaborn jupyter jupyterlab scipy scikit-learn
```

### 4. Launch Jupyter Lab
```bash
jupyter lab
```
Navigate to any lecture subfolder (e.g., `lecture_18/Notes_18.4/lecture_18_4.ipynb`) and run the interactive cells.

---

## 📜 Standards & Integrity

- **Original Illustrations**: All diagrams and schematics are custom-engineered in code to guarantee mathematical accuracy and eliminate third-party copyright concerns.
- **Reproducible Code**: Every notebook contains deterministic seed declarations where applicable and verified imports.
- **Dual Format Documentation**: High-resolution vector PDFs are accompanied by full Markdown notes for both quick reading and offline archival.

---

## 👤 Author & Maintainer
- **Shivam Keshari**
- GitHub: [@S1h2i3v4a](https://github.com/S1h2i3v4a)
- Repository: [AI_ML](https://github.com/S1h2i3v4a/AI_ML)
