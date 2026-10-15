# Lecture 05.06: Attributes: Class Vs Instance Attributes (हिंग्लिश)

## 📌 Module Overview
Class attributes (shared across all objects) vs Instance attributes (individual to each object), namespace lookup, aur shadowing trap.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Class vs Instance Attributes Ka Farq
- **Class Attribute:** Poori class ke liye single copy hoti hai jo saare objects ke beech share hoti hai (jaise `species = 'Homo Sapiens'`).
- **Instance Attribute:** Har object ka apna individual variable hota hai (jaise `self.name`).

### 2. Shadowing Trap (Sabse Badi Galti)
Agar aap `obj.class_attr = 50` likhte hain, toh class attribute change nahi hota! Balki us object ke andar ek naya instance attribute ban jaata hai jo class attribute ko "shadow" (chupa) deta hai. Class attribute ko mutate karne ke liye hamesha `Class.attr = 50` likhna chahiye.

---

## 💻 Python Code Aur Implementation
```python
class Employee:
    company_name = "AI Corp"  # Class attribute (shared)

    def __init__(self, name: str):
        self.name = name      # Instance attribute (unique)

e1 = Employee("Alice")
e2 = Employee("Bob")

print("Company E1:", e1.company_name)
print("Company E2:", e2.company_name)

# Mutating via class updates all instances
Employee.company_name = "Global AI Inc"
print("Updated E1:", e1.company_name)
print("Updated E2:", e2.company_name)
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Method dispatch $\mathcal{O}(1)$ descriptor lookup time leta hai.
- **Space Complexity:** Memory footprint instance attributes aur class namespace par depend karta hai.
