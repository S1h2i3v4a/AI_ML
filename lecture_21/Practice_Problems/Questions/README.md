# 🎯 Lecture 21: Practice Problems — Technical Case Studies

[![Notebook](https://img.shields.io/badge/Jupyter-questions.ipynb-orange.svg?logo=jupyter&logoColor=white)](questions.ipynb)
[![PDF](https://img.shields.io/badge/PDF-questions.pdf-red.svg)](questions.pdf)
[![Solutions](https://img.shields.io/badge/Solutions-View%20Solutions-green.svg)](../Solutions/README.md)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [💡 View Complete Solutions](../Solutions/README.md) | [📁 Overview](../README.md)

---

## 📌 Linear Algebra Practice Suite: Overview & Instructions

Linear Algebra is the foundational mathematical backbone of modern Artificial Intelligence and Deep Learning. From spatial coordinate transformations in Computer Vision to separating hyperplanes in Support Vector Machines, and spectral dimensionality reduction in high-dimensional financial factor modeling, AI algorithms rely on vectors, matrices, determinants, and eigendecomposition.

This practice module provides **3 comprehensive industry-grade case studies**:
1. **Case 1:** Computer Vision 2D Affine Transformations & Homogeneous Coordinates (Robotics & PyTorch Augmentation Pipelines)
2. **Case 2:** Support Vector Machine (SVM) Maximum-Margin Hyperplane & Vector Projections (Machine Learning Geometric Optimization)
3. **Case 3:** Quantitative Finance Risk & Sensor PCA Eigendecomposition (Multi-Asset Factor Risk & Spectral Analysis)

---

# 📌 Case Study 1: Computer Vision 2D Affine Transformations & Homogeneous Coordinates

### 🏢 Real-World Context & Engineering Problem

In modern computer vision and autonomous robotics pipelines (such as PyTorch `torchvision.transforms`, OpenCV, and Spatial Transformer Networks), image geometric transformations are modeled via linear maps in 2D projective space $\mathbb{P}^2$.

In standard 2D Cartesian coordinates $(x, y)$, **Rotation** and **Shear** are linear operations, but **Translation** (coordinate shift) is non-linear:

$$
\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} x + t_x \\ y + t_y \end{bmatrix}
$$

This translation cannot be expressed as a $2 \times 2$ matrix multiplication. To resolve this, computer vision engineers embed 2D coordinates into **Homogeneous Coordinates**:

$$
\tilde{\mathbf{x}} = \begin{bmatrix} x \\ y \\ 1 \end{bmatrix} \in \mathbb{P}^2
$$

An autonomous inspection robot camera captures a rectangular object whose polygon vertices are represented by the matrix $V \in \mathbb{R}^{3 \times 4}$:

$$
V = \begin{bmatrix} 0 & 2 & 2 & 0 \\ 0 & 0 & 3 & 3 \\ 1 & 1 & 1 & 1 \end{bmatrix}
$$

The 4 columns represent the 4 corner vertices:

$$
\mathbf{v}_1 = \begin{bmatrix} 0 \\ 0 \end{bmatrix}, \quad
\mathbf{v}_2 = \begin{bmatrix} 2 \\ 0 \end{bmatrix}, \quad
\mathbf{v}_3 = \begin{bmatrix} 2 \\ 3 \end{bmatrix}, \quad
\mathbf{v}_4 = \begin{bmatrix} 0 \\ 3 \end{bmatrix}
$$

The initial rectangle has width $w = 2$ units and height $h = 3$ units, with initial area:

$$
\text{Area}_{\text{initial}} = w \times h = 2 \times 3 = 6.0 \text{ square units}
$$

The vision augmentation pipeline requires applying **3 sequential geometric operations**:

1. **Counter-Clockwise Rotation:** Rotation around the origin $(0, 0)$ by angle:

$$
\theta = 45^\circ = \frac{\pi}{4} \text{ radians}
$$

2. **Horizontal Shear:** Shearing along the X-axis with shear factor:

$$
k_x = 0.5
$$

3. **Coordinate Translation:** Displacement by offset vector:

$$
\mathbf{t} = \begin{bmatrix} t_x \\ t_y \end{bmatrix} = \begin{bmatrix} 3.0 \\ -2.0 \end{bmatrix}
$$

---

### 📋 Questions Asked in This Case Study (Clear Objectives in Text Form)

You are required to address and solve the following **5 specific engineering deliverables**:

- **Bullet Point 1:** Construct explicit $3 \times 3$ Homogeneous Matrices for the three elementary transformations: Rotation, Horizontal Shear, and Translation.
- **Bullet Point 2:** Compute the standard composite transformation matrix and the alternate sequence matrix. Prove mathematically that matrix multiplication does not commute and explain why transformation ordering is critical in computer vision pipelines.
- **Bullet Point 3:** Calculate the determinant of the upper-left $2 \times 2$ linear block of the composite matrix. Prove that translation does not alter the area of the polygon, and evaluate the final Area Scaling Factor.
- **Bullet Point 4:** Explain why Forward Warping generates rasterization holes (unmapped destination pixels) in digital image processing, and derive the explicit analytical inverse matrix required for Backward Warping.
- **Bullet Point 5:** Implement an end-to-end Python script using NumPy to compute transformed vertex coordinates and visualize both original and transformed polygons on a coordinate grid.

---

### 🔍 Detailed In-Depth Explanation of Each Bullet Point

#### 1. Bullet Point 1 Explanation: Elementary Homogeneous Matrices Construction
- **What It Means:** Standard $2 \times 2$ matrices cannot accommodate translation because translation shifts the origin. Homogeneous coordinates append a dummy scale factor $w = 1$.
- **Why It Is Essential:** Standardizing all operations into $3 \times 3$ matrices allows hardware accelerators (GPUs) to chain multiple complex geometric transformations into a single matrix product.
- **How to Formulate:** Substitute the given parameters into the three elementary $3 \times 3$ matrices:

$$
R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad
Sh(k_x) = \begin{bmatrix} 1 & k_x & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad
T(t_x, t_y) = \begin{bmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{bmatrix}
$$

#### 2. Bullet Point 2 Explanation: Matrix Composition & Non-Commutativity
- **What It Means:** Investigate whether changing the order of transformation operations produces different geometric results.
- **Why It Is Essential:** In vision pipelines, translating an object before rotating it rotates the translation offset itself, displacing the object along an unintended orbital trajectory.
- **How to Formulate:** Evaluate the standard pipeline $M_1$ and the alternate pipeline $M_2$:

$$
M_1 = T \cdot Sh \cdot R, \qquad M_2 = R \cdot T \cdot Sh, \qquad M_1 \ne M_2
$$

#### 3. Bullet Point 3 Explanation: Determinant & Area Scaling Factor
- **What It Means:** The determinant of a transformation matrix measures the areal scaling induced by the linear map.
- **Why It Is Essential:** Evaluating whether data augmentation alters the physical area of detected bounding boxes and segmentation masks.
- **How to Formulate:** Partition $M_1$ into its block structure and evaluate the determinant of the $2 \times 2$ block $A = Sh \cdot R$:

$$
M_1 = \begin{bmatrix} A & \mathbf{t} \\ \mathbf{0}^T & 1 \end{bmatrix}, \qquad \det(A) = \det(Sh) \cdot \det(R), \qquad \text{Area}_{\text{transformed}} = |\det(A)| \times \text{Area}_{\text{initial}}
$$

#### 4. Bullet Point 4 Explanation: Backward Warping & Inverse Matrix
- **What It Means:** In forward mapping, rounding floating-point coordinates causes missing pixels in the output image. Backward warping traverses destination grid points and queries their source coordinates via $M_1^{-1}$.
- **Why It Is Essential:** Backward warping enables artifact-free bilinear and bicubic interpolation.
- **How to Formulate:** Apply the reversal law of matrix inverses:

$$
\tilde{\mathbf{x}}_{\text{src}} = M_1^{-1} \tilde{\mathbf{x}}_{\text{dst}}, \qquad M_1^{-1} = (T \cdot Sh \cdot R)^{-1} = R^{-1} \cdot Sh^{-1} \cdot T^{-1}
$$

#### 5. Bullet Point 5 Explanation: Python Pipeline & Visual Grid
- **What It Means:** Convert mathematical formulations into executable NumPy code and Matplotlib plots.
- **Why It Is Essential:** Real-world engineering requires code verification and visual sanity checks.
- **How to Formulate:** Compute the transformed vertex matrix:

$$
V' = M_1 V
$$

---

# 📌 Case Study 2: Support Vector Machine (SVM) Maximum-Margin Hyperplane & Vector Projections

### 🏢 Real-World Context & Engineering Problem

Support Vector Machines (SVM) find the optimal linear separating hyperplane in feature space that maximizes the geometric distance (margin $\gamma$) to the closest training examples of any class.

In a 2D feature space $\mathbb{R}^2$, consider a linearly separable binary classification dataset:

- **Positive Class ($y = +1$) Samples:**

$$
\mathbf{x}_1 = \begin{bmatrix} 1 \\ 2 \end{bmatrix}, \qquad \mathbf{x}_2 = \begin{bmatrix} 1 \\ 3 \end{bmatrix}
$$

- **Negative Class ($y = -1$) Samples:**

$$
\mathbf{x}_3 = \begin{bmatrix} 3 \\ 1 \end{bmatrix}, \qquad \mathbf{x}_4 = \begin{bmatrix} 4 \\ 2 \end{bmatrix}
$$

The decision boundary is defined by parameter weight vector $\mathbf{w}$ and scalar bias $b$:

$$
H = \left\{ \mathbf{x} \in \mathbb{R}^2 \;\middle|\; \mathbf{w}^T \mathbf{x} + b = 0 \right\}, \qquad \mathbf{w} = \begin{bmatrix} w_1 \\ w_2 \end{bmatrix} \in \mathbb{R}^2, \quad b \in \mathbb{R}
$$

---

### 📋 Questions Asked in This Case Study (Clear Objectives in Text Form)

You are required to address and solve the following **5 specific geometric deliverables**:

- **Bullet Point 1:** Prove from first principles that the parameter weight vector is strictly orthogonal (perpendicular) to the separating hyperplane.
- **Bullet Point 2:** Using vector projection along the unit normal vector, derive the formula for the orthogonal signed Euclidean distance from any arbitrary point to the hyperplane.
- **Bullet Point 3:** Prove that if the canonical supporting hyperplanes are placed at functional margins $+1$ and $-1$, the total geometric margin is inversely proportional to the Euclidean norm of the weight vector.
- **Bullet Point 4:** Given active support vectors, analytically calculate the optimal weight vector, scalar bias, and margin width.
- **Bullet Point 5:** Derive the explicit line equation of the decision boundary, verify that all four training points satisfy the canonical margin constraints, and implement Python visualization code.

---

### 🔍 Detailed In-Depth Explanation of Each Bullet Point

#### 1. Bullet Point 1 Explanation: Normal Vector Orthogonality Proof
- **What It Means:** Prove that every vector lying inside the hyperplane forms a $90^\circ$ angle with $\mathbf{w}$.
- **Why It Is Essential:** Establishes the geometric foundation of linear decision boundaries.
- **How to Formulate:** Take two distinct points $\mathbf{x}_a, \mathbf{x}_b \in H$ and show that their difference satisfies:

$$
\mathbf{w}^T \mathbf{x}_a + b = 0, \qquad \mathbf{w}^T \mathbf{x}_b + b = 0 \implies \mathbf{w}^T (\mathbf{x}_a - \mathbf{x}_b) = 0
$$

#### 2. Bullet Point 2 Explanation: Point-to-Hyperplane Distance Derivation
- **What It Means:** Measure the exact Euclidean perpendicular distance from any point $\mathbf{x}_0$ to the hyperplane $H$.
- **Why It Is Essential:** Needed to compute margin violations and classification confidence.
- **How to Formulate:** Project the vector $(\mathbf{x}_0 - \mathbf{x}_p)$ onto the unit normal vector $\hat{\mathbf{w}}$:

$$
\hat{\mathbf{w}} = \frac{\mathbf{w}}{\lVert \mathbf{w} \rVert_2}, \qquad d(\mathbf{x}_0, H) = \hat{\mathbf{w}}^T (\mathbf{x}_0 - \mathbf{x}_p) = \frac{\mathbf{w}^T \mathbf{x}_0 + b}{\lVert \mathbf{w} \rVert_2}
$$

#### 3. Bullet Point 3 Explanation: Total Geometric Margin Formula Derivation
- **What It Means:** Derive the width of the empty margin corridor separating the two classes.
- **Why It Is Essential:** Shows why maximizing geometric margin is mathematically equivalent to minimizing the squared weight norm.
- **How to Formulate:** Compute the perpendicular distance between the two canonical supporting hyperplanes:

$$
H_+: \quad \mathbf{w}^T \mathbf{x} + b = +1, \qquad H_-: \quad \mathbf{w}^T \mathbf{x} + b = -1
$$

$$
\gamma = d(H_+, H_-) = \frac{2}{\lVert \mathbf{w} \rVert_2}, \qquad \max_{\mathbf{w}, b} \gamma \iff \min_{\mathbf{w}, b} \frac{1}{2} \lVert \mathbf{w} \rVert_2^2
$$

#### 4. Bullet Point 4 Explanation: Analytical Parameter Determination
- **What It Means:** Solve the exact system of linear equations to determine numerical values for $w_1^*, w_2^*, b^*$, and $\gamma$.
- **Why It Is Essential:** Provides ground-truth analytical verification before running iterative quadratic programming solvers.
- **How to Formulate:** Solve the canonical support vector equations for $\mathbf{x}_1$ and $\mathbf{x}_3$:

$$
\mathbf{w}^T \mathbf{x}_1 + b = +1, \qquad \mathbf{w}^T \mathbf{x}_3 + b = -1
$$

#### 5. Bullet Point 5 Explanation: Verification & Visualization
- **What It Means:** Verify canonical margin inequalities across all samples and plot the hyperplane.
- **Why It Is Essential:** Confirms linear separability without margin violations:

$$
y_i \left( (\mathbf{w}^*)^T \mathbf{x}_i + b^* \right) \ge 1 \quad \forall \; i \in \{1, 2, 3, 4\}
$$

---

# 📌 Case Study 3: Quantitative Finance Risk & Sensor PCA Eigendecomposition

### 🏢 Real-World Context & Engineering Problem

A quantitative hedge fund tracks the daily returns of $p = 4$ correlated financial asset classes (Equities, Bonds, Commodities, FX) across $N = 500$ trading days. The empirical covariance matrix of centered returns $X_c \in \mathbb{R}^{500 \times 4}$ is:

$$
\mathbf{\Sigma} = \begin{bmatrix} 4.0 & 2.0 & 1.0 & 0.0 \\ 2.0 & 3.0 & 0.5 & 0.5 \\ 1.0 & 0.5 & 2.0 & 0.0 \\ 0.0 & 0.5 & 0.0 & 1.0 \end{bmatrix}
$$

The diagonal entries represent individual asset variances:

$$
\sigma_{11} = \text{Var}(\text{Equities}) = 4.0, \qquad \sigma_{22} = \text{Var}(\text{Bonds}) = 3.0
$$

$$
\sigma_{33} = \text{Var}(\text{Commodities}) = 2.0, \qquad \sigma_{44} = \text{Var}(\text{FX}) = 1.0
$$

The off-diagonal entries represent cross-asset covariances. To eliminate multi-collinearity, the research team deploys **Principal Component Analysis (PCA)** to find orthogonal synthetic factor portfolios.

---

### 📋 Questions Asked in This Case Study (Clear Objectives in Text Form)

You are required to address and solve the following **5 advanced spectral linear algebra deliverables**:

- **Bullet Point 1:** Prove mathematically that any sample covariance matrix is symmetric and positive semi-definite (PSD). State why all its eigenvalues must be real and non-negative.
- **Bullet Point 2:** Using constrained optimization with Lagrange Multipliers, prove from first principles that the unit direction vector that maximizes variance is the principal eigenvector of the covariance matrix.
- **Bullet Point 3:** Compute all 4 eigenvalues, verify that the sum of eigenvalues equals the matrix trace, and calculate the Proportion of Explained Variance (PEV) for each principal component.
- **Bullet Point 4:** Determine the minimum number of principal components required to preserve at least $80\%$ of total portfolio risk/variance.
- **Bullet Point 5:** Construct the rank-2 reconstructed covariance matrix and compute the Frobenius reconstruction error.

---

### 🔍 Detailed In-Depth Explanation of Each Bullet Point

#### 1. Bullet Point 1 Explanation: Symmetry, PSD & Non-Negative Eigenvalues
- **What It Means:** Prove $\mathbf{\Sigma} = \mathbf{\Sigma}^T$ and $\mathbf{v}^T \mathbf{\Sigma} \mathbf{v} \ge 0$ for all $\mathbf{v} \in \mathbb{R}^p$.
- **Why It Is Essential:** Portfolio variance $\mathbf{v}^T \mathbf{\Sigma} \mathbf{v}$ cannot physically be negative. A non-PSD covariance matrix would imply negative risk, breaking financial models.
- **How to Formulate:** Use the outer-product definition of sample covariance:

$$
\mathbf{\Sigma} = \frac{1}{N - 1} X_c^T X_c, \qquad \mathbf{\Sigma}^T = \mathbf{\Sigma}
$$

$$
\mathbf{v}^T \mathbf{\Sigma} \mathbf{v} = \frac{1}{N - 1} \lVert X_c \mathbf{v} \rVert_2^2 \ge 0 \implies \lambda_i \ge 0
$$

#### 2. Bullet Point 2 Explanation: Lagrange Multipliers Formulation
- **What It Means:** Prove that finding the direction of maximal variance naturally produces the matrix eigenvector equation.
- **Why It Is Essential:** Unifies multivariate statistics and linear algebra through calculus.
- **How to Formulate:** Formulate the Lagrangian and set its gradient to zero:

$$
\mathcal{L}(\mathbf{q}_1, \lambda) = \mathbf{q}_1^T \mathbf{\Sigma} \mathbf{q}_1 - \lambda \left( \mathbf{q}_1^T \mathbf{q}_1 - 1 \right)
$$

$$
\nabla_{\mathbf{q}_1} \mathcal{L} = 2 \mathbf{\Sigma} \mathbf{q}_1 - 2 \lambda \mathbf{q}_1 = \mathbf{0} \implies \mathbf{\Sigma} \mathbf{q}_1 = \lambda \mathbf{q}_1
$$

#### 3. Bullet Point 3 Explanation: Eigendecomposition, Trace & Variance Spectrum
- **What It Means:** Decompose $\mathbf{\Sigma}$ into principal spectral factors and compute the variance percentage captured by each factor.
- **Why It Is Essential:** Identifies the latent risk drivers across the portfolio.
- **How to Formulate:** Solve $\det(\mathbf{\Sigma} - \lambda I) = 0$ and evaluate:

$$
\text{Tr}(\mathbf{\Sigma}) = \sum_{i=1}^4 \sigma_{ii} = \sum_{i=1}^4 \lambda_i = 10.0, \qquad \text{PEV}_k = \frac{\lambda_k}{\text{Tr}(\mathbf{\Sigma})} \times 100\%
$$

#### 4. Bullet Point 4 Explanation: 80% Variance Retention Criterion
- **What It Means:** Identify how many dimensions can be dropped while retaining the dominant $80\%$ of variance.
- **Why It Is Essential:** Enables low-dimensional risk modeling and computational efficiency.
- **How to Formulate:** Find the smallest integer $k$ satisfying:

$$
\text{CEV}_k = \sum_{i=1}^k \text{PEV}_i \ge 80\%
$$

#### 5. Bullet Point 5 Explanation: Low-Rank Approximation & Frobenius Norm Error
- **What It Means:** Reconstruct the covariance matrix using only top-2 eigenvectors and measure the information lost.
- **Why It Is Essential:** Quantifies compression error according to the Eckart–Young–Mirsky theorem:

$$
\mathbf{\Sigma}_2 = \sum_{i=1}^2 \lambda_i \mathbf{q}_i \mathbf{q}_i^T, \qquad \lVert \mathbf{\Sigma} - \mathbf{\Sigma}_2 \rVert_F = \sqrt{\sum_{i=3}^4 \lambda_i^2} = \sqrt{\lambda_3^2 + \lambda_4^2}
$$
