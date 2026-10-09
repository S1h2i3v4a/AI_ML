# 💡 Lecture 18: Practice Problems — Comprehensive Solutions [Hinglish]

[![Notebook](https://img.shields.io/badge/Jupyter-solutions.ipynb-orange.svg?logo=jupyter&logoColor=white)](solutions.ipynb)
[![PDF](https://img.shields.io/badge/PDF-solutions.pdf-red.svg)](solutions.pdf)
[![Report](https://img.shields.io/badge/Report-saas__revenue__report.png-blue.svg)](saas_revenue_report.png)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [❓ Questions Par Wapas Jayein](../Questions/README_HINGLISH.md) | [⬅️ Practice Problems Overview Par Wapas Jayein](../README_HINGLISH.md)

---

## 📘 In-Depth Theoretical Analysis, Code Implementations & Best Practices

Is document me **Lecture 18 Practice Problem Set** ke sabhi teeno case-based problems ka production-grade solution, mathematical derivation aur code explanation diya gaya hai.

---

# 📌 Case 1 Solution: SaaS YoY Revenue Growth & Executive Reporting

### 1. Perception & Chart Selection Theory
- **Visual Encoding of Temporal Continuity**:
  Human perception naturally connected lines ko samay ke sath badlaav (rate of change, velocity) ke roop me read karta hai. Agar time-series ke liye bar chart use karein, toh har bar alag-alag disconnected event jaisa lagta hai na ki continuous trajectory.
- **Anscombe's Quartet & Data-Ink Ratio Formulation**:
  Table me dekhkar growth ka turning point (inflection point) samajhna mushkil hota hai. Do datasets ka mean aur variance same ho sakta hai par trend bilkul alag ho sakta hai. Multi-series line plot Edward Tufte ke **Data-Ink Ratio** $\eta$ ko maximize karta hai:

$$
  \boxed{
  \eta = \frac{\mathcal{I}_{\text{data}}}{\mathcal{I}_{\text{total}}} = 1.0 - \frac{\mathcal{I}_{\text{non-data}}}{\mathcal{I}_{\text{total}}}
  }
$$

  Jahan:
  - $\mathcal{I}_{\text{data}}$: Keval useful data information dikhane wali ink (lines, points, markers).
  - $\mathcal{I}_{\text{total}}$: Pure chart ki total ink (background, grids, borders, ticks).
  - Domain: $\eta \in (0, 1]$, aur sabse efficient chart tab hota hai jab $\eta \to 1.0$.

---

### 2. Complete Python Implementation
```python
import matplotlib.pyplot as plt

# Monthly Financial Datasets
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rev_2023 = [12, 14, 15, 18, 19, 22, 24, 25, 28, 30, 31, 35]
rev_2024 = [15, 18, 22, 25, 29, 34, 38, 42, 45, 50, 54, 60]

# 1. Establish high-resolution figure canvas (12 x 6 inches)
plt.figure(figsize=(12, 6), dpi=300)

# 2. Multi-dataset line plots utilizing fast format strings ('fmt')
# 'go--' -> green color ('g'), circle marker ('o'), dashed line ('--')
# 'bs-'  -> blue color ('b'), square marker ('s'), solid line ('-')
plt.plot(months, rev_2023, 'go--', linewidth=2, markersize=7, label='FY 2023 Revenue')
plt.plot(months, rev_2024, 'bs-', linewidth=2.5, markersize=8, label='FY 2024 Revenue')

# 3. Informative axis titling and hierarchy
plt.title('SaaS Monthly Recurring Revenue (MRR) YoY Comparison', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Fiscal Month', fontsize=12, fontweight='semibold')
plt.ylabel('Revenue (in Lakhs ₹)', fontsize=12, fontweight='semibold')

# 4. Subtle grid and executive legend styling
plt.grid(True, linestyle=':', alpha=0.6, color='gray')
plt.legend(loc='upper left', frameon=True, shadow=True, facecolor='#f8f9fa', fontsize=11)

# 5. Production export avoiding label clipping
plt.savefig('saas_revenue_report.png', dpi=300, bbox_inches='tight', transparent=False)
plt.show()
```

---

### 3. Production Export Analysis
- **Default export me kya problem aati hai**:
  By default `plt.savefig()` screen DPI (72-100 DPI) use karta hai, jisse 4K screens ya print paper par chart blur dikhta hai. Saath hi padding na hone par titles aur labels boundaries par cut jate hain.
- **Solution**:
  `dpi=300` crisp print quality deta hai, aur `bbox_inches='tight'` figure ke sabhi elements (titles, ticks, legends) ko auto-adjust karke label cut hone se bachata hai.

---

# 📌 Case 2 Solution: Enterprise Financial Audit & Spending Variance

### 1. Mathematical Coordinate Offset Derivation
Maan lijiye $N$ total departments hain aur $K = 2$ comparative series hain ($\text{Series}_1$: Budget, $\text{Series}_2$: Spend).

#### Definition 1 (Baseline Categorical Domain):
Category axis par $i$-th category ka discrete base index:

$$
x_i = i, \quad \forall i \in \{0, 1, 2, \dots, N-1\}
$$

#### Condition 1 (Non-Overlapping Criterion):
Agar uniform bar width $w$ hai, toh bars ke beech takraav na hone ke liye:

$$
K \cdot w < 1.0 \implies w < \frac{1}{K} = \frac{1}{2} = 0.5 \quad \left(\text{Chuna gaya: } w = 0.38\right)
$$

#### Symmetrical Shifted Coordinates:
Category $i$ ke liye shifted coordinates $(y_{1, i}, y_{2, i})$:

$$
\begin{cases}
y_{1, i} = x_i - \dfrac{w}{2} \\
y_{2, i} = x_i + \dfrac{w}{2}
\end{cases}
$$

jahan $y_{1, i}$ Series 1 (Budget) ka center coordinate hai aur $y_{2, i}$ Series 2 (Spend) ka center coordinate hai.

#### Center Tick Alignment Formula:
Category name tick mark $t_i$ dono bars ke bilkul theek beech me aane ke liye:

$$
\boxed{
t_i = \frac{y_{1, i} + y_{2, i}}{2} = \frac{\left(x_i - \dfrac{w}{2}\right) + \left(x_i + \dfrac{w}{2}\right)}{2} = x_i
}
$$

Isliye tick labels direct unshifted coordinate $x_i$ par set kiye jate hain.

---

### 2. Complete Python Implementation (Horizontal Grouped Bar Chart)
```python
import matplotlib.pyplot as plt
import numpy as np

departments = ['R&D / Innovation', 'Brand Marketing', 'Global Sales', 'Human Resources', 'Cloud Infrastructure']
budget = [45, 30, 60, 15, 40]
spend = [48, 26, 68, 14, 47]

# 1. Coordinate Offsets
y_indices = np.arange(len(departments))
bar_height = 0.38

fig, ax = plt.subplots(figsize=(11, 6), dpi=150)

# 2. Render horizontal bars
bars_budget = ax.barh(y_indices - bar_height/2, budget, height=bar_height, color='#2b5c8f', label='Allocated Budget')
bars_spend = ax.barh(y_indices + bar_height/2, spend, height=bar_height, color='#d95f02', label='Actual Spend')

# 3. Direct Labeling using modern ax.bar_label() container method
ax.bar_label(bars_budget, fmt='₹%dCr', padding=4, fontsize=9, color='#2b5c8f', fontweight='bold')
ax.bar_label(bars_spend, fmt='₹%dCr', padding=4, fontsize=9, color='#d95f02', fontweight='bold')

# 4. Axis ticks and Top-to-Bottom priority inversion
ax.set_yticks(y_indices)
ax.set_yticklabels(departments, fontsize=11, fontweight='semibold')
ax.invert_yaxis() # R&D sabse upar dikhega

# 5. Decoration
ax.set_xlabel('Expenditure (in Crores ₹)', fontsize=12, fontweight='bold')
ax.set_title('Departmental Budget Allocation vs. Actual Expenditure Audit', fontsize=14, fontweight='bold', pad=12)
ax.legend(loc='lower right', frameon=True, shadow=True)
ax.grid(axis='x', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
```

---

### 3. Comparison: `plt.text()` vs `ax.bar_label()`
- **Classic `plt.text()` loop**:
  Har bar ke upar manually loop chala kar coordinate calculate karna padta hai, jisme offset error hone ka risk rehta hai.
- **Modern `ax.bar_label()` (Matplotlib $\ge$ 3.4)**:
  `BarContainer` object leta hai, automatic alignment handle karta hai, aur single line me bina error number labels lagata hai.

---

# 📌 Case 3 Solution: Venture Capital Portfolio & Sector Allocation

### 1. 4D Visual Encoding & Alpha Transparency
2D plane par ek sath 4 dimensions ko encode karne ka mathematical model:

$$
\mathcal{P}_i = \left( X_i, \; Y_i, \; S_i, \; C_i \right) \in \mathbb{R}^4
$$

Mapping:

$$
\mathbf{p}_i = \begin{pmatrix} X_i \\ Y_i \\ S_i \\ C_i \end{pmatrix} \in \mathbb{R}^4
$$

jahan har visual channel ek mathematical mapping darshata hai:
- **Abscissa ($X_i$)**: $X_i \in \mathbb{R}_{>0}$ (Total Funding Raised, Millions USD me)
- **Ordinate ($Y_i$)**: $Y_i \in \mathbb{R}$ (Annual Revenue Growth Rate, percentage me)
- **Marker Area ($S_i$)**: $S_i = \kappa \cdot h_i$ (Employee headcount $h_i$ ke anusaar scaled area, jahan $\kappa = 2.5$)
- **Color Metric ($C_i$)**: $C_i = \phi(v_i)$ (Valuation score $v_i \in [1, 10]$ ko Viridis colormap function $\phi: [1, 10] \to [0, 1]^3$ me map karta hai)

#### Overplotting & Alpha ($\alpha$):
Jab multiple points aapas me chipak jate hain (overplotting), tab transparency model:

$$
\boxed{
I_{\text{transmitted}} = I_0 \cdot (1 - \alpha)^m
}
$$

Jahan points ki density $m$ badhne par intensity exponentially drop hoti hai aur human eye ko dense cluster turant samajh aa jata hai.

---

### 2. Complete Python Implementation (4D Scatter + Arrow Annotation)
```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
n_startups = 50
funding = np.random.uniform(2, 60, n_startups)
growth = funding * 5 + np.random.normal(0, 30, n_startups)
team_size = np.random.uniform(10, 200, n_startups)
valuation_tier = np.random.uniform(1, 10, n_startups)

# Injected Outlier (Apex AI)
funding = np.append(funding, [50])
growth = np.append(growth, [420])
team_size = np.append(team_size, [250])
valuation_tier = np.append(valuation_tier, [10])

plt.figure(figsize=(11, 6), dpi=150)

# 4D Scatter Execution
scatter = plt.scatter(
    funding, growth, 
    s=team_size * 2.5, 
    c=valuation_tier, 
    cmap='viridis', 
    alpha=0.75, 
    edgecolors='black', 
    linewidth=1
)

cbar = plt.colorbar(scatter)
cbar.set_label('Valuation Tier (1 - 10)', fontsize=11, fontweight='semibold')

# Pinpoint Outlier Annotation
plt.annotate(
    'Outlier Unicorn: Apex AI\n(Funding: $50M, Growth: 420%)',
    xy=(50, 420),
    xytext=(25, 380),
    arrowprops=dict(facecolor='crimson', shrink=0.05, width=2, headwidth=8),
    bbox=dict(boxstyle='round,pad=0.5', facecolor='#fffae6', edgecolor='crimson', lw=1.5),
    fontsize=10,
    fontweight='bold'
)

plt.title('AI Startup Portfolio: 4D Multi-Attribute Investment Landscape', fontsize=14, fontweight='bold', pad=12)
plt.xlabel('Total Funding Raised ($ Millions)', fontsize=12, fontweight='semibold')
plt.ylabel('Annual Revenue Growth Rate (%)', fontsize=12, fontweight='semibold')
plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()
```

---

### 3. Compositional Visualizations: Donut Chart Implementation
```python
import matplotlib.pyplot as plt

sectors = ['LLMs & Generative AI', 'Robotics & Automation', 'Computer Vision', 'FinTech AI', 'Healthcare AI']
allocations = [40, 20, 15, 15, 10]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
explode = (0.08, 0, 0, 0, 0) # Explode leading generative AI sector

plt.figure(figsize=(8, 8), dpi=150)

# Outer pie with wedge width
wedges, texts, autotexts = plt.pie(
    allocations,
    explode=explode,
    labels=sectors,
    autopct='%1.1f%%',
    pctdistance=0.78,
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.42, edgecolor='white', linewidth=2)
)

for at in autotexts:
    at.set_color('white')
    at.set_weight('bold')
    at.set_fontsize(11)

plt.title('Venture Capital Fund Allocation across Emerging AI Sectors', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()
```
