# 📝 Lecture 19: Practice Problems — Question Set

[![Notebook](https://img.shields.io/badge/Jupyter-questions.ipynb-orange.svg?logo=jupyter&logoColor=white)](questions.ipynb)
[![PDF](https://img.shields.io/badge/PDF-questions.pdf-red.svg)](questions.pdf)
[![Solutions](https://img.shields.io/badge/Solutions-Available-success.svg)](../Solutions/README.md)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [💡 View Complete Solutions](../Solutions/README.md) | [⬅️ Back to Practice Problems Overview](../README.md)

---

## 🎯 Comprehensive Case-Based & Technical Challenges

This problem set evaluates your mastery across all concepts taught in **Lecture 19 (Advanced Matplotlib & Seaborn Mastery)**:
- Continuous Distributions, Histograms, Density Normalization (`plt.hist`, `density=True`)
- Bin Estimation Models (Sturges' Formula vs Freedman-Diaconis Rule)
- Parametric Benchmarks & Vertical Reference Lines (`plt.axvline`)
- Box Plots, Tukey's Five-Number Summary, and Outlier Fences ($1.5 \times \text{IQR}$)
- Notched Box Plots for Visual Hypothesis Testing of Medians
- Split Violin Plots and Multimodal Distribution Discovery (`sns.violinplot`)
- Object-Oriented Subplot Grids (`fig, axes = plt.subplots`) & Scale Sharing
- Independent Dual-Axis Affine Coordinate Systems (`ax.twinx()`)
- Seaborn Grammar of Graphics Semantic Encodings (`hue`, `style`, `size`)
- Correlation Matrix Heatmaps with Upper-Triangular Masking (`sns.heatmap`)
- Edward Tufte Data-Ink Ratio Maximization

---

## 📌 Case 1: Algorithmic E-Commerce Logistics & Delivery Duration Distribution
### 🏢 **Domain**: Supply Chain Analytics & Fulfillment Optimization
### 🎯 **Tested Topics**: Lecture 19.01 – 19.03 & 19.14 (Histograms, Optimal Bins, Probability Density Normalization, Reference Lines, Gaussian KDE)

### 📖 **Business Scenario**:
You are the **Principal Logistics Data Scientist** at a tier-1 e-commerce platform. The operations engineering team has compiled delivery duration records across 5,000 completed orders across two distinct fulfillment mechanisms:
1. **Express Drone / Bike Courier**: Rapid urban delivery characterized by tight execution variance ($\mu = 2.5\text{ hours}, \sigma = 0.6$).
2. **Regional Fulfillment Warehousing**: Hub-and-spoke multi-stage delivery with right-skewed transit delays ($\mu = 7.5\text{ hours}, \sigma = 2.4$, heavy right tail).

The executive leadership has established a formal Service Level Agreement (SLA): **at least 90% of all platform deliveries must arrive within 6.0 hours**.

### 📊 **Dataset Specification (Synthetic Generation Template)**:
```python
import numpy as np

np.random.seed(42)
n_samples = 2500

# Express Urban Logistics (Normal Distribution)
express_durations = np.random.normal(loc=2.5, scale=0.6, size=n_samples)
express_durations = np.clip(express_durations, 0.5, 6.0)

# Regional Warehousing Logistics (Right-Skewed Lognormal Distribution)
regional_durations = np.random.lognormal(mean=1.9, sigma=0.45, size=n_samples)
regional_durations = np.clip(regional_durations, 2.0, 18.0)
```

### ❓ **Problem Statements & Questions to Solve**:
1. **Mathematical Bin Width Optimization**:
   - Calculate the optimal number of bins $k$ for the regional dataset using:
     - **Sturges' Rule**:

$$
k_{\text{sturges}} = 1 + \lceil \log_2(n) \rceil
$$

     - **Freedman-Diaconis Rule**:

$$
h = 2 \cdot \frac{\text{IQR}(X)}{n^{1/3}} \qquad\implies\qquad k_{\text{fd}} = \left\lceil \frac{\max(X) - \min(X)}{h} \right\rceil
$$

   - Explain why Sturges' formula severely under-bins heavy-tailed, skewed data, whereas Freedman-Diaconis preserves tail resolution.

2. **Dual-Series Normalized Density Histogram Implementation**:
   - Plot both delivery channels on a single canvas using `plt.hist()`.
   - Set `density=True` to normalize both distributions into genuine probability densities where total integrated area equals $1.0$.
   - Superimpose continuous Gaussian Kernel Density Estimation (KDE) curves for both channels using `sns.kdeplot()` or `scipy.stats.gaussian_kde`.
   - Use semi-transparent colors (`alpha=0.55`) and distinct edge borders (`edgecolor='black'`).

3. **Parametric Benchmarks & SLA Threshold Reference Lines (`plt.axvline`)**:
   - Add vertical dashed reference lines for:
     - Express Courier Median ($Q_{2, \text{express}}$) in dark green dashed style (`--`).
     - Regional Courier Median ($Q_{2, \text{regional}}$) in navy dashed style (`--`).
     - Target SLA Cutoff ($x = 6.0\text{ hours}$) in bold crimson dash-dot style (`-.`, linewidth 2.5).
   - Add a callout annotation showing the exact percentage of regional orders breaching the 6-hour SLA boundary.

---

## 📌 Case 2: Multi-Cohort Clinical Trial Biomarker & Outlier Audit
### 🏢 **Domain**: Biostatistics & Oncology Clinical Trials
### 🎯 **Tested Topics**: Lecture 19.04 – 19.07 & 19.13 (Box Plots, Five-Number Summary, Tukey's Fences, Notched Median Confidence Intervals, Split Violin Plots)

### 📖 **Business Scenario**:
A biopharmaceutical research group is analyzing tumor volume reduction percentage ($\%$) in a Phase III multi-center oncology trial. A cohort of $N = 480$ patients is partitioned across 4 treatment arms ($n = 120$ patients each):
- **Cohort A (Control)**: Standard Placebo ($\text{Median} \approx 6\%$)
- **Cohort B (SOC Chemotherapy)**: Conventional Cytotoxic Regimen ($\text{Median} \approx 28\%$)
- **Cohort C (Targeted Kinase Inhibitor)**: Monotherapy Small-Molecule Drug ($\text{Median} \approx 48\%$)
- **Cohort D (Combination Immuno-Oncology)**: Targeted Inhibitor + Monoclonal Antibody ($\text{Median} \approx 54\%$)

The clinical review board requires an audit of efficacy variance, outlier identification, and a visual hypothesis test to determine if Cohort D demonstrates statistically significant superiority over Cohort C without relying on parametric Student's t-tests.

### 📊 **Dataset Specification (Synthetic Generation Template)**:
```python
import numpy as np
import pandas as pd

np.random.seed(101)
n_patients = 120

cohort_a = np.random.normal(loc=6.0, scale=4.5, size=n_patients)
cohort_b = np.random.normal(loc=28.0, scale=8.0, size=n_patients)
cohort_c = np.random.normal(loc=48.0, scale=11.0, size=n_patients)

# Cohort D: Bimodal mixture (80% strong responders, 20% non-responders with genomic mutation)
d_responders = np.random.normal(loc=62.0, scale=6.0, size=int(n_patients * 0.8))
d_nonresponders = np.random.normal(loc=22.0, scale=5.0, size=int(n_patients * 0.2))
cohort_d = np.concatenate([d_responders, d_nonresponders])
```

### ❓ **Problem Statements & Questions to Solve**:
1. **Tukey's Five-Number Summary & Outlier Derivation**:
   - For Cohort B and Cohort C, compute John Tukey's Five-Number Summary:

$$
\text{Summary} = \left( X_{(1)}, \; Q_1, \; Q_2, \; Q_3, \; X_{(n)} \right)
$$

   - Derive the lower and upper outlier fences:

$$
\boxed{F_L = Q_1 - 1.5 \cdot \text{IQR} \qquad\text{and}\qquad F_U = Q_3 + 1.5 \cdot \text{IQR}}
$$

   - Identify any exceptional outlier patients whose tumor reduction exceeds $F_U$ or falls below $F_L$.

2. **Notched Box Plot Visual Hypothesis Testing**:
   - Construct side-by-side notched box plots (`plt.boxplot(..., notch=True)` or `sns.boxplot(..., notch=True)`).
   - State the mathematical formula for the 95% confidence interval notch width:

$$
\boxed{\text{Notch} = Q_2 \pm 1.57 \cdot \frac{\text{IQR}}{\sqrt{n}}}
$$

   - Based on whether the notches of Cohort C and Cohort D overlap, evaluate if their population medians differ with approximate 95% statistical confidence ($\alpha = 0.05$).

3. **Multimodal Density Discovery via Violin Plots (`sns.violinplot`)**:
   - Why does a standard box plot fail to communicate the critical clinical reality of Cohort D (the presence of a 20% resistant non-responder sub-population)?
   - Implement a horizontal or vertical Seaborn violin plot with embedded quartile markings (`inner='quartile'`) to expose the bimodal density distribution.

---

## 📌 Case 3: Quantitative Hedge Fund Multi-Asset Risk & Macroeconomic Regime Analysis
### 🏢 **Domain**: Quantitative Finance & Portfolio Risk Engineering
### 🎯 **Tested Topics**: Lecture 19.08 – 19.12 & 19.15 – 19.16 (Object-Oriented Subplots, Dual-Axis `twinx`, Heatmaps with Triangular Mask, Seaborn Relational Mapping, Edward Tufte Data-Ink)

### 📖 **Business Scenario**:
You are a **Quantitative Portfolio Manager** evaluating multi-asset cross-market risk across 500 trading days. The fund trades across 6 asset classes and macroeconomic indicators:
1. **$R_{\text{equity}}$**: S&P 500 Equity Index Returns (%)
2. **$R_{\text{bonds}}$**: 10-Year US Treasury Bond Returns (%)
3. **$\text{VIX}$**: CBOE Market Volatility Index (Level)
4. **$\Delta\text{Oil}$**: WTI Crude Oil Price Percentage Change (%)
5. **$\pi_{\text{CPI}}$**: Breakeven Inflation Expectations (%)
6. **$\text{DXY}$**: US Dollar Trade-Weighted Currency Index Change (%)

The portfolio risk committee requires:
- A triangular correlation matrix heatmap to detect risk clustering and multi-collinearity.
- A dual-axis time-series visualization tracking Cumulative Portfolio Returns against the VIX Volatility Index during a severe macroeconomic stress period.
- A faceted $2 \times 2$ subplot grid visualizing cross-asset dynamics engineered according to Edward Tufte's Data-Ink principles.

### 📊 **Dataset Specification (Synthetic Generation Template)**:
```python
import numpy as np
import pandas as pd

np.random.seed(42)
days = 500

dates = pd.date_range("2024-01-01", periods=days, freq="B")
equity_ret = np.random.normal(0.04, 1.1, days)
bonds_ret = -0.35 * equity_ret + np.random.normal(0.01, 0.45, days)
vix = 18 + np.maximum(0, -8.0 * equity_ret + np.random.normal(0, 3.5, days))
oil_chg = 0.25 * equity_ret + np.random.normal(0.02, 1.8, days)
inflation = 2.4 + 0.15 * oil_chg + np.random.normal(0, 0.2, days)
dxy = -0.20 * equity_ret + np.random.normal(0.01, 0.5, days)

market_df = pd.DataFrame({
    "Date": dates,
    "Equity": equity_ret,
    "Bonds": bonds_ret,
    "VIX": vix,
    "Oil": oil_chg,
    "Inflation": inflation,
    "DXY": dxy
})
```

### ❓ **Problem Statements & Questions to Solve**:
1. **Upper-Triangular Masked Correlation Heatmap (`sns.heatmap`)**:
   - Compute the full Pearson correlation matrix $\mathbf{R} \in \mathbb{R}^{6 \times 6}$:

$$
\boxed{r_{jk} = \frac{\sum_{i=1}^n (x_{ij} - \bar{x}_j)(x_{ik} - \bar{x}_k)}{\sqrt{\sum_{i=1}^n (x_{ij} - \bar{x}_j)^2} \sqrt{\sum_{i=1}^n (x_{ik} - \bar{x}_k)^2}}}
$$

   - Apply a triangular mask (`np.triu(np.ones_like(corr, dtype=bool))`) to eliminate redundant mirrored entries.
   - Use a diverging colormap (`cmap='coolwarm'`), fix `vmin=-1.0, vmax=1.0, center=0`, format numbers with two decimal places (`fmt='.2f'`), and enable grid cell borders (`linewidths=0.75`).

2. **Dual-Axis Independent Affine Time-Series (`ax.twinx()`)**:
   - On the primary left vertical axis, plot the fund's **Cumulative Return Index** ($Y_1$, base index 100.0) as a solid navy line.
   - On the secondary right vertical axis, instantiate an independent coordinate system using `ax.twinx()` and plot the **VIX Volatility Index** ($Y_2$) with a semi-transparent crimson fill (`fill_between`).
   - Eliminate visual confusion by explicitly coloring each axis spine and label to match the respective metric.

3. **Object-Oriented Subplot Layout & Edward Tufte Data-Ink Optimization**:
   - Construct a $2 \times 2$ grid (`fig, axes = plt.subplots(2, 2, figsize=(14, 9), dpi=150)`).
   - Populate the 4 panes:
     - Top-Left: Dual-Series Density Histograms (Equity vs Bond returns).
     - Top-Right: Notched Box Plot comparing factor distributions.
     - Bottom-Left: Relational Scatter Plot with Seaborn semantic hue mapping.
     - Bottom-Right: Masked Correlation Heatmap.
   - Apply Edward Tufte's Data-Ink maximization rule: remove unnecessary top and right borders (`ax.spines['top'].set_visible(False)`, `ax.spines['right'].set_visible(False)`), apply subtle gridlines (`linestyle=':'`, `alpha=0.5`), and prevent label clipping using `plt.tight_layout()`.

---

## 🚀 Ready to Review Answers?

When you have implemented your code in [`questions.ipynb`](questions.ipynb), compare your visual outputs and derivations against the [Complete Production Solutions](../Solutions/README.md).
