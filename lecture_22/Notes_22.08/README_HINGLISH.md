# 📈 Lecture 22.08: Minima aur Maxima Dhoondhna [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Numpy](https://img.shields.io/badge/Numpy-Numerical%20Computing-013243.svg)](https://numpy.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 22 Par Wapas Jayein](../README_HINGLISH.md)

---

## 📌 1. Critical Points aur Extrema

Jab function ka derivative zero ho jaye ($f'(x) = 0$), toh us point ko **Critical Point** kehte hain.

- **Second Derivative Test ($f''(x)$):**
  - Agar $f''(x) > 0$: Curve upar ki taraf khulta hai (Concave Up) $\implies$ **Local Minimum** (sabse neechi value).
  - Agar $f''(x) < 0$: Curve neeche ki taraf khulta hai (Concave Down) $\implies$ **Local Maximum** (sabse unchi value).
  - Agar $f''(x) = 0$: Inflection Point (jahan curvature badalta hai).

---

## 📐 2. Gradient Descent Algorithm

Machine Learning mein loss function ko minimize karne ke liye Gradient Descent use hota hai:

$$
w_{t+1} = w_t - \eta \frac{d\mathcal{L}}{dw}
$$

Derivative ka sign batata hai ki weight ko badhana hai ya ghatana hai.

---

## 💻 3. Python Code

```python
w = 8.0
lr = 0.2
for _ in range(15):
    grad = 2 * (w - 3) # derivative of (w-3)^2
    w = w - lr * grad
print("Converged w:", w) # -> 3.0
```
