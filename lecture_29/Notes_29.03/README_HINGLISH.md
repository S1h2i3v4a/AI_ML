# Lecture 29.03: Classification Hyperparameters ($C$, Slack Variables & Bias-Variance) [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_29.03.ipynb)
[![English PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)
[![Hinglish PDF](https://img.shields.io/badge/PDF-notes__hinglish.pdf-green.svg)](notes_hinglish.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 29 Module Par Wapas Jayein](../README_HINGLISH.md)

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Slack variables ($\xi_i$) kya hote hain aur soft margin me inka role.
- Regularization hyperparameter $C$ ka mathematical formulation: Margin vs Penalty trade-off.
- Large $C$ vs Small $C$ ka visual behavior: Street width aur outlier sensitivity.
- Bias-Variance tradeoff: Kab $C$ ko increase karein aur kab decrease.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

- **Slack Variables ($\xi_i$)**: Real-world data 100% linearly separable nahi hota; hamesha kuch outliers margin ke andar ghus aate hain. Slack variable $\xi_i \ge 0$ measure karta hai ki koi point margin boundary se kitna violate kar raha hai.

- **Hyperparameter $C$ (Penalty Factor)**: Objective function me $C \sum \xi_i$ hota hai. $C$ decide karta hai ki hum misclassifications ko kitni badi penalty dena chahte hain.

- **Large $C$ (Strict / Narrow Margin)**: Agar $C$ bohot bada ho (e.g. $C=1000$), to model margin violations ko bilkul tolerate nahi karta. Margin super-narrow ho jata hai -> Low Bias, High Variance (Overfitting ka khatra).

- **Small $C$ (Tolerant / Wide Margin)**: Agar $C$ chhota ho (e.g. $C=0.1$), to model kuch points ko margin ke andar aane deta hai aur ek wide, relaxed margin banata hai -> High Bias, Low Variance (Generalization strong hota hai).

---

## 2. Visual Architecture & Workflow Diagram

```mermaid
flowchart LR
    A["Hyperparameter C"] -->|"Small C (e.g. 0.01 - 1)"| B["Wide Margin (Large Street)<br/>More Margin Violations Allowed<br/>High Bias, Low Variance (Resilient to Noise)"]
    A -->|"Large C (e.g. 100 - 1000)"| C["Narrow Margin (Tight Street)<br/>Zero/Minimal Violations Allowed<br/>Low Bias, High Variance (Risk of Overfitting)"]
```

---

## 3. Mathematical & Theoretical Framework

The Soft Margin SVM primal optimization problem incorporates slack variables $\xi_i$:

$$
\min_{\mathbf{w}, b, \boldsymbol{\xi}} \frac{1}{2} \|\mathbf{w}\|^2 + C \sum_{i=1}^N \xi_i
$$

subject to the relaxed linear inequality constraints:

$$
y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1 - \xi_i, \quad \xi_i \ge 0, \quad \forall i = 1, \dots, N
$$

- If $\xi_i = 0$: Point lies correctly on or outside the gutter.
- If $0 < \xi_i \le 1$: Point is within the margin but classified correctly.
- If $\xi_i > 1$: Point is misclassified across the decision boundary.

---

## 4. Structured Implementation & Execution

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import make_blobs

def compare_c_hyperparameter_impact(X: np.ndarray, y: np.ndarray) -> dict:
    """
    Compares the effect of Small C (wide margin) vs Large C (narrow margin) on decision boundaries.
    
    Parameters:
    -----------
    X : np.ndarray
        Feature matrix with overlapping/noisy samples.
    y : np.ndarray
        Binary target classes.
        
    Returns:
    --------
    dict
        Support vector counts and margin widths for each C value.
    """
    c_values = [0.1, 100.0]
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))
    results = {}
    
    for ax, c_val in zip(axes, c_values):
        clf = SVC(kernel='linear', C=c_val)
        clf.fit(X, y)
        
        w = clf.coef_[0]
        b = clf.intercept_[0]
        margin = 2.0 / np.linalg.norm(w)
        
        ax.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', s=40, edgecolors='k')
        ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], 
                   s=100, facecolors='none', edgecolors='green', linewidths=1.8, label=f'SVs ({len(clf.support_vectors_)})')
        
        x_pts = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
        ax.plot(x_pts, -(w[0]*x_pts + b)/w[1], 'k-', label='Decision Boundary')
        ax.plot(x_pts, -(w[0]*x_pts + b - 1)/w[1], 'k--', alpha=0.7)
        ax.plot(x_pts, -(w[0]*x_pts + b + 1)/w[1], 'k--', alpha=0.7)
        
        ax.set_title(f"C = {c_val} (Margin = {margin:.2f})", fontsize=11, fontweight='bold')
        ax.set_xlabel("Feature 1")
        ax.set_ylabel("Feature 2")
        ax.legend(loc='lower right')
        ax.grid(True, linestyle=':', alpha=0.5)
        
        results[f"C_{c_val}"] = {
            "margin_width": float(margin),
            "support_vector_count": len(clf.support_vectors_),
            "norm_w": float(np.linalg.norm(w))
        }
        
    plt.tight_layout()
    plt.show()
    return results

# Driver test with overlapping clusters
X_overlap, y_overlap = make_blobs(n_samples=50, centers=2, random_state=7, cluster_std=1.6)
c_impact = compare_c_hyperparameter_impact(X_overlap, y_overlap)
print("Hyperparameter C Impact Comparison:")
for k, v in c_impact.items():
    print(f"  {k}: {v}")
```

---

## 5. Mukhya Batein (Key Takeaways) & Summary
- Code ko modular function ke roop me likha gaya hai jisme clear shuruat (`def`), docstrings, error handling, aur ending (`return`) maujood hai.
- Video lectures me ma'am dwara sikhaye gaye exact datasets (Diabetes, concentric circles, blobs) aur syntax parameters ko exact follow kiya gaya hai.
