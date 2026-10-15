# Lecture 05.04: Constructor: __init__() Method Ka Lifecycle (हिंग्लिश)

## 📌 Module Overview
Constructor ka role, `__new__` (allocation) aur `__init__` (initialization) ka farq, `self` parameter, aur object creation flow.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Constructor Kya Hota Hai?
Jab bhi class ka naya object banaya jata hai, Python automatically ek special method call karta hai jise constructor kehte hain: `__init__(self)`.

### 2. `__new__` vs `__init__`
- `__new__`: Memory allocate karke raw object banata hai.
- `__init__`: Us bane hue object ke andar attributes ko initial values deta hai.

### 3. `self` Kya Hai?
`self` current instance (jis object par kaam chal raha hai) ka reference hota hai. Iski madad se Python ko pata chalta hai ki kis object ke attributes ko modify karna hai.

---

## 💻 Python Code Aur Implementation
```python
class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self.balance = initial_balance
        print(f"Account created for {self.owner} with ${self.balance:,.2f}")

acc1 = BankAccount("Alice", 1000.0)
acc2 = BankAccount("Bob", 250.0)
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Method dispatch $\mathcal{O}(1)$ descriptor lookup time leta hai.
- **Space Complexity:** Memory footprint instance attributes aur class namespace par depend karta hai.
