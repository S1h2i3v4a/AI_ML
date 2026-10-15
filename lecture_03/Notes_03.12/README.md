# Lecture 03.12: The range() Function

## 📌 Executive Summary
The range immutable sequence type: start, stop, step parameters, lazy evaluation, constant memory O(1), and index slicing.

---

## 🔬 Theoretical Foundations & Principles
### 1. The Immutable Sequence Type `range`
In Python 3, `range` is not a generator or list; it is an immutable sequence type representing arithmetic progressions:

$$
\text{range}(\text{start}, \text{stop}, \text{step}) = \{ \text{start} + i \cdot \text{step} \mid 0 \le i < k \}
$$

Where the number of elements $k$ is:

$$
k = \max\left(0, \left\lceil \frac{\text{stop} - \text{start}}{\text{step}} \right\rceil\right)
$$

### 2. Strict $\mathcal{O}(1)$ Space Footprint
A `range` object stores only three integers: `start`, `stop`, and `step`. Whether generating 10 numbers or 10 billion numbers, its memory footprint remains exactly 48 bytes!

---

## 💻 Production Implementation & Code
```python
import sys

r_small = range(10)
r_huge = range(1_000_000_000)

print("Size of range(10):", sys.getsizeof(r_small), "bytes")
print("Size of range(1 billion):", sys.getsizeof(r_huge), "bytes")
print("Range indexing r_huge[500]:", r_huge[500])
```

---

## ⚙️ Algorithmic Complexity & Systems Analysis
- **Time Complexity:** Detailed in respective algorithmic operations.
- **Auxiliary Space:** Memory bounds and CPython frame management.
