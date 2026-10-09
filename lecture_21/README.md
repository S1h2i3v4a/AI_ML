# 📐 Lecture 21: Mathematics for AI — Linear Algebra Mastery

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Numpy](https://img.shields.io/badge/Numpy-Linear%20Algebra-013243.svg)](https://numpy.org/)
[![Scipy](https://img.shields.io/badge/Scipy-Linalg-blue.svg)](https://scipy.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Main Repository](../README.md)

---

## 📌 Module Overview

**Lecture 21** establishes the comprehensive, rigorous mathematical foundation of **Linear Algebra for Artificial Intelligence, Machine Learning, and Deep Learning**.
Linear Algebra is the universal language of AI computation. Every deep neural network layer, feature representation, attention mechanism, and loss projection is fundamentally a matrix-vector transformation operating in high-dimensional vector spaces.

From foundational vector spaces and geometric transformations to spectral decompositions, Singular Value Decomposition (SVD), and Low-Rank Adaptation (LoRA), this module equips engineers with both theoretical depth and production-ready numerical computing mastery.

### Core Pillars Covered:
- **Vector Spaces & Geometric Foundations:** Vectors, matrices, tensors, linear combinations, span, basis vectors, norms ($\ell_1, \ell_2, \ell_\infty$), and inner products.
- **Matrix Calculus & Transformations:** Matrix multiplication complexity, determinants, geometric area/volume scaling, invertibility, and rank.
- **Linear Systems & Projections:** Systems of linear equations, Gaussian elimination, Moore-Penrose pseudo-inverses, orthogonality, Gram-Schmidt, and QR decomposition.
- **Spectral Theory & Matrix Decompositions:** Eigenvalues, eigenvectors, characteristic equations, symmetric diagonalization, and Singular Value Decomposition ($A = U \Sigma V^T$).
- **Modern AI & Deep Learning Applications:** Principal Component Analysis (PCA), Convolutional tensor operations, Scaled Dot-Product Attention, and Low-Rank Adaptation (LoRA).

---

## 🗺️ Sub-Topic Navigation

| Sub-Module | Topic Title | Core Concepts Covered | Fast Links |
| :--- | :--- | :--- | :--- |
| **Notes_21.01** | Vectors, Scalars, Matrices & Tensors | Dimensional hierarchies, tensor ranks (0D to 4D), row/column vectors, batch tensors | [Notes](Notes_21.01/README.md) \| [PDF](Notes_21.01/notes.pdf) \| [Notebook](Notes_21.01/lecture_21_01.ipynb) |
| **Notes_21.02** | Vector Operations & Geometric Intuition | Vector addition, scalar scaling, Euclidean $\ell_2$ & Manhattan $\ell_1$ norms, cosine similarity | [Notes](Notes_21.02/README.md) \| [PDF](Notes_21.02/notes.pdf) \| [Notebook](Notes_21.02/lecture_21_02.ipynb) |
| **Notes_21.03** | Matrix Operations & Special Matrices | Addition, scalar multiplication, transposes, symmetric/diagonal/identity/orthogonal matrices | [Notes](Notes_21.03/README.md) \| [PDF](Notes_21.03/notes.pdf) \| [Notebook](Notes_21.03/lecture_21_03.ipynb) |
| **Notes_21.04** | Matrix Multiplication & AI Forward Passes | Inner product vs outer product, linear map composition, batch gemm complexity $\mathcal{O}(m n p)$ | [Notes](Notes_21.04/README.md) \| [PDF](Notes_21.04/notes.pdf) \| [Notebook](Notes_21.04/lecture_21_04.ipynb) |
| **Notes_21.05** | Linear Combinations, Span & Basis | Vector span, linear independence, basis sets, canonical vs arbitrary coordinate systems | [Notes](Notes_21.05/README.md) \| [PDF](Notes_21.05/notes.pdf) \| [Notebook](Notes_21.05/lecture_21_05.ipynb) |
| **Notes_21.06** | Linear Independence & Matrix Rank | Wronskian/determinant tests, row rank, column rank, rank-nullity theorem, dimensionality collapse | [Notes](Notes_21.06/README.md) \| [PDF](Notes_21.06/notes.pdf) \| [Notebook](Notes_21.06/lecture_21_06.ipynb) |
| **Notes_21.07** | Determinants & Geometric Singularity | Oriented volume scaling factor, permutation formula, Laplace expansion, singularity criterion | [Notes](Notes_21.07/README.md) \| [PDF](Notes_21.07/notes.pdf) \| [Notebook](Notes_21.07/lecture_21_07.ipynb) |
| **Notes_21.08** | Systems of Linear Equations & Gaussian Elimination | Augmented matrices, forward elimination, back-substitution, row echelon forms (REF/RREF) | [Notes](Notes_21.08/README.md) \| [PDF](Notes_21.08/notes.pdf) \| [Notebook](Notes_21.08/lecture_21_08.ipynb) |
| **Notes_21.09** | Matrix Inverses & Moore-Penrose Pseudo-Inverse | Gauss-Jordan inversion, non-invertible overdetermined systems, pseudo-inverse $A^+$, Least Squares | [Notes](Notes_21.09/README.md) \| [PDF](Notes_21.09/notes.pdf) \| [Notebook](Notes_21.09/lecture_21_09.ipynb) |
| **Notes_21.10** | Orthogonality, Orthonormality & Projections | Orthogonal subspaces, projection matrix $P$, Gram-Schmidt orthogonalization, QR decomposition | [Notes](Notes_21.10/README.md) \| [PDF](Notes_21.10/notes.pdf) \| [Notebook](Notes_21.10/lecture_21_10.ipynb) |
| **Notes_21.11** | Eigenvalues & Eigenvectors | Invariant transformation lines, characteristic polynomial $\det(A - \lambda I) = 0$, eigenspaces | [Notes](Notes_21.11/README.md) \| [PDF](Notes_21.11/notes.pdf) \| [Notebook](Notes_21.11/lecture_21_11.ipynb) |
| **Notes_21.12** | Diagonalization & Spectral Theorem | Modal matrix $P$, similarity transformation $A = P \Lambda P^{-1}$, real symmetric spectral theorem | [Notes](Notes_21.12/README.md) \| [PDF](Notes_21.12/notes.pdf) \| [Notebook](Notes_21.12/lecture_21_12.ipynb) |
| **Notes_21.13** | Singular Value Decomposition (SVD) | Rectangular factorization $A = U \Sigma V^T$, singular values, low-rank Eckart-Young approximation | [Notes](Notes_21.13/README.md) \| [PDF](Notes_21.13/notes.pdf) \| [Notebook](Notes_21.13/lecture_21_13.ipynb) |
| **Notes_21.14** | Principal Component Analysis (PCA) via Linear Algebra | Centered covariance matrix $\Sigma$, spectral projection, scree analysis, variance preservation | [Notes](Notes_21.14/README.md) \| [PDF](Notes_21.14/notes.pdf) \| [Notebook](Notes_21.14/lecture_21_14.ipynb) |
| **Notes_21.15** | Linear Algebra in Deep Learning & Attention | Dense feedforward layers, im2col convolution gemm, Transformer Scaled Dot-Product Attention, LoRA | [Notes](Notes_21.15/README.md) \| [PDF](Notes_21.15/notes.pdf) \| [Notebook](Notes_21.15/lecture_21_15.ipynb) |

---

## 📐 Mathematical Foundations Reference

### 1. Vector Inner Product, Norms & Cosine Distance
For vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$:

$$
\langle \mathbf{u}, \mathbf{v} \rangle = \mathbf{u}^T \mathbf{v} = \sum_{i=1}^n u_i v_i
$$

$$
\|\mathbf{u}\|_2 = \sqrt{\sum_{i=1}^n u_i^2}, \qquad \|\mathbf{u}\|_1 = \sum_{i=1}^n |u_i|, \qquad \cos(\theta) = \frac{\mathbf{u}^T \mathbf{v}}{\|\mathbf{u}\|_2 \|\mathbf{v}\|_2}
$$

---

### 2. Moore-Penrose Pseudo-Inverse & Linear Least Squares
For overdetermined system $A\mathbf{x} = \mathbf{b}$ where $A \in \mathbb{R}^{m \times n}$ has full column rank ($m > n$):

$$
A^+ = (A^T A)^{-1} A^T \qquad \implies \qquad \mathbf{x}^* = A^+ \mathbf{b} = (A^T A)^{-1} A^T \mathbf{b}
$$

---

### 3. Spectral Decomposition of Real Symmetric Matrices
For symmetric matrix $A = A^T \in \mathbb{R}^{n \times n}$ with orthogonal eigenvectors matrix $Q$ ($Q^T Q = I$):

$$
A = Q \Lambda Q^T = \sum_{i=1}^n \lambda_i \mathbf{q}_i \mathbf{q}_i^T
$$

---

### 4. Singular Value Decomposition (SVD) & Low-Rank Approximation
For any arbitrary rectangular matrix $A \in \mathbb{R}^{m \times n}$:

$$
A = U \Sigma V^T = \sum_{i=1}^r \sigma_i \mathbf{u}_i \mathbf{v}_i^T
$$

$$
A_k = \sum_{i=1}^k \sigma_i \mathbf{u}_i \mathbf{v}_i^T = \mathop{\arg\min}_{\text{rank}(B)=k} \|A - B\|_F
$$

---

### 5. Transformer Scaled Dot-Product Attention
For queries $Q$, keys $K$, and values $V$ in latent dimension $d_k$:

$$
\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V
$$

---

## 🎯 Practice Problems & Case Studies

To consolidate the mathematical concepts of Lecture 21, solve the production case studies in the [Practice Problems](Practice_Problems/) module:

- 📁 **[Questions/](Practice_Problems/Questions/)**:
  - [Questions README](Practice_Problems/Questions/README.md) | [questions.pdf](Practice_Problems/Questions/questions.pdf) | [questions.ipynb](Practice_Problems/Questions/questions.ipynb)
  - **Case 1**: Computer Vision 2D Affine Transformations & Homogeneous Coordinates (Composite Rotation, Shearing & Translation Pipeline)
  - **Case 2**: Support Vector Machine Maximum-Margin Hyperplane & Orthogonal Projections (Margin Optimization & Vector Projection)
  - **Case 3**: Financial Portfolio Risk Analysis via PCA & Covariance Matrix Eigendecomposition (Spectral Variance & Dimensionality Reduction)
- 📁 **[Solutions/](Practice_Problems/Solutions/)**:
  - [Solutions Guide](Practice_Problems/Solutions/README.md) | [solutions.pdf](Practice_Problems/Solutions/solutions.pdf) | [solutions.ipynb](Practice_Problems/Solutions/solutions.ipynb)
  - Full production Python solutions with formal mathematical proofs, numerical derivations, and generated high-resolution visualizations.
