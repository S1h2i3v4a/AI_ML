# Day 18 - Lecture 18.13: Scatter Plots (`plt.scatter`) [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_13.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 18 Module Par Wapas Jayein](../README_HINGLISH.md)

---

## 1. Overview & Purpose
A **Scatter Plot** displays values for two numerical variables as points on a 2D plane.
Unlike line plots, **no line segments connect the points**. Each point represents a single observation or subject.

### Primary Use Cases:
- **Correlation Analysis:** Is there a positive, negative, or zero correlation between $X$ and $Y$?
- **Non-Linear Relationships:** Detecting curvilinear or exponential trends.
- **Clustering:** Detecting naturally occurring groupings in feature space.
- **Outlier Spotting:** Immediately locating isolated points far away from the main cluster.

---

## 2. Syntax & Basic Parameters

```python
plt.scatter(
    x,                      # Continuous independent variable
    y,                      # Continuous dependent variable
    s=None,                 # Marker size (scalar or array)
    c=None,                 # Marker color (scalar or array of values)
    marker='o',             # Shape: 'o', 's', '^', 'x', 'd'
    alpha=None,             # Transparency (0.0 to 1.0)
    linewidths=None,        # Border outline width
    edgecolors=None         # Border outline color
)
```

---

## 3. Real-World Case Study: Age vs. Blood Pressure

Medical analysis of 10 patients studying whether systolic blood pressure increases monotonically with age:

```python
import matplotlib.pyplot as plt

age = [22, 25, 30, 35, 40, 45, 50, 55, 60, 65]
blood_pressure = [110, 115, 120, 122, 125, 130, 135, 123, 145, 150]

plt.figure(figsize=(8, 5))
plt.scatter(age, blood_pressure, color="crimson", s=80, edgecolor="black", alpha=0.85)

plt.title("Medical Analysis: Age vs Blood Pressure", fontsize=14, fontweight="bold")
plt.xlabel("Age (years)", fontsize=12)
plt.ylabel("Blood Pressure (mmHg)", fontsize=12)
plt.grid(True, linestyle=":", alpha=0.6)
plt.show()
```

---

## 📐 Correlation aur Scatter Dispersion Ka Ganitiya Sutra

Scatter plot par continuous variables $(X, Y)$ ke pairs plot kiye jaate hain. Dono ke beech linear sambandh **Pearson Correlation Coefficient** $r_{xy}$ se nikala jaata hai:

$$
\boxed{r_{xy} = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^n (y_i - \bar{y})^2}} \in [-1, +1]}
$$

Covariance aur standard deviation ke roop me:
$$
\boxed{\text{Cov}(X, Y) = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) \implies r_{xy} = \frac{\text{Cov}(X, Y)}{s_x \cdot s_y}}
$$

---
## 4. Mukhya Batein (Key Takeaways)
- The Pearson correlation coefficient $r \approx 0.96$ indicates a strong positive linear relationship between age and blood pressure.
- Notice patient at Age 55 with BP 123 mmHg dips below the trendline—scatter plots make individual variances instantly visible.
