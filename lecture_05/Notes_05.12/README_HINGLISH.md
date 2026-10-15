# Lecture 05.12: Inheritance: Code Reuse Aur Super() Delegation (हिंग्लिश)

## 📌 Module Overview
Base class aur Derived class, IS-A relationship, code reusability, `super()` proxy object, aur constructor chaining.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Inheritance Ka Purpose
Inheritance ka matlab hai nayi class banana jo purani class ke attributes aur methods ko reuse kare.
Jaise: `Car` IS-A `Vehicle`. `Vehicle` base class hai aur `Car` derived class hai.

### 2. `super()` Ka Role
Jab derived class apna naya `__init__` banati hai, toh pehle parent class ke constructor ko chalana zaroori hota hai. Iske liye hum `super().__init__(...)` call karte hain.

---

## 💻 Python Code Aur Implementation
```python
class Vehicle:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def describe(self) -> str:
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand: str, model: str, seats: int):
        super().__init__(brand, model)
        self.seats = seats

    def describe(self) -> str:
        return f"{super().describe()} (Seats: {self.seats})"

c = Car("Toyota", "Camry", 5)
print(c.describe())
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Method dispatch $\mathcal{O}(1)$ descriptor lookup time leta hai.
- **Space Complexity:** Memory footprint instance attributes aur class namespace par depend karta hai.
