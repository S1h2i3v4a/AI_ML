# Lecture 05.16: Polymorphism: Duck Typing Aur Dunder Methods (हिंग्लिश)

## 📌 Module Overview
Duck typing ka niyam, dunder methods (`__str__`, `__repr__`, `__add__`, `__len__`), aur custom operator overloading.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Duck Typing Kya Hai?
Python mein object ki class se zyada yeh matter karta hai ki object ke paas required methods hain ya nahi. Agar kisi object ke paas `speak()` method hai, toh Python ko farq nahi padta ki woh `Dog` hai ya `Robot`.

### 2. Dunder Methods Aur Operator Overloading
Python mein mathematical operators (`+`, `-`, `*`) ko custom classes ke sath use karne ke liye special double-underscore methods implement kiye jaate hain:
- `__add__`: `a + b` ko overload karta hai.
- `__str__`: User-friendly string representation deta hai.
- `__repr__`: Official developer representation deta hai.

---

## 💻 Python Code Aur Implementation
```python
class ComplexNumber:
    def __init__(self, real: float, imag: float):
        self.real = real
        self.imag = imag

    def __add__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __repr__(self) -> str:
        return f"ComplexNumber({self.real}, {self.imag})"

    def __str__(self) -> str:
        return f"{self.real} + {self.imag}j"

c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)
c3 = c1 + c2  # Operator overloading via __add__
print("c1 + c2 =", c3)
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Method dispatch $\mathcal{O}(1)$ descriptor lookup time leta hai.
- **Space Complexity:** Memory footprint instance attributes aur class namespace par depend karta hai.
