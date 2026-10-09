# Module 24.14: Logistic Regression — Cost Function & Optimization

## 1. Why Mean Squared Error (MSE) Fails for Logistic Regression

In linear regression, MSE yields a strictly convex paraboloid.
However, if we insert the non-linear Sigmoid hypothesis $\hat{y} = \sigma(\mathbf{w}^T \mathbf{x} + b)$ into the MSE loss:

$$
J_{\text{MSE}}(\mathbf{w}) = \frac{1}{2m} \sum_{i=1}^m \left( \sigma(\mathbf{w}^T \mathbf{x}^{(i)} + b) - y^{(i)} \right)^2
$$

The resulting loss surface is **non-convex**, riddled with flat plateaus and local minima! Gradient descent gets trapped and fails to converge to the optimal parameters.

---

## 2. Derivation of the Binary Cross-Entropy Cost via Maximum Likelihood Estimation (MLE)

For binary targets $y \in \{0, 1\}$, the outcome follows a **Bernoulli distribution**:

$$
P(y|\mathbf{x}) = \hat{y}^y (1 - \hat{y})^{1 - y}
$$

For a dataset of $m$ independent observations, the joint **Likelihood Function** is:

$$
L(\mathbf{w}, b) = \prod_{i=1}^m P(y^{(i)} | \mathbf{x}^{(i)}) = \prod_{i=1}^m (\hat{y}^{(i)})^{y^{(i)}} (1 - \hat{y}^{(i)})^{1 - y^{(i)}}
$$

### Taking the Log-Likelihood:
$$
\ln L(\mathbf{w}, b) = \sum_{i=1}^m \left[ y^{(i)} \ln \hat{y}^{(i)} + (1 - y^{(i)}) \ln(1 - \hat{y}^{(i)}) \right]
$$

### Converting to Minimization (Negative Log-Likelihood / Log Loss):
Dividing by $-m$, we obtain the **Binary Cross-Entropy (Log Loss)** cost function:

$$
J(\mathbf{w}, b) = -\frac{1}{m} \sum_{i=1}^m \left[ y^{(i)} \ln \hat{y}^{(i)} + (1 - y^{(i)}) \ln(1 - \hat{y}^{(i)}) \right]
$$

---

## 3. Piecewise Penalty Mechanics

The loss per sample $L(\hat{y}, y)$ exhibits asymmetric logarithmic penalties:

$$
L(\hat{y}, y) = \begin{cases} -\ln(\hat{y}) & \text{if } y = 1 \\ -\ln(1 - \hat{y}) & \text{if } y = 0 \end{cases}
$$

```
  If True Label y = 1:                    If True Label y = 0:
  Loss ^                                  Loss ^
       | \                                     |                                   /
       |  \                                    |                                  /
       |   \                                   |                                 /
       |    \                                  |                                /
     0 +-----+--------> \hat{y}              0 +-------------------------------+---> \hat{y}
       0     1                                 0                               1
  Prediction \hat{y} -> 1 ==> Loss -> 0   Prediction \hat{y} -> 0 ==> Loss -> 0
  Prediction \hat{y} -> 0 ==> Loss -> inf Prediction \hat{y} -> 1 ==> Loss -> inf
```

If the model predicts confident wrong answers ($y=1$ but $\hat{y}=0$), the penalty approaches **infinity**!

---

## 4. Analytic Gradient Derivation & Update Rule

Applying the chain rule using $\frac{d\sigma}{dz} = \sigma(z)(1 - \sigma(z))$:

$$
\frac{\partial J}{\partial w_j} = \frac{1}{m} \sum_{i=1}^m \left( \hat{y}^{(i)} - y^{(i)} \right) x_j^{(i)}
$$

$$
\frac{\partial J}{\partial b} = \frac{1}{m} \sum_{i=1}^m \left( \hat{y}^{(i)} - y^{(i)} \right)
$$

### Vectorized Gradient Descent Update:
$$
\mathbf{w} := \mathbf{w} - \alpha \left[ \frac{1}{m} \mathbf{X}^T (\hat{\mathbf{y}} - \mathbf{y}) \right]
$$

$$
b := b - \alpha \left[ \frac{1}{m} \sum_{i=1}^m (\hat{y}^{(i)} - y^{(i)}) \right]
$$
