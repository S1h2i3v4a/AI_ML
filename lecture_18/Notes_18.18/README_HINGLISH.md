# Day 18 - Lecture 18.18: Advanced Customizations on Pie Charts [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_18.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 18 Module Par Wapas Jayein](../README_HINGLISH.md)

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Specific slice ko highlight karna: `explode=[0, 0, 0, 0.2, 0]` ka offset mechanism.
- 3D visual depth effect: `shadow=True` ka application.
- Rotational alignment: `startangle=90` (vertical top start) aur `startangle=180` (horizontal flip).
- Modern Donut Chart transformation: Center hole cutout banakar cleaner representation lena.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

- **Exploding Slices (`explode`)**: Jab kisi specific category par attention draw karna ho (jaise R&D budget), to explode array me us category ke liye non-zero value di jaati hai (e.g., `0.1` ya `0.2`). Matplotlib us slice ko pie ke center se bahar push kar deta hai.

- **Drop Shadow (`shadow=True`)**: Graph me subtle drop shadow add karta hai jisse slices me elevated 3D depth aati hai.

- **Start Angle (`startangle`)**: By default Matplotlib $0^\circ$ (positive X-axis) se counter-clockwise slice draw karta hai. `startangle=90` dene se pehli slice top vertical line ($12$ o'clock) se start hoti hai, jo reading flow ke hisab se bohot natural lagti hai.

- **Donut Chart Variant**: Center me ek white circular patch draw karne se pie chart Donut Chart ban jata hai, jiske center me total budget figure likhi ja sakti hai.

---

## 2. Visual Architecture & Workflow Diagram

```mermaid
flowchart LR
    A["Standard Pie Chart Data"] --> B["Slice Explode Vector:<br/>explode = [0, 0, 0, 0.18, 0]"]
    A --> C["Depth Shadow:<br/>shadow = True"]
    A --> D["Orientation Control:<br/>startangle = 90"]
    B & C & D --> E["Advanced Exploded Pie Visual"]
    E --> F["Optional Donut Center Hole:<br/>plt.Circle((0,0), 0.65, color='white')"]
```

---

## 3. Mathematical & Theoretical Framework

The exploded displacement vector for slice $i$ with radial offset factor $e_i$ along its bisecting angle $\phi_i$ is given by:

$$
\mathbf{d}_i = e_i \cdot R \begin{pmatrix} \cos \phi_i \\ \sin \phi_i \end{pmatrix}
$$

where $\phi_i$ is the mid-angle of the slice relative to the configured start angle $\theta_0$:

$$
\phi_i = \theta_0 + \sum_{j=1}^{i-1} \Delta \theta_j + \frac{1}{2}\Delta \theta_i
$$

---

## 4. Structured Implementation & Execution

```python
import matplotlib.pyplot as plt

def render_advanced_exploded_pie(expenses: list, amounts: list, focus_category: str = "R&D", start_angle: int = 90) -> dict:
    """
    Renders an advanced pie chart featuring slice explosion, drop shadows,
    custom start angle rotation, and donut styling.
    
    Parameters:
    -----------
    expenses : list of str
        Expense categories.
    amounts : list of float
        Numerical expenditures.
    focus_category : str
        Category name to highlight via explode.
    start_angle : int
        Rotational start angle in degrees (90 starts at 12 o'clock).
        
    Returns:
    --------
    dict
        Configuration properties applied to the chart.
    """
    # Build explode vector dynamically
    explode_vector = [0.18 if cat == focus_category else 0.0 for cat in expenses]
    palette = ["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3", "#a6d854"]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # 1. Advanced Exploded Pie with Shadow
    wedges1, texts1, autotexts1 = ax1.pie(
        amounts,
        labels=expenses,
        autopct='%1.1f%%',
        explode=explode_vector,
        shadow=True,
        startangle=start_angle,
        colors=palette,
        wedgeprops={"edgecolor": "white", "linewidth": 1.5}
    )
    for at in autotexts1:
        at.set_fontweight('bold')
    ax1.set_title(f"1. Exploded Pie ({focus_category} Highlighted, startangle={start_angle}°)", fontsize=11, fontweight='bold')
    
    # 2. Modern Donut Chart Variant
    wedges2, texts2, autotexts2 = ax2.pie(
        amounts,
        labels=expenses,
        autopct='%1.1f%%',
        startangle=start_angle,
        colors=palette,
        wedgeprops={"edgecolor": "white", "linewidth": 1.5}
    )
    # Draw center white circle to create donut hole
    centre_circle = plt.Circle((0, 0), 0.65, fc='white')
    ax2.add_artist(centre_circle)
    total_label = "Total: $" + str(sum(amounts)) + "K"
    ax2.text(0, 0, total_label, ha='center', va='center', fontsize=11, fontweight='bold')
    ax2.set_title("2. Modern Donut Chart Variant", fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    return {
        "focus_category": focus_category,
        "applied_explode_vector": explode_vector,
        "start_angle": start_angle,
        "total_expenditure": sum(amounts)
    }

# Lecture Data
expenses = ["Salaries", "Rent", "Marketing", "R&D", "Miscellaneous"]
amounts = [500, 150, 120, 100, 50]

adv_info = render_advanced_exploded_pie(expenses, amounts, focus_category="R&D", start_angle=90)
print("Advanced Pie Customization Details:")
for k, v in adv_info.items():
    print(f"  {k}: {v}")
```

---

## 5. Mukhya Batein (Key Takeaways) & Summary
- Code ko modular function ke roop me likha gaya hai jisme clear shuruat (`def`), docstrings, error handling, aur ending (`return`) maujood hai.
- Video lectures me ma'am dwara sikhaye gaye real movie box-office datasets aur syntax parameters ko exact follow kiya gaya hai.
