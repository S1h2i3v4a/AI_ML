# Lecture 05.02: Classes Aur Objects: Blueprints Aur Instances (हिंग्लिश)

## 📌 Module Overview
Class ek blueprint hoti hai aur Object uska actual runtime memory instance hota hai. Memory allocation aur introspection.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Class Aur Object Ka Rishta
- **Class:** Ek naqsha (blueprint) hoti hai, jaise ghar ka blueprint.
- **Object:** Us blueprint se bana actual physical ghar (instance).

Aap ek single class se hazaron alag-alag objects bana sakte hain, aur har object ki apni alag memory space hoti hai.

### 2. Identity vs Equality (`is` vs `==`)
- `==` check karta hai ki kya dono objects ke andar ki value barabar hai.
- `is` check karta hai ki kya dono variable memory mein exact same heap address (`id()`) par point kar rahe hain:

$$
a \text{ is } b \iff \text{id}(a) == \text{id}(b)
$$

---

## 💻 Python Code Aur Implementation
```python
class Student:
    pass

s1 = Student()
s2 = Student()

print(f"s1 id: {hex(id(s1))}")
print(f"s2 id: {hex(id(s2))}")
print(f"s1 is s2? {s1 is s2}")  # False: Distinct heap objects
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Method dispatch $\mathcal{O}(1)$ descriptor lookup time leta hai.
- **Space Complexity:** Memory footprint instance attributes aur class namespace par depend karta hai.
