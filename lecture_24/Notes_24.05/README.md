# Module 24.05: Underfitting (High Bias & Oversimplification)

## 1. Theoretical Definition of Underfitting

**Underfitting** occurs when a machine learning model is overly simplistic and lacks the expressive mathematical capacity to capture the underlying structure, curvature, and relationships present in the data.

```
   Target Ground Truth: Non-linear parabolic curve (y = 2 x^2 + 3)
   
   Underfitted Model: Simple straight line (y = w x + b)
   Result:
   * Training Error  -> High (Fails even on the data it was trained on)
   * Test/Val Error  -> High (Equally poor generalization)
```

---

## 2. The Bias-Variance Perspective: High Bias

Underfitting represents the **High Bias** regime of the Bias-Variance tradeoff:

$$
\text{Bias}\left[\hat{f}(x)\right] = \mathbb{E}\left[\hat{f}(x)\right] - f(x) \gg 0
$$

- The fundamental assumptions made by the model family are too restrictive.
- For instance, forcing a strictly linear hypothesis $\hat{y} = w x + b$ onto an inherently sinusoidal or quadratic phenomenon.
- Even if infinite training samples ($m \to \infty$) were provided, an underfitted model cannot improve beyond its rigid capacity boundary.

---

## 3. Causes and Diagnostic Signatures of Underfitting

```
+-----------------------------------------------------------------------------------------+
| Root Causes of Underfitting                                                             |
+-----------------------------------------------------------------------------------------+
| 1. Model Too Simple: Linear model applied to non-linear physical systems.               |
| 2. Insufficient / Uninformative Features: Critical predictive signals are missing.     |
| 3. Excessive Regularization: Hyperparameter lambda is set so large that weights w -> 0. |
| 4. Under-trained Model: Gradient descent terminated before reaching local/global min.   |
+-----------------------------------------------------------------------------------------+
```

### Signature Diagnostic Sign:
Both training and validation loss remain unacceptably high with minimal gap:

$$
\mathcal{L}_{\text{train}} \approx \text{High}, \quad \mathcal{L}_{\text{val}} \approx \text{High}, \quad (\mathcal{L}_{\text{val}} - \mathcal{L}_{\text{train}} \approx 0)
$$
