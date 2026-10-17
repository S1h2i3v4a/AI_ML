# Notes_19.14: Seaborn histplot Aur KDE [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne **`sns.histplot()`** ka use karke continuous data ki distribution dekhna sikhaya hai: penguins dataset ke body mass ko plot karna aur uske upar smooth **KDE (Kernel Density Estimation)** curve draw karna.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- `sns.histplot()` function ka use (aur purane `sns.distplot` se iska badlav).
- `bins=30` parameter se data ko intervals mein divide karna.
- `kde=True` ka matlab: Discrete bars ke upar smooth bell-shaped curve kaise banta hai.
- Missing values (`NaN`) ko Seaborn kaise handle karta hai.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. `sns.histplot()` Kya Hai?
Jab humein kisi continuous metric ki distribution dekhni hoti hai (jaise penguins ka body mass grams mein), toh `sns.histplot()` Matplotlib ke histogram se bohot zyada clean aur powerful visual deta hai.

#### 2. KDE (Kernel Density Estimation) Kya Hai?
Histogram mein bars ki shape is baat par depend karti hai ki aapne bins 10 rakhe ya 30.
**KDE (`kde=True`)** har data point par ek chhota normal curve fit karta hai aur un sabko add karke ek continuous **smooth line** bana deta hai:

$$
\hat{f}(x) = \frac{1}{n h} \sum_{i=1}^n K\left( \frac{x - x_i}{h} \right)
$$

Is smooth curve se distribution ke peaks (modes) aur skewness ek glance mein samajh aate hain.

---

### 📊 Blackboard Diagram: Histogram Bars Se Smooth KDE Curve

```mermaid
flowchart LR
    A["Penguin Body Mass Data"] --> B["Discrete Histogram Bars"]
    A --> C["Gaussian Kernels Sum"]
    B & C --> D["Single Plot: Bars + Smooth Red/Blue KDE Line"]
```

---

### 💻 Python Code Implementation

```python
import seaborn as sns
import matplotlib.pyplot as plt

def plot_penguin_distribution(bins=30, kde=True, show_plot=True):
    """
    Plots the statistical distribution of continuous features using sns.histplot().
    Demonstrates binning, frequency histograms, and Kernel Density Estimation (KDE)
    on the penguins dataset.
    
    Parameters:
        bins (int): Number of histogram intervals.
        kde (bool): Whether to overlay smooth kernel density estimate.
        show_plot (bool): Display control.
        
    Returns:
        dict: Mean and standard deviation of penguin body mass.
    """
    sns.set_theme(style="whitegrid")
    penguins = sns.load_dataset("penguins")
    
    plt.figure(figsize=(9, 5))
    
    # Distribution plot with KDE overlay
    sns.histplot(
        data=penguins,
        x="body_mass_g",
        bins=bins,
        kde=kde,
        color="teal",
        edgecolor="black"
    )
    
    plt.title("Distribution of Penguin Body Mass (g) with KDE Curve", fontweight="bold")
    plt.xlabel("Body Mass (grams)")
    plt.ylabel("Count")
    
    plt.tight_layout()
    if show_plot:
        plt.show()
        
    clean_mass = penguins["body_mass_g"].dropna()
    return {
        "mean_mass": float(clean_mass.mean()),
        "std_mass": float(clean_mass.std()),
        "total_records": len(clean_mass)
    }

# --- Execution & Verification ---
stats = plot_penguin_distribution(show_plot=False)
print(f"Penguin Body Mass Mean: {stats['mean_mass']:.1f} g")
print(f"Standard Deviation: {stats['std_mass']:.1f} g")

```

---

### 🎯 Key Takeaways:
1. `sns.histplot(..., kde=True)` feature analysis ke liye sabse recommended plot hai.
2. KDE curve bin size par dependent nahi hota, isliye yeh data ki asli density accurately dikhata hai.
