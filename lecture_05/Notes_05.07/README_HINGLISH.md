# Lecture 05.07: Instance Methods: Self Binding Aur State Mutation (हिंग्लिश)

## 📌 Module Overview
Instance methods ka architecture, `self` binding, object ke state ko mutate karna, aur method chaining.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Instance Method Kya Hota Hai?
Aisa method jo object ke instance attributes ko read ya modify kar sake. Iska pehla parameter hamesha `self` hota hai.

Jab aap `acc.deposit(500)` call karte hain, Python use internally `BankAccount.deposit(acc, 500)` mein convert kar deta hai.

### 2. Method Chaining
Agar method ke aakhiri mein `return self` kar diya jaaye, toh hum ek hi line mein multiple methods chain kar sakte hain: `p.move_x(10).move_y(20)`.

---

## 💻 Python Code Aur Implementation
```python
class Vector2D:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def translate(self, dx: float, dy: float):
        self.x += dx
        self.y += dy
        return self  # Return self for chaining

    def scale(self, factor: float):
        self.x *= factor
        self.y *= factor
        return self

v = Vector2D(1, 2)
v.translate(3, 4).scale(2)  # Method chaining
print(f"Chained Vector Result: ({v.x}, {v.y})")
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Method dispatch $\mathcal{O}(1)$ descriptor lookup time leta hai.
- **Space Complexity:** Memory footprint instance attributes aur class namespace par depend karta hai.
