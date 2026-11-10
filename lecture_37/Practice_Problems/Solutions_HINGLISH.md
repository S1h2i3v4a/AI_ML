# Lecture 37 Practice Problems: Step-by-Step Solutions (Hinglish)

---

### Solution 1: Forward Pass Output
1. $z = (0.4)(2.0) + (-0.6)(-1.0) + (0.2)(3.0) - 0.5 = 0.8 + 0.6 + 0.6 - 0.5 = 1.5$.
2. $\hat{y} = \sigma(1.5) = \frac{1}{1 + e^{-1.5}} \approx 0.8176$.

---

### Solution 2: Outlier Regression Loss
Error $e = 10.0 - 60.0 = -50.0$.
1. $\mathcal{L}_{MSE} = \frac{1}{2}(-50)^2 = 1250.0$.
2. $\mathcal{L}_{MAE} = |-50| = 50.0$.
3. $\mathcal{L}_{\text{Huber}} = 2.0 \times 50.0 - \frac{1}{2}(2.0)^2 = 100 - 2 = 98.0$.
MSE ne outlier ko $25\times$ bada penalty diya, jabki Huber aur MAE ne gradient ko stable rakha.

---

### Solution 3: Binary Cross-Entropy Penalty
1. Sample A: $-\log(0.95) \approx 0.0513$.
2. Sample B: $-\log(0.05) \approx 2.9957$.
3. Penalty ratio: $\frac{2.9957}{0.0513} \approx 58.4\times$. Galat prediction par model ko lagbhag 60 guna bada jhatka lagta hai!

---

### Solution 4: Softmax & Categorical Cross-Entropy
1. $e^2 \approx 7.389, e^1 \approx 2.718, e^{0.1} \approx 1.105$. Sum $= 11.212$.
   Probabilities: $\hat{y} = [0.659, 0.242, 0.099]$.
2. $\mathcal{L} = -\log(0.659) \approx 0.4170$.

---

### Solution 5: Softmax Derivative Proof
Quotient rule se prove hota hai ki jab $i=j$ ho toh $\hat{y}_i(1 - \hat{y}_i)$ aur jab $i \ne j$ ho toh $-\hat{y}_i \hat{y}_j$. Kronecker delta se: $\frac{\partial \hat{y}_i}{\partial z_j} = \hat{y}_i(\delta_{ij} - \hat{y}_j)$.

---

### Solution 6: Gradient Descent Step
1. $\hat{y} = (2.5)(1.5) + 0.8 = 4.55$. Error $= 4.0 - 4.55 = -0.55$.
2. Gradients: $\frac{\partial \mathcal{L}}{\partial w} = -(-0.55)(1.5) = 0.825$; $\frac{\partial \mathcal{L}}{\partial b} = 0.55$.
3. Updates: $w_{new} = 2.5 - 0.1(0.825) = 2.4175$; $b_{new} = 0.8 - 0.1(0.55) = 0.745$.

---

### Solution 7: Chain Rule Backpropagation
1. $z = 1.0(3.0) - 1.0 = 2.0 \implies a = 2.0$. Loss $= \frac{1}{2}(5 - 2)^2 = 4.5$.
2. $\frac{\partial \mathcal{L}}{\partial a} = -(5 - 2) = -3$; $\frac{\partial a}{\partial z} = 1$; $\frac{\partial z}{\partial w} = 3$.
3. Chain rule: $\frac{\partial \mathcal{L}}{\partial w} = (-3) \times 1 \times 3 = -9.0$.

---

### Solution 8: Sigmoid Derivative & Vanishing Gradient
Derivative $g(u) = u(1-u)$ ka maximum $u = 0.5$ ($z=0$) par hota hai jo $0.25$ hai. 8 layers me $(0.25)^8 = 1.525 \times 10^{-5}$ ban jata hai, jisse gradient khatam ho jata hai.

---

### Solution 9: Dying ReLU Pathology
$z_{\max} = 0.5(1) - 0.2(0) - 2.0 = -1.5 < 0$. Har input par $z < 0$ hone se derivative hamesha $0$ rehta hai aur weight update kabhi nahi hota.

---

### Solution 10: Leaky ReLU Solution
Leaky ReLU me negative slope $0.01$ hone se derivative $0.01 \ne 0$ rehta hai, jisse weight update hota hai aur neuron wapas active ho jata hai.

---

### Solution 11: Epoch & Iteration Steps
1. Iterations per epoch: $\frac{128,000}{256} = 500$ steps.
2. Total iterations: $500 \times 50 = 25,000$ steps.
3. Time: $25,000 \times 0.12 = 3000\text{ s} = 50\text{ minutes}$.

---

### Solution 12: Mini-batch Gradient Variance
Sample mean ka variance $\text{Var}(\bar{g}) = \frac{\sigma^2}{B}$ hota hai. Batch size 64 hone se variance $64\times$ kam ho jata hai.

---

### Solution 13: Momentum Numerical Step
- $t=1$: $v_1 = 0.2, \theta_1 = 4.99$.
- $t=2$: $v_2 = 0.38, \theta_2 = 4.971$.
- $t=3$: $v_3 = 0.542, \theta_3 = 4.9439$.

---

### Solution 14: RMSProp Step Scaling
$s_{1,A} = 10.0, s_{1,B} = 0.001$. Dono parameters ka effective step size barabar hokar $-0.0316$ ban jata hai.

---

### Solution 15: Full Adam Step
$m_1 = 0.05, v_1 = 0.00025$. Bias-corrected: $\hat{m}_1 = 0.5, \hat{v}_1 = 0.25$.
Updated parameter: $\theta_1 = 1.0 - \frac{0.001}{\sqrt{0.25}}(0.5) = 1.0 - 0.001 = 0.999$.\n