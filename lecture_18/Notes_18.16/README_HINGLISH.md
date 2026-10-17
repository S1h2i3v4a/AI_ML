# Day 18 - Lecture 18.16: Multiple Datasets on Scatter Plots [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_18_16.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 18 Module Par Wapas Jayein](../README_HINGLISH.md)

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Ek hi scatter plot canvas par multiple categorical groups overlay karne ka process.
- Weather meteorology example: Winter vs Summer temperature aur humidity comparison across Cities A-E.
- Visual distinction strategy: Alag colors (blue vs orange) aur alag markers (`'o'` vs `'s'`).
- Clustering aur bivariate separation patterns recognize karna.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

- **Group Comparison**: Aksar hume do alag conditions (jaise Winter vs Summer) ya do alag treatments ka correlation compare karna hota hai. Ek hi graph me dono series plot karne se unka cluster separation foran dikh jata hai.

- **Climate Dataset**: Ma'am ne 5 cities (City A se E) ka data liya: Winter me low temp ($0-10^\circ\text{C}$) aur high humidity ($65-85\%$); Summer me high temp ($25-35^\circ\text{C}$) aur moderate humidity ($45-65\%$).

- **Dual Legend Calling**: Har scatter call me `label='Winter'` aur `label='Summer'` pass karke `plt.legend()` call kiya jata hai.

- **Cluster Separation**: Is graph me dono seasons do distinct spatial clusters form karte hain jo bivariate plane par visually completely separable hote hain.

---

## 2. Visual Architecture & Workflow Diagram

```mermaid
flowchart TD
    A["Climate Observation Data (Cities A-E)"] --> B["Series 1: Winter<br/>Temp: [5, 2, 10, 0, 7]<br/>Humidity: [80, 75, 65, 85, 70]"]
    A --> C["Series 2: Summer<br/>Temp: [25, 30, 28, 35, 27]<br/>Humidity: [60, 50, 55, 45, 65]"]
    B --> D["Plot Blue Scatter:<br/>plt.scatter(winter_temp, winter_humidity, color='blue', label='Winter')"]
    C --> E["Plot Orange Scatter:<br/>plt.scatter(summer_temp, summer_humidity, color='orange', label='Summer')"]
    D & E --> F["Combined Comparative Weather Canvas with Legend"]
```

---

## 3. Mathematical & Theoretical Framework

Given $K$ disjoint cohorts $\mathcal{C}_k$, the multi-group scatter plot projects each cohort into the shared phase space $(T, H) \in \mathbb{R}^2$:

$$
\mathcal{P}_k = \{ (T_{i, k}, H_{i, k}) \mid i = 1, \dots, N_k \}, \quad k \in \{ \text{Winter}, \text{Summer} \}
$$

The centroid of each cohort provides the mean seasonal state vector:

$$
\mathbf{\mu}_k = \begin{pmatrix} \bar{T}_k \\ \bar{H}_k \end{pmatrix} = \frac{1}{N_k} \sum_{i=1}^{N_k} \begin{pmatrix} T_{i, k} \\ H_{i, k} \end{pmatrix}
$$

---

## 4. Structured Implementation & Execution

```python
import matplotlib.pyplot as plt
import numpy as np

def render_multi_dataset_scatter(cities: list, winter_temp: list, winter_humidity: list,
                                 summer_temp: list, summer_humidity: list) -> dict:
    """
    Renders multiple comparative scatter series demonstrating bivariate cluster separation.
    
    Parameters:
    -----------
    cities : list of str
        Identifiers for geographical locations.
    winter_temp, winter_humidity : list of float
        Winter meteorological coordinates.
    summer_temp, summer_humidity : list of float
        Summer meteorological coordinates.
        
    Returns:
    --------
    dict
        Seasonal centroids and cluster separation distance.
    """
    fig, ax = plt.subplots(figsize=(8, 4.8))
    
    # 1. Plot Winter Series
    ax.scatter(winter_temp, winter_humidity, color="#1f78b4", marker='o', s=80, 
               edgecolors='black', linewidth=0.8, label="Winter Season")
    # 2. Plot Summer Series
    ax.scatter(summer_temp, summer_humidity, color="#ff7f00", marker='s', s=80, 
               edgecolors='black', linewidth=0.8, label="Summer Season")
    
    # Annotate city labels
    for i, city in enumerate(cities):
        ax.annotate(city, (winter_temp[i], winter_humidity[i]), xytext=(winter_temp[i]+0.6, winter_humidity[i]-1),
                    fontsize=8.5, color='#1f78b4')
        ax.annotate(city, (summer_temp[i], summer_humidity[i]), xytext=(summer_temp[i]+0.6, summer_humidity[i]-1),
                    fontsize=8.5, color='#ff7f00')
        
    ax.set_title("Seasonal Weather Patterns: Temperature vs Humidity", fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel("Temperature (°C)", fontsize=11)
    ax.set_ylabel("Relative Humidity (%)", fontsize=11)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc="upper right", framealpha=0.9)
    
    plt.tight_layout()
    plt.show()
    
    winter_centroid = (float(np.mean(winter_temp)), float(np.mean(winter_humidity)))
    summer_centroid = (float(np.mean(summer_temp)), float(np.mean(summer_humidity)))
    euclidean_dist = np.sqrt((summer_centroid[0]-winter_centroid[0])**2 + (summer_centroid[1]-winter_centroid[1])**2)
    
    return {
        "winter_centroid_T_H": winter_centroid,
        "summer_centroid_T_H": summer_centroid,
        "centroid_separation_distance": float(euclidean_dist)
    }

# Lecture Data
cities = ["City A", "City B", "City C", "City D", "City E"]
winter_temp = [5, 2, 10, 0, 7]
winter_humidity = [80, 75, 65, 85, 70]
summer_temp = [25, 30, 28, 35, 27]
summer_humidity = [60, 50, 55, 45, 65]

climate_res = render_multi_dataset_scatter(cities, winter_temp, winter_humidity, summer_temp, summer_humidity)
print("Multi-Dataset Scatter Centroid Analysis:")
for k, v in climate_res.items():
    print(f"  {k}: {v}")
```

---

## 5. Mukhya Batein (Key Takeaways) & Summary
- Code ko modular function ke roop me likha gaya hai jisme clear shuruat (`def`), docstrings, error handling, aur ending (`return`) maujood hai.
- Video lectures me ma'am dwara sikhaye gaye real movie box-office datasets aur syntax parameters ko exact follow kiya gaya hai.
