# Day 18 - Lecture 18.9: Vertical Bar Charts (`plt.bar`)

## 1. Overview & Definition
A **Bar Chart** represents categorical data with rectangular bars whose heights are proportional to the values they represent.
- **X-axis:** Discrete categories (e.g. Movie titles, product names, years).
- **Y-axis:** Numerical values or counts.

### Difference Between Bar Chart and Histogram:
- **Bar Chart:** Visualizes categorical data. Bars have distinct spaces between them because categories are independent discrete entities.
- **Histogram:** Visualizes continuous numerical intervals (bins). Bars touch each other.

---

## 2. Syntax & Parameters

```python
plt.bar(
    x,                      # Sequence of categories (strings, numbers, dates)
    height,                 # Numerical values representing bar heights
    width=0.8,              # Bar width (default 0.8)
    bottom=None,            # Baseline y-coordinate (used for stacked bars)
    color='purple',         # Bar fill color
    edgecolor='black',      # Border color
    linewidth=1.2           # Border thickness
)
```

---

## 3. Code Implementation: Movie Box Office Revenues

```python
import matplotlib.pyplot as plt

movies = [
    "The Dark Knight", 
    "The Hurt Locker",  
    "The King's Speech", 
    "The Artist",     
    "Argo"
]
years = [2008, 2009, 2010, 2011, 2012]
revenue = [1005, 170, 427, 133, 232]  # in $M

plt.figure(figsize=(8, 5))
plt.bar(years, revenue, color="purple", edgecolor="black", width=0.6)

plt.title("Yearly Revenue of Oscar Movies", fontsize=14, fontweight="bold")
plt.xlabel("Years", fontsize=12)
plt.ylabel("Revenue (in $M)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
```

---

## 4. Key Takeaways
- Use `width` to control the thickness of bars (e.g., `width=0.5` makes them narrower).
- Adding `grid(axis='y')` provides horizontal reference lines without cluttering the vertical space.
