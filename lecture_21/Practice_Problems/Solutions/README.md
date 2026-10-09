# 💡 Lecture 21: Practice Problems — Comprehensive Solutions Guide

[![Notebook](https://img.shields.io/badge/Jupyter-solutions.ipynb-orange.svg?logo=jupyter&logoColor=white)](solutions.ipynb)
[![PDF](https://img.shields.io/badge/PDF-solutions.pdf-red.svg)](solutions.pdf)
[![Questions](https://img.shields.io/badge/Questions-View%20Set-blue.svg)](../Questions/README.md)
[![Case 1 Plot](https://img.shields.io/badge/Plot-Case%201%20Affine%20Grid-blue.svg)](case1_affine_transformation_grid.png)
[![Case 2 Plot](https://img.shields.io/badge/Plot-Case%202%20SVM%20Margin-green.svg)](case2_svm_maximum_margin.png)
[![Case 3 Plot](https://img.shields.io/badge/Plot-Case%203%20PCA%20Spectrum-purple.svg)](case3_pca_covariance_eigenvectors.png)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Questions](../Questions/README.md) | [📁 Practice Problems Overview](../README.md)

---

## 📌 Executive Architecture & Engineering Standards

This document provides production-grade reference solutions, formal mathematical proofs, and executive visual engineering implementations for the 3 industry case studies in **Lecture 21**.

---

# 📌 Solution to Case 1: Computer Vision 2D Affine Transformations & Homogeneous Coordinates

### 1. Mathematical Derivations & Proofs

#### Task 1: Elementary Homogeneous Matrices
For angle $\theta = 45^\circ = \frac{\pi}{4}$, $\cos(\frac{\pi}{4}) = \sin(\frac{\pi}{4}) = \frac{\sqrt{2}}{2} \approx 0.7071$:

$$
R\left(\frac{\pi}{4}\right) = \begin{bmatrix} \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} & 0 \\ \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

For horizontal shear with $k_x = 0.5$:

$$
Sh(0.5) = \begin{bmatrix} 1 & 0.5 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

For translation vector $\mathbf{t} = [3, -2]^T$:

$$
T(3, -2) = \begin{bmatrix} 1 & 0 & 3 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{bmatrix}
$$

---

#### Task 2: Matrix Composition & Non-Commutativity
Computing $M_1 = T \cdot Sh \cdot R$:
First, multiply $Sh \cdot R$:

$$
Sh \cdot R = \begin{bmatrix} 1 & 0.5 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} & 0 \\ \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} & 0 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} \frac{3\sqrt{2}}{4} & -\frac{\sqrt{2}}{4} & 0 \\ \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

Now left-multiply by $T$:

$$
M_1 = T \cdot (Sh \cdot R) = \begin{bmatrix} \frac{3\sqrt{2}}{4} & -\frac{\sqrt{2}}{4} & 3 \\ \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} & -2 \\ 0 & 0 & 1 \end{bmatrix} \approx \begin{bmatrix} 1.0607 & -0.3536 & 3.0 \\ 0.7071 & 0.7071 & -2.0 \\ 0 & 0 & 1.0 \end{bmatrix}
$$

Now computing $M_2 = R \cdot T \cdot Sh$:
Notice that in $M_2$, the translation occurs before rotation. The translation vector $[3, -2]^T$ gets rotated by $R$, causing the translational component to become:

$$
R \begin{bmatrix} 3 \\ -2 \end{bmatrix} = \begin{bmatrix} \frac{\sqrt{2}}{2}(3 - (-2)) \\ \frac{\sqrt{2}}{2}(3 + (-2)) \end{bmatrix} = \begin{bmatrix} \frac{5\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} \end{bmatrix} \approx \begin{bmatrix} 3.5355 \\ 0.7071 \end{bmatrix} \ne \begin{bmatrix} 3 \\ -2 \end{bmatrix}
$$

Hence $M_1 \ne M_2$. In computer vision data augmentation pipelines, changing the order of rotation and translation completely relocates the bounding boxes.

---

#### Task 3: Determinant & Area Scaling
For any 2D affine map in homogeneous coordinates:

$$
M = \begin{bmatrix} A & \mathbf{t} \\ \mathbf{0}^T & 1 \end{bmatrix} \implies \det(M) = \det(A)
$$

For $M_1$, the linear transformation block is $A = Sh \cdot R$:

$$
\det(A) = \det(Sh) \cdot \det(R) = (1 \cdot 1 - 0.5 \cdot 0) \cdot (\cos^2\theta + \sin^2\theta) = 1 \cdot 1 = 1
$$

Since $|\det(A)| = 1.0$, the combined rotation, horizontal shearing, and translation preserves the total polygonal area exactly (area scaling factor is $1.0$).

---

#### Task 4: Backward Warping & Inverse Matrix
In forward mapping $\mathbf{x}_{\text{dst}} = M \mathbf{x}_{\text{src}}$, rounding floating-point coordinates to integer pixel coordinates creates "holes" (unmapped destination pixels) and collisions.
Backward warping avoids this by scanning every discrete destination coordinate $(x_d, y_d)$ and sampling the source image at:

$$
\tilde{\mathbf{x}}_{\text{src}} = M_1^{-1} \tilde{\mathbf{x}}_{\text{dst}}
$$

Since $M_1 = T \cdot Sh \cdot R$, its analytical inverse is:

$$
M_1^{-1} = R^{-1} \cdot Sh^{-1} \cdot T^{-1} = R(-\theta) \cdot Sh(-k_x) \cdot T(-\mathbf{t})
$$

Numerically:

$$
M_1^{-1} = \begin{bmatrix} 0.7071 & 0.3536 & -1.4142 \\ -0.7071 & 1.0607 & 4.2426 \\ 0 & 0 & 1 \end{bmatrix}
$$

---

# 📌 Solution to Case 2: Support Vector Machine (SVM) Maximum-Margin Hyperplane & Vector Projections

### 1. Mathematical Derivations & Proofs

#### Task 1: Normal Vector Orthogonality Proof
Let hyperplane $H = \{\mathbf{x} \in \mathbb{R}^n \mid \mathbf{w}^T \mathbf{x} + b = 0\}$.
Take any two distinct points $\mathbf{x}_a, \mathbf{x}_b \in H$. By definition:

$$
\mathbf{w}^T \mathbf{x}_a + b = 0 \quad\text{and}\quad \mathbf{w}^T \mathbf{x}_b + b = 0
$$

Subtracting the two equations:

$$
\mathbf{w}^T (\mathbf{x}_a - \mathbf{x}_b) = 0
$$

Since the vector $(\mathbf{x}_a - \mathbf{x}_b)$ lies entirely within the hyperplane surface $H$, its dot product with $\mathbf{w}$ is zero. Therefore, $\mathbf{w}$ is orthogonal to every vector in $H$, proving that $\mathbf{w}$ is the normal vector to the hyperplane.

---

#### Task 2: Orthogonal Point-to-Hyperplane Distance Formula
Let $\mathbf{x}_0 \in \mathbb{R}^n$ be any arbitrary point, and let $\mathbf{x}_p \in H$ be its orthogonal projection onto the hyperplane.
Because $\mathbf{x}_0 - \mathbf{x}_p$ is parallel to the normal vector $\mathbf{w}$:

$$
\mathbf{x}_0 - \mathbf{x}_p = d \cdot \hat{\mathbf{w}} = d \cdot \frac{\mathbf{w}}{\|\mathbf{w}\|_2} \implies \mathbf{x}_p = \mathbf{x}_0 - d \frac{\mathbf{w}}{\|\mathbf{w}\|_2}
$$

Since $\mathbf{x}_p \in H$, it satisfies $\mathbf{w}^T \mathbf{x}_p + b = 0$:

$$
\mathbf{w}^T \left(\mathbf{x}_0 - d \frac{\mathbf{w}}{\|\mathbf{w}\|_2}\right) + b = 0 \implies \mathbf{w}^T \mathbf{x}_0 + b - d \frac{\mathbf{w}^T \mathbf{w}}{\|\mathbf{w}\|_2} = 0
$$

Since $\mathbf{w}^T \mathbf{w} = \|\mathbf{w}\|_2^2$:

$$
\mathbf{w}^T \mathbf{x}_0 + b - d \|\mathbf{w}\|_2 = 0 \implies \boxed{d(\mathbf{x}_0, H) = \frac{\mathbf{w}^T \mathbf{x}_0 + b}{\|\mathbf{w}\|_2}}
$$

---

#### Task 3: Geometric Margin Derivation
For canonical support vectors $\mathbf{x}_+$ on $H_+: \mathbf{w}^T \mathbf{x} + b = +1$ and $\mathbf{x}_-$ on $H_-: \mathbf{w}^T \mathbf{x} + b = -1$:
Project the difference vector $(\mathbf{x}_+ - \mathbf{x}_-)$ onto the unit normal vector $\hat{\mathbf{w}}$:

$$
\gamma = (\mathbf{x}_+ - \mathbf{x}_-)^T \frac{\mathbf{w}}{\|\mathbf{w}\|_2} = \frac{\mathbf{w}^T \mathbf{x}_+ - \mathbf{w}^T \mathbf{x}_-}{\|\mathbf{w}\|_2} = \frac{(1 - b) - (-1 - b)}{\|\mathbf{w}\|_2} = \boxed{\frac{2}{\|\mathbf{w}\|_2}}
$$

---

#### Task 4: Analytical Parameter Determination
For support vectors $\mathbf{x}_1 = [1, 2]^T$ (class $+1$) and $\mathbf{x}_3 = [3, 1]^T$ (class $-1$):
The vector connecting the support vectors is $\mathbf{v} = \mathbf{x}_1 - \mathbf{x}_3 = [1 - 3, 2 - 1]^T = [-2, 1]^T$.
The normal vector $\mathbf{w}$ is oriented from $-1$ to $+1$, so $\mathbf{w} \propto \mathbf{x}_1 - \mathbf{x}_3 = [-2, 1]^T$.
Let $\mathbf{w} = k [-2, 1]^T = [-2k, k]^T$.
Setting up the canonical support vector constraint:

$$
\mathbf{w}^T \mathbf{x}_1 + b = 1 \implies -2k(1) + k(2) + b = 1 \implies 0 + b = 1 \implies b = 1
$$

$$
\mathbf{w}^T \mathbf{x}_3 + b = -1 \implies -2k(3) + k(1) + 1 = -1 \implies -5k = -2 \implies k = \frac{2}{5} = 0.4
$$

Thus:

$$
\mathbf{w}^* = \begin{bmatrix} -0.8 \\ 0.4 \end{bmatrix}, \qquad b^* = 1.0
$$

The norm of $\mathbf{w}^*$ is:

$$
\|\mathbf{w}^*\|_2 = \sqrt{(-0.8)^2 + (0.4)^2} = \sqrt{0.64 + 0.16} = \sqrt{0.80} \approx 0.8944
$$

The optimal margin is:

$$
\gamma = \frac{2}{\|\mathbf{w}^*\|_2} = \frac{2}{\sqrt{0.80}} = \frac{2}{0.8944} \approx 2.2361 = \sqrt{5}
$$

The decision boundary equation is:

$$
-0.8 x_1 + 0.4 x_2 + 1.0 = 0 \implies x_2 = 2 x_1 - 2.5
$$

---

# 📌 Solution to Case 3: Quantitative Finance Risk & Sensor PCA Eigendecomposition

### 1. Mathematical Derivations & Proofs

#### Task 1: Covariance Symmetry & Positive Semi-Definiteness
Given $X_c \in \mathbb{R}^{N \times p}$, the sample covariance matrix is $\mathbf{\Sigma} = \frac{1}{N-1} X_c^T X_c$.
1. **Symmetry:**
   $$
   \mathbf{\Sigma}^T = \left(\frac{1}{N-1} X_c^T X_c\right)^T = \frac{1}{N-1} (X_c)^T (X_c^T)^T = \frac{1}{N-1} X_c^T X_c = \mathbf{\Sigma}
   $$
2. **Positive Semi-Definiteness:** For any non-zero vector $\mathbf{v} \in \mathbb{R}^p$:
   $$
   \mathbf{v}^T \mathbf{\Sigma} \mathbf{v} = \mathbf{v}^T \left(\frac{1}{N-1} X_c^T X_c\right) \mathbf{v} = \frac{1}{N-1} (X_c \mathbf{v})^T (X_c \mathbf{v}) = \frac{1}{N-1} \|X_c \mathbf{v}\|_2^2 \ge 0
   $$
3. Since $\mathbf{\Sigma}$ is real symmetric, all eigenvalues are real. Since $\mathbf{v}^T \mathbf{\Sigma} \mathbf{v} \ge 0$, for any eigenvector $\mathbf{q}_i$ with eigenvalue $\lambda_i$:
   $$
   \mathbf{q}_i^T \mathbf{\Sigma} \mathbf{q}_i = \mathbf{q}_i^T (\lambda_i \mathbf{q}_i) = \lambda_i \|\mathbf{q}_i\|_2^2 \ge 0 \implies \lambda_i \ge 0 \quad \forall i
   $$

---

#### Task 2: Lagrange Multiplier Proof for Maximum Variance
We wish to maximize $\mathcal{J}(\mathbf{q}) = \mathbf{q}^T \mathbf{\Sigma} \mathbf{q}$ subject to $\|\mathbf{q}\|_2^2 = \mathbf{q}^T \mathbf{q} = 1$.
Construct the Lagrangian function:

$$
\mathcal{L}(\mathbf{q}, \lambda) = \mathbf{q}^T \mathbf{\Sigma} \mathbf{q} - \lambda (\mathbf{q}^T \mathbf{q} - 1)
$$

Take the gradient with respect to vector $\mathbf{q}$ and set to zero:

$$
\nabla_{\mathbf{q}} \mathcal{L} = 2 \mathbf{\Sigma} \mathbf{q} - 2 \lambda \mathbf{q} = \mathbf{0} \implies \mathbf{\Sigma} \mathbf{q} = \lambda \mathbf{q}
$$

This is the standard eigenvector equation!
Substitute $\mathbf{\Sigma} \mathbf{q} = \lambda \mathbf{q}$ into the objective function:

$$
\mathcal{J}(\mathbf{q}) = \mathbf{q}^T \mathbf{\Sigma} \mathbf{q} = \mathbf{q}^T (\lambda \mathbf{q}) = \lambda \mathbf{q}^T \mathbf{q} = \lambda
$$

To maximize $\mathcal{J}(\mathbf{q})$, we must choose the maximum eigenvalue $\lambda_1$, and the optimal projection direction $\mathbf{q}^*$ is the principal eigenvector $\mathbf{q}_1$.

---

#### Task 3: Eigendecomposition of the Financial Covariance Matrix
For matrix:

$$
\mathbf{\Sigma} = \begin{bmatrix} 4.0 & 2.0 & 1.0 & 0.0 \\ 2.0 & 3.0 & 0.5 & 0.5 \\ 1.0 & 0.5 & 2.0 & 0.0 \\ 0.0 & 0.5 & 0.0 & 1.0 \end{bmatrix}
$$

Computing eigenvalues via characteristic polynomial $\det(\mathbf{\Sigma} - \lambda I) = 0$:
1. $\lambda_1 \approx 5.8679$
2. $\lambda_2 \approx 2.0000$
3. $\lambda_3 \approx 1.2586$
4. $\lambda_4 \approx 0.8735$

Total Portfolio Variance (Trace):

$$
\text{Tr}(\mathbf{\Sigma}) = 4.0 + 3.0 + 2.0 + 1.0 = 10.0
$$

Sum of eigenvalues:

$$
\sum_{i=1}^4 \lambda_i = 5.8679 + 2.0000 + 1.2586 + 0.8735 = 10.0000 \quad (\text{Exact trace match!})
$$

Proportion of Explained Variance ($\text{PEV}_k$):
- Factor 1 ($\lambda_1$): $\frac{5.8679}{10.0} = 58.68\%$
- Factor 2 ($\lambda_2$): $\frac{2.0000}{10.0} = 20.00\%$
- Factor 3 ($\lambda_3$): $\frac{1.2586}{10.0} = 12.59\%$
- Factor 4 ($\lambda_4$): $\frac{0.8735}{10.0} = 8.74\%$

Cumulative Explained Variance:
- Top 1 Component: $58.68\%$
- Top 2 Components: $58.68\% + 20.00\% = 78.68\%$
- Top 3 Components: $78.68\% + 12.59\% = 91.27\%$

---

#### Task 4: Dimension Reduction Criterion
To achieve at least $80\%$ explained risk/variance:
- 1 component achieves $58.68\% < 80\%$
- 2 components achieve $78.68\% < 80\%$ (close, but strictly under threshold)
- 3 components achieve $91.27\% \ge 80\%$
Therefore, **$k = 3$ principal factors** are required to guarantee $>80\%$ risk coverage.

---

#### Task 5: Rank-2 Reconstruction & Frobenius Error
Using the top 2 eigenvectors $\mathbf{q}_1, \mathbf{q}_2$:

$$
\mathbf{\Sigma}_2 = \lambda_1 \mathbf{q}_1 \mathbf{q}_1^T + \lambda_2 \mathbf{q}_2 \mathbf{q}_2^T
$$

The residual matrix is:

$$
\mathbf{\Sigma} - \mathbf{\Sigma}_2 = \lambda_3 \mathbf{q}_3 \mathbf{q}_3^T + \lambda_4 \mathbf{q}_4 \mathbf{q}_4^T
$$

Since eigenvectors are mutually orthonormal ($\mathbf{q}_i^T \mathbf{q}_j = \delta_{ij}$):

$$
\|\mathbf{\Sigma} - \mathbf{\Sigma}_2\|_F = \sqrt{\lambda_3^2 + \lambda_4^2} = \sqrt{(1.2586)^2 + (0.8735)^2} = \sqrt{1.5841 + 0.7630} = \sqrt{2.3471} \approx 1.5320
$$

The low-rank error matches the theoretical spectral lower bound established by the Eckart-Young-Mirsky Theorem.
