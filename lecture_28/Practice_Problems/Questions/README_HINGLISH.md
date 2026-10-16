# Lecture 28: Practice Problems Suite (Questions - Hinglish)
## Supervised Machine Learning (Part 4) — Decision Trees

Yeh assignment set Decision Trees ke core impurity metrics (Entropy, Gini), threshold optimization, pruning regularizers, aur ShopSmart e-commerce purchase prediction par focused hai.

---
## Problem 01: Pure NumPy Shannon Entropy Calculator

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Pure NumPy use karke multi-class labels ke liye Shannon Entropy calculator class banayein.
2. Mathematical formula $H(S) = -\sum_{k=1}^K p_k \log_2(p_k)$ implement karein.
3. Zero probability limit condition $0 \log_2(0) \equiv 0$ ko numerically safe banayein.
4. Pure node par $H = 0.0$ aur 50-50 binary mixture par $H = 1.0$ bit assert karein.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**Formula Formulation**: Target array $y$ ke unique classes aur counts nikaal kar empirical class probabilities $p_k = N_k / N$ compute karein.

**Numerical Stability**: Log of zero mathematically undefined hota hai. Isliye zero probabilities ko filter out karein ya $\epsilon = 10^{-15}$ add karein.

**Base-2 Logarithm**: Base 2 logarithm se output Shannon 'bits' of information mein express hota hai.

**Integrity Assertions**: Unit tests mein perfectly pure array aur uniform distribution pass karke theoretical bounds verify karein.

---
## Problem 02: Pure NumPy Gini Impurity aur Weighted Split Evaluator

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Multi-class labels ke liye Gini Impurity formula $G(S) = 1 - \sum_{k=1}^K p_k^2$ implement karein.
2. Candidate split ke liye weighted child impurity calculate karein: $G(S, A) = \frac{|S_L|}{|S|} G(S_L) + \frac{|S_R|}{|S|} G(S_R)$.
3. Gini-based Information Gain define karein: $\Delta G = G(S) - G(S, A)$.
4. Pure node par $G = 0.0$ aur binary 50-50 mix par $G = 0.50$ assert verify karein.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**Gini Impurity Formula**: $1 - \sum p_k^2$ probability of misclassification measure karta hai.

**Split Evaluation**: Left child aur right child ke sample sizes ke proportional weights lagakar child impurity aggregate karein.

**Gain Metric**: $\Delta G$ measure karta hai ki split se disorder kitna kam hua.

**Verification**: Pure split par $\Delta G$ maximum aana chahiye.

---
## Problem 03: Continuous Feature Split Finder aur Threshold Optimizer

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Continuous numerical feature array aur class labels accept karne wala `ContinuousSplitFinder` construct karein.
2. Unique values ko sort karke adjacent values ke midpoints $\theta_i = \frac{x_i + x_{i+1}}{2}$ generate karein.
3. Har candidate threshold par binary split evaluate karke maximum Gini Gain locate karein.
4. Optimal split threshold $\theta^*$ aur peak Gini Gain return karein.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**Continuous Thresholding**: Continuous feature par infinite points nahi balki observed data points ke midpoints hi test karne hote hain.

**Search Protocol**: Sorted unique values $x_{(1)} < x_{(2)} < \dots < x_{(u)}$ ke beech $u-1$ split cutoffs test karein.

**Impurity Optimization**: Har cutoff $\theta$ ke liye $x \le \theta$ (Left) aur $x > \theta$ (Right) subsets banayein aur gain calculate karein.

**Output Contract**: Best threshold aur corresponding best gain score return ho.

---
## Problem 04: C4.5 Information Gain Ratio Optimizer

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. High-cardinality feature bias ko penalize karne wala `GainRatioOptimizer` implement karein.
2. Split Information formula $SplitInfo(S, A) = -\sum \frac{|S_v|}{|S|} \log_2 \frac{|S_v|}{|S|}$ calculate karein.
3. Information Gain Ratio $GainRatio = \frac{IG}{SplitInfo}$ compute karein.
4. Prove karein ki Gain Ratio unique IDs wale useless features ko reject karta hai.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**High-Cardinality Flaw**: Agar feature me har row ka unique ID ho, toh standard Information Gain use highest rank de deta hai jo severe overfitting hai.

**Split Information Regularizer**: Split Information split ke branches ki entropy measure karti hai. Zyada uniform chote branches hone par SplitInfo bohot high ho jaata hai.

**Gain Ratio Normalization**: $IG / SplitInfo$ ratio branching complexity ko control mein rakhta hai.

**Numerical Protection**: Division by zero prevent karne ke liye $\epsilon = 10^{-10}$ add karein.

---
## Problem 05: Regression Tree Variance Reduction Split Evaluator

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Continuous regression targets ke liye `VarianceReductionSplitter` implement karein.
2. Sample Variance formula $I_{\text{MSE}}(S) = \frac{1}{|S|} \sum (y_i - \bar{y})^2$ calculate karein.
3. Variance Reduction $\Delta V = \text{Var}(S) - [\frac{|S_L|}{|S|} \text{Var}(S_L) + \frac{|S_R|}{|S|} \text{Var}(S_R)]$ evaluate karein.
4. Bivariate continuous dataset par optimal regression split cutoff determine karein.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**Continuous Node Impurity**: Regression trees mein Gini ya Entropy ke bajaye target values ka sample variance impurity metric banta hai.

**Variance Reduction Criterion**: Split aisa hona chahiye jo children subsets ki overall variance ko maximum drop kare.

**Leaf Mean Estimation**: Child nodes apne respective target sample mean $\bar{y}_L$ aur $\bar{y}_R$ predict karte hain.

**Verification**: Numerical test par highest variance drop assert karein.

---
## Problem 06: Minimal Cost-Complexity Pruning Path Analyzer

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Scikit-Learn DecisionTreeClassifier se Cost Complexity Pruning path analyze karne wala tool develop karein.
2. `clf.cost_complexity_pruning_path(X, y)` se `ccp_alphas` aur `impurities` extract karein.
3. Har candidate alpha par tree fit karke total node count aur leaf count inspect karein.
4. Demonstrate karein ki alpha badhne par tree structure monotonically shrink hota hai.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**Breiman Cost-Complexity**: $R_\alpha(T) = R(T) + \alpha |T|$ mein $\alpha$ badhane se complex subtrees prune hote hain.

**Alpha Spectrum Extraction**: Scikit-Learn `cost_complexity_pruning_path` finite critical points calculate karta hai.

**Monotonic Shrinkage**: Assert karein ki agar $\alpha_2 > \alpha_1$ ho toh $|T(\alpha_2)| \le |T(\alpha_1)|$.

**Pruning Range**: Maximum alpha par poori tree single root node ban jaati hai.

---
## Problem 07: Automated Pre-Pruning Cross-Validation Optimizer

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Hyperparameter grid search evaluate karne wala `PrePruningGridSearchOptimizer` build karein.
2. Search space mein `max_depth`, `min_samples_split`, aur `min_samples_leaf` encompass karein.
3. Stratified K-Fold cross validation se imbalanced F1 metric optimize karein.
4. Best estimator extract karke test set par generalization score verify karein.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**Hyperparameter Surface**: Trees mein depth aur leaf constraints non-linearly interact karte hain. Exhaustive grid search optimal combination find karta hai.

**Stratified CV**: Imbalanced classification mein har fold mein class proportions preserve hona mandatory hai.

**F1 Optimization**: Accuracy ke bajaye `scoring='f1_macro'` use karein taaki minority class ignore na ho.

**Generalization Safeguards**: Training score aur test score ka difference evaluate karke overfitting check karein.

---
## Problem 08: ShopSmart E-Commerce Purchase Predictor Pipeline (F1 > 0.55)

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Official assignment dataset `shop_smart_ecommerce.csv` (12,330 sessions) par production pipeline design karein.
2. `ColumnTransformer` se continuous numerical standardization aur categorical OneHotEncoding implement karein.
3. Pruned `DecisionTreeClassifier` configure karein jo imbalanced target `Revenue` handle kare.
4. Holdout test set par official course benchmark **F1-Score > 0.55** exceed karein.

---

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

**Real-World E-Commerce Benchmark**: ShopSmart company online browsing sessions se purchase probability predict karna chahti hai.

**Imbalanced Class Target**: Majority sessions (84%) mein purchase nahi hota (`Revenue = False`). Sirf 16% purchase karte hain. Isliye F1 score critical metric hai.

**Clean Preprocessing Pipeline**: Numerical attributes (`PageValues`, `BounceRates`, `ExitRates`, etc.) aur categorical attributes (`Month`, `VisitorType`, `Weekend`) ko composite transformer me wrap karein.

**Benchmark Achievement**: Unpruned tree F1 0.45-0.50 par fail hoti hai. Pruning lagakar model ko 0.55+ benchmark surpass karwayein.

---
