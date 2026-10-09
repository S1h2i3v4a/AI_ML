# Module 24.14: Logistic Regression Ka Cost Function Aur MLE (Hinglish)

## 1. MSE Kyu Use Nahi Karte?

Agar hum Sigmoid function ko Mean Squared Error (MSE) mein daal dein, to curve wavy ban jata hai (Non-convex) jisme bohot saare local minima hote hain. Gradient descent waha phas jata hai aur fail ho jata hai.

---

## 2. Binary Cross-Entropy (Log Loss) Ka Derivation

Statistics ke **Maximum Likelihood Estimation (MLE)** se iska cost function derive hota hai jise **Binary Cross-Entropy (Log Loss)** kehte hain:

$$
J(\mathbf{w}, b) = -\frac{1}{m} \sum_{i=1}^m \left[ y^{(i)} \ln \hat{y}^{(i)} + (1 - y^{(i)}) \ln(1 - \hat{y}^{(i)}) \right]
$$

### Logarithmic Penalty Ka Jadoo:
- **Agar Actual $y = 1$ hai:** Loss hota hai $-\ln(\hat{y})$.
  - Agar prediction $\hat{y} = 1.0 \implies$ Loss $= 0$.
  - Agar prediction $\hat{y} = 0.0 \implies$ Loss $= +\infty$ (Infinite penalty!).
- **Agar Actual $y = 0$ hai:** Loss hota hai $-\ln(1 - \hat{y})$.
  - Galat prediction par model ko bohot tagda punishment milta hai.

---

## 3. Gradient Update Rule

Calculus se derivative lene par formula Linear Regression jaisa hi nikalta hai:

$$
\mathbf{w} := \mathbf{w} - \alpha \left[ \frac{1}{m} \mathbf{X}^T (\hat{\mathbf{y}} - \mathbf{y}) \right]
$$

Bas fark ye hai ki yaha $\hat{y} = \sigma(\mathbf{w}^T \mathbf{x} + b)$ hota hai!
