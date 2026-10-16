# Lecture 26.09: Logistic Regression from Scratch — Mathematical Formulation, Sigmoid & Log-Loss

## 📌 Saransh (Executive Summary)
Logistic Regression ka first-principles mathematical derivation, Sigmoid function $\sigma(z)$, Binary Cross-Entropy (Log-Loss), aur analytical gradients ka detailed proof.

---

## 🔬 First-Principles Theory & Intuition
### 1. Classification Mein Linear Regression Kyun Fail Hota Hai?
Linear Regression continuous output deta hai ($-\infty$ se $+\infty$). 
Agar hum classification ke liye linear line fit karein aur $0.5$ par threshold karein, toh ek single door ka outlier point puri line ko tilt kar deta hai, jisse sahi points bhi galat classify ho jate hain!

### 2. Sigmoid Activation Function $\sigma(z)$
Is problem ko solve karne ke liye hum linear output $z = \mathbf{w}^T \mathbf{x} + b$ ko Sigmoid function ke andar bhejte hain:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

Yeh kisi bhi number ko $0$ aur $1$ ke beech squash kar deta hai, jise hum probability $P(y=1|x)$ ki tarah interpret karte hain.

### 3. Log-Loss (Binary Cross Entropy) Ka Formula
Agar model galat prediction deta hai (jaise actual 1 hai aur model ne 0.01 predict kiya), toh error infinity ki taraf shoot karta hai:

$$
J(\mathbf{w}, b) = -\frac{1}{m} \sum_{i=1}^m \left[ y^{(i)} \log(\hat{y}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)}) \right]
$$

### 4. Mathematical Miracle: Gradients Ka Cancellation
Jab hum chain rule se derivative lete hain, toh Sigmoid ka derivative $\hat{y}(1-\hat{y})$ aur Log-Loss ka denominator aapas mein cancel out ho jate hain!
Isliye gradient wahi same ban jata hai:

$$
dw = \frac{1}{m} X^T (\hat{\mathbf{y}} - \mathbf{y}), \quad db = \frac{1}{m} \sum_{i=1}^m (\hat{y}^{(i)} - y^{(i)})
$$


---

## 💻 Python & NumPy Code Implementation
```python
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def compute_log_loss(y_true, y_pred, eps=1e-15):
    # Clip to prevent log(0) undefined numerical errors
    y_pred = np.clip(y_pred, eps, 1 - eps)
    m = len(y_true)
    loss = - (1.0 / m) * np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return loss

# Demo
z_test = np.array([-5.0, 0.0, 5.0])
probs = sigmoid(z_test)
print("Sigmoid values for [-5, 0, 5]:", probs)

```

---

## 🎯 Key Takeaways & Practical Tips
1. **Black-Box Se Azadi**: Libraries ko blind use karne ke bajaye unke andar ka math samajhna aapko top 1% engineer banata hai.
2. **Vectorization Ki Taqat**: Python loops ke bajaye NumPy array operations use karein jo C/BLAS speed provide karte hain.
3. **Debugging Mastery**: Jab loss decrease na ho raha ho, toh sabse pehle learning rate $\alpha$ aur gradient dimensions check karein.
