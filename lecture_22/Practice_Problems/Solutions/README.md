# 💡 Lecture 22: Practice Problems — Comprehensive Solutions Guide

[![Notebook](https://img.shields.io/badge/Jupyter-solutions.ipynb-orange.svg?logo=jupyter&logoColor=white)](solutions.ipynb)
[![PDF](https://img.shields.io/badge/PDF-solutions.pdf-red.svg)](solutions.pdf)
[![Questions](https://img.shields.io/badge/Questions-View%20Set-blue.svg)](../Questions/README.md)
[![Case 1 Plot](https://img.shields.io/badge/Plot-Case%201%20Gradient%20Descent-blue.svg)](case1_gradient_descent_loss_surface.png)
[![Case 2 Plot](https://img.shields.io/badge/Plot-Case%202%20Activation%20Derivatives-green.svg)](case2_activation_derivatives_comparison.png)
[![Case 3 Plot](https://img.shields.io/badge/Plot-Case%203%20Concavity%20Extrema-purple.svg)](case3_second_derivative_concavity_extrema.png)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Questions](../Questions/README.md) | [📁 Practice Problems Overview](../README.md)

---

## 📌 Executive Architecture & Engineering Standards

This document provides production-grade reference solutions, formal mathematical proofs, and executive visual engineering implementations for the 3 industry case studies in **Lecture 22**.

---

# 📌 Solution to Case 1: Gradient Descent Optimization on Non-Convex & Quadratic Loss Landscapes

### 1. Mathematical Derivations & Proofs

#### Task 1: Gradient & Recurrence Relation
For quadratic loss $\mathcal{L}(w) = 2(w - 3)^2 + 4$:

$$
\frac{d\mathcal{L}}{dw} = 4(w - 3)
$$

The Gradient Descent recurrence relation is:

$$
w_{t+1} = w_t - \eta \frac{d\mathcal{L}}{dw}(w_t) = w_t - 4\eta (w_t - 3)
$$

Subtract $3$ from both sides to analyze distance from optimal $w^* = 3$:

$$
w_{t+1} - 3 = (1 - 4\eta)(w_t - 3)
$$

By induction, the error after $t$ steps is:

$$
e_t = (w_t - 3) = (1 - 4\eta)^t (w_0 - 3)
$$

---

#### Task 2: Stability & Convergence Analysis
For the error to converge to zero as $t \to \infty$, the contraction factor must satisfy $|1 - 4\eta| < 1$:

$$
-1 < 1 - 4\eta < 1 \implies -2 < -4\eta < 0 \implies \boxed{0 < \eta < 0.5}
$$

Behavior breakdown:
1. **Monotonic Convergence ($0 < \eta < 0.25$):** $0 < 1 - 4\eta < 1$. No oscillations.
2. **Deadbeat Optimal Convergence ($\eta = 0.25$):** $1 - 4(0.25) = 0 \implies w_1 = 3$ in a single step!
3. **Oscillatory Convergence ($0.25 < \eta < 0.5$):** $-1 < 1 - 4\eta < 0$. Error alternates signs but decays.
4. **Divergent Explosion ($\eta > 0.5$):** $|1 - 4\eta| > 1$. Error exponentially amplifies to $\pm \infty$.

---

#### Task 3: Non-Convex Loss Extrema Analysis
For $\mathcal{J}(w) = w^4 - 4w^2 + 2w$:

$$
\mathcal{J}'(w) = 4w^3 - 8w + 2 = 2(2w^3 - 4w + 1) = 0
$$

The roots are approximately:
- $w_1 \approx -1.525$ (Global Minimum: $\mathcal{J} \approx -6.91$)
- $w_2 \approx 0.260$ (Local Maximum: $\mathcal{J} \approx 0.25$)
- $w_3 \approx 1.265$ (Local Minimum: $\mathcal{J} \approx -1.34$)

Evaluating the second derivative $\mathcal{J}''(w) = 12w^2 - 8$:
- $\mathcal{J}''(-1.525) \approx 12(2.326) - 8 = 19.91 > 0 \implies$ Local Minimum.
- $\mathcal{J}''(0.260) \approx 12(0.068) - 8 = -7.18 < 0 \implies$ Local Maximum.
- $\mathcal{J}''(1.265) \approx 12(1.600) - 8 = 11.20 > 0 \implies$ Local Minimum.

Initialization at $w_0 = -2$ leads to global minimum $w \approx -1.525$, whereas $w_0 = +2$ is trapped in sub-optimal local minimum $w \approx 1.265$.

---

# 📌 Solution to Case 2: Deep Learning Activation Derivatives & the Vanishing Gradient Dilemma

### 1. Mathematical Derivations & Proofs

#### Task 1: Sigmoid Derivative Proof & Upper Bound
For $\sigma(z) = (1 + e^{-z})^{-1}$:

$$
\sigma'(z) = -(1 + e^{-z})^{-2} \cdot (-e^{-z}) = \frac{e^{-z}}{(1 + e^{-z})^2}
$$

Rewrite:

$$
\sigma'(z) = \frac{1}{1 + e^{-z}} \cdot \frac{e^{-z}}{1 + e^{-z}} = \sigma(z) \cdot \left(\frac{1 + e^{-z} - 1}{1 + e^{-z}}\right) = \boxed{\sigma(z)(1 - \sigma(z))}
$$

To find the maximum of $g(s) = s(1 - s)$ where $s = \sigma(z) \in (0, 1)$:

$$
g'(s) = 1 - 2s = 0 \implies s = \frac{1}{2} \implies \sigma(z) = \frac{1}{2} \iff z = 0
$$

The maximum derivative is:

$$
\max_{z} \sigma'(z) = \frac{1}{2} \left(1 - \frac{1}{2}\right) = \boxed{\frac{1}{4} = 0.25}
$$

---

#### Task 2: Tanh Derivative Proof
For $\tanh(z) = \frac{\sinh(z)}{\cosh(z)}$:

$$
\tanh'(z) = \frac{\cosh(z)\cosh(z) - \sinh(z)\sinh(z)}{\cosh^2(z)} = \frac{\cosh^2(z) - \sinh^2(z)}{\cosh^2(z)} = \boxed{1 - \tanh^2(z)}
$$

Since $\tanh^2(z) \ge 0$, the maximum occurs when $\tanh(z) = 0 \implies z = 0$:

$$
\max_z \tanh'(z) = 1 - 0^2 = \boxed{1.0}
$$

---

#### Task 3: Gradient Attenuation Across 10 Layers
In an $L = 10$ layer network with Sigmoid activations:

$$
\prod_{l=1}^{10} \sigma'(z^{(l)}) \le \prod_{l=1}^{10} (0.25) = (0.25)^{10} = \frac{1}{4^{10}} = \frac{1}{1,048,576} \approx 9.537 \times 10^{-7}
$$

Gradients reaching the input layer are attenuated by over **one million times**, rendering weight updates completely stalled.

---

#### Task 4: Why ReLU Eliminates Gradient Attenuation
For Rectified Linear Unit:

$$
\text{ReLU}(z) = \max(0, z) \implies \text{ReLU}'(z) = \begin{cases} 1.0 & z > 0 \\ 0.0 & z < 0 \end{cases}
$$

For all active neurons ($z > 0$), $\text{ReLU}'(z) = 1.0$. The gradient product becomes:

$$
\prod_{l=1}^{10} 1.0 = 1.0
$$

There is zero multiplicative decay, allowing deep networks to scale to hundreds of layers.

---

# 📌 Solution to Case 3: Higher-Order Calculus & Curvature: Complete Polynomial Extremum Analysis

### 1. Mathematical Derivations & Proofs

#### Task 1: First Derivative & Critical Points
For $f(x) = x^3 - 6x^2 + 9x$:

$$
f'(x) = 3x^2 - 12x + 9 = 3(x^2 - 4x + 3) = 3(x - 1)(x - 3)
$$

Setting $f'(x) = 0$:

$$
(x - 1)(x - 3) = 0 \implies x_1 = 1, \quad x_2 = 3
$$

---

#### Task 2: Second Derivative Classification
Differentiating again:

$$
f''(x) = 6x - 12 = 6(x - 2)
$$

1. **At $x_1 = 1$:**
   $$
   f''(1) = 6(1 - 2) = -6 < 0 \implies \text{Concave Down} \implies \boxed{\text{Local Maximum}}
   $$
   $$
   y_{\text{max}} = f(1) = 1^3 - 6(1)^2 + 9(1) = 4
   $$
2. **At $x_2 = 3$:**
   $$
   f''(3) = 6(3 - 2) = +6 > 0 \implies \text{Concave Up} \implies \boxed{\text{Local Minimum}}
   $$
   $$
   y_{\text{min}} = f(3) = 3^3 - 6(3)^2 + 9(3) = 27 - 54 + 27 = 0
   $$

---

#### Task 3: Inflection Point
Setting $f''(x) = 0$:

$$
6(x - 2) = 0 \implies x_{\text{inf}} = 2
$$

Evaluating $f(2)$:

$$
f(2) = 2^3 - 6(2)^2 + 9(2) = 8 - 24 + 18 = 2
$$

The inflection point is located at $(2, 2)$, where the slope is:

$$
f'(2) = 3(2)^2 - 12(2) + 9 = 12 - 24 + 9 = -3
$$

---

#### Task 4: Second-Order Taylor Polynomial at $x = 3$
The second-order Taylor expansion around $x_0 = 3$ is:

$$
P_2(x) = f(3) + f'(3)(x - 3) + \frac{f''(3)}{2!} (x - 3)^2
$$

Substitute known values $f(3) = 0$, $f'(3) = 0$, $f''(3) = 6$:

$$
P_2(x) = 0 + 0(x - 3) + \frac{6}{2} (x - 3)^2 = \boxed{3(x - 3)^2}
$$

This parabola matches the curvature and local minimum of $f(x)$ at $x=3$, demonstrating how Newton's optimization method uses quadratic approximations to step directly to optimal points.
