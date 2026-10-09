# 📝 Lecture 19: Practice Problems — Question Set

[![Notebook](https://img.shields.io/badge/Jupyter-questions.ipynb-orange.svg?logo=jupyter&logoColor=white)](questions.ipynb)
[![PDF](https://img.shields.io/badge/PDF-questions.pdf-red.svg)](questions.pdf)
[![Solutions](https://img.shields.io/badge/Solutions-Available-success.svg)](../Solutions/README_HINGLISH.md)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [💡 Complete Solutions Dekhein](../Solutions/README_HINGLISH.md) | [⬅️ Back to Practice Problems Overview](../README_HINGLISH.md)

---

## 🎯 Case-Based & Technical Problem Set

Yeh problem set **Lecture 19 (Advanced Matplotlib & Seaborn Mastery)** ke sabhi core concepts par aapki pakad ko test karne ke liye design kiya gaya hai:
- Histograms, Density Normalization (`plt.hist`, `density=True`)
- Optimal Bin Rules (Sturges' Rule vs Freedman-Diaconis Rule)
- Statistical Reference Lines (`plt.axvline`)
- Box Plots, Tukey's Five-Number Summary, aur Outlier Detection ($1.5 \times \text{IQR}$)
- Notched Box Plots dwara Medians ka Visual Hypothesis Testing
- Split Violin Plots dwara Multimodal distributions ko identify karna
- Object-Oriented Subplots (`fig, axes = plt.subplots`)
- Dual-Axis Coordinate Systems (`ax.twinx()`)
- Seaborn Grammar of Graphics Aesthetic Mapping (`hue`, `style`, `size`)
- Correlation Heatmap with Triangular Mask (`sns.heatmap`)
- Edward Tufte Data-Ink Maximization

---

## 📌 Case 1: Algorithmic E-Commerce Logistics & Delivery Duration Distribution
### 🏢 **Domain**: Supply Chain Analytics & Fulfillment Optimization
### 🎯 **Tested Topics**: Lecture 19.01 – 19.03 & 19.14 (Histograms, Optimal Bins, Probability Density, Reference Lines, Gaussian KDE)

### 📖 **Business Scenario**:
Aap ek top e-commerce platform me **Lead Data Scientist** hain. Operations team ne 5,000 orders ka delivery duration (ghanton me) analyze karne ke liye data collect kiya hai:
1. **Express Drone / Bike Courier**: Shahri ilaakon me tezi se deliver hone wale orders ($\mu = 2.5\text{ hours}, \sigma = 0.6$).
2. **Regional Warehousing Logistics**: Hub-and-spoke multi-tier model jisme right-skewed transit delays aate hain ($\mu = 7.5\text{ hours}, \sigma = 2.4$).

Company ka strict SLA (Service Level Agreement) hai: **kam se kam 90% orders 6.0 ghante ke andar deliver hone chahiye**.

### 📊 **Dataset Generation Template**:
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

### ❓ **Problems to Solve**:
1. **Mathematical Bin Width Optimization**:
   - Regional dataset ke liye Sturges' formula aur Freedman-Diaconis rule se optimal bin count $k$ calculate karein:

$$
k_{\text{sturges}} = 1 + \lceil \log_2(n) \rceil
$$

$$
h = 2 \cdot \frac{\text{IQR}(X)}{n^{1/3}} \qquad\implies\qquad k_{\text{fd}} = \left\lceil \frac{\max(X) - \min(X)}{h} \right\rceil
$$

   - Explain karein ki skewed distribution me Sturges kyu fail hota hai aur Freedman-Diaconis kyu behtar hai.

2. **Dual-Series Normalized Density Histogram**:
   - Dono channels ko ek hi canvas par `plt.hist(..., density=True, alpha=0.55)` se plot karein taaki total area $1.0$ par integrate ho.
   - Dono distributions ke upar Gaussian Kernel Density Estimation (KDE) curve overlay karein (`sns.kdeplot`).

3. **SLA Reference Line & Breach Annotation**:
   - `plt.axvline()` ka use karke Express Median, Regional Median aur SLA Cutoff line ($x = 6.0\text{ hours}$) draw karein.
   - Text annotation add karein jo show kare ki kitne percent regional orders SLA breach kar rahe hain.

---

## 📌 Case 2: Multi-Cohort Clinical Trial Biomarker & Outlier Audit
### 🏢 **Domain**: Pharmaceuticals & Oncology Clinical Trials
### 🎯 **Tested Topics**: Lecture 19.04 – 19.07 & 19.13 (Box Plots, Five-Number Summary, Tukey's Fences, Notched Box Plots, Violin Plots)

### 📖 **Business Scenario**:
Cancer clinical trial me $N = 480$ patients par tumor biomarker reduction ($\%$) evaluate kiya ja raha hai (har cohort me $n = 120$ patients):
- **Cohort A (Control)**: Placebo ($\text{Median} \approx 6\%$)
- **Cohort B (SOC Chemotherapy)**: Standard Chemotherapy ($\text{Median} \approx 28\%$)
- **Cohort C (Targeted Kinase Inhibitor)**: Monotherapy Small Molecule ($\text{Median} \approx 48\%$)
- **Cohort D (Combination Immuno-Oncology)**: Targeted Drug + Monoclonal Antibody ($\text{Median} \approx 54\%$)

Clinical board ko outlier audit aur bina t-test lagaye yeh dekhna hai ki kya Cohort D, Cohort C se statistically significantly behtar hai ya nahi.

### 📊 **Dataset Generation Template**:
```python
import numpy as np
import pandas as pd

np.random.seed(101)
n_patients = 120

cohort_a = np.random.normal(loc=6.0, scale=4.5, size=n_patients)
cohort_b = np.random.normal(loc=28.0, scale=8.0, size=n_patients)
cohort_c = np.random.normal(loc=48.0, scale=11.0, size=n_patients)

# Cohort D: Bimodal mixture (80% responders, 20% resistant non-responders)
d_responders = np.random.normal(loc=62.0, scale=6.0, size=int(n_patients * 0.8))
d_nonresponders = np.random.normal(loc=22.0, scale=5.0, size=int(n_patients * 0.2))
cohort_d = np.concatenate([d_responders, d_nonresponders])
```

### ❓ **Problems to Solve**:
1. **Tukey's Five-Number Summary & Outlier Fences**:
   - Cohort B aur C ke liye Five-Number Summary $(X_{(1)}, Q_1, Q_2, Q_3, X_{(n)})$ aur Tukey's Fences calculate karein:

$$
\boxed{F_L = Q_1 - 1.5 \cdot \text{IQR} \qquad\text{aur}\qquad F_U = Q_3 + 1.5 \cdot \text{IQR}}
$$

2. **Notched Box Plot Hypothesis Testing**:
   - `notch=True` ke sath box plots plot karein.
   - Notch confidence interval ka ganitiya sutra:

$$
\boxed{\text{Notch} = Q_2 \pm 1.57 \cdot \frac{\text{IQR}}{\sqrt{n}}}
$$

   - Agar Cohort C aur D ke notches overlap nahi karte, toh conclusion draw karein.

3. **Multimodal Density Discovery via Violin Plots**:
   - Box plot Cohort D ke andar maujood 20% non-responders ko kyu hide kar deta hai?
   - `sns.violinplot(..., inner='quartile')` use karke bimodal density contours ko expose karein.

---

## 📌 Case 3: Quantitative Hedge Fund Multi-Asset Risk & Macroeconomic Regime Analysis
### 🏢 **Domain**: Quantitative Finance & Portfolio Risk Management
### 🎯 **Tested Topics**: Lecture 19.08 – 19.12 & 19.15 – 19.16 (Object-Oriented Subplots, Dual-Axis `twinx`, Heatmap Mask, Seaborn Relational Mapping, Edward Tufte Data-Ink)

### 📖 **Business Scenario**:
Ek quantitative fund 6 macroeconomic factors par 500 trading days ka risk audit kar raha hai:
- Equity Market Return, Bond Return, VIX Volatility Index, Oil Price Change, Inflation CPI, US Dollar Index.

### ❓ **Problems to Solve**:
1. **Upper-Triangular Masked Correlation Heatmap**:
   - Pearson correlation matrix $\mathbf{R} \in \mathbb{R}^{6 \times 6}$ derive karein:

$$
\boxed{r_{jk} = \frac{\sum_{i=1}^n (x_{ij} - \bar{x}_j)(x_{ik} - \bar{x}_k)}{\sqrt{\sum_{i=1}^n (x_{ij} - \bar{x}_j)^2} \sqrt{\sum_{i=1}^n (x_{ik} - \bar{x}_k)^2}}}
$$

   - `np.triu()` mask ke sath diverging colormap (`coolwarm`) aur `fmt='.2f'` se clean heatmap plot karein.

2. **Dual-Axis Independent Affine Time-Series (`ax.twinx()`)**:
   - Left axis par Cumulative Portfolio Returns ($Y_1$, line plot) aur right axis par VIX Volatility Index ($Y_2$, shaded area) plot karein.
   - Dono axes ko color coordinate karein.

3. **2x2 Object-Oriented Grid & Edward Tufte Data-Ink Optimization**:
   - `fig, axes = plt.subplots(2, 2, figsize=(14, 9), dpi=150)` se 4 clean panels render karein.
   - Unnecessary top aur right borders (`ax.spines['right'].set_visible(False)`) hata kar Data-Ink ratio maximize karein.

---

## 🚀 Navigation

- 💻 Starter Notebook: [`questions.ipynb`](questions.ipynb)
- 💡 Complete Solution: [Solutions Dekhein](../Solutions/README_HINGLISH.md)
