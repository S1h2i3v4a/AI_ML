# Lecture 03.11: Vowel Count (String Traversal & Filtering)

## 📌 Executive Summary
String character stream filtering, vowel set membership testing in O(1) time, and case normalization.

---

## 🔬 Theoretical Foundations & Principles
### 1. Character Stream Membership Problem
Given a string $S = (c_1, c_2, \dots, c_N)$ and vowel set $\mathcal{V} = \{'a', 'e', 'i', 'o', 'u'\}$, compute:

$$
V(S) = \sum_{i=1}^{N} \mathbb{I}_{\mathcal{V}}(\text{lower}(c_i))
$$

### 2. Data Structure Optimization for Membership
Checking `char in "aeiouAEIOU"` scans a 10-character string linearly ($\\mathcal{O}(|\\mathcal{V}|)$). Using a `frozenset` performs hash lookups in $\\mathcal{O}(1)$ time.

---

## 💻 Production Implementation & Code
```python
def count_vowels(text: str) -> dict[str, int]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    counts = {v: 0 for v in vowels}
    for char in text.lower():
        if char in vowels:
            counts[char] += 1
    return counts

sample = "Artificial Intelligence & Deep Learning 2026"
print("Vowel Frequencies:", count_vowels(sample))
```

---

## ⚙️ Algorithmic Complexity & Systems Analysis
- **Time Complexity:** Detailed in respective algorithmic operations.
- **Auxiliary Space:** Memory bounds and CPython frame management.
