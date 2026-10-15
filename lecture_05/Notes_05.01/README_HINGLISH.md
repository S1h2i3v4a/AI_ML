# Lecture 05.01: Object-Oriented Programming (OOP) Kya Hai? (हिंग्लिश)

## 📌 Module Overview
Procedural programming vs Object-Oriented Programming ka comparison, state aur behavior ka encapsulation, aur real-world systems ka design.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Procedural Programming Vs OOP
Procedural programming (jaise C) mein data aur functions alag-alag hote the. Isse bade software projects mein global variables mess ban jaate the.

Object-Oriented Programming (OOP) mein hum data (attributes) aur unpe kaam karne wale functions (methods) ko ek single unit (**Class / Object**) mein baandh dete hain:

$$
\text{Object} = \text{Data (State)} + \text{Functions (Behavior)}
$$

### 2. OOP Ke Chaar Mukhya Pillars
1. **Encapsulation:** Data ko methods ke saath pack karna aur sensitive data ko protect karna.
2. **Abstraction:** Complex internal working ko chupana aur user ko simple interface dena.
3. **Inheritance:** Ek purani class ki properties ko nayi class mein inherit karke code reuse karna.
4. **Polymorphism:** Ek hi method name ka alag-alag objects ke sath alag behavior show karna.

---

## 💻 Python Code Aur Implementation
```python
# Conceptual contrast: Procedural vs OOP
# Procedural style
car_brand = "Tesla"
car_speed = 0

def accelerate(speed, increment):
    return speed + increment

# OOP style: State and behavior bundled together
class ElectricCar:
    def __init__(self, brand: str):
        self.brand = brand
        self.speed = 0

    def accelerate(self, increment: int) -> None:
        self.speed += increment
        print(f"{self.brand} accelerating to {self.speed} km/h")

my_car = ElectricCar("Tesla")
my_car.accelerate(40)
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Method dispatch $\mathcal{O}(1)$ descriptor lookup time leta hai.
- **Space Complexity:** Memory footprint instance attributes aur class namespace par depend karta hai.
