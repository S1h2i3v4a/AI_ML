# Lecture 05.03: Attributes Aur Methods: State Aur Behavior (हिंग्लिश)

## 📌 Module Overview
Dot notation se attributes aur methods access karna, internal `__dict__` dictionary, aur dynamic attribute management.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Attributes Aur Methods Kya Hain?
- **Attributes:** Variables jo object ke data (state) ko store karte hain (jaise name, age, roll_no).
- **Methods:** Functions jo class ke andar define hote hain aur object ke data par kaam karte hain.

### 2. Internal `__dict__` Mechanics
Python internal level par har object ke attributes ko ek dictionary `obj.__dict__` mein store karta hai. Jab aap `s.marks = 95` likhte hain, toh Python internal dictionary mein key-value pair daal deta hai:

$$
\text{s.marks} \equiv \text{s.\_\_dict\_\_['marks']}
$$

---

## 💻 Python Code Aur Implementation
```python
class Product:
    def set_details(self, name: str, price: float):
        self.name = name
        self.price = price

p = Product()
p.set_details("Laptop", 1200.0)

print("Instance dictionary:", p.__dict__)
print("Has price?", hasattr(p, "price"))
print("Get price safely:", getattr(p, "price", 0.0))
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Method dispatch $\mathcal{O}(1)$ descriptor lookup time leta hai.
- **Space Complexity:** Memory footprint instance attributes aur class namespace par depend karta hai.
