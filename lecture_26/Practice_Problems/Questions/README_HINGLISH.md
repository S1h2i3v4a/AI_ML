# Lecture 26: Scratch Implementations — Problem Set (Questions - Hinglish)

Is document mein **Lecture 26: Scratch Implementations of Machine Learning Algorithms** ke saare practice questions detailed bilingual explanation ke saath shamil hain.

---

## Problem 01: Vectorized Batch Gradient Descent Linear Regression (`LinearRegressionGD`)

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek Python class `LinearRegressionGD` design karein jo bina kisi high-level library ke sirf pure NumPy se Linear Regression implement kare.
2. Model parameters (weights $\mathbf{w}$ aur bias $b$) ko zero initialize karein aur har iteration par vectorized predictions calculate karein.
3. Mean Squared Error (MSE) cost function ke analytical gradients ($dw$ aur $db$) derive karke compute karein.
4. Gradient Descent update rule implement karein aur har iteration ka loss track karein.
5. New unseen feature matrix par predictions generate karne ke liye `predict(X)` method provide karein.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation
1. **Class Architecture**: Aapko Scikit-Learn ka `LinearRegression` use nahi karna hai. Aapko khud ki OOP class likhni hai jisme `fit()` aur `predict()` methods hon.
2. **Vectorized Predictions**: Har point par loop chalane ke bajaye pura feature matrix $X \in \mathbb{R}^{m \times d}$ use karke $\hat{\mathbf{y}} = X \mathbf{w} + b$ ek saath calculate karna hai.
3. **Analytical Gradients**: Calculus chain rule ke mutabiq gradients calculate karein:

$$
dw = \nabla_\mathbf{w} J = \frac{1}{m} X^T (\hat{\mathbf{y}} - \mathbf{y})
$$

$$
db = \frac{\partial J}{\partial b} = \frac{1}{m} \sum_{i=1}^m (\hat{y}^{(i)} - y^{(i)})
$$

4. **Parameter Updates**: Har step par weights aur bias ko learning rate $\alpha$ se scale karke update karein: $\mathbf{w} := \mathbf{w} - \alpha \cdot dw$, $b := b - \alpha \cdot db$.
5. **Loss Tracking**: `loss_history` list maintain karein taaki hum plot karke verify kar sakein ki loss monotonically decrease ho raha hai ya nahi.

---

## Problem 02: Analytical Normal Equation with L2 Ridge Regularization (`LinearRegressionRidgeOLS`)

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek `LinearRegressionRidgeOLS` class implement karein jo bina kisi iterative loop ke direct analytical Closed-Form Normal Equation se solve kare.
2. Intercept term ke liye feature matrix $X$ mein first column ones ($1$) ka augment karein.
3. Multicollinearity aur singular matrix crash se bachne ke liye L2 Ridge penalty $\lambda$ integrate karein.
4. Optimal parameter vector $\boldsymbol{\theta} = [b, \mathbf{w}^T]^T$ extract karke `predict()` implement karein.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation
1. **Zero-Iteration Optimization**: Iterative gradient descent ke bajaye matrix calculus se closed-form solution nikalna hai.
2. **Bias Augmentation**: Matrix $X_b = [\mathbf{1}_m, X]$ banta hai taaki bias automatically solve ho sake.
3. **Ridge Regularization Invariant**: Agar $X^T X$ invertible na ho ya features correlated hon, toh standard OLS crash ho jata hai. Isliye L2 penalty add karte hain:

$$
\boldsymbol{\theta} = \left( X_b^T X_b + \lambda I' \right)^{-1} X_b^T \mathbf{y}
$$

Jahan $I'$ identity matrix hai jisme $I'_{0,0} = 0$ hota hai taaki bias penalize na ho.
4. **Parameter Extraction**: $\theta[0]$ bias ban jata hai aur $\theta[1:]$ weights ban jate hain.

---

## Problem 03: Vectorized Logistic Regression with Numerical Safeguards (`LogisticRegressionL2`)

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Binary classification ke liye `LogisticRegressionL2` class build karein.
2. Linear score $z = X\mathbf{w} + b$ ko bounded probability $[0, 1]$ mein convert karne ke liye Sigmoid activation implement karein.
3. Binary Cross-Entropy Loss (Log-Loss) calculate karein aur $\log(0)$ error se bachne ke liye probability clipping apply karein.
4. Vectorized gradient descent update rule implement karein jisme L2 regularization term included ho.
5. Probabilities return karne ke liye `get_probabilities()` aur class labels return karne ke liye `predict(X, threshold=0.5)` implement karein.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation
1. **Probabilistic Classification**: Linear target ke bajaye binary labels $y \in \{0, 1\}$ ke liye model train karna hai.
2. **Sigmoid Function**: Formula $\sigma(z) = \frac{1}{1 + e^{-z}}$ implement karein jo unbounded values ko $(0, 1)$ mein squash karta hai.
3. **Numerical Clipping Safeguard**: Computer float precision mein $\log(0)$ lene par $\text{NaN}$ ya $-\infty$ aa jata hai. Isliye `np.clip(probs, 1e-15, 1 - 1e-15)` use karein.
4. **Gradients**: L2 regularization ke saath weight update formula banta hai:

$$
\nabla_\mathbf{w} J = \frac{1}{m} X^T (\hat{\mathbf{y}} - \mathbf{y}) + \frac{\lambda}{m} \mathbf{w}
$$

5. **Decision Threshold**: Default threshold $0.5$ par predictions discrete integers $0$ ya $1$ return karein.

---

## Problem 04: Multi-Class Softmax Regression from Scratch (`SoftmaxRegression`)

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Binary Logistic Regression ko multi-class classification ($K$ classes) ke liye generalize karein.
2. Matrix dimension $W \in \mathbb{R}^{d \times K}$ aur bias vector $\mathbf{b} \in \mathbb{R}^K$ manage karein.
3. Softmax activation implement karein jisme floating-point overflow se bachne ke liye max-subtraction trick use ki gayi ho.
4. Categorical Cross-Entropy Loss aur uska vectorized gradient compute karein.
5. Test instances ke liye highest probability wali class index `np.argmax()` se predict karein.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation
1. **Multi-Class Expansion**: Jab targets $K > 2$ classes hon (jaise digits 0 se 9 ya iris flowers), tab single Sigmoid ke bajaye Softmax use hota hai.
2. **Logits Matrix**: Har sample ke liye $K$ scores aate hain: $Z = X W + \mathbf{b}^T$.
3. **Numerically Stable Softmax**: Agar $z = 1000$ ho jaye, toh $e^{1000} = \infty$ overflow ho jata hai. Isliye har row se uska maximum subtract karte hain:

$$
P(y=k \mid \mathbf{x}) = \frac{\exp(z_k - \max(\mathbf{z}))}{\sum_{j=1}^K \exp(z_j - \max(\mathbf{z}))}
$$

4. **Categorical Gradient**: One-hot encoded ground truth $Y \in \mathbb{R}^{m \times K}$ ke saath gradient simple rehta hai: $\nabla_W J = \frac{1}{m} X^T (\hat{Y} - Y)$.
5. **Prediction**: `np.argmax(probs, axis=1)` se predicted class label nikalna hai.

---

## Problem 05: Generalized K-Nearest Neighbors with Minkowski Metrics (`KNNClassifierAdvanced`)

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek versatile non-parametric classifier `KNNClassifierAdvanced` implement karein.
2. Multiple distance metrics support karein: Euclidean ($p=2$), Manhattan ($p=1$), aur general Minkowski ($p$).
3. Uniform voting aur Inverse-Distance-Weighted voting dono support karein.
4. Test query points ke $k$ nearest neighbors fast extract karke plurality voting se winner class declare karein.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation
1. **Metric Space Formulation**: KNN kisi equation ko train nahi karta; yeh metric space mein points ke beech ke geometrical distance par rely karta hai.
2. **Minkowski Metric**: General distance formula implement karein:

$$
D_p(\mathbf{x}_1, \mathbf{x}_2) = \left( \sum_{j=1}^d |x_{1j} - x_{2j}|^p \right)^{1/p}
$$

3. **Distance Weighting**: Nazdeek wale points ko zyada vote power dene ke liye weight $w_i = \frac{1}{d_i + 10^{-6}}$ implement karein.
4. **Voting Engine**: `np.bincount` ya dictionary accumulation se majority class decide karein.

---

## Problem 06: K-Nearest Neighbors Continuous Regressor (`KNNRegressor`)

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Discrete labels predict karne ke bajaye continuous target values predict karne ke liye `KNNRegressor` class likhein.
2. Query point ke $k$ nearest training samples identify karein.
3. Neighbors ke actual target values $y$ ka weighted average calculate karein.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation
1. **Continuous Target**: Classification mein voting hoti hai, regression mein average calculate kiya jata hai.
2. **Local Neighborhood Averaging**: Target value predict hoti hai:

$$
\hat{y}(\mathbf{x}) = \frac{\sum_{i \in \mathcal{N}_k(\mathbf{x})} w_i y^{(i)}}{\sum_{i \in \mathcal{N}_k(\mathbf{x})} w_i}
$$

3. **Boundary Smoothing**: Jaise-jaise $k$ badhta hai, predictions local average se global average ki taraf smooth hoti hain.

---

## Problem 07: Mini-Batch & Stochastic Gradient Descent Optimizer Engine (`MiniBatchGDOptimizer`)

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek modular optimizer implement karein jo Batch GD ($B=m$), Stochastic GD ($B=1$), aur Mini-Batch GD ($1 < B < m$) teeno modes mein run ho sake.
2. Har epoch mein data ko randomly shuffle karein taaki biased order prevent ho sake.
3. Har batch par weights aur bias update karein aur loss trajectory compare karein.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation
1. **Batching Modes**:
   - $B=m$: Batch Gradient Descent (Smooth loss curve, lekin slow on large datasets).
   - $B=1$: Stochastic Gradient Descent (Fastest updates, lekin noisy/oscillating path).
   - $B=32$ ya $64$: Mini-Batch Gradient Descent (Modern deep learning standard, balances GPU vectorization and gradient variance).
2. **Random Shuffling**: `np.random.permutation(m)` use karke batches create karein.
3. **Trajectory Comparison**: Teeno methods ke convergence paths ko compare karein.

---

## Problem 08: End-to-End Parity Test Harness vs Scikit-Learn

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Apne scratch models (`LinearRegressionGD`, `LinearRegressionRidgeOLS`, `LogisticRegressionL2`, `KNNClassifierAdvanced`) ko Scikit-Learn ke counterpart models ke saath identical data par compare karein.
2. Parameters aur metrics parity verify karein:
   - Linear Regression weights difference $\|\mathbf{w}_{\text{scratch}} - \mathbf{w}_{\text{sklearn}}\| < 10^{-4}$.
   - Logistic Regression test accuracy parity $> 98\%$.
   - KNN exact classification parity $100\%$.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation
1. **Validation Integrity**: Scratch code ki correctness tabhi prove hoti hai jab Scikit-Learn jaisi industry-standard library ke saath numerical parity achieve ho.
2. **Automated Assertions**: Python `assert` statements use karke statistical aur numerical tolerance verify karein.

---

## Systems Engineering Case Studies

- **Case Study 1**: Loss Surface Geometry, Hessian Condition Number aur Learning Rate Dynamics.
- **Case Study 2**: Curse of Dimensionality aur OLS vs Gradient Descent Computational Complexity Benchmark.
- **Case Study 3**: Metric-Space Geometry, Voronoi Tessellations aur High-Dimensional Distance Concentration.
