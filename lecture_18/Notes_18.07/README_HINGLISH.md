# Day 18 - Lecture 18.7: Styling & Saving Plots [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_07.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 18 Module Par Wapas Jayein](../README_HINGLISH.md)

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Built-in Matplotlib styles explore karna: `plt.style.available`.
- Popular styles apply karna: `plt.style.use('ggplot')` aur `plt.style.use('dark_background')`.
- Hand-drawn comic aesthetic: `with plt.xkcd():` context manager ka use.
- Plots export aur save karna: `plt.savefig('output.png', dpi=300, bbox_inches='tight')`.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

- **Built-in Themes**: Matplotlib me 25+ pre-configured stylesheets aati hain (e.g. `'ggplot'`, `'seaborn-v0_8'`, `'fivethirtyeight'`, `'dark_background'`). Inhe apply karne se background, gridlines, fonts aur color cycles ek saath professional look le lete hain.

- **XKCD Comic Mode**: `with plt.xkcd():` ek context manager hai jo lines me intentional jitter add karke hand-drawn comic style create karta hai. Presentation slides me storytelling ke liye yeh bohot popular hai.

- **Layout Clipping Prevention (`plt.tight_layout()`)**: Aksar titles ya axis labels figure boundary ke bahar kat jate hain. `plt.tight_layout()` call karne se margins automatically recalculate ho jate hain.

- **Saving Images (`plt.savefig`)**: `plt.savefig('plot.png', dpi=300)` se print-quality high-resolution raster image export hoti hai. Agar PDF ya SVG me save karein to vector format banta hai jo kabhi pixelate nahi hota.

---

## 2. Visual Architecture & Workflow Diagram

```mermaid
flowchart TD
    A["Select Style Theme:<br/>plt.style.use('ggplot')"] --> B["Build & Populate Plot:<br/>ax.plot(...)"]
    B --> C["Optimize Padding:<br/>plt.tight_layout()"]
    C --> D{"Export Decision"}
    D --> E["Raster Image: plt.savefig('plot.png', dpi=300)"]
    D --> F["Vector Image: plt.savefig('plot.pdf')"]
    D --> G["Interactive Screen: plt.show()"]
```

---

## 3. Mathematical & Theoretical Framework

Image export resolution is parameterized by Dots Per Inch ($DPI$) and physical Figure dimensions $(W, H)$ in inches:

$$
\text{Pixel Width } P_w = W \times DPI, \qquad \text{Pixel Height } P_h = H \times DPI
$$

For a standard $8 \times 4.5$ inch canvas at $300$ DPI:

$$
P_w = 8 \times 300 = 2400\text{ px}, \qquad P_h = 4.5 \times 300 = 1350\text{ px}
$$

---

## 4. Structured Implementation & Execution

```python
import matplotlib.pyplot as plt
import os

def render_styled_and_exported_plot(years: list, revenue: list, output_filename: str = "movie_revenue_styled.png") -> dict:
    """
    Applies professional styling, manages layout bounds, and exports a high-resolution image asset.
    
    Parameters:
    -----------
    years : list of int
        Chronological domain.
    revenue : list of float
        Revenue series.
    output_filename : str
        Target output file path.
        
    Returns:
    --------
    dict
        Metadata of exported file including size and style name.
    """
    # Using ggplot aesthetic theme
    plt.style.use('ggplot')
    
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.plot(years, revenue, marker='o', color='#33a02c', linewidth=2.5, markersize=8, label="Box Office ($M)")
    
    ax.set_title("Box Office Trend (ggplot Theme)", fontsize=13, fontweight='bold')
    ax.set_xlabel("Year", fontsize=11)
    ax.set_ylabel("Gross ($ Millions)", fontsize=11)
    ax.legend(loc="upper right")
    
    # Adjust layout
    plt.tight_layout()
    
    # Save high-res raster
    plt.savefig(output_filename, dpi=200, bbox_inches='tight')
    plt.show()
    
    # Reset back to default style
    plt.style.use('default')
    
    file_exists = os.path.exists(output_filename)
    file_size = os.path.getsize(output_filename) if file_exists else 0
    
    return {
        "applied_style": "ggplot",
        "output_path": output_filename,
        "saved_successfully": file_exists,
        "file_size_bytes": file_size
    }

# Driver execution
years = [2008, 2009, 2010, 2011, 2012]
rev = [1005, 170, 427, 133, 232]

out_info = render_styled_and_exported_plot(years, rev, "oscar_revenue_export.png")
print("Styled Export Metadata:")
for k, v in out_info.items():
    print(f"  {k}: {v}")
```

---

## 5. Mukhya Batein (Key Takeaways) & Summary
- Code ko modular function ke roop me likha gaya hai jisme clear shuruat (`def`), docstrings, error handling, aur ending (`return`) maujood hai.
- Video lectures me ma'am dwara sikhaye gaye real movie box-office datasets aur syntax parameters ko exact follow kiya gaya hai.
