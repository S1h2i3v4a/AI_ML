# Lecture 05.05: Constructors Ke Types Aur Overloading Simulation (हिंग्लिश)

## 📌 Module Overview
Default vs Parameterized constructors, Python mein direct constructor overloading kyu nahi hoti, aur `@classmethod` se factory constructors banana.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Python Mein Direct Overloading Kyu Nahi Hoti?
Java ya C++ mein ek hi class ke andar alag-alag arguments wale 3 `__init__` banaye ja sakte hain. Lekin Python mein dictionary namespace rule ke mutabiq aakhiri define kiya gaya function pehle wale ko overwrite kar deta hai.

### 2. Constructor Overloading Kaise Simulate Karein?
1. **Default Arguments:** Arguments ko default value `None` dekar optional banao.
2. **Classmethod Factories:** `@classmethod` ka use karke alag-alag formats (jaise JSON ya CSV string) se object construct karne ke factory methods banao.

---

## 💻 Python Code Aur Implementation
```python
class Date:
    # 1. Primary constructor with default parameters
    def __init__(self, year: int, month: int = 1, day: int = 1):
        self.year = year
        self.month = month
        self.day = day

    # 2. Alternative constructor via @classmethod
    @classmethod
    def from_iso_string(cls, date_str: str):
        y, m, d = map(int, date_str.split("-"))
        return cls(y, m, d)

d1 = Date(2026)
d2 = Date(2026, 10, 16)
d3 = Date.from_iso_string("2026-12-25")

print(f"d1: {d1.year}-{d1.month}-{d1.day}")
print(f"d2: {d2.year}-{d2.month}-{d2.day}")
print(f"d3: {d3.year}-{d3.month}-{d3.day}")
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Method dispatch $\mathcal{O}(1)$ descriptor lookup time leta hai.
- **Space Complexity:** Memory footprint instance attributes aur class namespace par depend karta hai.
