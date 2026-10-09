# Module 23.11: Gradient Descent Kya Hota Hai? (Formulas Aur Learning Rate)

## 1. Optimization Ka Core Concept

**Gradient Descent** ek universal iterative optimization algorithm hai jo kisi bhi differentiable function ke minimum point ko dhoondhne ke liye use hota hai.
Kyunki Linear Regression ka cost function bowl-shaped (convex) hota hai, gradient descent hamesha global minimum par hi converge hota hai.

---

## 2. Gradient Formulas Ka Derivation

Cost function:

$$
J(w, b) = \frac{1}{2m} \sum_{i=1}^m \left( w x^{(i)} + b - y^{(i)} \right)^2
$$

Calculus ke chain rule se derivatives nikaalne par:

### 1. Weight ($w$) Ke Respect Mein Gradient:
$$
\frac{\partial J}{\partial w} = \frac{1}{m} \sum_{i=1}^m \left( \hat{y}^{(i)} - y^{(i)} \right) x^{(i)}
$$

### 2. Bias ($b$) Ke Respect Mein Gradient:
$$
\frac{\partial J}{\partial b} = \frac{1}{m} \sum_{i=1}^m \left( \hat{y}^{(i)} - y^{(i)} \right)
$$

---

## 3. Simultaneous Update Rule

Har iteration mein dono parameters ko **ek saath (simultaneously)** update karna padta hai:

$$
w := w - \alpha \frac{\partial J}{\partial w}
$$

$$
b := b - \alpha \frac{\partial J}{\partial b}
$$

Yaha $\alpha$ (Alpha) ko **Learning Rate** kehte hain.
**Important:** Code likhte waqt pehle dono gradients calculate karein, phir ek saath $w$ aur $b$ ko update karein. Agar pehle $w$ update kar diya aur phir naye $w$ se $b$ ka gradient nikala to math galat ho jayegi.

---

## 4. Learning Rate $\alpha$ Ka Role

- **$\alpha$ Bahut Chhota:** Steps itne chote honge ki minimum tak pahunchne mein hazaron iterations lag jayenge.
- **$\alpha$ Sahi/Balanced:** Har step smoothly minimum ki taraf badhega aur jaldi converge ho jayega.
- **$\alpha$ Bahut Bada:** Steps itne bade honge ki algorithm minimum ko chhod kar doosri taraf jump kar jayega, cost badhti jayegi aur code explode (`NaN` / infinity) ho jayega.
