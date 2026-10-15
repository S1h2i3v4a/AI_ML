# 🚀 Lecture 04.10: Dictionary Methods & Dynamic Views

## 📌 Executive Architectural Summary
Dictionaries expose view objects (`keys()`, `values()`, `items()`) that reflect dynamic changes to the underlying hash table without copying keys or values into new memory lists.

---

## 🔬 Core Engineering Mechanics

### 1. Core Methods Suite
- `d.get(key, default)`: Retrieves value without raising `KeyError` if absent.
- `d.keys()`: Dynamic dictionary view of keys.
- `d.values()`: Dynamic view of values.
- `d.items()`: Dynamic view of `(key, value)` tuples for iteration.
- `d.update(other)`: Merges another dictionary or iterable of key-value pairs.
- `d.pop(key, default)`: Removes specified key and returns its value.

### 2. Dictionary Comprehensions
$$
\{k: f(k) 	ext{ for } k \in 	ext{iterable}\}
$$

---

## 💻 Production Python Implementation

```python
metrics = {"loss": 0.245, "accuracy": 0.945, "val_loss": 0.310}

# Iterating over items()
for metric_name, val in metrics.items():
    print(f"Metric: {metric_name:<10} = {val:.4f}")

# Dictionary Comprehension: Mapping word to its length
words = ["apple", "banana", "kiwi", "cherry", "mango"]
length_map = {w: len(w) for w in words}
print("
Word Length Map Comprehension:")
print(length_map)
```
