# Day 18 - Lecture 18.12: Horizontal Bar Charts (`plt.barh`) [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_12.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 18 Module Par Wapas Jayein](../README_HINGLISH.md)

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Horizontal bar chart ka syntax aur structure: `plt.barh(y, width)`.
- Kab horizontal orientation use karein: Long movie titles aur ranked lists.
- Axis roles ka reversal: Y-axis par categories aur X-axis par quantitative magnitude.
- Sorting aur ranking techniques: Data ko ascending order me arrange karke visual readability badhana.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

- **Long Label Readability**: Vertical bar charts me jab movie titles lambe hote hain (e.g., 'The King's Speech', 'Slumdog Millionaire'), tab labels aapas me collide karte hain ya unhe 90 degree rotate karna padta hai. `plt.barh()` me titles naturally left-to-right horizontal read hote hain.

- **Reversed Coordinate Roles**: `plt.barh(categories, values)` me pehla argument vertical Y-positions (categories) hota hai, aur doosra argument horizontal lengths (values) hota hai.

- **Natural Ranking**: Inverted order me plot karne se highest revenue movie top par aati hai jo business reports me standard executive view hota hai.

- **Lecture Code Reference**: Ma'am ne Oscar movies ke titles aur revenue ko `plt.barh(oscar_movies, oscar_revenue)` se clean layout me plot karke explain kiya.

---

## 2. Visual Architecture & Workflow Diagram

```mermaid
flowchart LR
    A["Input Data:<br/>Movies (Long Text Strings)<br/>Revenue (Numeric Quantities)"] --> B["Sort in Ascending Order<br/>(Top Performer on Top)"]
    B --> C["Render Horizontal Bars:<br/>plt.barh(movies, revenue, color='#41b6c4')"]
    C --> D["Configure Inverted Axes:<br/>X = Revenue Magnitude ($M)<br/>Y = Categorical Movie Titles"]
    D --> E["Clean Non-overlapping Horizontal Bar Chart"]
```

---

## 3. Mathematical & Theoretical Framework

A horizontal bar for item $i$ defines a rectangle aligned along the horizontal x-axis:

$$
R_i^{\text{horiz}} = [0, w_i] \times \left[ y_i - \frac{h}{2}, \; y_i + \frac{h}{2} \right]
$$

where $w_i$ represents the quantitative box office value and $h$ is the bar thickness (default $h = 0.8$).

---

## 4. Structured Implementation & Execution

```python
import matplotlib.pyplot as plt

def render_horizontal_bar_chart(categories: list, values: list, bar_color: str = "#41b6c4") -> dict:
    """
    Builds an uncluttered horizontal bar chart ideal for long string labels and rankings.
    
    Parameters:
    -----------
    categories : list of str
        Category names (e.g. movie titles).
    values : list of float
        Numerical values mapped to bar length.
    bar_color : str
        Hex color code for bars.
        
    Returns:
    --------
    dict
        Ranking metadata from top to bottom performer.
    """
    # Sort data ascending so top performer renders at the top
    sorted_pairs = sorted(zip(categories, values), key=lambda pair: pair[1])
    sorted_categories = [p[0] for p in sorted_pairs]
    sorted_values = [p[1] for p in sorted_pairs]
    
    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.barh(sorted_categories, sorted_values, color=bar_color, height=0.6, edgecolor='black', linewidth=0.7)
    
    ax.set_title("Movie Revenue Comparison (Horizontal Bar Chart)", fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel("Box Office Gross ($ Millions)", fontsize=11)
    ax.set_ylabel("Movie Titles", fontsize=11)
    
    # Add value labels at end of each bar
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 15, bar.get_y() + bar.get_height()/2, f"${int(width)}M", 
                va='center', fontsize=9.5, fontweight='bold', color='#333333')
        
    ax.set_xlim(0, max(sorted_values) * 1.15)
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
    
    return {
        "top_movie": sorted_categories[-1],
        "top_revenue": sorted_values[-1],
        "lowest_movie": sorted_categories[0],
        "lowest_revenue": sorted_values[0],
        "count": len(categories)
    }

# Lecture Data
oscar_movies = ["The Dark Knight", "The Hurt Locker", "The King's Speech", "The Artist", "Argo"]
oscar_revenue = [1005, 170, 427, 133, 232]

horiz_res = render_horizontal_bar_chart(oscar_movies, oscar_revenue)
print("Horizontal Bar Chart Ranking Summary:")
for k, v in horiz_res.items():
    print(f"  {k}: {v}")
```

---

## 5. Mukhya Batein (Key Takeaways) & Summary
- Code ko modular function ke roop me likha gaya hai jisme clear shuruat (`def`), docstrings, error handling, aur ending (`return`) maujood hai.
- Video lectures me ma'am dwara sikhaye gaye real movie box-office datasets aur syntax parameters ko exact follow kiya gaya hai.
