# 🎯 Lecture 22: Practice Problems — Technical Case Studies

[![Notebook](https://img.shields.io/badge/Jupyter-questions.ipynb-orange.svg?logo=jupyter&logoColor=white)](questions.ipynb)
[![PDF](https://img.shields.io/badge/PDF-questions.pdf-red.svg)](questions.pdf)
[![Solutions](https://img.shields.io/badge/Solutions-View%20Solutions-green.svg)](../Solutions/README.md)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [💡 View Complete Solutions](../Solutions/README.md) | [📁 Overview](../README.md)

---

# 📌 Case Study 1: Gradient Descent Optimization on Non-Convex & Quadratic Loss Landscapes

### 🏢 Context & Engineering Problem
In training deep learning models, convergence speed and numerical stability are governed by the curvature of the loss surface and the selected learning rate $\eta$.

Consider a 1D quadratic model loss function:

$$
\mathcal{L}(w) = 2(w - 3)^2 + 4
$$

and a non-convex quartic loss function with multiple extrema:

$$
\mathcal{J}(w) = w^4 - 4w^2 + 2w
$$

### 🎯 Mathematical & Implementation Tasks
1. **Analytical Gradient Descent Recurrence:**
   For quadratic loss $\mathcal{L}(w)$, compute the exact derivative $\frac{d\mathcal{L}}{dw}$. Write down the parameter recurrence relation for $w_{t+1}$ in terms of $w_t$ and learning rate $\eta$.
2. **Stability & Convergence Criterion:**
   Prove mathematically the exact range of learning rates $\eta$ for which gradient descent converges to $w^* = 3$. Find the threshold where oscillations begin and where divergence occurs.
3. **Non-Convex Extrema Analysis:**
   For $\mathcal{J}(w)$, compute $\mathcal{J}'(w)$ and $\mathcal{J}''(w)$. Show that gradient descent initialized from $w_0 = -2$ vs $w_0 = +2$ converges to distinct local minima.
4. **Python Pipeline:**
   Implement a reusable Python gradient descent simulator and plot parameter trajectories for stable, oscillatory, and diverging learning rates.

---

# 📌 Case Study 2: Deep Learning Activation Derivatives & the Vanishing Gradient Dilemma

### 🏢 Context & Engineering Problem
During backpropagation in deep feedforward networks, the gradient of the loss with respect to early layer weights is computed via the chain rule. If activation derivatives are strictly bounded below $1.0$, gradients exponentially attenuate as they backpropagate through depth, causing the notorious **Vanishing Gradient** problem.

### 🎯 Mathematical & Implementation Tasks
1. **Sigmoid Derivative Proof:**
   Starting from $\sigma(z) = \frac{1}{1 + e^{-z}}$, derive the analytical derivative $\sigma'(z) = \sigma(z)(1 - \sigma(z))$. Prove mathematically that the maximum possible value of $\sigma'(z)$ is $\frac{1}{4} = 0.25$, occurring at $z = 0$.
2. **Hyperbolic Tangent Derivative Proof:**
   Starting from $\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$, prove that $\tanh'(z) = 1 - \tanh^2(z)$, and show that its maximum derivative is $1.0$ at $z = 0$.
3. **Multi-Layer Attenuation Factor:**
   In an $L = 10$ layer neural network using Sigmoid activations, show that the product of activation derivatives along the backpropagation path satisfies:

$$
\prod_{l=1}^{10} \sigma'(z^{(l)}) \le (0.25)^{10} \approx 9.54 \times 10^{-7}
$$

4. **ReLU Superiority:**
   Explain why the Rectified Linear Unit ($\text{ReLU}(z) = \max(0, z)$) with derivative $\text{ReLU}'(z) = 1.0$ for $z > 0$ completely circumvents exponential gradient decay.
5. **Python Visualization:**
   Implement and plot the function values and first derivatives of Sigmoid, Tanh, and ReLU across $z \in [-5, 5]$.

---

# 📌 Case Study 3: Higher-Order Calculus & Curvature: Complete Polynomial Extremum Analysis

### 🏢 Context & Engineering Problem
In modern optimization (such as Newton-Raphson methods and Second-Order Optimization in ML), analyzing the second derivative $f''(x)$ reveals the local curvature, enabling identification of minima, maxima, and inflection points.

Consider the cubic function analyzed in the lecture:

$$
f(x) = x^3 - 6x^2 + 9x
$$

### 🎯 Mathematical & Implementation Tasks
1. **First Derivative & Critical Points:**
   Compute $f'(x)$, set $f'(x) = 0$, and find all critical points.
2. **Second Derivative & Classification:**
   Compute $f''(x)$. Evaluate $f''(x)$ at each critical point to formally prove which point is a local maximum and which is a local minimum.
3. **Inflection Point:**
   Find the exact coordinates $(x, y)$ of the inflection point where concavity transitions from concave down to concave up.
4. **Second-Order Taylor Approximation:**
   Compute the quadratic Taylor polynomial approximation of $f(x)$ centered around the local minimum $x = 3$. Prove that near the minimum, $f(x) \approx 3(x - 3)^2$.
5. **Python Visualization:**
   Plot $f(x)$, $f'(x)$, the horizontal tangent lines at the extrema, the inflection point, and the local quadratic approximation.
