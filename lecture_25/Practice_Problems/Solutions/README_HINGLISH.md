# 💡 Lecture 25: Practice Problems — Comprehensive Solutions Guide [Hinglish]

[![Notebook](https://img.shields.io/badge/Jupyter-solutions.ipynb-orange.svg?logo=jupyter&logoColor=white)](solutions.ipynb)
[![PDF](https://img.shields.io/badge/PDF-solutions.pdf-red.svg)](solutions.pdf)
[![Questions](https://img.shields.io/badge/Questions-View%20Set-blue.svg)](../Questions/README_HINGLISH.md)
[![Case 1 Plot](https://img.shields.io/badge/Plot-Case%201%20Confusion%20Matrix%20%26%20Cost-blue.svg)](case1_confusion_matrix_cost_curve.png)
[![Case 2 Plot](https://img.shields.io/badge/Plot-Case%202%20Naive%20Bayes%20Log%20Odds-red.svg)](case2_naive_bayes_log_odds.png)
[![Case 3 Plot](https://img.shields.io/badge/Plot-Case%203%20kNN%20Decision%20Boundaries-green.svg)](case3_knn_decision_boundaries_k.png)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Questions Par Wapas Jayein](../Questions/README_HINGLISH.md) | [📁 Overview](../README_HINGLISH.md)

---

## 📌 Executive Architecture & Solution Blueprint

Is document mein **Lecture 25** ke teeno industry case studies ke liye complete, step-by-step mathematical proofs, exact numerical calculations, pure Hinglish conceptual explanations, aur production-grade Python code diya gaya hai.

Har case study ko first-principles mathematics ke sath solve kiya gaya hai taaki har ek formula ka origin, uske peeche ka physical intuition, aur practical implementation aapko crystal clear samajh aaye.

---

# 📌 Solution to Case 1: Medical Diagnostics Clinical Triaging & Cost-Sensitive Confusion Matrix Optimization

### 🎯 Is Case Study Mein Pucha Kya Gaya Tha? (Quick Recap)

Hospital cohort data aur diagnostic test parameters:

$$
N = 10,000, \qquad P(D^+) = 0.02, \qquad P(D^-) = 0.98
$$

$$
\text{Sensitivity (TPR)} = 0.95, \qquad \text{Specificity (TNR)} = 0.90, \qquad \text{FPR} = 0.10
$$

Asymmetric error costs:

$$
C_{FN} = \$500, \qquad C_{FP} = \$20, \qquad C_{TP} = C_{TN} = \$0
$$

---

### 1. Step-by-Step Mathematical Derivations & Calculations

#### 🔹 Task 1: Complete Confusion Matrix ($TP, FP, FN, TN$) Construct Karna

##### Step 1: Actual Positive ($P$) aur Actual Negative ($N_{\text{neg}}$) Population Count Nikaalna
Total cohort $N = 10,000$ asymptomatic individuals hain:

$$
P = N \cdot P(D^+) = 10,000 \times 0.02 = 200 \text{ patients with true heart condition}
$$

$$
N_{\text{neg}} = N \cdot P(D^-) = 10,000 \times 0.98 = 9,800 \text{ healthy individuals}
$$

Verification:

$$
P + N_{\text{neg}} = 200 + 9,800 = 10,000
$$

##### Step 2: Model Predictions ke Charo Buckets Calculate Karna
1. **True Positives ($TP$):** Wo bimar log jinki bimari model ne correctly identify ki:

$$
TP = P \cdot \text{Sensitivity} = 200 \times 0.95 = 190 \text{ patients}
$$

2. **False Negatives ($FN$):** Wo bimar log jinhe model ne galati se swasth declare kar diya (Missed cases):

$$
FN = P - TP = 200 - 190 = 10 \text{ patients}
$$

3. **True Negatives ($TN$):** Wo healthy log jinhe model ne correctly healthy declare kiya:

$$
TN = N_{\text{neg}} \cdot \text{Specificity} = 9,800 \times 0.90 = 8,820 \text{ individuals}
$$

4. **False Positives ($FP$):** Wo healthy log jin par model ne jhootha alarm baja diya (False Alarms):

$$
FP = N_{\text{neg}} - TN = 9,800 - 8,820 = 980 \text{ individuals}
$$

##### Step 3: Complete $2 \times 2$ Contingency Table

| Actual Condition $\backslash$ Predicted | Predicted Negative ($T^-$) | Predicted Positive ($T^+$) | Total Actual |
| :--- | :--- | :--- | :--- |
| **Actual Healthy ($D^-$)** | $\mathbf{TN = 8,820}$ | $\mathbf{FP = 980}$ | $N_{\text{neg}} = 9,800$ |
| **Actual Diseased ($D^+$)** | $\mathbf{FN = 10}$ | $\mathbf{TP = 190}$ | $P = 200$ |
| **Total Predicted** | $8,830$ | $1,170$ | $N = 10,000$ |

---

#### 🔹 Task 2: Positive Predictive Value (Precision) & The Base Rate Fallacy

##### Step 1: Bayes' Theorem Derivation for Posterior Probability
Jab kisi patient ka diagnostic report "Positive" ($T^+$) aata hai, toh patient ko actual bimari hone ki conditional probability $P(D^+ \mid T^+)$ Bayes' Rule se calculate hoti hai:

$$
P(D^+ \mid T^+) = \frac{P(T^+ \mid D^+) P(D^+)}{P(T^+)}
$$

Law of Total Probability se denominator $P(T^+)$ expand karein:

$$
P(T^+) = P(T^+ \mid D^+) P(D^+) + P(T^+ \mid D^-) P(D^-)
$$

Numerator evaluate karein:

$$
P(T^+ \mid D^+) P(D^+) = 0.95 \times 0.02 = 0.019
$$

Denominator evaluate karein:

$$
P(T^+) = (0.95 \times 0.02) + (0.10 \times 0.98) = 0.019 + 0.098 = 0.117
$$

Values substitute karne par:

$$
P(D^+ \mid T^+) = \frac{0.019}{0.117} = \frac{19}{117} \approx 0.162393 \implies 16.24\%
$$

##### Step 2: Verification using Confusion Matrix Counts
Direct confusion matrix ratios:

$$
\text{Precision} = \frac{TP}{TP + FP} = \frac{190}{190 + 980} = \frac{190}{1,170} \approx 0.162393 \implies 16.24\%
$$

##### Step 3: Deep Intuitive Explanation of the Base Rate Fallacy / Screening Paradox
- **Confusion ka Karan:** Ek aam doctor ya patient sochta hai: *"Test ki accuracy/sensitivity toh 95% hai, toh positive aane par mujhe bimari hone ka 95% chance hona chahiye!"* Yeh sochna ek bohot badi statistical galti hai jise **Base Rate Fallacy** kaha jata hai.
- **Physical Reality:** Population mein $98\%$ log healthy hain. Bhale hi test ka false positive rate sirf $10\%$ ho, lekin kyunki healthy logon ka group bohot bada hai ($9,800$ log), unka $10\%$ false alarm milkar $980$ logo ka crowd khada kar deta hai!
- **Comparison:** Pure cohort mein total $1,170$ log positive test karte hain. In $1,170$ positive logon mein se sirf $190$ log sach mein bimar hain, jabki $980$ log bilkul swasth hain.
- **Conclusion:** Har positive aane wale $6$ mein se lagbhag $5$ log bilkul swasth hote hain! Isliye positive aane ke baad direct surgery ya invasive dawai shuru karne ke bajaye hamesha ek confirmatory secondary test kiya jata hai.

---

#### 🔹 Task 3: Accuracy Paradox & F1-Score Breakdown

##### Step 1: Overall Diagnostic Accuracy Calculate Karna

$$
\text{Accuracy} = \frac{TP + TN}{N} = \frac{190 + 8,820}{10,000} = \frac{9,010}{10,000} = 0.9010 \implies 90.10\%
$$

##### Step 2: The "Dummy Majority Classifier" (All-Negative Baseline)
Maan lijiye hum koi AI model nahi banate, balki ek aisi "Zero Rule" script likhte hain jo aakh band karke har aane wale patient ko "Healthy" ($0$) declare kar deti hai:

$$
\hat{y}_{\text{dummy}} = 0 \quad \forall \text{ patients}
$$

Is dummy classifier ka score:
- Correctly classified healthy: $9,800$ patients ($TN = 9800, FP = 0$).
- Correctly classified diseased: $0$ patients ($TP = 0, FN = 200$).
- **Dummy Accuracy:**

$$
\text{Accuracy}_{\text{dummy}} = \frac{0 + 9,800}{10,000} = 0.9800 \implies 98.00\%
$$

- **Accuracy Paradox:** Ek aisi bekar script jo ek bhi bimar patient ko nahi pakad sakti, uska accuracy score $98\%$ hai jabki hamare trained model ka score sirf $90.1\%$ hai!
- **Clinical Consequence:** Dummy model ke chalte sabhi $200$ cardiac patients bina ilaaj ke ghar chale jayenge aur unki maut ho sakti hai. Isliye imbalanced clinical data mein accuracy ek completely useless aur dangerous metric hai.

##### Step 3: Class-Wise & Harmonized F1-Scores

1. **Disease Class ($D^+$):**
   - $\text{Precision} = 0.1624$
   - $\text{Recall} = 0.9500$
   - **F1-Score ($D^+$):**

$$
F1_{\text{disease}} = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2 \cdot 0.162393 \cdot 0.95}{0.162393 + 0.95} = \frac{0.308547}{1.112393} \approx 0.27737 \implies 27.74\%
$$

2. **Healthy Class ($D^-$):**
   - $\text{Precision}_{\text{healthy}} = \frac{TN}{TN + FN} = \frac{8,820}{8,820 + 10} = \frac{8,820}{8,830} \approx 0.998867$
   - $\text{Recall}_{\text{healthy}} = \text{Specificity} = 0.9000$
   - **F1-Score ($D^-$):**

$$
F1_{\text{healthy}} = \frac{2 \cdot 0.998867 \cdot 0.90}{0.998867 + 0.90} = \frac{1.79796}{1.898867} \approx 0.94686 \implies 94.69\%
$$

3. **Macro Average F1-Score (Unweighted Class Mean):**

$$
F1_{\text{macro}} = \frac{F1_{\text{disease}} + F1_{\text{healthy}}}{2} = \frac{0.27737 + 0.94686}{2} = \frac{1.22423}{2} \approx 0.61211 \implies 61.21\%
$$

4. **Weighted Average F1-Score (Support-Weighted Mean):**

$$
F1_{\text{weighted}} = (0.02 \cdot F1_{\text{disease}}) + (0.98 \cdot F1_{\text{healthy}}) = (0.02 \times 0.27737) + (0.98 \times 0.94686) = 0.00555 + 0.92792 \approx 0.93347 \implies 93.35\%
$$

Notice karein ki Macro F1 ($61.21\%$) ne disease class ki low precision ko accurately capture kiya, jabki Weighted F1 ($93.35\%$) majority class ke weight ki wajah se inflate ho gaya. Isliye medical research mein hamesha Macro F1 report kiya jata hai!

---

#### 🔹 Task 4: Cost-Sensitive Risk & Optimal Decision Threshold $\tau^*$

##### Step 1: Expected Penalty Cost Objective Function
Hospital ke financial aur health risk ka objective function:

$$
\mathbb{E}[\text{Cost}] = C_{FN} \cdot FN + C_{FP} \cdot FP = 500 \cdot FN + 20 \cdot FP
$$

Is cohort mein hamare test parameters ke sath:

$$
\mathbb{E}[\text{Cost}] = (500 \times 10) + (20 \times 980) = 5,000 + 19,600 = \$24,600 \text{ total cohort penalty}
$$

Per-patient expected cost:

$$
\text{Cost}_{\text{per patient}} = \frac{\$24,600}{10,000} = \$2.46
$$

Agar Dummy Classifier use karte ($FN = 200, FP = 0$):

$$
\text{Cost}_{\text{dummy}} = 500 \times 200 + 20 \times 0 = \$100,000 \implies \$10.00 \text{ per patient}
$$

##### Step 2: Bayes Optimal Decision Threshold $\tau^*$ ki Analytical Derivation
Maan lijiye model kisi patient $x$ ke liye disease probability predict karta hai:

$$
p = P(D^+ \mid x)
$$

Healthy hone ki probability:

$$
1 - p = P(D^- \mid x)
$$

Hospital ke samne do actions hain:
1. **Action 1: Predict Disease ($\hat{y} = 1$):**
   - Agar patient sach mein bimar tha ($D^+$): Cost $= C_{TP} = \$0$.
   - Agar patient healthy tha ($D^-$): Cost $= C_{FP} = \$20$.
   - Expected loss:

$$
\mathcal{L}(\text{Action } 1) = p \cdot 0 + (1 - p) \cdot C_{FP} = (1 - p) C_{FP}
$$

2. **Action 2: Predict Healthy ($\hat{y} = 0$):**
   - Agar patient sach mein bimar tha ($D^+$): Cost $= C_{FN} = \$500$.
   - Agar patient healthy tha ($D^-$): Cost $= C_{TN} = \$0$.
   - Expected loss:

$$
\mathcal{L}(\text{Action } 2) = p \cdot C_{FN} + (1 - p) \cdot 0 = p C_{FN}
$$

Bayesian Decision Theory ke mutabiq, hume Action 1 (Predict Disease) tab lena chahiye jab uska expected loss Action 2 ke expected loss se kam ho:

$$
\mathcal{L}(\text{Action } 1) < \mathcal{L}(\text{Action } 2)
$$

$$
(1 - p) C_{FP} < p C_{FN}
$$

Brackets expand karein:

$$
C_{FP} - p C_{FP} < p C_{FN}
$$

$$
C_{FP} < p (C_{FN} + C_{FP})
$$

Dono taraf $(C_{FN} + C_{FP})$ se divide karein:

$$
p > \frac{C_{FP}}{C_{FN} + C_{FP}}
$$

Is critical boundary condition ko hi **Bayes Optimal Decision Threshold ($\tau^*$)** kaha jata hai:

$$
\tau^* = \frac{C_{FP}}{C_{FN} + C_{FP}}
$$

##### Step 3: Exact Numerical Value Substitution

$$
\tau^* = \frac{20}{500 + 20} = \frac{20}{520} = \frac{1}{26} \approx 0.0384615 \implies 3.85\%
$$

##### Step 4: Medical Triaging Intuition
- **Default Threshold Ki Galti:** Standard machine learning packages (jaise scikit-learn) default threshold $\tau = 0.50$ ($50\%$) use karte hain. Lekin medical diagnosis mein agar hum $50\%$ probability ka intezaar karenge, toh hum tab tak kisi ko positive nahi bolenge jab tak hum aadhi se zyada sure na hon!
- Is dauran bohot saare cardiac patients jin par model ka probability score $15\%$ ya $25\%$ tha, wo miss ($FN$) ho jayenge aur unki maut ho jayegi.
- **Optimal Strategy:** Jab miss karne ka jurmana (\$500) jhoothe alarm (\$20) se $25$ guna bada ho, toh threshold ko dramatically drop karke $\tau^* \approx 0.0385$ ($3.85\%$) par set kiya jata hai. Agar kisi patient mein cardiac issue ka sirf $4\%$ bhi doubt hai, toh turant confirmation ultrasound test kiya jana chahiye!

---

#### 🔹 Task 5: Python Visualization & Cost Analysis

Niche diye gaye graphical plots Case 1 ke Confusion Matrix heatmap aur Threshold vs Clinical Cost relationship ko clearly display karte hain:

![Case 1 Confusion Matrix & Cost Curve](case1_confusion_matrix_cost_curve.png)

```python
import numpy as np
import matplotlib.pyplot as plt

# Confusion Matrix counts
cm = np.array([[8820, 980],
               [10,   190]])

# Bayes Optimal Threshold
c_fn, c_fp = 500.0, 20.0
tau_star = c_fp / (c_fn + c_fp)
print(f"Bayes Optimal Decision Threshold: tau* = {tau_star:.4f} ({tau_star*100:.2f}%)")

# Cost comparison
cost_standard = (10 * c_fn) + (980 * c_fp)
print(f"Total Cohort Penalty Cost at standard sensitivity/specificity: ${cost_standard:,.2f}")
```

---

# 📌 Solution to Case 2: Bayesian Spam Filtering & Gaussian vs Multinomial Naive Bayes with Laplace Smoothing

### 🎯 Is Case Study Mein Pucha Kya Gaya Tha? (Quick Recap)

Gateway training parameters:

$$
N = 1,000, \qquad N_{\text{spam}} = 300, \qquad N_{\text{ham}} = 700
$$

$$
P(\text{Spam}) = 0.30, \qquad P(\text{Ham}) = 0.70
$$

$$
|V| = 500, \qquad T_{\text{spam}} = 3,000, \qquad T_{\text{ham}} = 7,000
$$

Continuous Urgency parameters:

$$
\text{Spam}: \mu_S = 8.5, \ \sigma_S = 1.5, \qquad \text{Ham}: \mu_H = 2.0, \ \sigma_H = 1.0
$$

Test email:

$$
E_{\text{test}} = \{\text{"lottery"}, \text{"winner"}, \text{"cryptocurrency"}\}, \qquad x_{\text{urgency}} = 6.0
$$

---

### 1. Step-by-Step Mathematical Derivations & Calculations

#### 🔹 Task 1: Conditional Independence Assumption & Likelihood Factorization

##### Step 1: Joint Likelihood Problem
Ek email document vector $\mathbf{x} = [x_1, x_2, \dots, x_d]^T$ ke liye exact joint conditional distribution hota hai:

$$
P(\mathbf{x} \mid C_k) = P(x_1, x_2, \dots, x_d \mid C_k)
$$

Chain rule of probability se iska general expansion:

$$
P(x_1, \dots, x_d \mid C_k) = P(x_1 \mid C_k) \cdot P(x_2 \mid x_1, C_k) \cdot P(x_3 \mid x_1, x_2, C_k) \cdots P(x_d \mid x_1, \dots, x_{d-1}, C_k)
$$

Agar vocabulary size $d = 500$ hai aur binary features hain, toh is distribution ko represent karne ke liye $2^d - 1 = 2^{500} - 1 \approx 10^{150}$ parameters ki zaroorat padegi, jo universe ke atoms se bhi zyada hai!

##### Step 2: The "Naive" Assumption
Naive Bayes algorithm yeh assume karta hai ki di gayi class $C_k$ ke context mein sabhi features aapas mein mutually conditionally independent hain:

$$
P(x_i \mid x_j, C_k) = P(x_i \mid C_k) \quad \forall i \ne j
$$

Is assumption ki wajah se joint likelihood simply har individual feature ki conditional probabilities ka direct product ban jati hai:

$$
P(\mathbf{x} \mid C_k) = \prod_{j=1}^d P(x_j \mid C_k)
$$

Parameters ki sankhya $10^{150}$ se collapse hokar sirf:

$$
\text{Total Parameters} = K \times d = 2 \times 500 = 1,000 \text{ parameters}
$$

ban jati hai, jise hum historical data se microseconds mein estimate kar sakte hain!

---

#### 🔹 Task 2: Zero-Frequency Problem & Laplace Add-1 Smoothing ($\alpha = 1$)

##### Step 1: The Catastrophic Zero-Frequency Crash
Test email mein rare word $w_4 = \text{"cryptocurrency"}$ मौजूद hai. Ham training data mein yeh word ek baar bhi nahi dekha gaya tha ($\text{count}(w_4, \text{Ham}) = 0$).

Agar hum Standard Maximum Likelihood Estimation (MLE) use karein:

$$
P_{\text{MLE}}(w_4 \mid \text{Ham}) = \frac{\text{count}(w_4, \text{Ham})}{T_{\text{ham}}} = \frac{0}{7000} = 0.0
$$

Ab Ham class ka joint posterior likelihood calculate karein:

$$
P(E_{\text{test}} \mid \text{Ham}) = P(w_1 \mid H) \cdot P(w_2 \mid H) \cdot P(w_4 \mid H)
$$

$$
P(E_{\text{test}} \mid \text{Ham}) = P(w_1 \mid H) \cdot P(w_2 \mid H) \cdot 0 = 0.0
$$

**The Disaster:** Chahe baki ke 99 words kitne bhi clean aur legitimate business terms kyu na rahe hon, ek single zero ne pure product ko instant $0$ bana diya! Gateway is email ka $P(\text{Ham} \mid E) = 0$ aur $P(\text{Spam} \mid E) = 1.0$ nikaal dega, jisse legitimate emails block ho jayengi.

##### Step 2: Laplace Add-1 Smoothing ($\alpha = 1$) Formulation
Is problem ko solve karne ke liye hum Laplace regularizer use karte hain. Har word ke count mein pseudo-count $\alpha = 1$ add kiya jata hai, aur denominator mein vocabulary size $|V|$ add kiya jata hai taaki probabilities ka sum abhi bhi $1$ rahe:

$$
\hat{P}(w_j \mid C_k) = \frac{\text{count}(w_j, C_k) + \alpha}{\sum_{w \in V} \text{count}(w, C_k) + \alpha |V|}
$$

Yahan $\alpha = 1$ aur $|V| = 500$ ke sath denominators:
- **Spam Denominator:**

$$
\text{Denom}_{\text{spam}} = T_{\text{spam}} + \alpha |V| = 3,000 + (1 \times 500) = 3,500
$$

- **Ham Denominator:**

$$
\text{Denom}_{\text{ham}} = T_{\text{ham}} + \alpha |V| = 7,000 + (1 \times 500) = 7,500
$$

##### Step 3: Exact Smoothed Conditional Probabilities Calculation

1. **Word $w_1 = \text{"lottery"}$:**

$$
\hat{P}(\text{"lottery"} \mid \text{Spam}) = \frac{120 + 1}{3,500} = \frac{121}{3,500} \approx 0.0345714
$$

$$
\hat{P}(\text{"lottery"} \mid \text{Ham}) = \frac{2 + 1}{7,500} = \frac{3}{7,500} = 0.0004000
$$

2. **Word $w_2 = \text{"winner"}$:**

$$
\hat{P}(\text{"winner"} \mid \text{Spam}) = \frac{90 + 1}{3,500} = \frac{91}{3,500} \approx 0.0260000
$$

$$
\hat{P}(\text{"winner"} \mid \text{Ham}) = \frac{5 + 1}{7,500} = \frac{6}{7,500} = 0.0008000
$$

3. **Word $w_3 = \text{"meeting"}$:**

$$
\hat{P}(\text{"meeting"} \mid \text{Spam}) = \frac{15 + 1}{3,500} = \frac{16}{3,500} \approx 0.0045714
$$

$$
\hat{P}(\text{"meeting"} \mid \text{Ham}) = \frac{420 + 1}{7,500} = \frac{421}{7,500} \approx 0.0561333
$$

4. **Word $w_4 = \text{"cryptocurrency"}$:**

$$
\hat{P}(\text{"cryptocurrency"} \mid \text{Spam}) = \frac{10 + 1}{3,500} = \frac{11}{3,500} \approx 0.0031429
$$

$$
\hat{P}(\text{"cryptocurrency"} \mid \text{Ham}) = \frac{0 + 1}{7,500} = \frac{1}{7,500} \approx 0.0001333
$$

Notice karein ki $w_4$ ka ham conditional probability ab $0$ nahi raha, balki ek small positive baseline probability $\frac{1}{7500} \approx 0.000133$ ban gaya!

---

#### 🔹 Task 3: Log-Likelihood Formulation & Underflow Prevention

##### Step 1: The IEEE-754 Underflow Limit
Modern CPU registers 64-bit double precision floating point numbers (IEEE-754 standard) use karte hain. Inka minimum positive non-zero representable number hota hai:

$$
\text{DBL\_MIN} \approx 2.225 \times 10^{-308}
$$

Agar ek lambi email mein $100$ words hain aur har word ki conditional probability average $10^{-4}$ hai, toh direct multiplication:

$$
\prod_{j=1}^{100} 10^{-4} = 10^{-400} < 10^{-308}
$$

Computer hardware ke registers is value ko store nahi kar sakte aur ise automatically `0.0` mein round off kar dete hain (**Arithmetic Underflow**). Dono classes ka score zero ho jata hai aur system crash ho jata hai.

##### Step 2: Logarithmic Transformation
Kyunki natural logarithm $\ln(x)$ ek strictly monotonically increasing function hai:

$$
a > b \iff \ln(a) > \ln(b)
$$

Log lene se relative ranking aur maximum point bilkul change nahi hota. Multiplication addition mein transform ho jata hai:

$$
\log P(C_k \mid \mathbf{x}) \propto \log P(C_k) + \sum_{j=1}^d \log P(x_j \mid C_k)
$$

Small numbers jaise $10^{-4}$ log space mein comfortable negative numbers ban jaate hain:

$$
\ln(10^{-4}) \approx -9.21
$$

Sum of 100 log values lagbhag $-921$ aayega, jise 64-bit float perfectly represent aur add kar sakta hai bina kisi data loss ke!

---

#### 🔹 Task 4: Continuous Features via Gaussian Naive Bayes PDF

##### Step 1: Gaussian Density Formula

$$
f(x \mid \mu, \sigma^2) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right)
$$

Test email ka continuous urgency score:

$$
x = 6.0
$$

##### Step 2: Probability Density for Ham Class ($\mu_H = 2.0, \sigma_H = 1.0$)

$$
\text{Exponent}_H = -\frac{(6.0 - 2.0)^2}{2(1.0)^2} = -\frac{4.0^2}{2} = -\frac{16.0}{2} = -8.0
$$

$$
\exp(-8.0) \approx 0.0003354626
$$

$$
\frac{1}{\sqrt{2\pi (1.0)^2}} = \frac{1}{\sqrt{2\pi}} \approx 0.3989423
$$

$$
f(6.0 \mid \text{Ham}) = 0.3989423 \times 0.0003354626 \approx 0.00013383
$$

##### Step 3: Probability Density for Spam Class ($\mu_S = 8.5, \sigma_S = 1.5$)

$$
\text{Exponent}_S = -\frac{(6.0 - 8.5)^2}{2(1.5)^2} = -\frac{(-2.5)^2}{2 \times 2.25} = -\frac{6.25}{4.50} \approx -1.3888889
$$

$$
\exp(-1.3888889) \approx 0.2493522
$$

$$
\frac{1}{\sqrt{2\pi (1.5)^2}} = \frac{1}{1.5 \sqrt{2\pi}} = \frac{0.3989423}{1.5} \approx 0.2659615
$$

$$
f(6.0 \mid \text{Spam}) = 0.2659615 \times 0.2493522 \approx 0.0663189
$$

##### Step 4: Likelihood Ratio Calculation

$$
\text{LR}_{\text{urgency}} = \frac{f(6.0 \mid \text{Spam})}{f(6.0 \mid \text{Ham})} = \frac{0.0663189}{0.00013383} \approx 495.545
$$

Continuous urgency score $x = 6.0$ akele hi spam hone ki evidence ko lagbhag **$495$ guna** badha deta hai!

---

#### 🔹 Task 5: Joint Bayesian Scoring & Classification Decision

Test email $E_{\text{test}}$ mein words hain: $\{\text{"lottery"}, \text{"winner"}, \text{"cryptocurrency"}\}$ aur urgency score $x=6.0$.

##### Step 1: Joint Score for Spam Class

$$
\text{Score}(\text{Spam}) = P(\text{Spam}) \cdot \hat{P}(\text{"lottery"} \mid S) \cdot \hat{P}(\text{"winner"} \mid S) \cdot \hat{P}(\text{"cryptocurrency"} \mid S) \cdot f(6.0 \mid S)
$$

Exact fractions substitute karein:

$$
\text{Score}(\text{Spam}) = 0.30 \times \frac{121}{3500} \times \frac{91}{3500} \times \frac{11}{3500} \times 0.0663189
$$

$$
\text{Text Product}_{\text{spam}} = 0.0345714 \times 0.0260000 \times 0.0031429 \approx 2.8250 \times 10^{-6}
$$

$$
\text{Score}(\text{Spam}) = 0.30 \times (2.8250 \times 10^{-6}) \times 0.0663189 \approx 5.6206 \times 10^{-8}
$$

##### Step 2: Joint Score for Ham Class

$$
\text{Score}(\text{Ham}) = P(\text{Ham}) \cdot \hat{P}(\text{"lottery"} \mid H) \cdot \hat{P}(\text{"winner"} \mid H) \cdot \hat{P}(\text{"cryptocurrency"} \mid H) \cdot f(6.0 \mid H)
$$

Exact fractions substitute karein:

$$
\text{Score}(\text{Ham}) = 0.70 \times \frac{3}{7500} \times \frac{6}{7500} \times \frac{1}{7500} \times 0.00013383
$$

$$
\text{Text Product}_{\text{ham}} = 0.0004000 \times 0.0008000 \times 0.00013333 \approx 4.2667 \times 10^{-11}
$$

$$
\text{Score}(\text{Ham}) = 0.70 \times (4.2667 \times 10^{-11}) \times 0.00013383 \approx 3.9970 \times 10^{-15}
$$

##### Step 3: Posterior Odds & Final Normalization

$$
\text{Evidence Ratio} = \frac{\text{Score}(\text{Spam})}{\text{Score}(\text{Ham})} = \frac{5.6206 \times 10^{-8}}{3.9970 \times 10^{-15}} \approx 14,062,046 \implies 1.406 \times 10^7
$$

Normalized posterior probability of Spam:

$$
P(\text{Spam} \mid E_{\text{test}}) = \frac{\text{Score}(\text{Spam})}{\text{Score}(\text{Spam}) + \text{Score}(\text{Ham})} = \frac{5.6206 \times 10^{-8}}{5.6206 \times 10^{-8} + 3.9970 \times 10^{-15}} \approx 0.999999928 \implies 99.99999\%
$$

##### Step 4: Final Gateway Automated Verdict
- **Automated Decision:** **DEFINITIVE MALICIOUS SPAM / PHISHING DETECTED**.
- **Action:** Gateway inbound email ko reject karega aur sandbox quarantine folder mein move karega.

![Case 2 Naive Bayes Distributions & Log Odds](case2_naive_bayes_log_odds.png)

---

# 📌 Solution to Case 3: Metric-Space Nearest Neighbor Classification (kNN), Curse of Dimensionality & Leakage-Free Stratified K-Fold Pipeline

### 🎯 Is Case Study Mein Pucha Kya Gaya Tha? (Quick Recap)

Baseline historical points:

$$
\begin{aligned}
P_1 &= [25.0, 0.005]^T, \quad y_1 = 0 \\
P_2 &= [30.0, 0.008]^T, \quad y_2 = 0 \\
P_3 &= [35.0, 0.012]^T, \quad y_3 = 0 \\
P_4 &= [80.0, 0.040]^T, \quad y_4 = 1 \\
P_5 &= [85.0, 0.045]^T, \quad y_5 = 1 \\
P_6 &= [90.0, 0.048]^T, \quad y_6 = 1
\end{aligned}
$$

Query point:

$$
Q = [40.0, 0.042]^T
$$

---

### 1. Step-by-Step Mathematical Derivations & Calculations

#### 🔹 Task 1: Unscaled Euclidean Distances & Feature Dominance

##### Step 1: Distance Metric Definition
2D unscaled Euclidean distance:

$$
d(Q, P_i) = \sqrt{(x_{Q, 1} - x_{i, 1})^2 + (x_{Q, 2} - x_{i, 2})^2}
$$

##### Step 2: Step-by-step Evaluation for Each Point

1. **Point $P_1 = [25.0, 0.005]^T$ ($y=0$):**
   - $\Delta x_1^2 = (40.0 - 25.0)^2 = 15.0^2 = 225.0$
   - $\Delta x_2^2 = (0.042 - 0.005)^2 = 0.037^2 = 0.001369$
   - $d(Q, P_1) = \sqrt{225.0 + 0.001369} = \sqrt{225.001369} \approx 15.0000456$
   - Contribution of $x_1$: $\frac{225.0}{225.001369} \approx 99.99939\%$

2. **Point $P_2 = [30.0, 0.008]^T$ ($y=0$):**
   - $\Delta x_1^2 = (40.0 - 30.0)^2 = 10.0^2 = 100.0$
   - $\Delta x_2^2 = (0.042 - 0.008)^2 = 0.034^2 = 0.001156$
   - $d(Q, P_2) = \sqrt{100.0 + 0.001156} = \sqrt{100.001156} \approx 10.0000578$
   - Contribution of $x_1$: $\frac{100.0}{100.001156} \approx 99.99884\%$

3. **Point $P_3 = [35.0, 0.012]^T$ ($y=0$):**
   - $\Delta x_1^2 = (40.0 - 35.0)^2 = 5.0^2 = 25.0$
   - $\Delta x_2^2 = (0.042 - 0.012)^2 = 0.030^2 = 0.000900$
   - $d(Q, P_3) = \sqrt{25.0 + 0.000900} = \sqrt{25.000900} \approx 5.0000900$
   - Contribution of $x_1$: $\frac{25.0}{25.000900} \approx 99.99640\%$

4. **Point $P_4 = [80.0, 0.040]^T$ ($y=1$):**
   - $\Delta x_1^2 = (40.0 - 80.0)^2 = (-40.0)^2 = 1600.0$
   - $\Delta x_2^2 = (0.042 - 0.040)^2 = 0.002^2 = 0.000004$
   - $d(Q, P_4) = \sqrt{1600.0 + 0.000004} = \sqrt{1600.000004} \approx 40.00000005$

5. **Point $P_5 = [85.0, 0.045]^T$ ($y=1$):**
   - $\Delta x_1^2 = (40.0 - 85.0)^2 = (-45.0)^2 = 2025.0$
   - $\Delta x_2^2 = (0.042 - 0.045)^2 = (-0.003)^2 = 0.000009$
   - $d(Q, P_5) = \sqrt{2025.0 + 0.000009} = \sqrt{2025.000009} \approx 45.0000001$

6. **Point $P_6 = [90.0, 0.048]^T$ ($y=1$):**
   - $\Delta x_1^2 = (40.0 - 90.0)^2 = (-50.0)^2 = 2500.0$
   - $\Delta x_2^2 = (0.042 - 0.048)^2 = (-0.006)^2 = 0.000036$
   - $d(Q, P_6) = \sqrt{2500.0 + 0.000036} = \sqrt{2500.000036} \approx 50.0000004$

##### Step 3: Unscaled Nearest Neighbors
Sorted order of raw distances:
1. $P_3$ ($d \approx 5.00$, Class $0$)
2. $P_2$ ($d \approx 10.00$, Class $0$)
3. $P_1$ ($d \approx 15.00$, Class $0$)
4. $P_4$ ($d \approx 40.00$, Class $1$)
5. $P_5$ ($d \approx 45.00$, Class $1$)
6. $P_6$ ($d \approx 50.00$, Class $1$)

**Failure Insight:** Unscaled space mein $k=3$ nearest neighbors hain: $\{P_3, P_2, P_1\}$. Sabhi ke sabhi Class 0 (Normal) hain! Vibration sensor ($x_2$) ka contribution $>99.99\%$ suppress ho gaya, jabki turbine ka vibration $0.042\text{ mm}$ extreme breakdown level par hai.

---

#### 🔹 Task 2: Z-Score Standardization & Nearest Neighbor Inversion

##### Step 1: Reference Dataset Sample Statistics Calculation
1. **Feature 1 (Temperature $x_1$):**

$$
\mu_1 = \frac{25 + 30 + 35 + 80 + 85 + 90}{6} = \frac{345}{6} = 57.5^\circ\text{C}
$$

Deviations $(x_{i, 1} - \mu_1)$: $[-32.5, -27.5, -22.5, +22.5, +27.5, +32.5]$.
Squared deviations sum:

$$
\sum (x_{i, 1} - \mu_1)^2 = 2 \times (32.5^2 + 27.5^2 + 22.5^2) = 2 \times (1056.25 + 756.25 + 506.25) = 2 \times 2318.75 = 4637.5
$$

Sample Standard Deviation ($n - 1 = 5$):

$$
\sigma_1 = \sqrt{\frac{4637.5}{5}} = \sqrt{927.5} \approx 30.454886^\circ\text{C}
$$

2. **Feature 2 (Vibration $x_2$):**

$$
\mu_2 = \frac{0.005 + 0.008 + 0.012 + 0.040 + 0.045 + 0.048}{6} = \frac{0.158}{6} \approx 0.0263333\text{ mm}
$$

Deviations $(x_{i, 2} - \mu_2)$: $[-0.021333, -0.018333, -0.014333, +0.013667, +0.018667, +0.021667]$.
Squared deviations sum:

$$
\sum (x_{i, 2} - \mu_2)^2 \approx 0.001943333
$$

Sample Standard Deviation:

$$
\sigma_2 = \sqrt{\frac{0.001943333}{5}} = \sqrt{0.000388667} \approx 0.0197146\text{ mm}
$$

##### Step 2: Z-Score Transformation of Reference Points and Query $Q$

Standardization formula:

$$
z_{i, j} = \frac{x_{i, j} - \mu_j}{\sigma_j}
$$

- Query Point $Q = [40.0, 0.042]^T$:

$$
z_{Q, 1} = \frac{40.0 - 57.5}{30.454886} = \frac{-17.5}{30.454886} \approx -0.57462
$$

$$
z_{Q, 2} = \frac{0.042 - 0.0263333}{0.0197146} = \frac{0.0156667}{0.0197146} \approx +0.79468
$$

- Reference Points in Z-space $\mathbf{z}_i = [z_{i, 1}, z_{i, 2}]^T$:

$$
\begin{aligned}
\mathbf{z}_1 &= [-1.06715, -1.08211]^T, \quad y_1 = 0 \\
\mathbf{z}_2 &= [-0.90298, -0.92994]^T, \quad y_2 = 0 \\
\mathbf{z}_3 &= [-0.73880, -0.72704]^T, \quad y_3 = 0 \\
\mathbf{z}_4 &= [+0.73880, +0.69322]^T, \quad y_4 = 1 \\
\mathbf{z}_5 &= [+0.90298, +0.94684]^T, \quad y_5 = 1 \\
\mathbf{z}_6 &= [+1.06715, +1.09903]^T, \quad y_6 = 1
\end{aligned}
$$

##### Step 3: Scaled Euclidean Distances $d_{\text{scaled}}(Q, P_i)$

$$
d_{\text{scaled}}(Q, P_i) = \sqrt{(z_{Q, 1} - z_{i, 1})^2 + (z_{Q, 2} - z_{i, 2})^2}
$$

1. **For $P_4$ ($y=1$):**
   - $\Delta z_1 = -0.57462 - 0.73880 = -1.31342 \implies \Delta z_1^2 \approx 1.72507$
   - $\Delta z_2 = 0.79468 - 0.69322 = 0.10146 \implies \Delta z_2^2 \approx 0.01029$
   - $d_{\text{scaled}}(Q, P_4) = \sqrt{1.72507 + 0.01029} = \sqrt{1.73536} \approx \mathbf{1.3173}$

2. **For $P_5$ ($y=1$):**
   - $\Delta z_1 = -0.57462 - 0.90298 = -1.47760 \implies \Delta z_1^2 \approx 2.18330$
   - $\Delta z_2 = 0.79468 - 0.94684 = -0.15216 \implies \Delta z_2^2 \approx 0.02315$
   - $d_{\text{scaled}}(Q, P_5) = \sqrt{2.18330 + 0.02315} = \sqrt{2.20645} \approx \mathbf{1.4854}$

3. **For $P_3$ ($y=0$):**
   - $\Delta z_1 = -0.57462 - (-0.73880) = 0.16418 \implies \Delta z_1^2 \approx 0.02695$
   - $\Delta z_2 = 0.79468 - (-0.72704) = 1.52172 \implies \Delta z_2^2 \approx 2.31563$
   - $d_{\text{scaled}}(Q, P_3) = \sqrt{0.02695 + 2.31563} = \sqrt{2.34258} \approx \mathbf{1.5305}$

4. **For $P_6$ ($y=1$):**
   - $\Delta z_1 = -0.57462 - 1.06715 = -1.64177 \implies \Delta z_1^2 \approx 2.69541$
   - $\Delta z_2 = 0.79468 - 1.09903 = -0.30435 \implies \Delta z_2^2 \approx 0.09263$
   - $d_{\text{scaled}}(Q, P_6) = \sqrt{2.69541 + 0.09263} = \sqrt{2.78804} \approx \mathbf{1.6697}$

5. **For $P_2$ ($y=0$):**
   - $\Delta z_1 = -0.57462 - (-0.90298) = 0.32836 \implies \Delta z_1^2 \approx 0.10782$
   - $\Delta z_2 = 0.79468 - (-0.92994) = 1.72462 \implies \Delta z_2^2 \approx 2.97431$
   - $d_{\text{scaled}}(Q, P_2) = \sqrt{0.10782 + 2.97431} = \sqrt{3.08213} \approx \mathbf{1.7556}$

6. **For $P_1$ ($y=0$):**
   - $\Delta z_1 = -0.57462 - (-1.06715) = 0.49253 \implies \Delta z_1^2 \approx 0.24259$
   - $\Delta z_2 = 0.79468 - (-1.08211) = 1.87679 \implies \Delta z_2^2 \approx 3.52234$
   - $d_{\text{scaled}}(Q, P_1) = \sqrt{0.24259 + 3.52234} = \sqrt{3.76493} \approx \mathbf{1.9403}$

##### Step 4: Comparison Table & Inversion Proof

| Reference Point | True State | Unscaled Distance | Unscaled Rank | Scaled Distance ($z$-space) | Scaled Rank |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **$P_4$** | **Faulty ($y=1$)** | $40.000$ | $4$ | $\mathbf{1.3173}$ | $\mathbf{1}$ (Nearest) |
| **$P_5$** | **Faulty ($y=1$)** | $45.000$ | $5$ | $\mathbf{1.4854}$ | $\mathbf{2}$ |
| **$P_3$** | Normal ($y=0$) | $5.000$ | $1$ | $\mathbf{1.5305}$ | $\mathbf{3}$ |
| **$P_6$** | **Faulty ($y=1$)** | $50.000$ | $6$ | $\mathbf{1.6697}$ | $4$ |
| **$P_2$** | Normal ($y=0$) | $10.000$ | $2$ | $\mathbf{1.7556}$ | $5$ |
| **$P_1$** | Normal ($y=0$) | $15.000$ | $3$ | $\mathbf{1.9403}$ | $6$ (Farthest) |

**Mathematical Proof of Inversion:**
- Unscaled space mein top-3 nearest neighbors the: $\{P_3, P_2, P_1\}$ $\implies$ $100\%$ Normal ($y=0$).
- Standardized space mein top-2 nearest neighbors hain: $\{P_4, P_5\}$ $\implies$ $100\%$ Faulty ($y=1$).
Standardization ne critical vibration hazard ko restore kiya aur classifier ko catastrophically wrong prediction se bacha liya!

---

#### 🔹 Task 3: Uniform vs Distance-Weighted Voting Mechanics

##### 1. Case $k = 3$:
Nearest neighbors set:

$$
\mathcal{N}_3(Q) = \{P_4 (y=1), P_5 (y=1), P_3 (y=0)\}
$$

- **Uniform Majority Voting:**

$$
\text{Votes}(y = 1) = 2 \quad (P_4, P_5), \qquad \text{Votes}(y = 0) = 1 \quad (P_3)
$$

$$
\hat{y} = \arg\max(1, 2) = \mathbf{1 \quad (\text{Faulty Turbine})}
$$

- **Inverse Distance Weighted Voting ($w_i = \frac{1}{d_i}$):**

$$
w_4 = \frac{1}{1.3173} \approx 0.75913, \qquad w_5 = \frac{1}{1.4854} \approx 0.67322, \qquad w_3 = \frac{1}{1.5305} \approx 0.65338
$$

Aggregate class weights:

$$
W(y = 1) = w_4 + w_5 = 0.75913 + 0.67322 = 1.43235
$$

$$
W(y = 0) = w_3 = 0.65338
$$

Weighted probability of Faulty class:

$$
P(y = 1 \mid Q) = \frac{1.43235}{1.43235 + 0.65338} = \frac{1.43235}{2.08573} \approx 0.6867 \implies \mathbf{68.67\% \text{ Confidence (Faulty)}}
$$

##### 2. Case $k = 5$:
Nearest neighbors set:

$$
\mathcal{N}_5(Q) = \{P_4(1), P_5(1), P_3(0), P_6(1), P_2(0)\}
$$

- **Uniform Majority Voting:**

$$
\text{Votes}(y = 1) = 3 \quad (P_4, P_5, P_6), \qquad \text{Votes}(y = 0) = 2 \quad (P_3, P_2)
$$

$$
\hat{y} = \arg\max(2, 3) = \mathbf{1 \quad (\text{Faulty Turbine})}
$$

- **Inverse Distance Weighted Voting:**

$$
w_6 = \frac{1}{1.6697} \approx 0.59891, \qquad w_2 = \frac{1}{1.7556} \approx 0.56961
$$

Aggregate class weights:

$$
W(y = 1) = 1.43235 + 0.59891 = 2.03126
$$

$$
W(y = 0) = 0.65338 + 0.56961 = 1.22299
$$

Weighted probability of Faulty class:

$$
P(y = 1 \mid Q) = \frac{2.03126}{2.03126 + 1.22299} = \frac{2.03126}{3.25425} \approx 0.6242 \implies \mathbf{62.42\% \text{ Confidence (Faulty)}}
$$

---

#### 🔹 Task 4: Curse of Dimensionality & Metric Collapse Theorem

##### Step 1: Formal Mathematical Theorem (Beyer et al., 1999)
Agar $d$-dimensional space $\mathbb{R}^d$ mein points kisi independent identically distributed (i.i.d.) distribution se draw kiye jayein, aur $D_{\min}$ nearest neighbor distance ho jabki $D_{\max}$ farthest neighbor distance ho:

$$
D_{\min} = \min_{i=1,\dots,n} \lVert \mathbf{x}_i - \mathbf{q} \rVert_2, \qquad D_{\max} = \max_{i=1,\dots,n} \lVert \mathbf{x}_i - \mathbf{q} \rVert_2
$$

Toh jaise-jaise dimensionality $d \to \infty$ grow karti hai:

$$
\lim_{d \to \infty} \frac{D_{\max} - D_{\min}}{D_{\min}} = 0
$$

##### Step 2: Proof Intuition (Law of Large Numbers)
Euclidean distance squared hota hai:

$$
D^2 = \sum_{j=1}^d (x_j - q_j)^2
$$

Let $Z_j = (x_j - q_j)^2$. Kyunki sabhi features independent hain, Central Limit Theorem / Law of Large Numbers kehta hai ki:

$$
\mathbb{E}[D^2] = d \cdot \mu_Z, \qquad \text{Var}(D^2) = d \cdot \sigma_Z^2
$$

Standard deviation of distance:

$$
\text{Std}(D^2) = \sqrt{d} \cdot \sigma_Z
$$

Relative standard deviation (Coefficient of Variation):

$$
\frac{\text{Std}(D^2)}{\mathbb{E}[D^2]} = \frac{\sqrt{d}\sigma_Z}{d\mu_Z} = \frac{\sigma_Z}{\mu_Z} \frac{1}{\sqrt{d}} \xrightarrow{d \to \infty} 0
$$

##### Step 3: Geometric Meaning & kNN Failure
- **Sphere Volume Collapse:** $d$-dimensional hypersphere ka volume uske radius $R$ par $V_d(R) \propto R^d$ behave karta hai. High dimensions mein lagbhag saara volume surface ke ek extremely thin outer shell par concentrate ho jata hai.
- **Metric Collapse:** High dimensions mein dataset ka sabse kareebi point ($D_{\min}$) aur sabse door ka point ($D_{\max}$) dono query point se lagbhag ek hi distance par aa jaate hain:

$$
\frac{D_{\max}}{D_{\min}} \to 1.000
$$

- Jab sabhi points ka distance barabar ho jaye, toh "Nearest Neighbor" ka concept hi khatam ho jata hai. kNN random guessing jaisa behave karne lagta hai. Isliye high-dimensional data par kNN lagane se pehle **PCA (Principal Component Analysis)** ya feature selection lagana mandatory hota hai.

---

#### 🔹 Task 5: Data Leakage Elimination & Scikit-Learn Pipeline

##### Step 1: Data Leakage Mechanism
Jab log galti se cross-validation se pehle scaling run kar dete hain:

```python
# ❌ CATASTROPHIC DATA LEAKAGE: DO NOT DO THIS!
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X) # Test set statistics leak into training!
scores = cross_val_score(knn, X_scaled, y, cv=5)
```

- **Leakage Path:** `scaler.fit_transform(X)` poore dataset ke mean $\mu_{\text{global}}$ aur standard deviation $\sigma_{\text{global}}$ ko calculate karta hai. Isme validation split ke hidden data points ka distribution bhi jud gaya!
- Jab model validation split par evaluate hota hai, toh wo pehle se validation set ki information dekh chuka hota hai.
- Is leakage se test score $95\%$ dikhta hai, lekin production mein jab unseen customer data aata hai toh model crash ho jata hai.

##### Step 2: Zero-Leakage Architecture via `Pipeline`
Scikit-Learn ka `Pipeline` ensure karta hai ki preprocessing transformer (`StandardScaler`) har Cross-Validation fold ke andar encapsulate ho:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
import numpy as np

# 1. Zero-Leakage Pipeline Definition
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=5, weights='distance'))
])

# 2. Stratified Cross-Validation (Preserving 2% Rare Class Ratio)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# 3. Leakage-Free Cross-Validation
# Har fold mein:
# Scaler FITS ONLY ON 4 TRAIN FOLDS
# Scaler ONLY TRANSFORMS THE 1 VALIDATION FOLD
scores = cross_val_score(pipeline, X_sensor, y_status, cv=cv, scoring='f1_macro')

print(f"Leakage-Free Macro F1: {np.mean(scores):.4f} +/- {np.std(scores):.4f}")
```

![Case 3 kNN Decision Boundaries](case3_knn_decision_boundaries_k.png)
