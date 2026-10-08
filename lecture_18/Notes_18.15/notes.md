# Day 18 - Lecture 18.15: Adding Annotations to Scatter Plots

## 1. Overview & Purpose
In exploratory medical, financial, or performance analysis, each dot in a scatter plot often corresponds to a specific **named entity** (e.g. *Patient A*, *Company X*, *City Y*).
Adding **annotations** attaches textual labels directly to coordinates so viewers can instantly identify individual points.

---

## 2. Syntax: `plt.annotate()` vs `plt.text()`

### Method 1: `plt.annotate()` (Recommended for point labeling)
```python
plt.annotate(
    text="Person A",
    xy=(age, bp),                   # Coordinate of the point being annotated
    xytext=(age + 0.8, bp + 1.2),   # Text position (offset to avoid overlapping the marker)
    arrowprops=dict(...)            # Optional pointer arrow
)
```

### Preventing Label Clipping with `plt.xlim()`:
When annotating the rightmost point (e.g., Age 65), the text label extends further to the right. Without adjusting axis limits, the text will be cropped!
```python
plt.xlim(min(age) - 2, max(age) + 10)
```

---

## 3. Code Implementation

```python
import matplotlib.pyplot as plt

people = ["Person A", "Person B", "Person C", "Person D", "Person E", 
          "Person F", "Person G", "Person H", "Person I", "Person J"]
age = [22, 25, 30, 35, 40, 45, 50, 55, 60, 65]
blood_pressure = [110, 115, 120, 122, 125, 130, 135, 123, 145, 150]

plt.figure(figsize=(10, 6))
plt.scatter(age, blood_pressure, c=blood_pressure, cmap="OrRd", s=130, edgecolor="black", alpha=0.9)
plt.colorbar(label="Blood Pressure (mmHg)")

# Loop through and annotate each person
for i in range(len(age)):
    plt.annotate(
        text=people[i],
        xy=(age[i], blood_pressure[i]),
        xytext=(age[i] + 0.8, blood_pressure[i] + 0.5), # Slight offset to top-right
        fontsize=9,
        fontweight='semibold'
    )

# Add padding to right margin so Person J is not cut off
plt.xlim(min(age) - 3, max(age) + 8)

plt.title("Age vs Blood Pressure with Patient Annotations", fontsize=14, fontweight="bold")
plt.xlabel("Age (Years)", fontsize=12)
plt.ylabel("Blood Pressure (mmHg)", fontsize=12)
plt.grid(True, linestyle=":", alpha=0.6)
plt.show()
```

---

## 📐 Vector Annotation & Directed Callout Mathematics

An annotation arrow represents a directed displacement vector $\mathbf{v} \in \mathbb{R}^2$ connecting text coordinate $\mathbf{x}_{\text{text}}$ to target data point $\mathbf{x}_{\text{target}}$:

$$
\boxed{\mathbf{v} = \mathbf{x}_{\text{target}} - \mathbf{x}_{\text{text}} = \begin{pmatrix} x_{\text{target}} - x_{\text{text}} \\ y_{\text{target}} - y_{\text{text}} \end{pmatrix}}
$$

The Euclidean length and directional angle $\theta$ of the callout arrow are:
$$
\boxed{\|\mathbf{v}\|_2 = \sqrt{(x_{\text{target}} - x_{\text{text}})^2 + (y_{\text{target}} - y_{\text{text}})^2} \qquad\text{and}\qquad \theta = \operatorname{atan2}(v_y, v_x)}
$$

---
## 4. Key Takeaways
- Always apply an offset (`x + dx`, `y + dy`); placing text at the exact point coordinate will superimpose text directly over the marker symbol.
- Use `plt.xlim()` and `plt.ylim()` padding whenever annotations sit near the plot periphery.
