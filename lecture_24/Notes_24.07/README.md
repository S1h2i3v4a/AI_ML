# Module 24.07: Diagnostic Framework — Detecting Underfitting vs. Overfitting

## 1. The Diagnostic Dilemma

Looking solely at a single test accuracy number is insufficient to determine whether a machine learning model is underfitting or overfitting. A structured diagnostic methodology is required to inspect training dynamics and loss curves.

---

## 2. Learning Curves: Training Set Size ($m$) vs. Error

A **learning curve** plots training error and validation error as a function of the training sample size $m$:

### Case A: Underfitting (High Bias) Learning Curve
```
Error ^
      |     Training Error (rises and plateaus early at high error)
      |   -------------------------------------
      |                   High Error Plateau
      |   -------------------------------------
      |     Validation Error (drops slightly and plateaus)
      +-------------------------------------------------> Training Size (m)
```
- **Diagnostic Signature:** Both training and validation errors plateau at a **high error level**.
- **Crucial Rule:** Adding more training data **will NOT help**! The model is already saturated at its maximum capacity.

### Case B: Overfitting (High Variance) Learning Curve
```
Error ^
      |     Validation Error (high, slowly descending)
      |   \
      |    \------------------------- Generalization Gap
      |   
      |    .-------------------------
      |     Training Error (very low)
      +-------------------------------------------------> Training Size (m)
```
- **Diagnostic Signature:** There is a **large gap** between low training error and high validation error.
- **Crucial Rule:** Adding more training data **WILL help**! As $m$ increases, the validation curve continues to converge toward the training curve.

---

## 3. Systematic Diagnostic Decision Matrix

| Observation | Primary Problem | Prescribed Next Step |
| :--- | :--- | :--- |
| $\mathcal{L}_{\text{train}}$ is high, $\mathcal{L}_{\text{val}}$ is high | **High Bias (Underfitting)** | 1. Add more features / interactions<br/>2. Try a more complex model<br/>3. Decrease regularization ($\alpha \downarrow$) |
| $\mathcal{L}_{\text{train}}$ is low, $\mathcal{L}_{\text{val}}$ is high | **High Variance (Overfitting)** | 1. Collect more training data ($m \uparrow$)<br/>2. Apply / increase regularization ($\alpha \uparrow$)<br/>3. Feature selection (prune noise) |
| $\mathcal{L}_{\text{train}}$ is low, $\mathcal{L}_{\text{val}}$ is low | **Optimal Model** | Ready for production deployment |
