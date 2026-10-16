# Lecture 27.08: Multi-Model Training aur Evaluation — Baseline Classification Suite

## 📌 Executive Summary (Hinglish)
Logistic Regression, KNN ($k=5$), aur Gaussian Naive Bayes ka baseline training, Confusion Matrix metrics, aur banking perspective se precision comparison.

---

### 📋 Is Topic/Section Mein Hum Kya Cover Kar Rahe Hain?
1. Logistic Regression baseline classifier ka implementation aur evaluation.
2. K-Nearest Neighbors ($k=5$) instance-based classifier ka training aur test evaluation.
3. Gaussian Naive Bayes probabilistic model ka execution.
4. Precision, Recall, F1-Score aur Confusion Matrix ka multi-model comparison table.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**Logistic Regression**: Standard linear decision boundary hyperplane $\mathbf{w}^T \mathbf{x} + b = 0$ fit karta hai. Baseline accuracy decent hoti hai lekin kuch False Positives generate hote hain.

**KNN ($k=5$)**: Metric space mein 5 nearest applicants ke labels par voting karta hai. Boundary highly complex hoti hai.

**Gaussian Naive Bayes**: Normal distribution assumption $P(x_j|y) = \mathcal{N}(\mu_{jc}, \sigma_{jc}^2)$ ke sath class posterior calculate karta hai. Loan dataset par iska **Precision** highest aata hai.

**Metric Tradeoff Analysis**: Banking requirements ke under Gaussian Naive Bayes baseline phase mein winner banta hai kyunki isme False Positives (defaulters approval) sabse kam hote hain.

---

## 🏛️ Mathematical Architecture & Detailed Theory

### 🥊 Multi-Model Architectural Benchmark Suite

To discover the optimal inductive bias for credit underwriting, we establish three distinct mathematical learners on the standardized training partition $\mathcal{D}_{	ext{train}}$:

#### 1. Discriminative Linear Hyperplane: Logistic Regression
Models the posterior probability via the Sigmoid logistic link:

$$
P(Y = 1 | \mathbf{x}) = \sigma(\mathbf{w}^T \mathbf{x} + b) = rac{1}{1 + e^{-(\mathbf{w}^T \mathbf{x} + b)}}
$$

Loss function is convex Binary Cross-Entropy (Log-Loss):

$$
J(\mathbf{w}, b) = -rac{1}{m} \sum_{i=1}^m \left[ y_i \ln \hat{y}_i + (1 - y_i) \ln(1 - \hat{y}_i) ight]
$$

#### 2. Non-Parametric Metric Space: K-Nearest Neighbors ($k=5$)
Assigns class probability via local majority density within neighborhood $\mathcal{N}_k(\mathbf{x})$:

$$
P(Y = 1 | \mathbf{x}) = rac{1}{k} \sum_{i \in \mathcal{N}_k(\mathbf{x})} y_i
$$

#### 3. Generative Class-Conditional Density: Gaussian Naive Bayes
Applies Bayes' rule under the conditional feature independence assumption:

$$
P(Y = c | \mathbf{x}) \propto P(Y = c) \prod_{j=1}^d rac{1}{\sqrt{2\pi \sigma_{jc}^2}} \exp\left( -rac{(x_j - \mu_{jc})^2}{2\sigma_{jc}^2} ight)
$$

---

### 📊 Comparative Baseline Metrics Matrix

| Classifier | Accuracy | Precision (Safety) | Recall (Coverage) | F1-Score | Primary Architectural Characteristic |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | $pprox 84.7\%$ | $pprox 78.5\%$ | $pprox 71.4\%$ | $pprox 0.75$ | Linear decision boundary, high interpretability |
| **KNN ($k=5$)** | $pprox 81.6\%$ | $pprox 73.1\%$ | $pprox 64.3\%$ | $pprox 0.68$ | Non-linear local tessellation, sensitive to local noise |
| **Gaussian Naive Bayes** | $pprox 83.2\%$ | $pprox \mathbf{88.6\%}$ | $pprox 55.4\%$ | $pprox 0.68$ | **Maximum Precision**, lowest false approval defaults |

---

## 💻 Python Implementation & Code Example

```python
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

models = {
    "Logistic Regression": LogisticRegression(),
    "KNN (k=5)": KNeighborsClassifier(n_neighbors=5),
    "Gaussian Naive Bayes": GaussianNB()
}

for name, clf in models.items():
    clf.fit(X_train_scaled, y_train)
    preds = clf.predict(X_test_scaled)
    print(f"=== {name} ===")
    print("Precision:", round(precision_score(y_test, preds), 4))
    print("Recall:   ", round(recall_score(y_test, preds), 4))
    print("F1-Score: ", round(f1_score(y_test, preds), 4))
    print("Accuracy: ", round(accuracy_score(y_test, preds), 4))
    print("Confusion Matrix:
", confusion_matrix(y_test, preds), "
")

```

---

## 🎯 Quick Revision Points (Interview Notes)
- **Objective**: Credit risk modeling mein precision hamesha accuracy se zyada important hoti hai.
- **Data Invariant**: SimpleImputer aur StandardScaler ko hamesha training data par `fit` karke test set par sirf `transform` kiya jaata hai.
- **Decision Boundary**: Non-linear feature transformations ($DTI^2$, $Credit^2$) linear models ko non-linear patterns capture karne ki capability provide karte hain.
