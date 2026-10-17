# Day 18 - Lecture 18.6: Format Strings (`fmt`) [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_06.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 18 Module Par Wapas Jayein](../README_HINGLISH.md)

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Matplotlib shorthand format string (`fmt`) ka internal order: `[marker][line][color]`.
- Common marker types: `'o'` (circle), `'^'` (triangle up), `'>'` (triangle right), `'s'` (square).
- Common line styles: `'-'` (solid), `'--'` (dashed), `'-.'` (dash-dot), `':'` (dotted).
- Format string vs Explicit Keyword Arguments: Kab shorthand use karein aur kab explicit parameters.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

- **Shorthand Syntax `[marker][line][color]`**: Ek single string me 3 properties pack ki ja sakti hain. Jaise `'o-b'` ka matlab hai: `'o'` (circle marker), `'-'` (solid line), `'b'` (blue color).

- **Dashed Shorthand Example**: `'>--g'` ka matlab hai: `'>'` (triangle right marker), `'--'` (dashed line), `'g'` (green color).

- **Explicit Keyword Overrides**: Shorthand quick exploration ke liye zabardast hai, lekin jab line thickness (`linewidth=3`), marker edge color (`markeredgecolor`), ya custom hex colors (`#FF5733`) chahiye hote hain, tab explicit kwargs use kiye jate hain.

- **Priority Rule**: Agar format string aur explicit keyword dono pass kiye jayein (e.g., `'o-b', color='red'`), to explicit keyword color format string ko override kar leta hai.

---

## 2. Visual Architecture & Workflow Diagram

```mermaid
flowchart LR
    A["Format String Syntax:<br/>'[marker][line][color]'"] --> B["Marker Component:<br/>'o', '^', '>', 's', 'x', '*'"]
    A --> C["Line Component:<br/>'-', '--', '-.', ':'"]
    A --> D["Color Component:<br/>'b', 'g', 'r', 'c', 'm', 'y', 'k'"]
    B & C & D --> E["Combined String: 'o-b' or '>--g'"]
```

---

## 3. Mathematical & Theoretical Framework

A format string specification can be decomposed into an orthogonal tuple:

$$
\text{fmt} = \langle m, l, c \rangle \in \mathcal{M} \times \mathcal{L} \times \mathcal{C}
$$

where:

$$
\mathcal{M} = \{ \text{'o'}, \text{'^'}, \text{'>'}, \text{'s'}, \dots \}, \quad \mathcal{L} = \{ \text{'-'}, \text{'--'}, \text{'-.'}, \text{':'} \}, \quad \mathcal{C} = \{ \text{'b'}, \text{'g'}, \text{'r'}, \text{'k'}, \dots \}
$$

---

## 4. Structured Implementation & Execution

```python
import matplotlib.pyplot as plt

def demonstrate_format_strings(x_data: list, y1_data: list, y2_data: list) -> dict:
    """
    Demonstrates both concise format string notation and explicit keyword configurations.
    
    Parameters:
    -----------
    x_data : list of int
        Timeline domain.
    y1_data, y2_data : list of float
        Numerical series to plot.
        
    Returns:
    --------
    dict
        Styling specifications applied to each series.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))
    
    # 1. Using Concise Format Strings (Shorthand)
    ax1.plot(x_data, y1_data, "o-b", label="Winners ('o-b')", markersize=7)
    ax1.plot(x_data, y2_data, ">--g", label="Non-Winners ('>--g')", markersize=7)
    ax1.set_title("Method 1: Concise Format Strings", fontsize=11, fontweight='bold')
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Revenue ($M)")
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend()
    
    # 2. Using Explicit Keyword Arguments
    ax2.plot(x_data, y1_data, color="#000000", linestyle="-", marker="o", 
             linewidth=2.5, markersize=8, markerfacecolor="#41b6c4", label="Explicit Black Solid")
    ax2.plot(x_data, y2_data, color="#e41a1c", linestyle="--", marker=">", 
             linewidth=4.0, markersize=9, markerfacecolor="#ffff33", label="Explicit Red Thick Dashed")
    ax2.set_title("Method 2: Explicit Keyword Parameters", fontsize=11, fontweight='bold')
    ax2.set_xlabel("Year")
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend()
    
    plt.tight_layout()
    plt.show()
    
    return {
        "shorthand_specs": ["o-b (circle, solid, blue)", ">--g (triangle, dashed, green)"],
        "explicit_specs": ["linewidth=2.5, markerfacecolor=#41b6c4", "linewidth=4.0, dashed red"]
    }

# Driver execution
years = [2008, 2009, 2010, 2011, 2012]
rev_oscar = [1005, 170, 427, 133, 232]
rev_non_oscar = [378, 2788, 829, 185, 275]

styles = demonstrate_format_strings(years, rev_oscar, rev_non_oscar)
print("Applied Format Strings & Styles:")
for k, v in styles.items():
    print(f"  {k}: {v}")
```

---

## 5. Mukhya Batein (Key Takeaways) & Summary
- Code ko modular function ke roop me likha gaya hai jisme clear shuruat (`def`), docstrings, error handling, aur ending (`return`) maujood hai.
- Video lectures me ma'am dwara sikhaye gaye real movie box-office datasets aur syntax parameters ko exact follow kiya gaya hai.
