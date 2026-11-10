# Lecture 37 Practice Problems: Neural Network Training (Hinglish)

Yeh problem set 15 high-yield practical aur theoretical sawalon ka sangrah hai jo Backpropagation, Loss functions, Gradient descent, aur Modern optimizers par adharit hain.

---

### Sawal 1: Forward Pass Output Calculation
Ek artificial neuron me inputs $x = [2.0, -1.0, 3.0]$, weights $w = [0.4, -0.6, 0.2]$ aur bias $b = -0.5$ hain. Activation function Sigmoid hai. Linear sum $z$ aur final prediction $\hat{y}$ calculate karo.

### Sawal 2: Regression Loss me Outlier ka Asar
Target $y = 10.0$ hai aur prediction $\hat{y} = 60.0$ (bada outlier) hai:
1. MSE loss penalty nikaalo.
2. MAE loss penalty nikaalo.
3. Huber loss ($\delta = 2.0$) nikaalo aur batao kaunsa loss outlier se bachaata hai.

### Sawal 3: Binary Cross-Entropy Penalty
Sample A ($y = 1, \hat{y} = 0.95$) aur Sample B ($y = 1, \hat{y} = 0.05$) dono ka BCE loss nikaalo aur compare karo.

### Sawal 4: Softmax aur Categorical Cross-Entropy
3-class network ke logits $z = [2.0, 1.0, 0.1]$ hain aur actual class Cat ($y = [1, 0, 0]$) hai. Softmax probabilities aur Categorical CE loss nikaalo.

### Sawal 5: Softmax Derivative ka Proof
Prove karo ki Softmax ka derivative $\frac{\partial \hat{y}_i}{\partial z_j} = \hat{y}_i(\delta_{ij} - \hat{y}_j)$ hota hai.

### Sawal 6: Gradient Descent Step
Weight $w = 2.5$, bias $b = 0.8$, input $x = 1.5$, target $y = 4.0$, aur $\eta = 0.1$ ke liye naye $w_{new}$ aur $b_{new}$ compute karo.

### Sawal 7: Chain Rule se Gradient Calculation
$z = wx + b, a = \text{ReLU}(z), \mathcal{L} = \frac{1}{2}(y-a)^2$ ke liye Chain Rule se $\frac{\partial \mathcal{L}}{\partial w}$ derive karo.

### Sawal 8: Sigmoid Derivative aur Vanishing Gradient Proof
Prove karo ki Sigmoid derivative ka maximum value sirf $0.25$ hota hai aur 8 layers ke baad gradient $(0.25)^8$ kyu ban jata hai.

### Sawal 9: Dying ReLU Problem
Agar $w = [0.5, -0.2], b = -2.0$ ho aur $x_1, x_2 \in [0, 1]$ hon, toh prove karo ki neuron hamesha ke liye dead ho jata hai.

### Sawal 10: Leaky ReLU Solution
Leaky ReLU ($\alpha = 0.01$) lagane se dying ReLU kaise theek hota hai?

### Sawal 11: Epoch, Batch aur Iteration ka Calculation
Dataset me $N = 128,000$ images hain, batch size $B = 256$, aur $E = 50$ epochs hain. Iterations per epoch aur total steps nikaalo.

### Sawal 12: Mini-batch me Gradient Variance ka Formula
Prove karo ki Mini-batch GD me gradient ka variance $\frac{\sigma^2}{B}$ hota hai.

### Sawal 13: Momentum ka Numerical Step
Momentum ($\beta = 0.9, \eta = 0.05$) ke saath 3 time steps ke liye velocity $v_t$ aur parameter $\theta_t$ calculate karo.

### Sawal 14: RMSProp Adaptive Learning Rate
Badi gradient ($g_A = 10.0$) aur chhoti gradient ($g_B = 0.1$) ke liye RMSProp ka effective step nikaal kar prove karo ki updates normalize ho jaate hain.

### Sawal 15: Full Adam Optimizer Step
Adam optimizer ke formula se $t=1, g_1=0.5$ par bias-corrected moments $\hat{m}_1, \hat{v}_1$ aur updated parameter $\theta_1$ nikaalo.\n