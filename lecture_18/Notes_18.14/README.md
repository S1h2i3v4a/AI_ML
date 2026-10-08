# Day 18 - Lecture 18.14: Advanced Customizations on Scatter Plots

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_14.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Lecture 18 Module](../README.md)

---

## 1. Overview & Semantic Encoding
Scatter plots can convey **up to 4 dimensions of data** simultaneously on a 2D plane:
1. **$X$-position:** Dimension 1 (e.g. Age)
2. **$Y$-position:** Dimension 2 (e.g. Blood Pressure)
3. **Point Area (`s`):** Dimension 3 (e.g. Magnitude / Severity)
4. **Color Mapping (`c` + `cmap`):** Dimension 4 (e.g. Risk Level)

---

## 2. Dynamic Colors & Continuous Colormaps

### 1. Conditional Categorical Colors (List Comprehension):
```python
colors = ["green" if bp < 135 else "red" for bp in blood_pressure]
plt.scatter(age, blood_pressure, color=colors)
```

### 2. Continuous Colormap (`cmap`) with Colorbar:
```python
plt.scatter(age, blood_pressure, c=blood_pressure, cmap="OrRd", s=blood_pressure)
plt.colorbar(label="Blood Pressure Severity")
```
- Available colormaps: `'viridis'`, `'plasma'`, `'inferno'`, `'OrRd'`, `'coolwarm'`.

---

## 3. Code Implementation

```python
import matplotlib.pyplot as plt

age = [22, 25, 30, 35, 40, 45, 50, 55, 60, 65]
blood_pressure = [110, 115, 120, 122, 125, 130, 135, 123, 145, 150]

# 1. Discrete Conditional Colors + Dynamic Size
colors = ["seagreen" if bp < 135 else "crimson" for bp in blood_pressure]
sizes = [bp * 1.5 for bp in blood_pressure]

plt.figure(figsize=(9, 5))
plt.scatter(age, blood_pressure, color=colors, s=sizes, marker='^', alpha=0.7, edgecolor='black')
plt.title("Conditional Styling: Green = Normal (<135), Red = Elevated (>=135)", fontsize=13, fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.grid(True, linestyle=":", alpha=0.6)
plt.show()

# 2. Continuous Colormap with Colorbar
plt.figure(figsize=(9, 5))
scatter = plt.scatter(age, blood_pressure, c=blood_pressure, cmap="OrRd", s=120, edgecolor="black", alpha=0.9)
cbar = plt.colorbar(scatter)
cbar.set_label("Blood Pressure (mmHg)", fontsize=11)

plt.title("Color by Value using Colormap ('OrRd')", fontsize=14, fontweight="bold")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
```

---

## 📐 4D Multivariate Mathematical Mapping

A 2D Cartesian scatter canvas is formally extended to represent 4-dimensional observations $\mathbf{p}_i \in \mathbb{R}^4$:

$$
\boxed{\mathbf{p}_i = \begin{pmatrix} X_i \\ Y_i \\ S_i \\ C_i \end{pmatrix} \in \mathbb{R}^4}
$$

where visual channels correspond to formal mathematical transformations:
- **Abscissa ($X_i$)**: $X_i \in \mathbb{R}_{>0}$ (Primary continuous metric)
- **Ordinate ($Y_i$)**: $Y_i \in \mathbb{R}$ (Secondary continuous metric)
- **Marker Area ($S_i$)**: $S_i = \kappa \cdot h_i$ where area scales linearly with metric $h_i$ ($\kappa = 2.5$)
- **Color Metric ($C_i$)**: $C_i = \phi(v_i)$ where continuous metric $v_i$ is mapped through colormap function $\phi: [v_{\min}, v_{\max}] \to [0, 1]^3$

The optical transmission $I$ under marker overplotting follows the discrete Beer-Lambert model:
$$
\boxed{I_{\text{transmitted}} = I_0 \cdot (1 - \alpha)^m}
$$

---
## 4. Key Takeaways
- `c=` accepts an array of numerical values mapped through `cmap`, whereas `color=` takes static color strings or an array of literal color names.
- Always include `plt.colorbar()` when using `cmap` so viewers understand what the gradient represents.
