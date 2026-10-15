# Lecture 05.15: Polymorphism: Method Overriding Aur Dynamic Dispatch (हिंग्लिश)

## 📌 Module Overview
Method overriding ka concept, runtime dynamic dispatch, base method ko replace karna, aur geometric area calculations.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Method Overriding Kya Hai?
Jab child class mein wahi exact method name define kiya jata hai jo parent class mein tha, toh child class ka method parent class ke method ko override (replace) kar deta hai.

### 2. Dynamic Dispatch Ka Fayda
Aap `shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]` ki list bana kar single loop mein `shape.area()` call kar sakte hain. Python automatically runtime par decide karega ki circle ke liye $\pi r^2$ lagana hai aur rectangle ke liye $w \times h$.

---

## 💻 Python Code Aur Implementation
```python
import math

class Shape:
    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement area()")

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

shapes = [Circle(3.0), Rectangle(4.0, 5.0)]
for s in shapes:
    print(f"Shape: {s.__class__.__name__:<10s} | Area: {s.area():.2f}")
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Method dispatch $\mathcal{O}(1)$ descriptor lookup time leta hai.
- **Space Complexity:** Memory footprint instance attributes aur class namespace par depend karta hai.
