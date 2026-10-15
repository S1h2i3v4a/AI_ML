# Lecture 05.14: Abstraction: Abstract Base Classes (abc) Aur Interfaces (हिंग्लिश)

## 📌 Module Overview
Python mein Abstraction: `abc` module, `ABC` base class, `@abstractmethod` decorator, aur architectural contracts enforce karna.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Abstraction Ka Concept
Abstraction ka matlab hai complex details ko chupa kar sirf zaroori interface define karna.
Jaise ek `Employee` class declare karti hai ki har employee ka `calculate_salary()` hona chahiye, lekin salary kaise niklegi yeh har subclass (`Intern`, `FullTimeEmployee`) khud implement karegi.

### 2. `abc` Module Aur `@abstractmethod`
Python mein abstraction enforce karne ke liye `from abc import ABC, abstractmethod` use hota hai. Agar koi subclass abstract method ko implement nahi karegi, toh Python uska object hi nahi banne dega (compile-time safety).

---

## 💻 Python Code Aur Implementation
```python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def calculate_salary(self) -> float:
        pass

class Intern(Employee):
    def calculate_salary(self) -> float:
        return 15000.0  # Fixed stipend

class FullTimeEmployee(Employee):
    def __init__(self, name: str, base_salary: float, bonus: float):
        super().__init__(name)
        self.base = base_salary
        self.bonus = bonus

    def calculate_salary(self) -> float:
        return self.base + self.bonus

intern = Intern("Charlie")
fte = FullTimeEmployee("Dana", 80000.0, 15000.0)
print(f"{intern.name} Salary: ${intern.calculate_salary():,.2f}")
print(f"{fte.name} Salary: ${fte.calculate_salary():,.2f}")
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Method dispatch $\mathcal{O}(1)$ descriptor lookup time leta hai.
- **Space Complexity:** Memory footprint instance attributes aur class namespace par depend karta hai.
