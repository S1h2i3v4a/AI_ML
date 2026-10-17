# Day 18 - Lecture 18.10: Adding Labels to Bars (`plt.text`) [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_10.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 18 Module Par Wapas Jayein](../README_HINGLISH.md)

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Bar charts ke top par exact data labels lagane ka method: `plt.text()`.
- Function parameters ka breakdown: `x` position, `y` height + offset, text string, aur horizontal alignment (`ha='center'`).
- Data label collision aur top border clipping prevent karne ke liye dynamic headroom calculation (`plt.ylim`).
- Modern alternative: `ax.bar_label()` vs foundational loop-based `plt.text()`.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

- **Kyu Lagate Hain Bar Labels**: Jab bar ki height 1005 hoti hai, to Y-axis grid dekh kar viewer sirf andaza laga sakta hai ki value ~1000 hai. Top par '1005' print karne se viewer ko exact data turant mil jata hai.

- **`plt.text()` Positioning Logic**: `plt.text(x, y, text)` me `x` bar ka center coordinate hota hai, aur `y` bar ki height plus thoda sa vertical buffer (e.g., `revenue[i] + 20`) hota hai taaki label bar ke andar merge na ho.

- **Alignment Rule (`ha='center'`)**: `ha='center'` ensure karta hai ki text string ka horizontal center bar ke x-center ke bilkul upar aligned rahe.

- **Lecture Code Reference**: Ma'am ne exact yeh loop sikhaya tha: `for i in range(len(revenue)): plt.text(years[i], revenue[i] + 20, str(revenue[i]), ha='center')`.

---

## 2. Visual Architecture & Workflow Diagram

```mermaid
flowchart TD
    A["Iterate over Data Bars:<br/>i = 0, 1, ..., len(revenue)-1"] --> B["Compute Label Placement:<br/>x_pos = years[i]<br/>y_pos = revenue[i] + vertical_offset"]
    B --> C["Format Numeric Value:<br/>label_str = f'${revenue[i]}M'"]
    C --> D["Render Text Element:<br/>plt.text(x_pos, y_pos, label_str, ha='center')"]
    D --> E["Expand Ceiling Buffer:<br/>plt.ylim(0, max_val + offset * 5)"]
```

---

## 3. Mathematical & Theoretical Framework

For each bar index $i \in \{1, 2, \dots, N\}$, the label text anchor coordinate is positioned at:

$$
(x_{\text{label}}, y_{\text{label}})_i = \left( x_i, \; h_i + \delta_y \right)
$$

where $\delta_y = \gamma \cdot \max(h)$ is a proportional vertical clearance offset (typically $\gamma \approx 0.02$). The y-axis upper limit must satisfy:

$$
y_{\max} \ge \max(h) + 2\delta_y + \text{fontsize\_offset}
$$

---

## 4. Structured Implementation & Execution

```python
import matplotlib.pyplot as plt

def render_bar_chart_with_direct_labels(years: list, revenue: list, bar_color: str = "#8856a7") -> dict:
    """
    Generates a vertical bar chart with exact numerical labels positioned atop each bar.
    
    Parameters:
    -----------
    years : list of int
        Categorical year timeline.
    revenue : list of float
        Revenue values for each corresponding year.
    bar_color : str
        Hex color for the vertical bars.
        
    Returns:
    --------
    dict
        Metadata of rendered labels including coordinates and text values.
    """
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    bars = ax.bar(years, revenue, color=bar_color, width=0.55, edgecolor='black', linewidth=0.8)
    
    max_rev = max(revenue)
    vertical_offset = max_rev * 0.025  # Dynamic clearance offset
    
    label_records = []
    # Iterative labeling loop as taught in lecture
    for i in range(len(revenue)):
        x_pos = years[i]
        y_pos = revenue[i] + vertical_offset
        text_val = str(revenue[i])
        
        ax.text(x_pos, y_pos, text_val, ha="center", va="bottom", fontsize=10, fontweight='bold', color="#222222")
        label_records.append({"year": x_pos, "label_y": y_pos, "text": text_val})
        
    ax.set_title("Yearly Revenue of Movies (With Direct Labels)", fontsize=13, fontweight='bold', pad=14)
    ax.set_xlabel("Release Years", fontsize=11)
    ax.set_ylabel("Revenue ($ Millions)", fontsize=11)
    
    # Expand upper limit to give breathing room for labels
    ax.set_ylim(0, max_rev + (max_rev * 0.20))
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.show()
    
    return {
        "total_bars_labeled": len(label_records),
        "labels_rendered": label_records,
        "upper_bound_ylim": max_rev + (max_rev * 0.20)
    }

# Lecture Data
years = [2008, 2009, 2010, 2011, 2012]
revenue = [1005, 170, 427, 133, 232]

label_info = render_bar_chart_with_direct_labels(years, revenue)
print("Bar Labeling Metadata:")
print(f"  Total Labels: {label_info['total_bars_labeled']}")
print(f"  Ceiling Limit: {label_info['upper_bound_ylim']}")
```

---

## 5. Mukhya Batein (Key Takeaways) & Summary
- Code ko modular function ke roop me likha gaya hai jisme clear shuruat (`def`), docstrings, error handling, aur ending (`return`) maujood hai.
- Video lectures me ma'am dwara sikhaye gaye real movie box-office datasets aur syntax parameters ko exact follow kiya gaya hai.
