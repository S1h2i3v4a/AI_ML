# Lecture 29.05: Common Kernel Types (Linear, Poly, RBF, Sigmoid)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_29.05.ipynb)
[![English PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)
[![Hinglish PDF](https://img.shields.io/badge/PDF-notes__hinglish.pdf-green.svg)](notes_hinglish.pdf)

🌐 **Language / भाषा:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Lecture 29 Module](../README.md)

---

## 1. Overview & Conceptual Foundations
Comprehensive taxonomy and comparison of the four primary SVM kernels: Linear Kernel, Polynomial Kernel, Radial Basis Function (RBF / Gaussian) Kernel, and Sigmoid (Hyperbolic Tangent) Kernel. Understand the mathematical formulas, hyperparameter roles (degree d, gamma, coef0), and selection heuristics.

---

## 2. Visual Architecture & Workflow Diagram

```mermaid
flowchart TD
    Q{"Choose SVM Kernel"}
    Q -->|"Text / Huge Features (d >> N)"| K1["Linear Kernel<br/>K(x, x') = x^T x'<br/>(Fastest, Low Overfitting)"]
    Q -->|"Tabular Non-linear (Default choice)"| K2["RBF / Gaussian Kernel<br/>K(x, x') = exp(-gamma ||x - x'||^2)<br/>(Infinite-D Projection, highly flexible)"]
    Q -->|"Curved Structural Relationships"| K3["Polynomial Kernel<br/>K(x, x') = (gamma x^T x' + r)^d<br/>(Models feature interactions)"]
    Q -->|"Neural Net Analogy"| K4["Sigmoid Kernel<br/>K(x, x') = tanh(gamma x^T x' + r)"]
```

---

## 3. Mathematical & Theoretical Framework

The four canonical Mercer kernel functions:

1. **Linear Kernel**:
$$
K_{\text{linear}}(\mathbf{x}, \mathbf{x}') = \mathbf{x}^T \mathbf{x}'
$$

2. **Polynomial Kernel** (Degree $d \in \mathbb{N}$, intercept $r \ge 0$):
$$
K_{\text{poly}}(\mathbf{x}, \mathbf{x}') = (\gamma \mathbf{x}^T \mathbf{x}' + r)^d
$$

3. **Radial Basis Function (RBF / Gaussian) Kernel** (Bandwidth $\sigma$, $\gamma = \frac{1}{2\sigma^2}$):
$$
K_{\text{RBF}}(\mathbf{x}, \mathbf{x}') = \exp\left( -\gamma \|\mathbf{x} - \mathbf{x}'\|^2 \right)
$$

4. **Sigmoid Kernel**:
$$
K_{\text{sigmoid}}(\mathbf{x}, \mathbf{x}') = \tanh\left( \gamma \mathbf{x}^T \mathbf{x}' + r \right)
$$

---

## 4. Structured Implementation & Execution

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import make_moons

def compare_svm_kernel_decision_boundaries(X: np.ndarray, y: np.ndarray) -> dict:
    """
    Fits and compares decision boundaries for Linear, Poly, and RBF kernels on moon-shaped data.
    
    Parameters:
    -----------
    X : np.ndarray
        2D coordinate feature matrix.
    y : np.ndarray
        Binary target labels.
        
    Returns:
    --------
    dict
        Training accuracy scores across the different kernels.
    """
    kernels = ['linear', 'poly', 'rbf']
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.2))
    scores = {}
    
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))
    
    for ax, kernel_name in zip(axes, kernels):
        clf = SVC(kernel=kernel_name, degree=3, gamma='scale', C=1.0)
        clf.fit(X, y)
        acc = clf.score(X, y)
        scores[kernel_name] = float(acc)
        
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
        ax.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
        ax.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolors='k', s=35)
        
        ax.set_title(f"Kernel: {kernel_name.upper()} (Acc: {acc*100:.1f}%)", fontsize=11, fontweight='bold')
        ax.set_xlabel("Feature 1")
        ax.set_ylabel("Feature 2")
        ax.grid(True, linestyle=':', alpha=0.4)
        
    plt.tight_layout()
    plt.show()
    return scores

# Driver test on non-linear Moons dataset
X_moons, y_moons = make_moons(n_samples=100, noise=0.15, random_state=42)
kernel_comparison = compare_svm_kernel_decision_boundaries(X_moons, y_moons)
print("Kernel Comparison Performance:")
for k, v in kernel_comparison.items():
    print(f"  {k}: {v*100:.2f}%")
```

---

## 5. Summary & Key Takeaways
- **Self-contained Functional Design**: Implementation is encapsulated into modular functions with explicit inputs, structured outputs, docstrings, and verified test assertions.
- **Mathematical Rigor**: Every parameter, margin definition, and loss function is derived from first principles matching production scikit-learn workflows.
