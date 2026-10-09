# Day 18 - Lecture 18.6: Format Strings (`fmt`)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_06.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Lecture 18 Module](../README.md)

---

## 1. Overview & Syntax
In Matplotlib, a **Format String** (`fmt`) provides an ultra-compact shorthand to specify **marker**, **line style**, and **color** in a single string argument:

$$\text{fmt} = \text{'[marker][linestyle][color]'} \quad \text{or} \quad \text{'[color][marker][linestyle]'}$$

### Examples:
- `'o-b'`: Circle marker (`o`), Solid line (`-`), Blue color (`b`)
- `'>--g'`: Triangle-right marker (`>`), Dashed line (`--`), Green color (`g`)
- `'r:'`: Red color (`r`), Dotted line (`:`), No marker
- `'ks'`: Black color (`k`), Square marker (`s`), No line

---

## 2. Format String Components Reference Table

| Marker Codes | Line Styles | Color Codes |
| :--- | :--- | :--- |
| `.` (point) | `-` (solid) | `b` (blue) |
| `o` (circle) | `--` (dashed) | `g` (green) |
| `s` (square) | `-.` (dash-dot) | `r` (red) |
| `^` (triangle up) | `:` (dotted) | `c` (cyan) |
| `>` (triangle right) | *(omitted = no line)* | `m` (magenta) |
| `x` (cross) / `+` (plus) | | `y` (yellow) |
| `*` (star) / `d` (diamond) | | `k` (black) / `w` (white) |

---

## 3. Shorthand vs. Explicit Keyword Arguments

Format strings are quick, but explicit keyword arguments offer granular control:
```python
# Shorthand (Format String):
plt.plot(x, y, "o-b", label="Winners")

# Equivalent Explicit Keyword Arguments:
plt.plot(x, y, color="blue", linestyle="-", marker="o", linewidth=2, markersize=8, label="Winners")
```

---

## 4. Code Implementation

```python
import matplotlib.pyplot as plt

years = [2008, 2009, 2010, 2011, 2012]
oscar_revenue = [1005, 170, 427, 133, 232]
non_oscar_revenue = [378, 2788, 829, 185, 275]

plt.figure(figsize=(9, 5))

# 1. Shorthand Format String
plt.plot(years, oscar_revenue, "o-b", label="Oscar (fmt: 'o-b')")
plt.plot(years, non_oscar_revenue, ">--g", label="Non-Oscar (fmt: '>--g')")

# 2. Detailed explicit styling
plt.plot(years, [r * 0.5 for r in oscar_revenue], color="black", linestyle=":", marker="s", 
         linewidth=2, markersize=6, label="Half Revenue (Explicit kwargs)")

plt.title("Format Strings Demonstration", fontsize=14, fontweight='bold')
plt.xlabel("Years")
plt.ylabel("Revenue ($M)")
plt.legend()
plt.grid(True)
plt.show()
```

---

## 5. Key Takeaways
- Use format strings for rapid prototyping and notebooks.
- Use explicit keyword arguments (`color`, `linestyle`, `linewidth`, `marker`) in production code for readability and maintainability.


---

## 📐 Axis Range Discretization & Aspect Ratio Mathematics

Grid and tick interval placement along continuous interval $[x_{\min}, x_{\max}]$ with $k$ major ticks follows uniform discretization:

$$
\boxed{\Delta x = \frac{x_{\max} - x_{\min}}{k - 1}}
$$

The optical aspect ratio ($\text{AR}$) of the visual data curve on a canvas of physical width $W$ and height $H$ is:

$$
\boxed{\text{AR} = \left(\frac{y_{\max} - y_{\min}}{x_{\max} - x_{\min}}\right) \cdot \left(\frac{W}{H}\right)}
$$

Maintaining an aspect ratio close to $1.0$ (or banking slopes to $45^\circ$) minimizes perceptual error in trend judgment.
