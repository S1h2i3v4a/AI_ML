# Module 23.10: Understanding the Cost Function Curve (Convexity & Contour Plots)

## 1. Feature Space vs. Parameter Space

Understanding machine learning requires switching between two complementary geometric representations:

| Dimension | Feature Space (Data Space) | Parameter Space (Loss Surface) |
| :--- | :--- | :--- |
| **Axes** | Horizontal: $x$, Vertical: $y$ | Horizontal: $w$, Vertical: $b$ (and Height: $J$) |
| **Data Points** | Individual scatter points $(x^{(i)}, y^{(i)})$ | Transformed into constants within the cost equation |
| **Model** | A candidate straight line $\hat{y} = w x + b$ | A **single point** $(w, b)$ on the landscape |
| **Goal** | Find line that fits data scatter | Find the lowest coordinate (valley bottom) in the landscape |

---

## 2. The 1D Cost Curve: A Quadratic Parabola

To understand the geometry, consider the simplified univariate case where intercept $b = 0$. The hypothesis is $\hat{y} = w x$.

$$
J(w) = \frac{1}{2m} \sum_{i=1}^m (w x^{(i)} - y^{(i)})^2 = \frac{1}{2m} \sum_{i=1}^m \left[ (x^{(i)})^2 w^2 - 2 x^{(i)} y^{(i)} w + (y^{(i)})^2 \right]
$$

Rearranging terms in powers of $w$:

$$
J(w) = A w^2 - B w + C
$$

Where:
$$
A = \frac{1}{2m} \sum_{i=1}^m (x^{(i)})^2, \quad B = \frac{1}{m} \sum_{i=1}^m x^{(i)} y^{(i)}, \quad C = \frac{1}{2m} \sum_{i=1}^m (y^{(i)})^2
$$

Since $(x^{(i)})^2 \ge 0$, coefficient $A > 0$ for any non-trivial dataset.
Therefore, $J(w)$ is a **parabola opening upwards** (convex quadratic curve). It has a single unique global minimum at the vertex:

$$
w^* = \frac{B}{2A} = \frac{\sum x^{(i)} y^{(i)}}{\sum (x^{(i)})^2}
$$

---

## 3. The 2D Cost Landscape: 3D Paraboloid Bowl

When both parameters $w$ and $b$ are variable, the cost function $J(w, b)$ forms a 3-dimensional surface shaped like a **bowl** (an elliptic paraboloid).

```
         J(w, b) ^
                 |     \           /
                 |      \         /
                 |       \_______/  <-- Global Minimum (Bottom of Bowl)
                 |
                 +--------------------> w
                /
               /
            b v
```

### Strict Convexity and the Hessian Matrix
A function is strictly convex if its Hessian matrix $\mathbf{H}$ (matrix of second-order partial derivatives) is positive definite everywhere:

$$
\mathbf{H} = \begin{bmatrix} \frac{\partial^2 J}{\partial w^2} & \frac{\partial^2 J}{\partial w \partial b} \\ \frac{\partial^2 J}{\partial b \partial w} & \frac{\partial^2 J}{\partial b^2} \end{bmatrix} = \begin{bmatrix} \frac{1}{m} \sum (x^{(i)})^2 & \frac{1}{m} \sum x^{(i)} \\ \frac{1}{m} \sum x^{(i)} & 1 \end{bmatrix}
$$

Evaluating the determinant of $\mathbf{H}$:

$$
\det(\mathbf{H}) = \frac{1}{m} \sum (x^{(i)})^2 - (\bar{x})^2 = \text{Var}(X)
$$

Because sample variance $\text{Var}(X) > 0$ whenever $x$ contains varying values, $\mathbf{H}$ is strictly positive definite.
> **Key Consequence:** Linear regression with MSE has **no local minima**! Any local minimum is guaranteed to be the unique **global minimum**.

---

## 4. Contour Plots (Level Curves)

A **contour plot** projects 3D surface slices of constant cost $J(w, b) = c$ onto a 2D plane:
- Each closed elliptical ring represents a set of parameters $(w, b)$ yielding identical cost.
- The concentric rings contract toward a single central point: the global minimum $(w^*, b^*)$.
- The gradient vector $\nabla J(w, b)$ is always **strictly perpendicular** to the tangent of the contour curve at that point.
