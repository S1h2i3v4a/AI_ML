# 🎯 Lecture 20: Practice Problems — Technical Case Studies

[![Notebook](https://img.shields.io/badge/Jupyter-questions.ipynb-orange.svg?logo=jupyter&logoColor=white)](questions.ipynb)
[![PDF](https://img.shields.io/badge/PDF-questions.pdf-red.svg)](questions.pdf)
[![Solutions](https://img.shields.io/badge/Solutions-View%20Solutions-green.svg)](../Solutions/README.md)

🌐 **Language:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [💡 View Complete Solutions](../Solutions/README.md) | [📁 Overview](../README.md)

---

# 📌 Case Study 1: High-Frequency FinTech Bayesian Fraud & Anomaly Detection Pipeline

### 🏢 Context & Engineering Problem
A tier-1 payment processor handles $10,000,000$ transactions daily. True fraudulent transactions are rare, with an established historical base rate:

$$
\boxed{P(\text{Fraud}) = 0.002 \quad (0.2\%)}
$$

The risk engineering team deploys two sequential fraud detection heuristic signals:
1. **Signal 1 ($S_1$ - Device Fingerprint Anomaly):**
   - Sensitivity (True Positive Rate): $P(S_1 \mid \text{Fraud}) = 0.85$
   - False Positive Rate: $P(S_1 \mid \text{Legitimate}) = 0.04$
2. **Signal 2 ($S_2$ - Impossible Geo-Velocity Movement):**
   - Sensitivity (True Positive Rate): $P(S_2 \mid \text{Fraud}) = 0.90$
   - False Positive Rate: $P(S_2 \mid \text{Legitimate}) = 0.03$

Assume that conditional on transaction class (Fraud vs. Legitimate), signals $S_1$ and $S_2$ are conditionally independent.

### 🎯 Mathematical & Implementation Tasks
1. **Single-Signal Bayesian Update:**
   Calculate the posterior probability of fraud given that only Signal 1 triggers ($P(\text{Fraud} \mid S_1)$). Explain why this posterior is surprisingly low despite high sensitivity (demonstrating the Base Rate Fallacy).
2. **Sequential Bayesian Updating:**
   Using the posterior probability from Task 1 as the new prior probability, calculate the updated posterior probability of fraud after Signal 2 also triggers ($P(\text{Fraud} \mid S_1, S_2)$).
3. **Simultaneous Verification:**
   Prove mathematically that sequential updating yields the exact same posterior as the joint simultaneous likelihood formulation:

$$
\boxed{P(\text{Fraud} \mid S_1, S_2) = \frac{P(S_1 \mid \text{Fraud}) P(S_2 \mid \text{Fraud}) P(\text{Fraud})}{P(S_1, S_2)}}
$$

4. **Python Pipeline:** Implement a reusable Python function that accepts any list of sequential binary diagnostic test results and returns the step-by-step posterior belief vector.

---

# 📌 Case Study 2: Bioinformatics Clinical Drug Efficacy via Binomial Testing

### 🏢 Context & Engineering Problem
A biotechnology firm is conducting a Phase II clinical oncology trial for a novel immunotherapy agent across $n = 50$ terminal cancer patients.
- **Historical Standard-of-Care (SOC) Remission Rate:** $p_0 = 0.20$ (20% historical response rate).
- **Trial Outcome:** At the conclusion of the trial, $k = 18$ patients achieve verified complete tumor remission.

Regulatory agencies require formal statistical proof that the new compound is significantly superior to standard-of-care before granting Phase III progression.

### 🎯 Mathematical & Implementation Tasks
1. **Hypothesis Formulation:**
   Formulate the formal null ($H_0$) and alternative ($H_1$) statistical hypotheses for a one-tailed efficacy trial.
2. **Exact Binomial Tail Probability (p-value):**
   Under null hypothesis $H_0: X \sim B(50, 0.20)$, derive and compute the exact one-tailed p-value:

$$
\boxed{p\text{-value} = P(X \ge 18 \mid n=50, p_0=0.20) = \sum_{j=18}^{50} \binom{50}{j} (0.20)^j (0.80)^{50-j}}
$$

3. **Gaussian (Normal) Approximation with Continuity Correction:**
   Compute the expected mean $\mu = np_0$ and standard deviation $\sigma = \sqrt{np_0(1-p_0)}$. Using the Yates continuity correction ($k - 0.5 = 17.5$), compute the standardized Z-score:

$$
\boxed{Z = \frac{(k - 0.5) - np_0}{\sqrt{np_0(1 - p_0)}}}
$$

Evaluate the Gaussian p-value $P(Z \ge z)$ and assess percentage error relative to the exact Binomial result.
4. **Statistical Decision:** Given standard significance threshold $\alpha = 0.01$, does the compound warrant clinical Phase III approval?

---

# 📌 Case Study 3: Autonomous Vehicle LiDAR Sensor Calibration & Gaussian Noise Normalization

### 🏢 Context & Engineering Problem
An autonomous vehicle navigation subsystem uses a pulsed LiDAR sensor to estimate distance to roadside obstacles. Due to atmospheric dust, temperature fluctuation, and optical refraction, sensor distance readings exhibit zero-mean additive Gaussian noise:

$$
\boxed{X_{\text{meas}} = d_{\text{true}} + \epsilon, \qquad \epsilon \sim \mathcal{N}(0, \sigma^2), \quad \sigma = 0.15\text{ meters}}
$$

The vehicle's collision avoidance system triggers three warning states:
- **Green (Normal):** Error within 1 standard deviation ($|\epsilon| \le \sigma = 0.15\text{ m}$)
- **Yellow (Advisory):** Error between 1 and 2 standard deviations ($0.15\text{ m} < |\epsilon| \le 0.30\text{ m}$)
- **Red (Critical Safety Violation):** Error exceeds 3 standard deviations ($|\epsilon| > 0.45\text{ m}$)

### 🎯 Mathematical & Implementation Tasks
1. **68-95-99.7 Empirical Integration:**
   Calculate the exact theoretical probability of the sensor operating in each state (Green, Yellow, and Red).
2. **Z-Score Standardization & Probability Density Integration:**
   Derive the probability that measurement error exceeds safety cutoff $\delta = 0.25\text{ meters}$ using the Standard Normal CDF $\Phi(z)$:

$$
\boxed{P(|\epsilon| > 0.25) = 2 \cdot \left[ 1 - \Phi\left( \frac{0.25}{\sigma} \right) \right]}
$$

3. **Monte Carlo Calibration Simulation:**
   Simulate $N = 1,000,000$ synthetic LiDAR sensor pings. Compute sample mean, sample variance, empirical fraction of critical violations, and compare with theoretical predictions.
