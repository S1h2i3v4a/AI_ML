# Day 18 - Lecture 18.8: Common Plots & Charts Taxonomy

## 1. Overview & Chart Taxonomy
Choosing the right chart is the single most important skill in data visualization. Using the wrong chart distorts findings and confuses stakeholders.

```mermaid
flowchart TD
    Data{"What kind of data do you have?"}
    Data -->|"Continuous Progression over Time"| Line["Line Plot (plt.plot)"]
    Data -->|"Discrete Categories comparison"| Bar["Bar Chart (plt.bar / plt.barh)"]
    Data -->|"Relationship between 2 Continuous Variables"| Scatter["Scatter Plot (plt.scatter)"]
    Data -->|"Relative Proportions / Part-to-Whole"| Pie["Pie Chart (plt.pie)"]
    Data -->|"Distribution of 1 Continuous Variable"| Hist["Histogram (plt.hist)"]
```

---

## 2. Summary Chart Selection Guide

| Chart Type | Best Used When... | Avoid When... |
| :--- | :--- | :--- |
| **Line Plot** | Tracking trends and continuous sequential changes (time series) | Categories have no natural ordering |
| **Bar Chart** | Comparing numerical values across discrete categories | Data is continuous without groupings |
| **Scatter Plot** | Detecting correlations, clusters, and relationships between two continuous variables | Variables are pure categorical names |
| **Pie Chart** | Showing proportions of a whole for a very small number of categories (3–5 max) | More than 5 categories or comparing subtle differences |
| **Histogram** | Showing frequency distribution, skewness, and spread of continuous values | Data is discrete categories (use Bar Chart instead) |

---

## 3. Key Takeaways
- **The Golden Rule:** Always identify whether your variables are **continuous (quantitative)** or **categorical (qualitative)** before selecting a chart type.


---

## 📐 Visual Encoding Channel Capacity & Dimensionality

Information visualization maps raw data attributes $\mathcal{D} = \{d_1, d_2, \dots, d_m\}$ into orthogonal visual channels $\mathcal{V} = \{\text{position}, \text{length}, \text{hue}, \text{area}, \text{shape}\}$:

$$
\boxed{\Phi: \mathcal{D}_1 \times \mathcal{D}_2 \times \dots \times \mathcal{D}_m \to \mathcal{V}_1 \times \mathcal{V}_2 \times \dots \times \mathcal{V}_m}
$$

According to Cleveland and McGill's psychophysical hierarchy, positional and length encodings exhibit minimal decoding error $\epsilon$, while area and color encodings have higher perceptual error variance:
$$
\boxed{\epsilon_{\text{position}} < \epsilon_{\text{length}} < \epsilon_{\text{angle}} < \epsilon_{\text{area}} < \epsilon_{\text{color intensity}}}
$$
