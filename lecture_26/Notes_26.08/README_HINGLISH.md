# Lecture 26.08: Linear Regression — Gradient Descent vs Ordinary Least Squares (Algorithmic Trade-offs)

## 📌 Saransh (Executive Summary)
Gradient Descent vs OLS ka architectural comparison: Time complexity $\mathcal{O}(d^3)$ vs $\mathcal{O}(k \cdot m \cdot d)$, memory limits, aur decision tree.

---

## 🔬 First-Principles Theory & Intuition
### 1. Kab Kaunsa Algorithm Use Karein?
Donon algorithms ke apne pros aur cons hain:

#### Kab OLS Best Hai?
- Jab features kam hon ($d < 1,000$) aur dataset memory mein fit ho jaye.
- OLS mein koi learning rate set nahi karni padti, koi loop nahi chalana padta; ek baar mein exact mathematically perfect answer mil jata hai.

#### Kab Gradient Descent Compulsory Hai?
1. **Jab Features bohot zyada hon (High Dimensions, $d > 10,000$)**:
   Matrix inversion ka time complexity $\mathcal{O}(d^3)$ hota hai. Agar $d = 10,000$ hai, toh $(10^4)^3 = 10^{12}$ operations lagenge jo computer ko crash kar denge! GD linear $\mathcal{O}(d)$ hota hai.
2. **Jab Big Data ho ($m > 1,000,000$)**:
   Mini-batch GD data ko chhote chunks mein process kar leta hai.
3. **Streaming / Online Data**:
   Agar data live stream ho raha hai, toh har naye data point par GD model ko incrementally update kar sakta hai.


---

## 💻 Python & NumPy Code Implementation
```python
import numpy as np
import time

# Empirical Benchmark: OLS vs GD as feature dimension d scales
m = 10000
for d in [10, 100, 500, 1500]:
    X = np.random.randn(m, d)
    y = np.random.randn(m)
    
    # OLS Benchmark
    t0 = time.perf_counter()
    X_b = np.c_[np.ones((m, 1)), X]
    theta_ols = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
    t_ols = time.perf_counter() - t0
    
    # GD Benchmark (10 iterations)
    t0 = time.perf_counter()
    w = np.zeros(d)
    b = 0.0
    for _ in range(10):
        y_pred = X @ w + b
        res = y_pred - y
        dw = (1/m) * (X.T @ res)
        db = (1/m) * np.sum(res)
        w -= 0.01 * dw
        b -= 0.01 * db
    t_gd = time.perf_counter() - t0
    
    print(f"Features d={d:<5} | OLS Time: {t_ols:.4f}s | GD (10 iters): {t_gd:.4f}s")

```

---

## 🎯 Key Takeaways & Practical Tips
1. **Black-Box Se Azadi**: Libraries ko blind use karne ke bajaye unke andar ka math samajhna aapko top 1% engineer banata hai.
2. **Vectorization Ki Taqat**: Python loops ke bajaye NumPy array operations use karein jo C/BLAS speed provide karte hain.
3. **Debugging Mastery**: Jab loss decrease na ho raha ho, toh sabse pehle learning rate $\alpha$ aur gradient dimensions check karein.
