# Module 24.04: Overfitting (High Variance & Memorizing Noise)

## 1. Theoretical Definition of Overfitting

**Overfitting** occurs when a machine learning model fits too closely or exclusively to a specific dataset, learning the empirical random noise, statistical fluctuations, and idiosyncrasies rather than the true underlying data-generating distribution $P(X, Y)$.

```
   Target Ground Truth: y = f(x) + epsilon (where epsilon ~ N(0, sigma^2) is irreducible noise)
   
   Overfitted Model: Learns f(x) + epsilon perfectly!
   Result:
   * Training Error  -> 0.0 (Near zero loss, R^2 ~ 1.0)
   * Test/Val Error  -> Very Large (Catastrophic failure on unseen real-world data)
```

---

## 2. The Bias-Variance Decomposition Perspective

For any regression model $\hat{f}(x)$, the expected generalization error on an unseen test point $x^*$ decomposes strictly into three orthogonal components:

$$
\mathbb{E}\left[ (y - \hat{f}(x^*))^2 \right] = \text{Bias}^2\left[\hat{f}(x^*)\right] + \text{Var}\left[\hat{f}(x^*)\right] + \sigma^2
$$

Where:
- **$\text{Bias}\left[\hat{f}(x^*)\right] = \mathbb{E}[\hat{f}(x^*)] - f(x^*)$:** Error introduced by simplifying assumptions.
- **$\text{Var}\left[\hat{f}(x^*)\right] = \mathbb{E}\left[ (\hat{f}(x^*) - \mathbb{E}[\hat{f}(x^*)])^2 \right]$:** The sensitivity of the model to the specific training dataset drawn.
- **$\sigma^2$:** Irreducible noise variance inherent in the physical process.

### Mathematical Anatomy of High Variance:
In an overfitted model:
1. $\text{Bias} \approx 0$: The model has excessive capacity to bend through every training point.
2. $\text{Variance} \to \text{Extremely High}$: Training on dataset $\mathcal{D}_1$ vs $\mathcal{D}_2$ produces radically disparate weight parameters.
3. The model exhibits explosive sensitivity to infinitesimal shifts in inputs.

---

## 3. Causes and Symptoms of Overfitting

```
+-----------------------------------------------------------------------------------------+
| Root Causes of Overfitting                                                              |
+-----------------------------------------------------------------------------------------+
| 1. Excessive Model Complexity: High polynomial degrees (e.g., degree 15 on 20 points).  |
| 2. Insufficient Training Samples: Sample size m is too small relative to features d.    |
| 3. Noisy / Corrupted Data: Training set contaminated with outliers and mislabeled rows. |
| 4. Unconstrained Weights: Model parameters w_j grow into massive magnitudes.            |
+-----------------------------------------------------------------------------------------+
```

### Signature Diagnostic Sign:
A large and expanding **generalization gap**:

$$
\text{Gap} = \mathcal{L}_{\text{val}} - \mathcal{L}_{\text{train}} \gg 0
$$

As model capacity increases, $\mathcal{L}_{\text{train}}$ monotonically descends, while $\mathcal{L}_{\text{val}}$ initially drops but then violently explodes upwards.
