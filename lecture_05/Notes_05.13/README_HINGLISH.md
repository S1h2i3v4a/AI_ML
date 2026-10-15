# Lecture 05.13: Inheritance Ke Types Aur C3 Linearization (MRO) (हिंग्लिश)

## 📌 Module Overview
Inheritance ke sabhi prakar (Single, Multiple, Multilevel, Hierarchical, Hybrid), Diamond problem, aur C3 Linearization MRO algorithm.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Types of Inheritance
- **Single Inheritance:** 1 Parent $\to$ 1 Child.
- **Multilevel Inheritance:** Grandparent $\to$ Parent $\to$ Child.
- **Multiple Inheritance:** Do ya zyada Parents $\to$ 1 Child.
- **Hierarchical Inheritance:** 1 Parent $\to$ Multiple Children.

### 2. Diamond Problem Aur MRO (Method Resolution Order)
Agar Class D do classes B aur C se inherit karti hai, aur B aur C dono A se inherit karti hain, toh method dhoondhne ka order kya hoga?
Python **C3 Linearization algorithm** use karta hai jo `Class.mro()` ke dwara monotonic search path nikaal leta hai:

$$
L(D) = [D, B, C, A, \text{object}]
$$

---

## 💻 Python Code Aur Implementation
```python
class Herbivore:
    def feed(self):
        return "Consumes plants & berries"

class Carnivore:
    def hunt(self):
        return "Hunts fish & small mammals"

class Bear(Herbivore, Carnivore):
    """Multiple inheritance: Omnivore entity."""
    pass

b = Bear()
print("Bear Diet:", b.feed(), "|", b.hunt())
print("Bear MRO:", [cls.__name__ for cls in Bear.mro()])
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Method dispatch $\mathcal{O}(1)$ descriptor lookup time leta hai.
- **Space Complexity:** Memory footprint instance attributes aur class namespace par depend karta hai.
