# Lecture 28.05: Entropy vs Gini Impurity

## 📌 Topic Overview
Both Entropy and Gini Impurity measure node impurity, but which one should you choose in practice? In this lecture, we compare training speed, mathematical complexity, split behaviour, and Scikit-Learn defaults.

---

## ⚖️ Head-to-Head Comparison Table
The instructor presents the following clear comparison on the slide:

| Scenario / Property | Entropy | Gini Impurity |
| :--- | :--- | :--- |
| **Training Speed** | Slightly slower (due to $\log_2$ calculations) | **Faster computation** (only simple multiplication & squaring) |
| **Split Behaviour** | Produces slightly more **balanced** node partitions | Creates splits quickly, slightly favouring **dominant classes** |
| **Dataset Size** | Well-suited for small, structured datasets | **Efficient for large**, high-dimensional datasets |
| **Sensitivity to Distribution** | More sensitive to subtle probability variations | Less sensitive to tiny probability fluctuations |
| **Library Standard** | Preferred in theoretical formulations (ID3, C4.5) | **Default in Scikit-Learn** (`criterion="gini"`) |

---

## 🎯 Practical Rule of Thumb
As summarized on the blackboard:
- **Small Datasets**: Using **Entropy** is completely fine since log computation overhead is negligible.
- **Large Datasets**: Always prefer **Gini Impurity** because avoiding $\log_2$ saves significant CPU training time!
- **Model Accuracy**: In over 98% of machine learning tasks, both metrics produce virtually identical classification accuracy.

---

## 💻 Python Benchmark: Execution Speed

```python
import time
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier

# Generate a synthetic dataset with 50,000 samples
X, y = make_classification(n_samples=50000, n_features=20, random_state=42)

# Benchmark Gini
start = time.time()
clf_gini = DecisionTreeClassifier(criterion='gini', random_state=42).fit(X, y)
time_gini = time.time() - start

# Benchmark Entropy
start = time.time()
clf_entropy = DecisionTreeClassifier(criterion='entropy', random_state=42).fit(X, y)
time_entropy = time.time() - start

print(f"Gini Training Time:    {time_gini:.4f} seconds")
print(f"Entropy Training Time: {time_entropy:.4f} seconds")
print(f"Gini Speed Advantage:  {((time_entropy - time_gini)/time_entropy)*100:.1f}% faster")
```

---

## 🔑 Key Takeaways
1. Gini Impurity is faster because it does not compute logarithms.
2. Entropy tends to produce slightly more balanced trees.
3. Scikit-Learn uses Gini by default (`criterion='gini'`).
