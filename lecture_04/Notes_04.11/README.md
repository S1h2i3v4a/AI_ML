# 🚀 Lecture 04.11: Sets & Mathematical Set Theory Architecture

## 📌 Executive Architectural Summary
A set (`set`) is an **unordered, mutable collection of unique, hashable elements**. Under CPython (`PySetObject`), a set is implemented as a hash table with dummy values, providing $\mathcal{O}(1)$ average-case membership testing ($x \in S$).

---

## 🔬 Core Engineering Mechanics

### 1. Uniqueness & Deduplication Invariant
By definition of a mathematical set:
$$
S = \{x_1, x_2, \dots, x_N\} \quad 	ext{where } x_i 
e x_j \quad orall i 
e j
$$
Passing an iterable containing duplicates into `set()` eliminates all redundant elements in $\mathcal{O}(N)$ time.

### 2. Membership Testing Complexity
- **List Search (`x in list`):** Linear search $\mathcal{O}(N)$.
- **Set Search (`x in set`):** Hash lookup $\mathcal{O}(1)$ average case.

---

## 💻 Production Python Implementation

```python
# 1. Set Creation and Deduplication
raw_ids = [101, 102, 101, 103, 104, 102, 105]
unique_ids = set(raw_ids)
print("Raw List:", raw_ids)
print("Deduplicated Set:", unique_ids)

# 2. O(1) Membership Testing
print(f"Is 103 in set? {103 in unique_ids}")
print(f"Is 999 in set? {999 in unique_ids}")

# Empty set creation (Note: {} creates an empty dict, must use set())
empty_set = set()
print("Empty Set Type:", type(empty_set))
```
