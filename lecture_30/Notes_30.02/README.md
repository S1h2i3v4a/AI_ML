# Lecture 30.02: Gradient Boosting Classifier — Log-Odds & Probability Math

[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#)
[![Theory](https://img.shields.io/badge/Topic-Theory%20%26%20Math-lightgrey.svg)](#)
[![Hinglish Notes](https://img.shields.io/badge/Notes-Hinglish-yellow.svg)](README_HINGLISH.md)
[![English PDF](https://img.shields.io/badge/PDF-English-red.svg)](notes.pdf)
[![Hinglish PDF](https://img.shields.io/badge/PDF-Hinglish-green.svg)](notes_hinglish.pdf)

---

## 📌 Topic Overview
Gradient Boosting for classification operates in Log-Odds space. The initial baseline prediction is log(p / (1 - p)), transformed via Sigmoid into probability. Trees are fitted on pseudo-residuals (y - p) and updated sequentially.


---

### 📋 Key Learning Objectives
- How Gradient Boosting adapts from regression to binary classification.
- Initial Baseline Model: Why classification starts with Log-Odds instead of raw class labels.
- Sigmoid Transformation: Converting log-odds into probabilities p = 1 / (1 + e^-F).
- Pseudo-Residuals Calculation: Computing r_i = y_i - p_i (actual binary label minus predicted probability).
- Leaf Output Calculation: Second-order Taylor approximation formula sum(r) / sum(p * (1 - p)).
- Shrinkage Update in Log-Odds Space: F_m(x) = F_{m-1}(x) + eta * Tree(x).

---

### 🔍 In-Depth Conceptual Breakdown

- **Binary Classification Setup**: Target variable mein do classes hoti hain: $0$ aur $1$ (jahan $1$ ko success consider karte hain, jaise Email Spam vs Ham).

- **Step 1: Baseline Model ($F_0$) via Log-Odds**: Direct majority class predict karne ke bajay model training data ki probability $p$ nikalta hai: $p = \text{count}(1) / N$. Fir **Log-Odds** calculate karta hai: $F_0 = \ln\left(\frac{p}{1 - p}\right)$.

- **Step 2: Convert to Probability (Sigmoid)**: Is log-odds value ko probability mein convert karne ke liye **Sigmoid function** use hota hai: $p = \sigma(F) = \frac{1}{1 + e^{-F}}$.

- **Step 3: Residuals Calculate Karo ($r_i = y_i - p_i$)**: Har sample ka actual label ($y_i \in \{0, 1\}$) aur predicted probability ($p_i$) ka difference nikalo. Jaise agar actual $y=1$ hai aur $p=0.7$ hai, toh residual $r = 1 - 0.7 = 0.3$.

- **Step 4: Train Regression Tree on Residuals**: Ek regression tree in residuals $r_i$ par train hota hai.

- **Step 5: Leaf Output Value Calculation**: Classification ke liye leaf ka output direct residual mean nahi hota, balki formula hota hai: $\gamma = \frac{\sum r_i}{\sum p_i(1 - p_i)}$.

- **Step 6: Update In Log-Odds Space**: Prediction log-odds space mein update hoti hai: $F_1(x) = F_0 + \eta \cdot \gamma$.

- **Final Class Prediction**: Final log-odds ko sigmoid se pass karo. Agar $p \ge 0.5$ hai toh **Class 1**, warna **Class 0** predict hota hai!

---

### 📊 Architectural Flowchart

```mermaid
flowchart TD
    A["Binary Target y in {0, 1}"] --> B["Step 1: Calculate Prior Probability p = count(1) / N"]
    B --> C["Step 2: Initial Baseline Log-Odds F_0 = ln(p / (1 - p))"]
    C --> D["Step 3: Convert Log-Odds to Probability: p_i = 1 / (1 + e^-F)"]
    D --> E["Step 4: Compute Residuals r_i = y_i - p_i"]
    E --> F["Step 5: Fit Regression Tree on Pseudo-Residuals"]
    F --> G["Step 6: Compute Leaf Output: gamma = sum(r_i) / sum(p_i * (1 - p_i))"]
    G --> H["Step 7: Update Log-Odds: F_m = F_{m-1} + eta * gamma"]
    H --> I{"Final Probability p = sigma(F_M) >= 0.5?"}
    I -->|"Yes"| J1["Predict Class 1"]
    I -->|"No"| J0["Predict Class 0"]
```

---



---

### 📋 Ma'am's Classroom Binary Classification Matrix

| Sample Index | Features ($X$) | Actual Label ($y \in \{0, 1\}$) | Initial Baseline Log-Odds ($F_0$) | Probability ($p_0 = \sigma(F_0)$) | Pseudo-Residual ($r_1 = y - p_0$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | $x_1$ | **1 (Success)** | $\ln(p / (1 - p))$ | $p_0$ | **$1 - p_0$** |
| **2** | $x_2$ | **0 (Failure)** | $\ln(p / (1 - p))$ | $p_0$ | **$0 - p_0$** |
| **3** | $x_3$ | **1 (Success)** | $\ln(p / (1 - p))$ | $p_0$ | **$1 - p_0$** |
| **4** | $x_4$ | **0 (Failure)** | $\ln(p / (1 - p))$ | $p_0$ | **$0 - p_0$** |

---

### 📊 Ma'am's Blackboard Classification Workflow

```mermaid
flowchart TD
    A["Binary Target y in {0, 1}"] --> B["Step 1: Compute Prior Probability p = count(1) / N"]
    B --> C["Step 2: Initial Baseline Log-Odds F_0 = ln(p / (1 - p))"]
    C --> D["Step 3: Transform Log-Odds to Probability: p_i = 1 / (1 + e^-F)"]
    D --> E["Step 4: Compute Residuals r_i = y_i - p_i"]
    E --> F["Step 5: Fit Regression Tree on Residuals"]
    F --> G["Step 6: Compute Leaf Output: gamma = sum(r_i) / sum(p_i * (1 - p_i))"]
    G --> H["Step 7: Update Log-Odds: F_m = F_{m-1} + eta * gamma"]
    H --> I{"Final Probability p = sigma(F_M) >= 0.5?"}
    I -->|"Yes"| J1["Predict Class 1"]
    I -->|"No"| J0["Predict Class 0"]
```

### 🔢 Mathematical Formulation

For binary cross-entropy (log-loss) $L(y, F) = -y \ln(p) - (1 - y) \ln(1 - p)$ where $p = \sigma(F) = \frac{1}{1 + e^{-F}}$:

The negative gradient with respect to log-odds $F$ simplifies elegantly to:

$$
r_{im} = -\left[ \frac{\partial L(y_i, F(x_i))}{\partial F(x_i)} \right] = y_i - p_i
$$

The initial baseline log-odds $F_0$ from training class prior $p$:

$$
F_0 = \ln\left( \frac{p}{1 - p} \right) = \ln\left( \frac{\sum_{i=1}^N y_i}{N - \sum_{i=1}^N y_i} \right)
$$

The terminal leaf output $\gamma_{jm}$ for region $R_{jm}$ in a tree maximizing the second-order Taylor expansion:

$$
\gamma_{jm} = \frac{\sum_{x_i \in R_{jm}} r_{im}}{\sum_{x_i \in R_{jm}} p_{im}(1 - p_{im})}
$$

---

### 📌 Note on Code
This is a pure conceptual, mathematical, and blackboard theory lecture. In accordance with course guidelines, no synthetic code is appended.

