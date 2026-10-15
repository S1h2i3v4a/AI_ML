# 🎯 Lecture 25: Practice Problems — Technical Case Studies

[![Notebook](https://img.shields.io/badge/Jupyter-questions.ipynb-orange.svg?logo=jupyter&logoColor=white)](questions.ipynb)
[![PDF](https://img.shields.io/badge/PDF-questions.pdf-red.svg)](questions.pdf)
[![Solutions](https://img.shields.io/badge/Solutions-View%20Solutions-green.svg)](../Solutions/README.md)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [💡 View Solutions](../Solutions/README.md) | [📁 Overview](../README.md)

---

## 📌 Classification Practice Suite: Overview & Instructions

In machine learning applications, classification algorithms (such as Naive Bayes and k-Nearest Neighbors) serve as foundational operational engines. From clinical diagnostics to cybersecurity spam detection and industrial IoT telemetry, deploying production-grade systems requires far more than calling a generic `.fit()` method. Real-world engineering requires:
- Managing acute class imbalance with rigorous metric design (Confusion Matrix, Precision, Recall, Specificity, Macro and Weighted F1-Scores).
- Minimizing asymmetric real-world financial and life-safety penalty costs by calibrating optimal decision thresholds.
- Engineering mixed-type Bayesian generative classifiers handling discrete text tokens alongside continuous sensor features while eliminating zero-frequency pathology via Laplace smoothing.
- Navigating metric-space geometry in kNN, overcoming the Curse of Dimensionality, and eliminating insidious Data Leakage in Cross-Validation pipelines.

This suite features **3 comprehensive, textbook-grade industry case studies**:
1. **Case 1:** Medical Diagnostics Clinical Triaging & Cost-Sensitive Confusion Matrix Optimization
2. **Case 2:** Bayesian Spam Filtering & Gaussian vs Multinomial Naive Bayes with Laplace Smoothing
3. **Case 3:** Metric-Space Nearest Neighbor Classification (kNN), Curse of Dimensionality & Leakage-Free Stratified K-Fold Pipeline

---

# 📌 Case Study 1: Medical Diagnostics Clinical Triaging & Cost-Sensitive Confusion Matrix Optimization

### 🏢 Real-World Context & Engineering Problem

A leading healthcare hospital network is deploying an automated AI screening diagnostic system designed to detect a rare, life-threatening cardiac arrhythmia condition from routine physiological telemetry (similar to features analyzed in our `heart.csv` dataset).

The hospital's screening cohort and diagnostic test parameters are formally defined as follows:

- **Total Patient Cohort:** The screening program processes $N = 10,000$ asymptomatic individuals per month:

$$
N = 10,000
$$

- **Disease Prevalence (Prior Probability):** The condition is rare across the general population, with a prevalence of $2\%$:

$$
P(D^+) = 0.02, \qquad P(D^-) = 1 - P(D^+) = 0.98
$$

- **Diagnostic Model Sensitivity (Recall / True Positive Rate):** Clinical validation establishes a sensitivity of $95\%$:

$$
\text{Sensitivity} = \text{TPR} = P(T^+ \mid D^+) = \frac{TP}{P} = 0.95
$$

- **Diagnostic Model Specificity (True Negative Rate):** Correct identification of healthy patients is certified at $90\%$:

$$
\text{Specificity} = \text{TNR} = P(T^- \mid D^-) = \frac{TN}{N_{\text{neg}}} = 0.90
$$

- **False Positive Rate (FPR):** Probability of a false alarm on a healthy patient:

$$
\text{FPR} = 1 - \text{Specificity} = 0.10
$$

Hospital clinical leadership and data engineering face two paramount challenges:
1. **The Screening Paradox / Base Rate Fallacy:** When a patient tests positive ($T^+$), clinical intuition erroneously suggests a $95\%$ probability of disease. The true posterior probability $P(D^+ \mid T^+)$ is substantially lower.
2. **Asymmetric Risk & Cost Penalties:** In clinical medicine, errors carry vastly unequal consequences:
   - **False Negative (FN) Cost:** A missed diagnosis allows a fatal cardiac event to occur untreated. Legal, remedial, and life-safety costs average $C_{FN} = \$500$ per incident.
   - **False Positive (FP) Cost:** A false alarm results in a secondary non-invasive confirmation ultrasound costing $C_{FP} = \$20$.
   - **Correct Classifications:** True Positives ($C_{TP}$) and True Negatives ($C_{TN}$) incur $\$0$ penalty.

---

### 📋 What Is Being Asked in This Question? (Clear Objectives in Text Form)

You are tasked with providing the following **5 specific engineering deliverables**:

- **Bullet Point 1:** Construct the complete $2 \times 2$ Confusion Matrix ($TP, FP, FN, TN$) with exact integer counts for the $10,000$ patient cohort.
- **Bullet Point 2:** Apply Bayes' Theorem to derive and compute the Positive Predictive Value (PPV / Precision) $P(D^+ \mid T^+)$, providing a rigorous explanation of the Base Rate Fallacy.
- **Bullet Point 3:** Calculate Overall Accuracy, Macro F1-Score, and Weighted F1-Score. Mathematically prove why a "Dummy Baseline Classifier" predicting healthy for all patients attains $98\%$ accuracy and why accuracy is dangerously misleading for medical triage.
- **Bullet Point 4:** Formulate the Cost-Sensitive Risk function, express expected clinical cost per patient, and analytically derive the Bayes optimal decision threshold $\tau^*$ that minimizes aggregate penalty loss.
- **Bullet Point 5:** Implement an executable Python script rendering a two-panel visualization: (a) Annotated Confusion Matrix heatmap, and (b) Expected Cost versus Decision Threshold curve highlighting the optimal operating cutoff.

---

### 🔍 Detailed Explanation of Each Bullet Point (Formulas & Theoretical Rationale)

#### 1. Explanation of Bullet Point 1: Cohort Confusion Matrix Construction
- **Objective:** Quantify the exact partition of all $10,000$ screening subjects into the four fundamental outcomes of diagnostic classification.
- **Significance:** The confusion matrix represents the foundational truth table from which all classification metrics are derived.
- **Methodology:** Determine total diseased ($P$) and healthy ($N_{\text{neg}}$) sub-populations from prior prevalence:

$$
P = N \cdot P(D^+), \qquad N_{\text{neg}} = N \cdot (1 - P(D^+))
$$

Compute exact integer cell counts using sensitivity and specificity:

$$
TP = P \cdot \text{Sensitivity}, \qquad FN = P - TP
$$

$$
TN = N_{\text{neg}} \cdot \text{Specificity}, \qquad FP = N_{\text{neg}} - TN
$$

#### 2. Explanation of Bullet Point 2: Precision & The Base Rate Fallacy
- **Objective:** Compute the true conditional probability of illness given a positive diagnostic report.
- **Significance:** Understanding why highly sensitive tests produce low precision under severe class imbalance is essential for clinical communication and engineering alert systems.
- **Methodology:** Expand Bayes' Theorem across the partitioned evidence:

$$
P(D^+ \mid T^+) = \frac{P(T^+ \mid D^+) P(D^+)}{P(T^+)} = \frac{P(T^+ \mid D^+) P(D^+)}{P(T^+ \mid D^+) P(D^+) + P(T^+ \mid D^-) P(D^-)}
$$

Cross-verify against the direct empirical ratio from the confusion matrix:

$$
\text{Precision} = \frac{TP}{TP + FP}
$$

#### 3. Explanation of Bullet Point 3: Accuracy Paradox & F1-Score Breakdown
- **Objective:** Contrast naive aggregate accuracy against class-balanced harmonic metrics.
- **Significance:** Demonstrates the vulnerability of unweighted accuracy under extreme class distribution skew.
- **Methodology:** Compute aggregate accuracy:

$$
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
$$

Compute the disease class harmonic F1-score:

$$
F1_{\text{disease}} = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
$$

Evaluate Macro F1 (unweighted class average) and Weighted F1 (support-weighted average).

#### 4. Explanation of Bullet Point 4: Cost-Sensitive Risk & Optimal Threshold $\tau^*$
- **Objective:** Calibrate the probability decision boundary to minimize expected asymmetric loss.
- **Significance:** Machine learning models defaulting to $\tau = 0.50$ fail in asymmetric risk environments where missing a positive case is 25 times more costly than a false alarm.
- **Methodology:** Formulate total expected clinical risk:

$$
\mathbb{E}[\text{Cost}] = C_{FN} \cdot FN + C_{FP} \cdot FP
$$

By setting the expected marginal cost of positive classification equal to negative classification given posterior probability $p = P(D^+ \mid x)$, derive the Bayes optimal operating threshold:

$$
\tau^* = \frac{C_{FP}}{C_{FP} + C_{FN}}
$$

#### 5. Explanation of Bullet Point 5: Python Simulation & Heatmap Visualizations
- **Objective:** Build an end-to-end Python pipeline illustrating triage metrics and cost curves.
- **Significance:** Visual validation bridges theoretical derivation and clinical operations.
- **Methodology:** Use `matplotlib` to render a labeled confusion matrix heatmap and a continuous cost trace sweeping $\tau \in [0.001, 0.50]$.

---

# 📌 Case Study 2: Bayesian Spam Filtering & Gaussian vs Multinomial Naive Bayes with Laplace Smoothing

### 🏢 Real-World Context & Engineering Problem

An enterprise email gateway processes high-throughput email traffic to block phishing scams and malware distribution while ensuring zero legitimate business communications (ham) are dropped.

The security gateway captures two complementary feature spaces:
1. **Discrete Word Token Occurrences:** Specific lexical trigger terms modeled via Multinomial Naive Bayes.
2. **Continuous Metadata Metric:** An aggregate urgency score $x_{\text{urgency}} \in \mathbb{R}$, combining uppercase character density, punctuation frequency, and server dispatch rates, modeled via Gaussian Naive Bayes.

Training data comprises $N = 1,000$ verified emails:

- **Total Corpus Size:**

$$
N = 1,000
$$

- **Class Priors:**

$$
N_{\text{spam}} = 300, \qquad N_{\text{ham}} = 700
$$

$$
P(\text{Spam}) = \frac{300}{1000} = 0.30, \qquad P(\text{Ham}) = \frac{700}{1000} = 0.70
$$

- **Lexicon Characteristics:** Vocabulary size $|V| = 500$ distinct tokens.
  - Total token occurrences in spam corpus: $T_{\text{spam}} = 3,000$.
  - Total token occurrences in ham corpus: $T_{\text{ham}} = 7,000$.

- **Word Frequency Table for Critical Terms:**

| Keyword ($w_j$) | Spam Corpus Count ($\text{count}(w_j, S)$) | Ham Corpus Count ($\text{count}(w_j, H)$) |
| :--- | :--- | :--- |
| $w_1 = \text{"lottery"}$ | $120$ | $2$ |
| $w_2 = \text{"winner"}$ | $90$ | $5$ |
| $w_3 = \text{"meeting"}$ | $15$ | $420$ |
| $w_4 = \text{"cryptocurrency"}$ | $10$ | $0$ |

- **Continuous Urgency Feature Parameters ($x_{\text{urgency}}$):**
  - Spam class distribution follows Gaussian $\mathcal{N}(\mu_S, \sigma_S^2)$:

$$
\mu_S = 8.5, \qquad \sigma_S = 1.5 \implies \sigma_S^2 = 2.25
$$

  - Ham class distribution follows Gaussian $\mathcal{N}(\mu_H, \sigma_H^2)$:

$$
\mu_H = 2.0, \qquad \sigma_H = 1.0 \implies \sigma_H^2 = 1.00
$$

An incoming suspicious test email $E_{\text{test}}$ arrives with keywords:
$$\{\text{"lottery"}, \text{"winner"}, \text{"cryptocurrency"}\}$$
and urgency metric:
$$x_{\text{urgency}} = 6.0$$

---

### 📋 What Is Being Asked in This Question? (Clear Objectives in Text Form)

You are tasked with providing the following **5 specific engineering deliverables**:

- **Bullet Point 1:** Formulate the Conditional Independence Assumption of Naive Bayes and explain why joint likelihood simplifies to a product of marginal likelihoods.
- **Bullet Point 2:** Define the Zero-Frequency Problem, prove why an unregularized MLE calculation for $w_4 = \text{"cryptocurrency"}$ forces $P(\text{Ham} \mid E) = 0$, derive Laplace Add-1 Smoothing, and compute smoothed conditional probabilities for all four terms across both classes.
- **Bullet Point 3:** Formulate the Log-Likelihood objective and prove how transformation to log-space prevents floating-point underflow under 64-bit IEEE-754 arithmetic.
- **Bullet Point 4:** State the Gaussian Naive Bayes PDF, compute class-conditional probability densities for urgency score $x = 6.0$, and evaluate the urgency likelihood ratio.
- **Bullet Point 5:** Synthesize discrete lexical likelihoods, continuous Gaussian density, and prior probabilities to evaluate posterior probabilities $P(\text{Spam} \mid E_{\text{test}})$ and $P(\text{Ham} \mid E_{\text{test}})$, issuing the final gateway verdict.

---

### 🔍 Detailed Explanation of Each Bullet Point (Formulas & Theoretical Rationale)

#### 1. Explanation of Bullet Point 1: Conditional Independence Assumption
- **Objective:** Deconstruct the foundational statistical assumption powering Naive Bayes classification.
- **Significance:** Explains how linear parameter scaling $\mathcal{O}(d \cdot K)$ replaces exponential parameter explosion $\mathcal{O}(2^d \cdot K)$.
- **Methodology:** Express the decomposition of the joint class-conditional likelihood:

$$
P(\mathbf{x} \mid C_k) = P(x_1, x_2, \dots, x_d \mid C_k) = \prod_{j=1}^d P(x_j \mid C_k)
$$

#### 2. Explanation of Bullet Point 2: Zero-Frequency Problem & Laplace Smoothing ($\alpha = 1$)
- **Objective:** Prevent catastrophic probability collapse when encountering novel or unobserved vocabulary in test instances.
- **Significance:** Without smoothing, a single unseen token annihilates evidence from dozens of highly informative tokens.
- **Methodology:** State the Laplace smoothed estimator:

$$
\hat{P}(w_j \mid C_k) = \frac{\text{count}(w_j, C_k) + \alpha}{\sum_{w \in V} \text{count}(w, C_k) + \alpha |V|}
$$

Apply $\alpha = 1$, $|V| = 500$, $T_{\text{spam}} = 3000$, and $T_{\text{ham}} = 7000$ to evaluate all word conditional probabilities.

#### 3. Explanation of Bullet Point 3: Log-Likelihood Formulation & Underflow Prevention
- **Objective:** Eliminate IEEE-754 floating point arithmetic underflow in high-dimensional feature spaces.
- **Significance:** Products of hundreds of small fractional probabilities rapidly drop below double-precision limit ($10^{-308}$).
- **Methodology:** Apply monotonic logarithmic transformation:

$$
\log P(C_k \mid \mathbf{x}) \propto \log P(C_k) + \sum_{j=1}^d \log P(x_j \mid C_k)
$$

#### 4. Explanation of Bullet Point 4: Continuous Features via Gaussian Naive Bayes PDF
- **Objective:** Incorporate continuous real-valued metrics alongside discrete word frequency counts.
- **Significance:** Allows hybrid systems to leverage continuous telemetry without arbitrary binning or quantization.
- **Methodology:** Evaluate the univariate Gaussian probability density function:

$$
f(x \mid \mu_k, \sigma_k^2) = \frac{1}{\sqrt{2\pi \sigma_k^2}} \exp\left( -\frac{(x - \mu_k)^2}{2\sigma_k^2} \right)
$$

Compute densities for Ham ($\mu = 2.0, \sigma = 1.0$) and Spam ($\mu = 8.5, \sigma = 1.5$) at $x = 6.0$.

#### 5. Explanation of Bullet Point 5: Joint Posterior Inference & Decision Rule
- **Objective:** Synthesize multi-modal evidence into an actionable classification verdict.
- **Significance:** Demonstrates full-system Bayesian reasoning from priors and disparate likelihoods to calibrated posterior odds.
- **Methodology:** Compute unnormalized class scores:

$$
\text{Score}(\text{Spam}) = P(\text{Spam}) \cdot \left( \prod_{w \in E_{\text{test}}} \hat{P}(w \mid \text{Spam}) \right) \cdot f(6.0 \mid \text{Spam})
$$

$$
\text{Score}(\text{Ham}) = P(\text{Ham}) \cdot \left( \prod_{w \in E_{\text{test}}} \hat{P}(w \mid \text{Ham}) \right) \cdot f(6.0 \mid \text{Ham})
$$

Normalize to obtain posterior percentages and apply the maximum a posteriori (MAP) decision rule.

---

# 📌 Case Study 3: Metric-Space Nearest Neighbor Classification (kNN), Curse of Dimensionality & Leakage-Free Stratified K-Fold Pipeline

### 🏢 Real-World Context & Engineering Problem

An industrial automation manufacturing facility utilizes edge telemetry IoT sensors mounted on high-speed rotational turbines. The predictive maintenance classification pipeline monitors real-time telemetry to classify turbine operational health as either Normal ($y = 0$) or Faulty ($y = 1$).

Sensors capture two physical continuous telemetry dimensions:
- **Feature 1:** Bearing Operating Temperature $x_1$ ($^\circ\text{C}$), spanning range $[20, 100]$ ($\Delta x_1 \approx 80$).
- **Feature 2:** Micro-vibration Amplitude $x_2$ ($\text{mm}$), spanning range $[0.001, 0.050]$ ($\Delta x_2 \approx 0.049$).

Six historical calibration baseline samples are stored in the edge memory index:

$$
\begin{aligned}
P_1 &= [25.0, 0.005]^T, \quad y_1 = 0 \quad (\text{Normal}) \\
P_2 &= [30.0, 0.008]^T, \quad y_2 = 0 \quad (\text{Normal}) \\
P_3 &= [35.0, 0.012]^T, \quad y_3 = 0 \quad (\text{Normal}) \\
P_4 &= [80.0, 0.040]^T, \quad y_4 = 1 \quad (\text{Faulty}) \\
P_5 &= [85.0, 0.045]^T, \quad y_5 = 1 \quad (\text{Faulty}) \\
P_6 &= [90.0, 0.048]^T, \quad y_6 = 1 \quad (\text{Faulty})
\end{aligned}
$$

A live telemetry observation query $Q$ is received from turbine unit \#7:

$$
Q = [40.0, 0.042]^T
$$

Crucially, query $Q$ registers moderate temperature ($40^\circ\text{C}$, close to normal operating baselines) but hazardous micro-vibration ($0.042\text{ mm}$, characteristic of impending bearing seizure).

Engineering leadership mandates addressing two algorithmic risks:
1. **Metric Space Distortion from Unstandardized Scales:** Raw distance calculation causes the high-magnitude temperature scale to completely overshadow vibration amplitude.
2. **Data Leakage in Cross-Validation:** Performing global preprocessing transformations before dataset splitting leaks test set distributions into training splits, yielding over-optimistic evaluation metrics that fail in deployment.

---

### 📋 What Is Being Asked in This Question? (Clear Objectives in Text Form)

You are tasked with providing the following **5 specific engineering deliverables**:

- **Bullet Point 1:** Calculate raw unscaled Euclidean distances from query $Q$ to all reference points $P_1 \dots P_6$. Prove mathematically that temperature differences contribute $>99.99\%$ of the total distance metric, completely blinding the classifier to vibration.
- **Bullet Point 2:** Calculate reference sample mean vector $\boldsymbol{\mu}$ and standard deviation vector $\boldsymbol{\sigma}$. Perform Z-score standardization on all points and compute standardized Euclidean distances. Prove that the top 3 nearest neighbors completely invert between unscaled and scaled spaces.
- **Bullet Point 3:** Formulate Uniform Majority Voting and Inverse-Distance Weighted Voting schemes, computing the predicted class label for query $Q$ under both rules for $k = 3$ and $k = 5$.
- **Bullet Point 4:** Formulate the Curse of Dimensionality and the Metric Collapse Theorem, proving mathematically why relative distance contrast collapses to zero as dimensionality $d \to \infty$ ($\lim_{d \to \infty} \frac{D_{\max} - D_{\min}}{D_{\min}} \to 0$).
- **Bullet Point 5:** Explain the mechanism of Data Leakage during feature scaling and construct a production-ready Scikit-Learn `Pipeline` pairing `StandardScaler` and `KNeighborsClassifier` inside `StratifiedKFold(n_splits=5)` to guarantee zero leakage during cross-validation.

---

### 🔍 Detailed Explanation of Each Bullet Point (Formulas & Theoretical Rationale)

#### 1. Explanation of Bullet Point 1: Unscaled Euclidean Distances & Scale Distortion
- **Objective:** Quantify how differences in feature measurement units distort geometric proximity.
- **Significance:** Metric-space classifiers measure similarity via geometric distance; arbitrary scale disparities destroy physical meaning.
- **Methodology:** Compute standard Euclidean distance:

$$
d(Q, P_i) = \sqrt{(x_{Q, 1} - x_{i, 1})^2 + (x_{Q, 2} - x_{i, 2})^2}
$$

Compute the proportional variance contribution of dimension 1 versus dimension 2.

#### 2. Explanation of Bullet Point 2: Z-Score Standardization & Neighbor Inversion
- **Objective:** Equalize feature dimensional contributions to geometric distance.
- **Significance:** Standardization ensures each feature contributes proportionally to unit variance.
- **Methodology:** Evaluate sample moments across the training set:

$$
\mu_j = \frac{1}{n} \sum_{i=1}^n x_{i, j}, \qquad \sigma_j = \sqrt{\frac{1}{n-1} \sum_{i=1}^n (x_{i, j} - \mu_j)^2}
$$

Standardize reference points and query point:

$$
z_{i, j} = \frac{x_{i, j} - \mu_j}{\sigma_j}, \qquad z_{Q, j} = \frac{x_{Q, j} - \mu_j}{\sigma_j}
$$

Recompute standardized Euclidean distances:

$$
d_{\text{scaled}}(Q, P_i) = \sqrt{\sum_{j=1}^2 (z_{Q, j} - z_{i, j})^2}
$$

#### 3. Explanation of Bullet Point 3: Uniform vs Distance-Weighted Voting
- **Objective:** Compare decision aggregation rules across nearest neighborhood sets.
- **Significance:** Distance weighting prevents distant outliers from outvoting immediate proximate neighbors.
- **Methodology:** Compute uniform majority prediction:

$$
\hat{y} = \text{mode}(\{y_i : P_i \in \mathcal{N}_k(Q)\})
$$

Compute inverse distance weighted prediction:

$$
w_i = \frac{1}{d_{\text{scaled}}(Q, P_i) + \epsilon}, \qquad \hat{y} = \arg\max_{c \in \{0, 1\}} \sum_{i \in \mathcal{N}_k(Q), y_i = c} w_i
$$

#### 4. Explanation of Bullet Point 4: Curse of Dimensionality & Metric Collapse
- **Objective:** Mathematically analyze nearest neighbor degradation in high-dimensional feature spaces.
- **Significance:** Guides feature selection and dimensionality reduction (PCA) prior to distance-based modeling.
- **Methodology:** Analyze distance variance as $d \to \infty$ for i.i.d. random variables:

$$
\lim_{d \to \infty} \frac{D_{\max} - D_{\min}}{D_{\min}} \to 0
$$

Explain why the concept of "nearest" neighbor becomes mathematically indistinguishable from any arbitrary point.

#### 5. Explanation of Bullet Point 5: Data Leakage Prevention via Scikit-Learn Pipelines
- **Objective:** Implement rigorous cross-validation isolation for data-dependent transformations.
- **Significance:** Prevents optimistic cross-validation score inflation caused by test set leakage.
- **Methodology:** Encapsulate preprocessing and estimation within `sklearn.pipeline.Pipeline`:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=5, weights='distance'))
])

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(pipeline, X, y, cv=cv, scoring='f1_macro')
```
