# Lecture 03.14: Python Mein Functions: Syntax, Scope Aur Call Stack (हिंग्लिश)

## 📌 Module Overview
Functions ki definition (`def`), parameters vs arguments, return values, LEGB scoping rule, aur CPython call stack activation frames.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Functions Ka Purpose
Functions reusable code blocks hote hain jo inputs (parameters) lete hain, processing karte hain, aur output (return value) dete hain:

$$
f: \mathcal{A} \to \mathcal{B}
$$

### 2. Call Stack Aur Activation Frames
Jab function call hota hai, CPython memory ke stack section mein ek naya frame (`PyFrameObject`) banata hai jisme function ke local variables rehte hain. Function execute hote hi yeh frame stack se hat (pop) jaata hai.

### 3. LEGB Variable Scoping Rule
Jab Python kisi variable ka naam dhoondhta hai, toh woh is order mein search karta hai:
1. **L**ocal: Function ke andar.
2. **E**nclosing: Bahar wale parent function ke andar (agar nested ho).
3. **G**lobal: Module level par.
4. **B**uilt-in: Python ke internal functions jaise `print`, `len`, `range`.

---

## 💻 Python Code Aur Implementation
```python
def calculate_circle_metrics(radius: float) -> tuple[float, float]:
    """Calculates area and circumference of circle."""
    import math
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = calculate_circle_metrics(5.0)
print(f"Radius 5.0 -> Area: {a:.2f}, Circumference: {c:.2f}")
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Har operation ki asymptotic execution limits.
- **Space Complexity:** Memory footprint aur call stack activation analysis.
