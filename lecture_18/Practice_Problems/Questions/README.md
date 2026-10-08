# 📝 Lecture 18: Practice Problems — Question Set

[![Notebook](https://img.shields.io/badge/Jupyter-questions.ipynb-orange.svg?logo=jupyter&logoColor=white)](questions.ipynb)
[![PDF](https://img.shields.io/badge/PDF-questions.pdf-red.svg)](questions.pdf)
[![Solutions](https://img.shields.io/badge/Solutions-Available-success.svg)](../Solutions/README.md)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [💡 View Complete Solutions](../Solutions/README.md) | [⬅️ Back to Practice Problems Overview](../README.md)

---

## 🎯 Comprehensive Case-Based & Technical Challenges

This problem set evaluates your mastery across all concepts taught in **Lecture 18 (Matplotlib Fundamentals, Methods, Styling, Bars, Scatter, & Pie Charts)**.

---

## 📌 Case 1: SaaS YoY Revenue Growth & Executive Reporting
### 🏢 **Domain**: B2B SaaS Growth & Business Intelligence
### 🎯 **Tested Topics**: Lecture 18.01 – 18.07 (Visual Perception, Matplotlib Architecture, Line Plots, Format Strings, Figure Styling, & Production Export)

### 📖 **Business Scenario**:
You are the **Lead Data Analyst** at a high-growth B2B SaaS startup. During the upcoming annual board meeting, the CEO and investment partners need to evaluate monthly revenue trajectory differences between Fiscal Year 2023 and Fiscal Year 2024.

You have extracted the following financial metrics:
- **Months**: `['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']`
- **FY 2023 Revenue (Lakhs ₹)**: `[12, 14, 15, 18, 19, 22, 24, 25, 28, 30, 31, 35]`
- **FY 2024 Revenue (Lakhs ₹)**: `[15, 18, 22, 25, 29, 34, 38, 42, 45, 50, 54, 60]`

The deliverables must be embedded into an A4 print-ready executive memo as well as presented on a 4K auditorium display.

### ❓ **Problem Statements & Questions to Solve**:
1. **Perception & Chart Selection Theory**:
   - Why is a multi-series **Line Plot** mathematically and cognitively superior to a tabular summary or a vertical bar chart for this specific use case? Refer to Edward Tufte's *Data-Ink Ratio* and Anscombe's Quartet principles.
2. **Technical Implementation (Multi-Series & Fast Format Strings)**:
   - Construct a Matplotlib visualization using fast format strings (`fmt`):
     - FY 2023: Green dashed line with circular markers (`'go--'`), line width 2, marker size 7.
     - FY 2024: Blue solid line with square markers (`'bs-'`), line width 2.5, marker size 8.
   - Include:
     - Clear axis labels with measurement units (`₹ in Lakhs`).
     - Subtle grid styling (`linestyle=':'`, `alpha=0.6`, `color='gray'`).
     - An upper-left legend with frame and drop shadow enabled (`frameon=True`, `shadow=True`).
3. **Production Export & DPI Tuning**:
   - Default Matplotlib figures often produce clipped axis labels and blurry raster artifacts when projected on high-resolution displays. Specify how `figsize`, `dpi`, and `plt.savefig()` parameters (`bbox_inches='tight'`) should be configured to prevent clipping and ensure crisp 300 DPI vector/raster export.

---

## 📌 Case 2: Enterprise Financial Audit & Spending Variance
### 🏢 **Domain**: Corporate Finance & Operational Analytics
### 🎯 **Tested Topics**: Lecture 18.08 – 18.12 (Chart Taxonomy, Vertical & Horizontal Bars, Index Offsets, & Direct Labeling)

### 📖 **Business Scenario**:
An enterprise technology corporation is conducting its annual expenditure audit across five major operational departments:
- **Departments**: `['R&D / Innovation', 'Brand Marketing', 'Global Sales', 'Human Resources', 'Cloud Infrastructure']`
- **Allocated Budget (Crores ₹)**: `[45, 30, 60, 15, 40]`
- **Actual Spend (Crores ₹)**: `[48, 26, 68, 14, 47]`

A junior analyst attempted to plot this comparative data using the following code:
```python
# Junior Analyst's Attempt
plt.bar(Departments, Allocated_Budget, color='blue', label='Budget')
plt.bar(Departments, Actual_Spend, color='orange', label='Actual')
plt.legend()
plt.show()
```

### 🚨 **Audit Deficiencies**:
- The two datasets completely overlap instead of displaying side-by-side.
- The department text strings collide on the horizontal X-axis, making labels illegible.
- Executives cannot determine exact surplus/deficit amounts without zooming in and guessing coordinates.

### ❓ **Problem Statements & Questions to Solve**:
1. **Mathematical Coordinate Offset Derivation**:
   - Explain mathematically how `np.arange(len(departments))` and a custom `bar_width` (e.g., `0.35`) are used to shift the two bars side-by-side with zero overlap.
   - Where must the categorical ticks (`plt.xticks`) be placed so that department names align precisely between both bars?
2. **Direct Numerical Annotation**:
   - Implement direct value labels on top of each bar (e.g., `₹45Cr`).
   - Compare the traditional `plt.text(x, y, text, ha='center', va='bottom')` approach with the modern Matplotlib `ax.bar_label()` container method.
3. **Horizontal Transformation (`plt.barh`)**:
   - Due to the lengthy department names, convert the visualization into an executive **Horizontal Grouped Bar Chart (`plt.barh`)**.
   - Ensure the highest-priority department appears at the top using `ax.invert_yaxis()`.

---

## 📌 Case 3: Venture Capital Portfolio & Sector Allocation
### 🏢 **Domain**: Venture Capital & Private Equity Analytics
### 🎯 **Tested Topics**: Lecture 18.13 – 18.18 (Scatter Plots, 4D Visual Encoding, Annotations with Arrows, & Donut/Pie Charts)

### 📖 **Business Scenario**:
A venture capital investment committee is evaluating 50 portfolio AI startups across multiple quantitative dimensions simultaneously:
1. **Total Funding Raised** ($ Millions)
2. **Annual Revenue Growth Rate** (%)
3. **Team Size / Headcount** (Total employees)
4. **Valuation Tier** (Score from 1 to 10)

Additionally, the partners require a visual breakdown of how fund capital is currently distributed across five emerging AI domains:
- `LLMs & Generative AI`: 40%
- `Robotics & Automation`: 20%
- `Computer Vision`: 15%
- `FinTech AI`: 15%
- `Healthcare AI`: 10%

### ❓ **Problem Statements & Questions to Solve**:
1. **4D Multivariate Visual Encoding**:
   - How can a 2D Cartesian plane encode four distinct data attributes simultaneously using `plt.scatter()`?
   - Detail the mapping of:
     - $X$-axis $\to$ Funding Raised
     - $Y$-axis $\to$ Annual Growth
     - Marker Size (`s`) $\to$ Employee Headcount
     - Color (`c` & `cmap`) $\to$ Valuation Tier
   - Why is the `alpha` (transparency) parameter critical when visualizing dense clusters (overplotting)?
2. **Strategic Outlier Annotation (`plt.annotate`)**:
   - One standout startup (`Apex AI`: Funding = $50M, Growth = 420%, Team = 250) represents the portfolio's star unicorn.
   - Implement `plt.annotate()` with custom pointer arrows (`arrowprops`) and a highlighted bounding box (`bbox`) pointing from an empty section of the figure directly to the outlier point.
3. **Compositional Visualizations: Pie vs. Donut Chart Trade-offs**:
   - From a human perception standpoint, why are standard pie charts often discouraged in statistical literature?
   - Implement a modern **Donut Chart** for the five AI domains:
     - Explode the primary sector (`LLMs & Generative AI`) outward (`explode=[0.08, 0, 0, 0, 0]`).
     - Display formatted percentage labels (`autopct='%1.1f%%'`).
     - Create a hollow center wedge using a white circular patch or `wedgeprops=dict(width=...)`.
