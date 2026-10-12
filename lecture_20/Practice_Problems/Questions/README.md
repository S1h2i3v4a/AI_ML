# 🎯 Lecture 20: Practice Problems — Technical Case Studies

[![Notebook](https://img.shields.io/badge/Jupyter-questions.ipynb-orange.svg?logo=jupyter&logoColor=white)](questions.ipynb)
[![PDF](https://img.shields.io/badge/PDF-questions.pdf-red.svg)](questions.pdf)
[![Solutions](https://img.shields.io/badge/Solutions-View%20Solutions-green.svg)](../Solutions/README.md)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [💡 View Complete Solutions](../Solutions/README.md) | [📁 Overview](../README.md)

---

# 📌 Case Study 1: High-Frequency FinTech Bayesian Fraud & Anomaly Detection Pipeline

### 🏢 Context & Engineering Problem
A tier-1 payment processor handles $10,000,000$ transactions daily. True fraudulent transactions are rare, with an established historical base rate.

#### 1. State of Nature & Prior Base Rate
The transaction sample space $\Omega$ is partitioned into two mutually exclusive and exhaustive states of nature:
- $F$: Transaction is **Fraudulent**
- $L = F^c$: Transaction is **Legitimate**

Partition Invariants:

$$
F \cap L = \emptyset, \qquad F \cup L = \Omega, \qquad P(F) + P(L) = 1
$$

Established prior base rate:

$$
P(F) = 0.002 \quad (0.2\%), \qquad P(L) = 1 - P(F) = 0.998 \quad (99.8\%)
$$

#### 2. Diagnostic Heuristic Signals (Likelihoods)
The risk engineering team deploys two sequential fraud detection heuristic signals:

1. **Signal 1 ($S_1$ — Device Fingerprint Anomaly):**
   - Sensitivity (True Positive Rate):

$$
P(S_1 \mid F) = 0.85
$$

   - False Positive Rate:

$$
P(S_1 \mid L) = 0.04
$$

   - Specificity (True Negative Rate):

$$
P(S_1^c \mid L) = 1 - P(S_1 \mid L) = 0.96
$$

2. **Signal 2 ($S_2$ — Impossible Geo-Velocity Movement):**
   - Sensitivity (True Positive Rate):

$$
P(S_2 \mid F) = 0.90
$$

   - False Positive Rate:

$$
P(S_2 \mid L) = 0.03
$$

   - Specificity (True Negative Rate):

$$
P(S_2^c \mid L) = 1 - P(S_2 \mid L) = 0.97
$$

#### 3. Conditional Independence Axiom
Assume that conditional on transaction class ($F$ or $L$), signals $S_1$ and $S_2$ are conditionally independent:

$$
P(S_1 \cap S_2 \mid F) = P(S_1 \mid F) \cdot P(S_2 \mid F)
$$

$$
P(S_1 \cap S_2 \mid L) = P(S_1 \mid L) \cdot P(S_2 \mid L)
$$

---

### 🎯 Mathematical & Implementation Tasks

#### Task 1: Single-Signal Bayesian Update ($S_1$)
1. **Law of Total Probability:** Express and compute the total marginal evidence $P(S_1)$:

$$
P(S_1) = P(S_1 \mid F) P(F) + P(S_1 \mid L) P(L)
$$

2. **Bayes' Theorem Formulation:** Derive and compute the posterior probability of fraud given Signal 1:

$$
P(F \mid S_1) = \frac{P(S_1 \mid F) P(F)}{P(S_1)} = \frac{P(S_1 \mid F) P(F)}{P(S_1 \mid F) P(F) + P(S_1 \mid L) P(L)}
$$

3. **Base Rate Fallacy Analysis:** Explain mathematically why $P(F \mid S_1) \ll P(S_1 \mid F)$ despite high test sensitivity when $P(F) \ll P(L)$.

#### Task 2: Sequential Bayesian Updating (Recursive Bayes)
1. Treat the posterior from Task 1 as the updated prior belief:

$$
\pi_1(F) = P(F \mid S_1), \qquad \pi_1(L) = P(L \mid S_1) = 1 - \pi_1(F)
$$

2. Compute marginal evidence for Signal 2 conditional on Signal 1:

$$
P(S_2 \mid S_1) = P(S_2 \mid F) \pi_1(F) + P(S_2 \mid L) \pi_1(L)
$$

3. Derive the sequentially updated posterior belief:

$$
P(F \mid S_1, S_2) = \frac{P(S_2 \mid F) \pi_1(F)}{P(S_2 \mid S_1)} = \frac{P(S_2 \mid F) P(F \mid S_1)}{P(S_2 \mid F) P(F \mid S_1) + P(S_2 \mid L) P(L \mid S_1)}
$$

#### Task 3: Joint Simultaneous Likelihood Verification
Prove mathematically that sequential updating yields the exact same posterior as the joint simultaneous likelihood formulation:

$$
P(F \mid S_1 \cap S_2) = \frac{P(S_1 \cap S_2 \mid F) P(F)}{P(S_1 \cap S_2)} = \frac{P(S_1 \mid F) P(S_2 \mid F) P(F)}{P(S_1 \mid F) P(S_2 \mid F) P(F) + P(S_1 \mid L) P(S_2 \mid L) P(L)}
$$

#### Task 4: Odds & Bayes Factor Formulation
Express the update using Bayes' Rule in Odds form:

$$
\text{Prior Odds:} \quad O(F) = \frac{P(F)}{P(L)}
$$

$$
\text{Bayes Factor (Likelihood Ratio):} \quad \Lambda_1 = \frac{P(S_1 \mid F)}{P(S_1 \mid L)}, \qquad \Lambda_2 = \frac{P(S_2 \mid F)}{P(S_2 \mid L)}
$$

$$
\text{Posterior Odds:} \quad O(F \mid S_1, S_2) = O(F) \cdot \Lambda_1 \cdot \Lambda_2
$$

$$
\text{Posterior Probability Recovery:} \quad P(F \mid S_1, S_2) = \frac{O(F \mid S_1, S_2)}{1 + O(F \mid S_1, S_2)}
$$

---

# 📌 Case Study 2: Bioinformatics Clinical Drug Efficacy via Binomial Testing

### 🏢 Context & Engineering Problem
A biotechnology firm is conducting a Phase II clinical oncology trial for a novel immunotherapy agent across $n = 50$ terminal cancer patients.
- **Historical Standard-of-Care (SOC) Remission Rate:** $p_0 = 0.20$ ($20\%$ historical response rate).
- **Trial Outcome:** At the conclusion of the trial, $k = 18$ patients achieve verified complete tumor remission.

#### 1. Random Variable & Probability Model
Let $X = \sum_{i=1}^n Y_i$ denote the total number of remissions, where each patient outcome $Y_i \sim \text{Bernoulli}(p)$:

$$
X \sim \text{Binomial}(n, p), \qquad X \in \{0, 1, 2, \dots, n\}
$$

Binomial Probability Mass Function (PMF):

$$
P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k} = \frac{n!}{k!(n - k)!} p^k (1 - p)^{n - k}
$$

Expectation and Variance:

$$
\mathbb{E}[X] = n p, \qquad \text{Var}(X) = n p (1 - p), \qquad \sigma = \sqrt{n p (1 - p)}
$$

---

### 🎯 Mathematical & Implementation Tasks

#### Task 1: Hypothesis Formulation
Formulate the formal statistical hypotheses for a one-tailed efficacy trial:

$$
\begin{cases}
H_0: p \le p_0 = 0.20 \quad (\text{Null Hypothesis: New drug is no better than SOC}) \\
H_1: p > p_0 = 0.20 \quad (\text{Alternative Hypothesis: New drug has superior efficacy})
\end{cases}
$$

#### Task 2: Exact Binomial Tail Probability (p-value)
Under null hypothesis $H_0: X \sim B(50, 0.20)$, derive and compute the exact one-tailed p-value:

$$
p\text{-value} = P(X \ge 18 \mid n=50, p_0=0.20) = \sum_{j=18}^{50} \binom{50}{j} (0.20)^j (0.80)^{50 - j}
$$

Complementary Cumulative Distribution Function (CDF) form:

$$
p\text{-value} = 1 - P(X \le 17 \mid H_0) = 1 - \sum_{j=0}^{17} \binom{50}{j} (0.20)^j (0.80)^{50 - j}
$$

#### Task 3: Gaussian (Normal) Approximation via Central Limit Theorem
1. Compute the expected mean $\mu$ and standard deviation $\sigma$:

$$
\mu = n p_0 = 50 \times 0.20 = 10
$$

$$
\sigma = \sqrt{n p_0 (1 - p_0)} = \sqrt{50 \times 0.20 \times 0.80} = \sqrt{8} \approx 2.8284
$$

2. Verify the Rule-of-Thumb validity condition:

$$
n p_0 = 10 \ge 5 \quad \text{and} \quad n (1 - p_0) = 40 \ge 5
$$

3. Using Yates' continuity correction ($k - 0.5 = 17.5$), compute the standardized Z-score:

$$
Z = \frac{(k - 0.5) - \mu}{\sigma} = \frac{(18 - 0.5) - 10}{\sqrt{8}} = \frac{7.5}{2.8284} \approx 2.6516
$$

4. Evaluate the Gaussian p-value using the Standard Normal CDF $\Phi(z)$:

$$
p_{\text{approx}} = P(Z \ge 2.6516) = 1 - \Phi(2.6516) = 1 - \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{2.6516} e^{-\frac{u^2}{2}} du
$$

#### Task 4: Statistical Decision Rule & Regulatory Inference
Given standard clinical significance threshold $\alpha = 0.01$ (99% confidence level):

$$
\text{Decision Rule:} \quad \text{Reject } H_0 \iff p\text{-value} < \alpha
$$

Assess percentage discrepancy between the exact Binomial and Gaussian approximation results, and deliver the formal Phase III approval recommendation.

---

# 📌 Case Study 3: Autonomous Vehicle LiDAR Sensor Calibration & Gaussian Noise Normalization

### 🏢 Context & Engineering Problem
An autonomous vehicle navigation subsystem uses a pulsed LiDAR sensor to estimate distance to roadside obstacles.

#### 1. Stochastic Error Model
Distance measurement model:

$$
X_{\text{meas}} = d_{\text{true}} + \epsilon
$$

Where measurement error $\epsilon$ is an additive zero-mean continuous Gaussian random variable:

$$
\epsilon \sim \mathcal{N}(\mu, \sigma^2), \qquad \mu = 0, \quad \sigma = 0.15\text{ meters}
$$

Probability Density Function (PDF):

$$
f(\epsilon; \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{(\epsilon - \mu)^2}{2\sigma^2} \right) = \frac{1}{0.15 \sqrt{2\pi}} \exp\left( -\frac{\epsilon^2}{2(0.15)^2} \right)
$$

Standard Normal CDF:

$$
\Phi(z) = P(Z \le z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^z e^{-\frac{u^2}{2}} du = \frac{1}{2} \left[ 1 + \text{erf}\left( \frac{z}{\sqrt{2}} \right) \right]
$$

---

### 🎯 Mathematical & Implementation Tasks

#### Task 1: 68-95-99.7 Empirical Rule Zone Probabilities
Evaluate the exact theoretical probabilities of the three operational safety zones:

1. **Green Zone (Normal Operation: $|\epsilon| \le 1\sigma$):**

$$
P(|\epsilon| \le \sigma) = P(-\sigma \le \epsilon \le \sigma) = \frac{1}{\sigma \sqrt{2\pi}} \int_{-\sigma}^{\sigma} e^{-\frac{\epsilon^2}{2\sigma^2}} d\epsilon
$$

$$
P(|\epsilon| \le 0.15) = \Phi(1) - \Phi(-1) = 2\Phi(1) - 1 \approx 0.68269 \quad (68.27\%)
$$

2. **Yellow Zone (Advisory Warning: $1\sigma < |\epsilon| \le 2\sigma$):**

$$
P(\sigma < |\epsilon| \le 2\sigma) = 2 \cdot [\Phi(2) - \Phi(1)] \approx 2 \cdot (0.97725 - 0.84134) = 0.27181 \quad (27.18\%)
$$

3. **Red Zone (Critical Sensor Hazard: $|\epsilon| > 3\sigma$):**

$$
P(|\epsilon| > 3\sigma) = 2 \cdot [1 - \Phi(3)] \approx 2 \cdot (1 - 0.99865) = 0.00270 \quad (0.27\%)
$$

#### Task 2: Z-Score Standardization & Tail Probability Integration
Derive the probability that measurement error exceeds safety cutoff $\delta = 0.25\text{ meters}$:

1. Standardized Cutoff Z-Score:

$$
Z_{\text{cutoff}} = \frac{\delta - \mu}{\sigma} = \frac{0.25 - 0}{0.15} = \frac{5}{3} \approx 1.6667
$$

2. Two-Tailed Exceedance Probability:

$$
P(|\epsilon| > 0.25) = P(\epsilon > 0.25) + P(\epsilon < -0.25) = 2 \cdot P(Z > 1.6667)
$$

$$
P(|\epsilon| > 0.25) = 2 \cdot \left[ 1 - \Phi\left( \frac{0.25}{0.15} \right) \right] = 2 \cdot \left[ 1 - \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{1.6667} e^{-\frac{u^2}{2}} du \right]
$$

$$
P(|\epsilon| > 0.25) = 2 \cdot (1 - 0.95221) \approx 0.09558 \quad (9.56\%)
$$

#### Task 3: Monte Carlo Calibration Simulation
Simulate $N = 1,000,000$ synthetic LiDAR sensor pings to verify empirical convergence:

1. **Sample Mean Convergence (Weak Law of Large Numbers):**

$$
\bar{\epsilon}_N = \frac{1}{N} \sum_{i=1}^N \epsilon_i \xrightarrow{P} \mathbb{E}[\epsilon] = 0
$$

2. **Sample Variance Unbiased Estimator:**

$$
s_N^2 = \frac{1}{N - 1} \sum_{i=1}^N (\epsilon_i - \bar{\epsilon}_N)^2 \xrightarrow{P} \sigma^2 = 0.15^2 = 0.0225
$$

3. **Empirical Critical Violation Rate:**

$$
\hat{p}_{\text{fail}} = \frac{1}{N} \sum_{i=1}^N \mathbb{I}\left( |\epsilon_i| > 0.25 \right) \xrightarrow{P} P(|\epsilon| > 0.25) \approx 0.0956
$$
