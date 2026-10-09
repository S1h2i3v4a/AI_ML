# Module 24.03: Other Feature Engineering Techniques

## 1. Taxonomy of Advanced Feature Transformations

Feature engineering is the process of transforming raw empirical attributes into informative representations that maximize the hypothesis capacity of machine learning algorithms:

```
                          Feature Engineering Toolbox
                                       |
        +------------------+-----------+-----------+------------------+
        |                  |                       |                  |
        v                  v                       v                  v
  Feature Scaling     Discretization          Polynomial         Missing Data
  (Normalization)       (Binning)            Interactions         Imputation
```

---

## 2. Feature Scaling: Normalization vs. Standardization

When numerical features possess disparate scales ($x_1 \in [0, 1]$ vs $x_2 \in [10^4, 10^7]$), gradient descent oscillates violently and distance metrics are dominated entirely by large-magnitude variables.

### 1. Standardization (Z-Score Normalization)
Transforms distribution to zero mean ($\mu = 0$) and unit standard deviation ($\sigma = 1$):

$$
z = \frac{x - \mu}{\sigma}
$$

- **Properties:** Preserves outliers, unbounded $z \in (-\infty, \infty)$.
- **Best For:** Gradient Descent, Logistic/Linear Regression, PCA, Support Vector Machines.

### 2. Min-Max Normalization (Feature Scaling)
Compresses feature values into a rigid bounded interval, typically $[0, 1]$:

$$
x_{\text{scaled}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
$$

- **Properties:** Extremely sensitive to outliers (a single extreme value squashes remaining points into a narrow sliver).
- **Best For:** Neural networks with bounded activations, KNN, Image pixel processing ($[0, 255] \to [0, 1]$).

### 3. Robust Scaling (IQR Scaling)
Removes the median and scales according to the Interquartile Range:

$$
x_{\text{robust}} = \frac{x - Q_2}{Q_3 - Q_1} = \frac{x - \text{Median}}{\text{IQR}}
$$

- **Best For:** Data laden with severe anomalies and heavy-tailed distributions.

---

## 3. Discretization & Binning

Discretization converts continuous real features into discrete categorical bins.
- **Equal-Width Binning:** Divides the range $[x_{\min}, x_{\max}]$ into $K$ intervals of equal width:
  $$
  w = \frac{x_{\max} - x_{\min}}{K}
  $$
- **Equal-Frequency (Quantile) Binning:** Partitions data such that each bin contains exactly $\frac{m}{K}$ observations.
- **Utility:** Suppresses minor measurement noise and introduces non-linear step-function behavior into linear models.

---

## 4. Polynomial Features & Interaction Terms

Linear models can capture complex non-linear curvatures through polynomial basis expansion:

$$
\phi(x_1, x_2) = [1, x_1, x_2, x_1^2, x_1 x_2, x_2^2]
$$

- **Interaction Terms ($x_1 x_2$):** Encodes synergistic effects where the influence of feature $x_1$ depends on the level of $x_2$ (e.g., $\text{BMI} \times \text{Smoker}$).
- **Caution:** Feature count explodes combinatorially: $\binom{d + k}{k}$ where $d$ is feature count and $k$ is polynomial degree.
