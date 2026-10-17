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

def benchmark_gini_vs_entropy(n_samples=50000, random_state=42):
    """
    Benchmarks training runtime of Gini Impurity vs Shannon Entropy
    to demonstrate why Gini is Scikit-Learn's default criterion.
    """
    # 1. Generate large synthetic classification dataset
    X, y = make_classification(
        n_samples=n_samples, n_features=20, n_informative=10, random_state=random_state
    )

    # 2. Measure Gini runtime
    t0 = time.time()
    clf_gini = DecisionTreeClassifier(criterion='gini', random_state=random_state)
    clf_gini.fit(X, y)
    gini_time = time.time() - t0

    # 3. Measure Entropy runtime
    t0 = time.time()
    clf_entropy = DecisionTreeClassifier(criterion='entropy', random_state=random_state)
    clf_entropy.fit(X, y)
    entropy_time = time.time() - t0

    results = {
        'gini_time': gini_time,
        'entropy_time': entropy_time,
        'speedup': entropy_time / gini_time
    }
    return results

# --- Function Call & Output ---
res = benchmark_gini_vs_entropy()
print(f"Gini Impurity Fit Time:  {res['gini_time']:.4f}s")
print(f"Shannon Entropy Fit Time: {res['entropy_time']:.4f}s")
print(f"Gini is {res['speedup']:.2f}x faster!")
```

---

## 🔑 Key Takeaways
1. Gini Impurity is faster because it does not compute logarithms.
2. Entropy tends to produce slightly more balanced trees.
3. Scikit-Learn uses Gini by default (`criterion='gini'`).
