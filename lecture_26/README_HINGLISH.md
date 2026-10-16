# Lecture 26: Scratch Implementations of Machine Learning Algorithms [ADD-ON] (Hinglish)

Swagat hai **Lecture 26** mein! Yeh master module classical machine learning algorithms ko bina kisi external library ke pure Python aur vectorized NumPy se scratch se build karne par focused hai. First-principles engineering se aapko algorithms ki actual mathematical functioning aur systems performance ka deep understanding milta hai.

---

## 1. Curriculum Architecture & Subtopic Index

Is lecture ko **12 comprehensive submodules** mein divide kiya gaya hai:

| Submodule | Video / Topic Title | Core Mathematical & Algorithmic Concepts | Artifacts |
| :--- | :--- | :--- | :--- |
| [**Notes_26.01**](./Notes_26.01/) | **Section Introduction & Philosophy** | Black-box vs white-box systems, C-contiguous arrays, Python numerical stack | [Notes](./Notes_26.01/README.md) \| [Hinglish](./Notes_26.01/README_HINGLISH.md) \| [PDF](./Notes_26.01/notes.pdf) \| [Notebook](./Notes_26.01/lecture_26_01.ipynb) |
| [**Notes_26.02**](./Notes_26.02/) | **Linear Regression Formulation** | Continuous mapping $\mathcal{X} \to \mathcal{Y}$, affine hyperplanes, inner product $h_\theta(x) = \theta^T x$ | [Notes](./Notes_26.02/README.md) \| [Hinglish](./Notes_26.02/README_HINGLISH.md) \| [PDF](./Notes_26.02/notes.pdf) \| [Notebook](./Notes_26.02/lecture_26_02.ipynb) |
| [**Notes_26.03**](./Notes_26.03/) | **LR with GD (Step 1: Initialization)** | Convex quadratic optimization, zero initialization safety, hyperparameter configuration | [Notes](./Notes_26.03/README.md) \| [Hinglish](./Notes_26.03/README_HINGLISH.md) \| [PDF](./Notes_26.03/notes.pdf) \| [Notebook](./Notes_26.03/lecture_26_03.ipynb) |
| [**Notes_26.04**](./Notes_26.04/) | **LR with GD (Step 2: MSE Cost)** | Error residuals $e^{(i)} = \hat{y}^{(i)} - y^{(i)}$, Mean Squared Error objective $J = \frac{1}{2m}\|Xw+b-y\|^2$ | [Notes](./Notes_26.04/README.md) \| [Hinglish](./Notes_26.04/README_HINGLISH.md) \| [PDF](./Notes_26.04/notes.pdf) \| [Notebook](./Notes_26.04/lecture_26_04.ipynb) |
| [**Notes_26.05**](./Notes_26.05/) | **LR with GD (Step 3: Gradients)** | Multivariable calculus chain rule, weight gradient $dw = \frac{1}{m}X^T(\hat{y}-y)$, bias gradient $db$ | [Notes](./Notes_26.05/README.md) \| [Hinglish](./Notes_26.05/README_HINGLISH.md) \| [PDF](./Notes_26.05/notes.pdf) \| [Notebook](./Notes_26.05/lecture_26_05.ipynb) |
| [**Notes_26.06**](./Notes_26.06/) | **LR with GD (Step 4: Update Rule)** | Convergence theorem, parameter update loop $w := w - \alpha dw$, complete `LinearRegressionGD` OOP class | [Notes](./Notes_26.06/README.md) \| [Hinglish](./Notes_26.06/README_HINGLISH.md) \| [PDF](./Notes_26.06/notes.pdf) \| [Notebook](./Notes_26.06/lecture_26_06.ipynb) |
| [**Notes_26.07**](./Notes_26.07/) | **Linear Regression with OLS** | Closed-form analytical Normal Equation $\theta = (X_b^T X_b)^{-1} X_b^T y$, matrix calculus proof | [Notes](./Notes_26.07/README.md) \| [Hinglish](./Notes_26.07/README_HINGLISH.md) \| [PDF](./Notes_26.07/notes.pdf) \| [Notebook](./Notes_26.07/lecture_26_07.ipynb) |
| [**Notes_26.08**](./Notes_26.08/) | **Gradient Descent vs OLS** | Complexity comparison: $\mathcal{O}(d^3)$ matrix inversion vs $\mathcal{O}(kmd)$ iterative updates, Big Data scaling | [Notes](./Notes_26.08/README.md) \| [Hinglish](./Notes_26.08/README_HINGLISH.md) \| [PDF](./Notes_26.08/notes.pdf) \| [Notebook](./Notes_26.08/lecture_26_08.ipynb) |
| [**Notes_26.09**](./Notes_26.09/) | **Logistic Regression Formulation** | Sigmoid activation $\sigma(z) = \frac{1}{1+e^{-z}}$, Bernoulli likelihood, Binary Cross-Entropy (Log-Loss) | [Notes](./Notes_26.09/README.md) \| [Hinglish](./Notes_26.09/README_HINGLISH.md) \| [PDF](./Notes_26.09/notes.pdf) \| [Notebook](./Notes_26.09/lecture_26_09.ipynb) |
| [**Notes_26.10**](./Notes_26.10/) | **Logistic Regression Implementation** | Vectorized OOP `LogisticRegression` class, decision boundary geometry $w_1 x_1 + w_2 x_2 + b = 0$ | [Notes](./Notes_26.10/README.md) \| [Hinglish](./Notes_26.10/README_HINGLISH.md) \| [PDF](./Notes_26.10/notes.pdf) \| [Notebook](./Notes_26.10/lecture_26_10.ipynb) |
| [**Notes_26.11**](./Notes_26.11/) | **KNN Classifier Formulation** | Non-parametric lazy learning, Euclidean distance metric $d(x, x') = \|x-x'\|_2$, hyperparameter $k$ selection | [Notes](./Notes_26.11/README.md) \| [Hinglish](./Notes_26.11/README_HINGLISH.md) \| [PDF](./Notes_26.11/notes.pdf) \| [Notebook](./Notes_26.11/lecture_26_11.ipynb) |
| [**Notes_26.12**](./Notes_26.12/) | **KNN Classifier Implementation** | Vectorized `KNNClassifier` class, `np.argsort` neighbor retrieval, `np.bincount` plurality voting | [Notes](./Notes_26.12/README.md) \| [Hinglish](./Notes_26.12/README_HINGLISH.md) \| [PDF](./Notes_26.12/notes.pdf) \| [Notebook](./Notes_26.12/lecture_26_12.ipynb) |

---

## 2. Practice Problems Suite

Located in the [**`Practice_Problems/`**](./Practice_Problems/) directory:
- **Problem Statements**: [Questions README](./Practice_Problems/Questions/README_HINGLISH.md) \| [questions.pdf](./Practice_Problems/Questions/questions.pdf) \| [Starter Notebook](./Practice_Problems/Questions/questions.ipynb)
- **Complete Solutions**: [Solutions README](./Practice_Problems/Solutions/README_HINGLISH.md) \| [solutions.pdf](./Practice_Problems/Solutions/solutions.pdf) \| [Executed Notebook](./Practice_Problems/Solutions/solutions.ipynb)
