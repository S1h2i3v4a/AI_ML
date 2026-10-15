# Lecture 03.08: Number N Ka Multiplication Table (हिंग्लिश)

## 📌 Module Overview
Multiplication table generate karna, arithmetic progression formulas, aur formatted output.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Multiplication Table Ka Ganit
Pahada (Multiplication Table) ek arithmetic progression hoti hai jisme common difference $d = N$ hota hai:

$$
a_i = N \times i
$$

### 2. Formatted Table Output
Clean console alignment ke liye f-string width specifiers use kiye jaate hain jaise `{i:>2d}` taaki columns seedhi line mein print ho.

---

## 💻 Python Code Aur Implementation
```python
def print_multiplication_table(n: int, max_multiplier: int = 10) -> None:
    print(f"--- Multiplication Table for N = {n} ---")
    for i in range(1, max_multiplier + 1):
        product = n * i
        print(f"{n:>3d}  x  {i:>2d}  =  {product:>4d}")

print_multiplication_table(7, 10)
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Har operation ki asymptotic execution limits.
- **Space Complexity:** Memory footprint aur call stack activation analysis.
