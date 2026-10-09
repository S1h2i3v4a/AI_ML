# 🧠 AI & Machine Learning Masterclass (Hinglish)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Viz-4c72b0.svg)](https://seaborn.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Actively%20Maintained-success.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish**

Yeh repository complete **Artificial Intelligence & Machine Learning Journey (Lectures 00 se 60)** ka structured, organized aur production-grade study hub hai.

Har lecture module ke andar aapko milenge:
- 📝 **Structured Markdown Notes (`notes.md`)**: Complete theory, real-world examples, syntax breakdowns aur best practices.
- 📕 **High-Definition PDFs (`notes.pdf`)**: Offline study ke liye formatted PDFs jisme KaTeX formulas, tables aur diagrams embedded hain.
- 💻 **Hands-On Jupyter Notebooks (`.ipynb`)**: Self-contained, runnable Python code jise aap directly execute karke practice kar sakte hain.
- 📊 **Original Visuals & Custom Diagrams**: Code-generated clean diagrams bina kisi copyright issue ke.

---

## 📂 Repository Architecture (Folder Structure)

```plaintext
AI-ML/
├── .gitignore
├── README.md                     # English Documentation
├── README_HINGLISH.md            # Hinglish Documentation
├── lecture_00/                   # Course Orientation & Environment Setup
├── lecture_01/ ... lecture_17/   # (Foundations, Python & Numerical Computing)
├── lecture_18/                   # Data Visualization (Part 1 - Matplotlib Fundamentals)
│   ├── Notes_18.01/ to 18.18/    # Sub-topics (notes.md, notes.pdf, .ipynb)
│   ├── Practice_Problems/        # Case Studies & Challenges (Questions & Solutions)
│   │   ├── Questions/            # questions.md, questions.pdf, questions.ipynb
│   │   └── Solutions/            # solutions.md, solutions.pdf, solutions.ipynb
│   └── reference_materials/      # Cheatsheets & references
├── lecture_19/                   # Data Visualization (Part 2 - Advanced Matplotlib & Seaborn)
│   ├── Notes_19.01/ to 19.16/    # Sub-topics (notes.md, notes.pdf, .ipynb, diagrams)
├── lecture_20/                   # Mathematics for AI (Part 1 - Probability Theory)
│   ├── Notes_20.01/ to 20.20/    # Sub-topics (README_HINGLISH.md, notes.pdf, .ipynb)
│   └── Practice_Problems/        # Industry Case Studies (Questions & Solutions)
├── lecture_21/                   # Mathematics for AI (Part 2 - Linear Algebra Mastery)
│   ├── Notes_21.01/ to 21.15/    # Sub-topics (README_HINGLISH.md, notes.pdf, .ipynb)
│   └── Practice_Problems/        # Industry Case Studies (Questions & Solutions)
├── lecture_22/                   # Mathematics for AI (Part 3 - Calculus Mastery)
│   ├── Notes_22.01/ to 22.09/    # Sub-topics (README_HINGLISH.md, notes.pdf, .ipynb)
│   └── Practice_Problems/        # Industry Case Studies (Questions & Solutions)
└── lecture_23/ ... lecture_60/   # (Machine Learning, Deep Learning, NLP & Deployment)
```

---

## 📊 Detailed Module Breakdown

### 🎨 Day 18: Data Visualization (Part 1 — Matplotlib Mastery)
*Module Guides:* [📖 Hinglish Guide](lecture_18/README_HINGLISH.md) \| [English Guide](lecture_18/README.md)

Data visualization theory, visual perception, aur **Matplotlib** ke saath core 2D plotting par focused module.

| Lecture | Topic Title | Core Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **18.01** | What is Data Visualization? | Visual perception, exploratory vs explanatory viz, Anscombe's Quartet | [Notes](lecture_18/Notes_18.01/README.md) \| [PDF](lecture_18/Notes_18.01/notes.pdf) \| [Notebook](lecture_18/Notes_18.01/lecture_18_01.ipynb) |
| **18.02** | How to Plot Data - Basic Structure | Coordinate systems, Data Prep $\to$ Canvas $\to$ Plot $\to$ Decoration $\to$ Render | [Notes](lecture_18/Notes_18.02/README.md) \| [PDF](lecture_18/Notes_18.02/notes.pdf) \| [Notebook](lecture_18/Notes_18.02/lecture_18_02.ipynb) |
| **18.03** | Introduction to Matplotlib | Matplotlib history, architecture (`backend`, `artist`, `scripting`), Pyplot interface | [Notes](lecture_18/Notes_18.03/README.md) \| [PDF](lecture_18/Notes_18.03/notes.pdf) \| [Notebook](lecture_18/Notes_18.03/lecture_18_03.ipynb) |
| **18.04** | Important Plot Methods | `plt.plot()`, `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.grid()`, `plt.show()` | [Notes](lecture_18/Notes_18.04/README.md) \| [PDF](lecture_18/Notes_18.04/notes.pdf) \| [Notebook](lecture_18/Notes_18.04/lecture_18_04.ipynb) |
| **18.05** | Multiple Datasets on Line Plot | Ek canvas par multiple lines plot karna, legends (`plt.legend`), color aur z-order | [Notes](lecture_18/Notes_18.05/README.md) \| [PDF](lecture_18/Notes_18.05/notes.pdf) \| [Notebook](lecture_18/Notes_18.05/lecture_18_05.ipynb) |
| **18.06** | Format Strings (`fmt`) | Fast syntax `[marker][line][color]`, jaise `'ro--'`, `'b^:'`, hex colors | [Notes](lecture_18/Notes_18.06/README.md) \| [PDF](lecture_18/Notes_18.06/notes.pdf) \| [Notebook](lecture_18/Notes_18.06/lecture_18_06.ipynb) |
| **18.07** | Styling & Saving Plots | Figure sizing (`figsize`), DPI scaling, `plt.savefig()` (PNG, SVG, PDF), themes | [Notes](lecture_18/Notes_18.07/README.md) \| [PDF](lecture_18/Notes_18.07/notes.pdf) \| [Notebook](lecture_18/Notes_18.07/lecture_18_07.ipynb) |
| **18.08** | Chart Selection Taxonomy | Sahi chart choose karna: Comparison, Distribution, Composition, Relationship | [Notes](lecture_18/Notes_18.08/README.md) \| [PDF](lecture_18/Notes_18.08/notes.pdf) \| [Notebook](lecture_18/Notes_18.08/lecture_18_08.ipynb) |
| **18.09** | Vertical Bar Charts (`plt.bar`) | Discrete categorical comparison, bar width, alignment, edge styling | [Notes](lecture_18/Notes_18.09/README.md) \| [PDF](lecture_18/Notes_18.09/notes.pdf) \| [Notebook](lecture_18/Notes_18.09/lecture_18_09.ipynb) |
| **18.10** | Adding Labels to Bars | Bars ke upar exact numbers likhna: `plt.text()` aur `ax.bar_label()` | [Notes](lecture_18/Notes_18.10/README.md) \| [PDF](lecture_18/Notes_18.10/notes.pdf) \| [Notebook](lecture_18/Notes_18.10/lecture_18_10.ipynb) |
| **18.11** | Grouped Bar Charts | Side-by-side comparative bars, NumPy index offset math (`np.arange()`) | [Notes](lecture_18/Notes_18.11/README.md) \| [PDF](lecture_18/Notes_18.11/notes.pdf) \| [Notebook](lecture_18/Notes_18.11/lecture_18_11.ipynb) |
| **18.12** | Horizontal Bar Charts (`plt.barh`) | Lambe label names ke liye horizontal bars, axis sorting & inversion | [Notes](lecture_18/Notes_18.12/README.md) \| [PDF](lecture_18/Notes_18.12/notes.pdf) \| [Notebook](lecture_18/Notes_18.12/lecture_18_12.ipynb) |
| **18.13** | Scatter Plots (`plt.scatter`) | Do continuous variables ke beech correlation aur bivariate relationship | [Notes](lecture_18/Notes_18.13/README.md) \| [PDF](lecture_18/Notes_18.13/notes.pdf) \| [Notebook](lecture_18/Notes_18.13/lecture_18_13.ipynb) |
| **18.14** | Advanced Scatter Customizations | 4D visual encoding: Marker size (`s`), colormap (`c`, `cmap`), alpha transparency | [Notes](lecture_18/Notes_18.14/README.md) \| [PDF](lecture_18/Notes_18.14/notes.pdf) \| [Notebook](lecture_18/Notes_18.14/lecture_18_14.ipynb) |
| **18.15** | Annotations on Scatter Plots | Specific points par callouts/arrows lagana (`plt.annotate`, `arrowprops`, `bbox`) | [Notes](lecture_18/Notes_18.15/README.md) \| [PDF](lecture_18/Notes_18.15/notes.pdf) \| [Notebook](lecture_18/Notes_18.15/lecture_18_15.ipynb) |
| **18.16** | Multiple Datasets on Scatter Plots | Multi-class categories ko alag-alag color aur marker se represent karna | [Notes](lecture_18/Notes_18.16/README.md) \| [PDF](lecture_18/Notes_18.16/notes.pdf) \| [Notebook](lecture_18/Notes_18.16/lecture_18_16.ipynb) |
| **18.17** | Pie Charts (`plt.pie`) | Part-to-whole composition, `autopct`, `startangle`, shadow, aur use cases | [Notes](lecture_18/Notes_18.17/README.md) \| [PDF](lecture_18/Notes_18.17/notes.pdf) \| [Notebook](lecture_18/Notes_18.17/lecture_18_17.ipynb) |
| **18.18** | Advanced Pie Charts | Donut charts (center hollow circle), `explode` slices, custom palettes | [Notes](lecture_18/Notes_18.18/README.md) \| [PDF](lecture_18/Notes_18.18/notes.pdf) \| [Notebook](lecture_18/Notes_18.18/lecture_18_18.ipynb) |

> [!TIP]
> **🧪 Day 18 Comprehensive Case Studies & Practice Problem Set:**  
> *Module Guides:* [📖 Hinglish Guide](lecture_18/Practice_Problems/README_HINGLISH.md) \| [English Guide](lecture_18/Practice_Problems/README.md)  
> - 📝 **Problem Statements:** [Questions](lecture_18/Practice_Problems/Questions/README.md) \| [questions.pdf](lecture_18/Practice_Problems/Questions/questions.pdf) \| [Starter Notebook](lecture_18/Practice_Problems/Questions/questions.ipynb)
> - 💡 **Complete Solutions:** [Solutions](lecture_18/Practice_Problems/Solutions/README.md) \| [solutions.pdf](lecture_18/Practice_Problems/Solutions/solutions.pdf) \| [Executed Notebook](lecture_18/Practice_Problems/Solutions/solutions.ipynb)

---

### 📈 Day 19: Data Visualization (Part 2 — Advanced Matplotlib & Seaborn)
*Module Guides:* [📖 Hinglish Guide](lecture_19/README_HINGLISH.md) \| [English Guide](lecture_19/README.md)

Statistical distributions, Five-Number Summary, Modern Object-Oriented Matplotlib API, aur high-level **Seaborn** statistical graphics.

| Lecture | Topic Title | Core Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **19.01** | Histograms (`plt.hist`) | Continuous distribution, bin count & width, density normalization, skewness | [Notes](lecture_19/Notes_19.01/README.md) \| [PDF](lecture_19/Notes_19.01/notes.pdf) \| [Notebook](lecture_19/Notes_19.01/lecture_19_01.ipynb) |
| **19.02** | Multiple Datasets on Histogram | Side-by-side vs stacked histograms, overlapping distributions with alpha | [Notes](lecture_19/Notes_19.02/README.md) \| [PDF](lecture_19/Notes_19.02/notes.pdf) \| [Notebook](lecture_19/Notes_19.02/lecture_19_02.ipynb) |
| **19.03** | Vertical Reference Lines (`plt.axvline`) | Mean, Median, Mode benchmarks aur threshold lines plot karna | [Notes](lecture_19/Notes_19.03/README.md) \| [PDF](lecture_19/Notes_19.03/notes.pdf) \| [Notebook](lecture_19/Notes_19.03/lecture_19_03.ipynb) |
| **19.04** | Box Plots (Five-Number Summary) | Tukey's 5-number summary ($Q_1, Q_2, Q_3, \text{IQR}$), $1.5 \times \text{IQR}$ outlier detection | [Notes](lecture_19/Notes_19.04/README.md) \| [PDF](lecture_19/Notes_19.04/notes.pdf) \| [Notebook](lecture_19/Notes_19.04/lecture_19_04.ipynb) |
| **19.05** | Advanced Box Plot Operations | Notched box plots (median confidence), horizontal orientation, custom fliers | [Notes](lecture_19/Notes_19.05/README.md) \| [PDF](lecture_19/Notes_19.05/notes.pdf) \| [Notebook](lecture_19/Notes_19.05/lecture_19_05.ipynb) |
| **19.06** | Stack Plots (Area Charts) | Time ke sath cumulative part-to-whole trends (`plt.stackplot`) | [Notes](lecture_19/Notes_19.06/README.md) \| [PDF](lecture_19/Notes_19.06/notes.pdf) \| [Notebook](lecture_19/Notes_19.06/lecture_19_06.ipynb) |
| **19.07** | Subplots in Matplotlib | Multi-panel figures via `plt.subplot()` and `plt.subplots()`, `tight_layout()` | [Notes](lecture_19/Notes_19.07/README.md) \| [PDF](lecture_19/Notes_19.07/notes.pdf) \| [Notebook](lecture_19/Notes_19.07/lecture_19_07.ipynb) |
| **19.08** | Modern Matplotlib (Object-Oriented API) | Explicit `fig, ax = plt.subplots()`, axis methods (`ax.set_*()`), production code | [Notes](lecture_19/Notes_19.08/README.md) \| [PDF](lecture_19/Notes_19.08/notes.pdf) \| [Notebook](lecture_19/Notes_19.08/lecture_19_08.ipynb) |
| **19.09** | Practice Task: Weekly Weather Analysis | Multi-axis dual plotting ($Y_1$ temperature line, $Y_2$ precipitation bars) | [Notes](lecture_19/Notes_19.09/README.md) \| [PDF](lecture_19/Notes_19.09/notes.pdf) \| [Notebook](lecture_19/Notes_19.09/lecture_19_09.ipynb) |
| **19.10** | Introduction to Seaborn | High-level statistical visualization library, themes (`darkgrid`, `whitegrid`) | [Notes](lecture_19/Notes_19.10/README.md) \| [PDF](lecture_19/Notes_19.10/notes.pdf) \| [Notebook](lecture_19/Notes_19.10/lecture_19_10.ipynb) |
| **19.11** | Creating Plots with Seaborn | Semantic mapping attributes: `x`, `y`, `hue`, `style`, `size`, `palette` | [Notes](lecture_19/Notes_19.11/README.md) \| [PDF](lecture_19/Notes_19.11/notes.pdf) \| [Notebook](lecture_19/Notes_19.11/lecture_19_11.ipynb) |
| **19.12** | Relational Plots in Seaborn | Figure-level `sns.relplot()`, `sns.scatterplot()`, `sns.lineplot()`, faceting | [Notes](lecture_19/Notes_19.12/README.md) \| [PDF](lecture_19/Notes_19.12/notes.pdf) \| [Notebook](lecture_19/Notes_19.12/lecture_19_12.ipynb) |
| **19.13** | Categorical Plots in Seaborn | Figure-level `sns.catplot()`, `sns.barplot()` with CI, `sns.boxplot()`, `violinplot` | [Notes](lecture_19/Notes_19.13/README.md) \| [PDF](lecture_19/Notes_19.13/notes.pdf) \| [Notebook](lecture_19/Notes_19.13/lecture_19_13.ipynb) |
| **19.14** | Distribution Plots in Seaborn | Figure-level `sns.displot()`, Kernel Density (`kdeplot`), `histplot`, `rugplot` | [Notes](lecture_19/Notes_19.14/README.md) \| [PDF](lecture_19/Notes_19.14/notes.pdf) \| [Notebook](lecture_19/Notes_19.14/lecture_19_14.ipynb) |
| **19.15** | Relational & Matrix Plots: Heatmaps | `sns.heatmap()`, correlation matrix (`df.corr()`), `annot=True`, color maps | [Notes](lecture_19/Notes_19.15/README.md) \| [PDF](lecture_19/Notes_19.15/notes.pdf) \| [Notebook](lecture_19/Notes_19.15/lecture_19_15.ipynb) |
| **19.16** | Best Practices for Data Visualization | Edward Tufte principles (Data-Ink ratio, chartjunk), color accessibility, ethics | [Notes](lecture_19/Notes_19.16/README.md) \| [PDF](lecture_19/Notes_19.16/notes.pdf) \| [Notebook](lecture_19/Notes_19.16/lecture_19_16.ipynb) |


> [!TIP]
> **🧪 Day 19 Comprehensive Case Studies & Practice Problem Set:**  
> *Module Guides:* [📖 Hinglish Guide](lecture_19/Practice_Problems/README_HINGLISH.md) \| [English Guide](lecture_19/Practice_Problems/README.md)  
> - 📝 **Problem Statements:** [Questions](lecture_19/Practice_Problems/Questions/README.md) \| [questions.pdf](lecture_19/Practice_Problems/Questions/questions.pdf) \| [Starter Notebook](lecture_19/Practice_Problems/Questions/questions.ipynb)
> - 💡 **Complete Solutions:** [Solutions](lecture_19/Practice_Problems/Solutions/README.md) \| [solutions.pdf](lecture_19/Practice_Problems/Solutions/solutions.pdf) \| [Executed Notebook](lecture_19/Practice_Problems/Solutions/solutions.ipynb)

### 🎲 Day 20: Mathematics for AI (Part 1 — Probability Theory) [Hinglish]
*Module Guides:* [📖 Hinglish Guide](lecture_20/README_HINGLISH.md) | [English Guide](lecture_20/README.md)

Artificial Intelligence aur Machine Learning ke liye Probability Theory ka mathematical foundation: Kolmogorov axioms, conditional probability, Bayes' Theorem, random variables, expectation, variance, aur parametric distributions (Binomial, Uniform, Gaussian).

| Lecture | Topic Title | Core Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **20.01** | Math for AI & Why Probability Matters | Uncertainty quantification, MLE, cross-entropy, generative modeling | [Notes](lecture_20/Notes_20.01/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.01/notes.pdf) \| [Notebook](lecture_20/Notes_20.01/lecture_20_01.ipynb) |
| **20.02** | Core Foundations of Probability | Random experiments, sample space, events, Kolmogorov ke 3 axioms | [Notes](lecture_20/Notes_20.02/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.02/notes.pdf) \| [Notebook](lecture_20/Notes_20.02/lecture_20_02.ipynb) |
| **20.03** | Classical vs. Empirical Probability | Theoretical symmetry, frequentist relative frequency, Law of Large Numbers | [Notes](lecture_20/Notes_20.03/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.03/notes.pdf) \| [Notebook](lecture_20/Notes_20.03/lecture_20_03.ipynb) |
| **20.04** | Foundation Probability Practice Problems | Combinatorics, permutations $P(n,k)$, combinations $C(n,k)$, counting rules | [Notes](lecture_20/Notes_20.04/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.04/notes.pdf) \| [Notebook](lecture_20/Notes_20.04/lecture_20_04.ipynb) |
| **20.05** | Types of Events | Mutually exclusive vs independent events, exhaustive events, partitions | [Notes](lecture_20/Notes_20.05/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.05/notes.pdf) \| [Notebook](lecture_20/Notes_20.05/lecture_20_05.ipynb) |
| **20.06** | The Complementary Rule | Complement $P(A') = 1 - P(A)$, De Morgan's laws, at-least-one calculations | [Notes](lecture_20/Notes_20.06/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.06/notes.pdf) \| [Notebook](lecture_20/Notes_20.06/lecture_20_06.ipynb) |
| **20.07** | The Addition Rule of Probability | General addition rule, double-counting correction, inclusion-exclusion | [Notes](lecture_20/Notes_20.07/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.07/notes.pdf) \| [Notebook](lecture_20/Notes_20.07/lecture_20_07.ipynb) |
| **20.08** | The Multiplication Rule of Probability | Joint intersection, dependent vs independent, probability chain rule | [Notes](lecture_20/Notes_20.08/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.08/notes.pdf) \| [Notebook](lecture_20/Notes_20.08/lecture_20_08.ipynb) |
| **20.09** | Probability Rules Practice Problems | Series vs parallel system reliability, fault tolerance, urn problems | [Notes](lecture_20/Notes_20.09/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.09/notes.pdf) \| [Notebook](lecture_20/Notes_20.09/lecture_20_09.ipynb) |
| **20.10** | Conditional Probability | Reduced sample space, $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$, contingency tables | [Notes](lecture_20/Notes_20.10/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.10/notes.pdf) \| [Notebook](lecture_20/Notes_20.10/lecture_20_10.ipynb) |
| **20.11** | The Law of Total Probability | Sample space partition, marginalization, total defect calculations | [Notes](lecture_20/Notes_20.11/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.11/notes.pdf) \| [Notebook](lecture_20/Notes_20.11/lecture_20_11.ipynb) |
| **20.12** | Bayes' Theorem | Prior, likelihood, marginal evidence, posterior belief updating | [Notes](lecture_20/Notes_20.12/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.12/notes.pdf) \| [Notebook](lecture_20/Notes_20.12/lecture_20_12.ipynb) |
| **20.13** | Bayes' Theorem Practice Problems | Medical diagnosis paradox, base rate fallacy, false positives in AI | [Notes](lecture_20/Notes_20.13/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.13/notes.pdf) \| [Notebook](lecture_20/Notes_20.13/lecture_20_13.ipynb) |
| **20.14** | Random Variables | Mapping $X: \mathcal{S} \to \mathbb{R}$, discrete vs continuous, PMF, PDF, CDF | [Notes](lecture_20/Notes_20.14/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.14/notes.pdf) \| [Notebook](lecture_20/Notes_20.14/lecture_20_14.ipynb) |
| **20.15** | Mean, Median & Mode | Expected value $\mathbb{E}[X]$, linearity of expectation, skewness impact | [Notes](lecture_20/Notes_20.15/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.15/notes.pdf) \| [Notebook](lecture_20/Notes_20.15/lecture_20_15.ipynb) |
| **20.16** | Variance & Standard Deviation | Dispersion $\text{Var}(X) = \mathbb{E}[(X-\mu)^2]$, shortcut $\mathbb{E}[X^2] - (\mathbb{E}[X])^2$ | [Notes](lecture_20/Notes_20.16/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.16/notes.pdf) \| [Notebook](lecture_20/Notes_20.16/lecture_20_16.ipynb) |
| **20.17** | Probability Distributions & its Types | Discrete vs continuous families, PMF/PDF properties, AI loss mapping | [Notes](lecture_20/Notes_20.17/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.17/notes.pdf) \| [Notebook](lecture_20/Notes_20.17/lecture_20_17.ipynb) |
| **20.18** | Binomial Distribution | Bernoulli trials, PMF $\binom{n}{k} p^k (1-p)^{n-k}$, mean $np$, variance $np(1-p)$ | [Notes](lecture_20/Notes_20.18/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.18/notes.pdf) \| [Notebook](lecture_20/Notes_20.18/lecture_20_18.ipynb) |
| **20.19** | Uniform Distribution | Constant density $\mathcal{U}(a, b)$, PDF $\frac{1}{b-a}$, mean $\frac{a+b}{2}$, variance $\frac{(b-a)^2}{12}$ | [Notes](lecture_20/Notes_20.19/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.19/notes.pdf) \| [Notebook](lecture_20/Notes_20.19/lecture_20_19.ipynb) |
| **20.20** | Normal Distribution | Bell curve PDF, 68-95-99.7 rule, Z-score standardization, CLT connection | [Notes](lecture_20/Notes_20.20/README_HINGLISH.md) \| [PDF](lecture_20/Notes_20.20/notes.pdf) \| [Notebook](lecture_20/Notes_20.20/lecture_20_20.ipynb) |


> [!TIP]
> **🧪 Day 20 Comprehensive Case Studies & Practice Problem Set:**  
> *Module Guides:* [📖 Hinglish Guide](lecture_20/Practice_Problems/README_HINGLISH.md) | [English Guide](lecture_20/Practice_Problems/README.md)  
> - 📝 **Problem Statements:** [Questions](lecture_20/Practice_Problems/Questions/README.md) | [questions.pdf](lecture_20/Practice_Problems/Questions/questions.pdf) | [Starter Notebook](lecture_20/Practice_Problems/Questions/questions.ipynb)
> - 💡 **Complete Solutions:** [Solutions](lecture_20/Practice_Problems/Solutions/README.md) | [solutions.pdf](lecture_20/Practice_Problems/Solutions/solutions.pdf) | [Executed Notebook](lecture_20/Practice_Problems/Solutions/solutions.ipynb)

### 📐 Day 21: Mathematics for AI (Part 2 — Linear Algebra Mastery) [Hinglish]
*Module Guides:* [📖 Hinglish Guide](lecture_21/README_HINGLISH.md) | [English Guide](lecture_21/README.md)

Artificial Intelligence, Machine Learning aur Deep Learning ke liye Linear Algebra ka complete mathematical foundation: Vectors, matrices, tensors, inner products, norms, span, basis, rank, determinants, Gaussian elimination, Moore-Penrose pseudo-inverses, Gram-Schmidt orthogonalization, QR decomposition, eigenvalues, eigenvectors, symmetric spectral theorem, Singular Value Decomposition (SVD), PCA, aur Deep Learning attention mechanisms (LoRA).

| Lecture | Topic Title | Core Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **21.01** | Vectors, Scalars, Matrices & Tensors | Tensor rank hierarchy (0D se 4D), row/column vectors, batch tensors | [Notes](lecture_21/Notes_21.01/README_HINGLISH.md) \| [PDF](lecture_21/Notes_21.01/notes.pdf) \| [Notebook](lecture_21/Notes_21.01/lecture_21_01.ipynb) |
| **21.02** | Vector Operations & Geometric Intuition | Vector addition, scalar multiplication, $\ell_1$ & $\ell_2$ norms, cosine similarity | [Notes](lecture_21/Notes_21.02/README_HINGLISH.md) \| [PDF](lecture_21/Notes_21.02/notes.pdf) \| [Notebook](lecture_21/Notes_21.02/lecture_21_02.ipynb) |
| **21.03** | Matrix Operations & Special Matrices | Addition, scaling, transposes, symmetric, diagonal, identity, orthogonal matrices | [Notes](lecture_21/Notes_21.03/README_HINGLISH.md) \| [PDF](lecture_21/Notes_21.03/notes.pdf) \| [Notebook](lecture_21/Notes_21.03/lecture_21_03.ipynb) |
| **21.04** | Matrix Multiplication & AI Forward Passes | Dot products vs outer products, linear composition, batch gemm $\mathcal{O}(mnp)$ | [Notes](lecture_21/Notes_21.04/README_HINGLISH.md) \| [PDF](lecture_21/Notes_21.04/notes.pdf) \| [Notebook](lecture_21/Notes_21.04/lecture_21_04.ipynb) |
| **21.05** | Linear Combinations, Span & Basis | Linear combinations, span subspaces, linear independence, canonical basis | [Notes](lecture_21/Notes_21.05/README_HINGLISH.md) \| [PDF](lecture_21/Notes_21.05/notes.pdf) \| [Notebook](lecture_21/Notes_21.05/lecture_21_05.ipynb) |
| **21.06** | Linear Independence & Matrix Rank | Row/column rank, rank-nullity theorem, full rank vs rank deficiency | [Notes](lecture_21/Notes_21.06/README_HINGLISH.md) \| [PDF](lecture_21/Notes_21.06/notes.pdf) \| [Notebook](lecture_21/Notes_21.06/lecture_21_06.ipynb) |
| **21.07** | Determinants & Geometric Singularity | Oriented volume scaling, Laplace expansion, invertibility criterion $\det(A) \ne 0$ | [Notes](lecture_21/Notes_21.07/README_HINGLISH.md) \| [PDF](lecture_21/Notes_21.07/notes.pdf) \| [Notebook](lecture_21/Notes_21.07/lecture_21_07.ipynb) |
| **21.08** | Systems of Linear Equations & Gaussian Elimination | Augmented matrix, forward elimination, back-substitution, REF & RREF | [Notes](lecture_21/Notes_21.08/README_HINGLISH.md) \| [PDF](lecture_21/Notes_21.08/notes.pdf) \| [Notebook](lecture_21/Notes_21.08/lecture_21_08.ipynb) |
| **21.09** | Matrix Inverses & Moore-Penrose Pseudo-Inverse | Gauss-Jordan inversion, overdetermined systems, pseudo-inverse $A^+$, Least Squares | [Notes](lecture_21/Notes_21.09/README_HINGLISH.md) \| [PDF](lecture_21/Notes_21.09/notes.pdf) \| [Notebook](lecture_21/Notes_21.09/lecture_21_09.ipynb) |
| **21.10** | Orthogonality, Orthonormality & Projections | Orthogonal projections, Gram-Schmidt orthogonalization, QR decomposition | [Notes](lecture_21/Notes_21.10/README_HINGLISH.md) \| [PDF](lecture_21/Notes_21.10/notes.pdf) \| [Notebook](lecture_21/Notes_21.10/lecture_21_10.ipynb) |
| **21.11** | Eigenvalues & Eigenvectors | Invariant directions, characteristic equation $\det(A - \lambda I) = 0$, eigenspaces | [Notes](lecture_21/Notes_21.11/README_HINGLISH.md) \| [PDF](lecture_21/Notes_21.11/notes.pdf) \| [Notebook](lecture_21/Notes_21.11/lecture_21_11.ipynb) |
| **21.12** | Diagonalization & Spectral Theorem | Modal matrix $P$, similarity transformation $A = P \Lambda P^{-1}$, symmetric spectral theorem | [Notes](lecture_21/Notes_21.12/README_HINGLISH.md) \| [PDF](lecture_21/Notes_21.12/notes.pdf) \| [Notebook](lecture_21/Notes_21.12/lecture_21_12.ipynb) |
| **21.13** | Singular Value Decomposition (SVD) | Rectangular factorization $A = U \Sigma V^T$, Eckart-Young low-rank theorem | [Notes](lecture_21/Notes_21.13/README_HINGLISH.md) \| [PDF](lecture_21/Notes_21.13/notes.pdf) \| [Notebook](lecture_21/Notes_21.13/lecture_21_13.ipynb) |
| **21.14** | Principal Component Analysis (PCA) via Linear Algebra | Covariance matrix $\mathbf{\Sigma}$, spectral projection, scree plot, dimensionality reduction | [Notes](lecture_21/Notes_21.14/README_HINGLISH.md) \| [PDF](lecture_21/Notes_21.14/notes.pdf) \| [Notebook](lecture_21/Notes_21.14/lecture_21_14.ipynb) |
| **21.15** | Linear Algebra in Deep Learning & Attention | Dense layers, im2col gemm convolution, Transformer Scaled Dot-Product Attention, LoRA | [Notes](lecture_21/Notes_21.15/README_HINGLISH.md) \| [PDF](lecture_21/Notes_21.15/notes.pdf) \| [Notebook](lecture_21/Notes_21.15/lecture_21_15.ipynb) |

> [!TIP]
> **🧪 Day 21 Comprehensive Case Studies & Practice Problem Set:**  
> *Module Guides:* [📖 Hinglish Guide](lecture_21/Practice_Problems/README_HINGLISH.md) | [English Guide](lecture_21/Practice_Problems/README.md)  
> - 📝 **Problem Statements:** [Questions](lecture_21/Practice_Problems/Questions/README_HINGLISH.md) | [questions.pdf](lecture_21/Practice_Problems/Questions/questions.pdf) | [Starter Notebook](lecture_21/Practice_Problems/Questions/questions.ipynb)
> - 💡 **Complete Solutions:** [Solutions](lecture_21/Practice_Problems/Solutions/README_HINGLISH.md) | [solutions.pdf](lecture_21/Practice_Problems/Solutions/solutions.pdf) | [Executed Notebook](lecture_21/Practice_Problems/Solutions/solutions.ipynb)

### 📉 Day 22: Mathematics for AI (Part 3 — Calculus Mastery) [Hinglish]
*Module Guides:* [📖 Hinglish Guide](lecture_22/README_HINGLISH.md) | [English Guide](lecture_22/README.md)

Artificial Intelligence, Machine Learning aur Deep Learning Optimization ke liye Calculus ka complete mathematical foundation: Functions, composite functions, function arithmetic, vertical/horizontal transformations, limit definition of derivative, differentiation rules, activation derivatives (Sigmoid, Tanh, ReLU), critical points, concavity tests, aur Gradient Descent optimization.

| Lecture | Topic Title | Core Concepts | Quick Links |
| :--- | :--- | :--- | :--- |
| **22.01** | Calculus ka Parichay aur Continuous Change | Continuous change, differential vs integral, parameter sensitivity, loss minimization | [Notes](lecture_22/Notes_22.01/README_HINGLISH.md) \| [PDF](lecture_22/Notes_22.01/notes.pdf) \| [Notebook](lecture_22/Notes_22.01/lecture_22_01.ipynb) |
| **22.02** | Mathematical Functions aur Transformations | Domain, codomain, range, root functions, sinusoids, exponentials, logs in AI | [Notes](lecture_22/Notes_22.02/README_HINGLISH.md) \| [PDF](lecture_22/Notes_22.02/notes.pdf) \| [Notebook](lecture_22/Notes_22.02/lecture_22_02.ipynb) |
| **22.03** | Composite Functions aur Deep Neural Architectures | Function composition $(f \circ g)(x)$, nested deep neural network forward pass, non-commutativity | [Notes](lecture_22/Notes_22.03/README_HINGLISH.md) \| [PDF](lecture_22/Notes_22.03/notes.pdf) \| [Notebook](lecture_22/Notes_22.03/lecture_22_03.ipynb) |
| **22.04** | Functions par Operations: Multiplication & Addition | Vertical stretch, compression, shift, reflection, linear combinations, residual connections | [Notes](lecture_22/Notes_22.04/README_HINGLISH.md) \| [PDF](lecture_22/Notes_22.04/notes.pdf) \| [Notebook](lecture_22/Notes_22.04/lecture_22_04.ipynb) |
| **22.05** | Input Transformations: Scaling & Shifts | Horizontal shifts, horizontal scaling, affine input maps ($z = w x + b$), standardization | [Notes](lecture_22/Notes_22.05/README_HINGLISH.md) \| [PDF](lecture_22/Notes_22.05/notes.pdf) \| [Notebook](lecture_22/Notes_22.05/lecture_22_05.ipynb) |
| **22.06** | Differentiation aur Instantaneous Rate of Change | Secant to tangent limit, derivative definition, first-principles proofs, Taylor linear approximation | [Notes](lecture_22/Notes_22.06/README_HINGLISH.md) \| [PDF](lecture_22/Notes_22.06/notes.pdf) \| [Notebook](lecture_22/Notes_22.06/lecture_22_06.ipynb) |
| **22.07** | Differentiation ke Niyam aur Activation Derivatives | Power, product, quotient, chain rule. Sigmoid, Tanh, ReLU derivatives derivations | [Notes](lecture_22/Notes_22.07/README_HINGLISH.md) \| [PDF](lecture_22/Notes_22.07/notes.pdf) \| [Notebook](lecture_22/Notes_22.07/lecture_22_07.ipynb) |
| **22.08** | Minima aur Maxima Dhoondhna | Critical points, First & Second Derivative Tests, concavity, Gradient Descent algorithm | [Notes](lecture_22/Notes_22.08/README_HINGLISH.md) \| [PDF](lecture_22/Notes_22.08/notes.pdf) \| [Notebook](lecture_22/Notes_22.08/lecture_22_08.ipynb) |
| **22.09** | Calculus Optimization Practice Problem | Analytical derivation of $f(x) = x^3 - 6x^2 + 9x$, critical points, double derivative test, extrema | [Notes](lecture_22/Notes_22.09/README_HINGLISH.md) \| [PDF](lecture_22/Notes_22.09/notes.pdf) \| [Notebook](lecture_22/Notes_22.09/lecture_22_09.ipynb) |

> [!TIP]
> **🧪 Day 22 Comprehensive Case Studies & Practice Problem Set:**  
> *Module Guides:* [📖 Hinglish Guide](lecture_22/Practice_Problems/README_HINGLISH.md) | [English Guide](lecture_22/Practice_Problems/README.md)  
> - 📝 **Problem Statements:** [Questions](lecture_22/Practice_Problems/Questions/README_HINGLISH.md) | [questions.pdf](lecture_22/Practice_Problems/Questions/questions.pdf) | [Starter Notebook](lecture_22/Practice_Problems/Questions/questions.ipynb)
> - 💡 **Complete Solutions:** [Solutions](lecture_22/Practice_Problems/Solutions/README_HINGLISH.md) | [solutions.pdf](lecture_22/Practice_Problems/Solutions/solutions.pdf) | [Executed Notebook](lecture_22/Practice_Problems/Solutions/solutions.ipynb)

---

## 📐 Mathematical Formulations & Statistical Expressions (Textbook Reference)

Visualizations ke peeche ke mathematical formulas standard academic textbook style mein:

### 1. Data-Ink Principle (Tufte Formulation)
Visual chart ki efficiency measure karne ke liye **Data-Ink Ratio** $\eta$ use hota hai:

$$
\boxed{
\eta = \frac{\mathcal{I}_{\text{data}}}{\mathcal{I}_{\text{total}}} = 1.0 - \frac{\mathcal{I}_{\text{non-data}}}{\mathcal{I}_{\text{total}}}
}
$$

jahan $\mathcal{I}_{\text{data}}$ actual data points/trendlines ka ink hai, aur $\mathcal{I}_{\text{total}}$ chart ka total ink hai. Optimal target $\eta \to 1.0$ hota hai.

---

### 2. Grouped Bar Clustered Coordinate Mathematics
Jab $K = 2$ series ko $N$ categories ke liye plot karna ho (width $w < 0.5$ ke sath):

Har category ka baseline index $x_i = i$ ($i \in \{0, 1, \dots, N-1\}$) hota hai. Shifted bar coordinates $(y_{1, i}, y_{2, i})$ symmetric piecewise system follow karte hain:

$$
\begin{cases}
y_{1, i} = x_i - \dfrac{w}{2} \\
y_{2, i} = x_i + \dfrac{w}{2}
\end{cases}
$$

jahan $y_{1, i}$ Series 1 (Budget) ka center coordinate hai aur $y_{2, i}$ Series 2 (Spend) ka center coordinate hai.

Tick label $t_i$ dono bars ke arithmetic mean par perfectly center hota hai:

$$
\boxed{t_i = \frac{y_{1, i} + y_{2, i}}{2} = x_i}
$$

---

### 3. Tukey's Five-Number Summary & Box Plot Outlier Fences
Ordered dataset $\mathcal{D} = \{x_{(1)}, x_{(2)}, \dots, x_{(n)}\}$ ke liye:

$$
\boxed{\text{IQR} = Q_3 - Q_1}
$$

$$
\begin{cases}
\text{Lower Whisker Fence} &= Q_1 - 1.5 \times \text{IQR} \\
\text{Upper Whisker Fence} &= Q_3 + 1.5 \times \text{IQR}
\end{cases}
$$

$$
\boxed{\mathcal{O} = \left\{ x_i \in \mathcal{D} \;\middle|\; x_i < F_L \;\lor\; x_i > F_U \right\}}
$$

---

### 4. Histogram Bin Estimation Models
Continuous feature distribution ke liye optimal bin count:

- **Sturges' Rule** (Normal distributions ke liye):
  $$k = \left\lceil 1 + \log_2(n) \right\rceil$$

- **Freedman-Diaconis Rule** (Outliers ke khilaaf robust):
  $$h = 2 \cdot \frac{\text{IQR}}{\sqrt[3]{n}}, \qquad k = \left\lceil \frac{\max(x) - \min(x)}{h} \right\rceil$$

---

## 🗺️ 60-Day Curriculum Roadmap

Foundational mathematics aur Python se shuru karke cutting-edge GenAI aur real-world deployment tak ka roadmap:

```mermaid
flowchart LR
    A["Lectures 01-15<br/>Python & Math Foundations"] --> B["Lectures 16-25<br/>Data Analysis & Visualization"]
    B --> C["Lectures 26-40<br/>Classical Machine Learning"]
    C --> D["Lectures 41-52<br/>Deep Learning & Computer Vision"]
    D --> E["Lectures 53-60<br/>NLP, LLMs & MLOps Deployment"]
```

- **Lectures 01 – 15**: Python Programming, Linear Algebra, Calculus, NumPy, aur Data Manipulation.
- **Lectures 16 – 25**: Exploratory Data Analysis (EDA), Advanced Pandas, Matplotlib, Seaborn, Feature Engineering.
- **Lectures 26 – 40**: Supervised & Unsupervised Machine Learning (Regression, Classification, Random Forest, XGBoost, K-Means, PCA).
- **Lectures 41 – 52**: Deep Learning Foundations (Neural Networks, Backpropagation, PyTorch/TensorFlow, CNNs, Transfer Learning).
- **Lectures 53 – 60**: Natural Language Processing (RNNs, Transformers, Attention Mechanism, LLM Fine-Tuning, MLOps, CI/CD).

---

## ⚡ Quickstart & Setup Guide

### 1. Repository Clone Karein
```bash
git clone https://github.com/S1h2i3v4a/AI_ML.git
cd AI_ML
```

### 2. Environment Setup
```bash
# Conda ke through
conda create -n aiml python=3.10 -y
conda activate aiml

# Ya fir standard venv
python -m venv venv
# Windows par:
.\venv\Scripts\activate
# Linux/macOS par:
source venv/bin/activate
```

### 3. Dependencies Install Karein
```bash
pip install numpy pandas matplotlib seaborn jupyter jupyterlab scipy scikit-learn
```

### 4. Jupyter Lab Start Karein
```bash
jupyter lab
```

---

## 📜 Standards & Integrity
- **Original Illustrations**: Sabhi diagrams custom code se generate kiye gaye hain taaki koi copyright issue na aaye.
- **Reproducible Code**: Har notebook standalone aur reproducible hai.
- **Dual Format Documentation**: Markdown notes ke saath high-definition vector PDFs offline reading ke liye available hain.

---

## 👤 Author & Maintainer
- **Shivam Keshari**
- GitHub: [@S1h2i3v4a](https://github.com/S1h2i3v4a)
- Repository: [AI_ML](https://github.com/S1h2i3v4a/AI_ML)
