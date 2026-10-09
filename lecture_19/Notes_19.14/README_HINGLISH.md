# Day 19 - Lecture 19.14: Distribution Plots in Seaborn (`displot`, `histplot`, `kdeplot`) [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_19_14.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 19 Module Par Wapas Jayein](../README_HINGLISH.md)

---

## 1. Overview & Purpose
**Distribution Plots** allow us to inspect the shape, spread, modality, and skewness of continuous variables.
Modern Seaborn (v0.11+) provides:
- **`sns.histplot()`:** Modern, powerful replacement for `plt.hist()`.
- **`sns.kdeplot()`:** Kernel Density Estimation (smooth probability density curve).
- **`sns.displot()`:** Figure-level function providing access to histograms, KDEs, and ECDFs with automated subplot faceting.

---

## 2. Kernel Density Estimation (KDE) Theory

A histogram's appearance depends heavily on arbitrary bin boundaries. 
**KDE** replaces discrete bins with a smooth, continuous estimate of the probability density function $f(x)$:
$$\hat{f}_h(x) = \frac{1}{n h} \sum_{i=1}^{n} K\left( \frac{x - x_i}{h} \right)$$
where $K(\cdot)$ is a Gaussian kernel function and $h$ is the smoothing **bandwidth**.
- In `sns.histplot()`, setting **`kde=True`** overlays this smooth mathematical density over the discrete bins.

---

## 3. Code Implementation: The Penguins Dataset

```python
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")
print("Penguins Dataset Preview:")
print(penguins.head())

# 1. Distribution of Body Mass (30 bins with KDE overlay)
plt.figure(figsize=(9, 5))
sns.histplot(
    data=penguins,
    x="body_mass_g",
    bins=30,
    kde=True,
    color="teal"
)
plt.title("Penguin Body Mass Distribution with KDE Overlay", fontsize=14, fontweight="bold")
plt.xlabel("Body Mass (grams)", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()

# 2. Multi-class distribution with hue
plt.figure(figsize=(9, 5))
sns.histplot(
    data=penguins,
    x="body_mass_g",
    hue="species",
    element="step",  # 'bars', 'step', or 'poly'
    kde=True
)
plt.title("Body Mass Distribution Across Penguin Species", fontsize=14, fontweight="bold")
plt.xlabel("Body Mass (grams)")
plt.show()
```

---

## 📐 Kernel Density Estimation (KDE) Ka Ganitiya Sutra

Kernel Density Estimation non-parametric continuous probability density function $f(x)$ estimate karne ka method hai:

$$
\boxed{\hat{f}_h(x) = \frac{1}{n h} \sum_{i=1}^n K\left(\frac{x - x_i}{h}\right)}
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

## 4. Mukhya Batein (Key Takeaways)
- `sns.histplot()` handles missing values (`NaN`) gracefully without crashing.
- Setting `element="step"` or `multiple="stack"` creates clean, uncluttered visual comparisons across multiple species.
