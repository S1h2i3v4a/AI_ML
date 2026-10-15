# Lecture 05.11: Encapsulation: Access Modifiers Aur Property Getters/Setters (हिंग्लिश)

## 📌 Module Overview
Encapsulation ka concept, public, protected (`_`), private (`__`), CPython name mangling, aur `@property` getters/setters.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Python Mein Access Modifiers
- **Public (`name`):** Kahin se bhi access ho sakta hai.
- **Protected (`_name`):** Ek underscore indicate karta hai ki yeh internal use ke liye hai (sirf convention hai, Python block nahi karta).
- **Private (`__name`):** Do underscores lagane par Python **Name Mangling** trigger kar deta hai.

### 2. Name Mangling Kya Hai?
Jab aap `self.__marks` likhte hain, toh Python internal level par uska naam badalkar `_Student__marks` kar deta hai taaki subclass accidental overwrite na kare.

### 3. Property Decorators (`@property`)
Getters aur Setters likhne ke liye Python `@property` deta hai jisse validation lag jaati hai aur syntax clean `s.marks = 80` rehta hai.

---

## 💻 Python Code Aur Implementation
```python
class Student:
    def __init__(self, name: str, roll_no: int, marks: float):
        self._name = name
        self._roll_no = roll_no
        self._marks = marks

    @property
    def marks(self) -> float:
        return self._marks

    @marks.setter
    def marks(self, value: float) -> None:
        if value < 0:
            raise ValueError(f"Marks cannot be negative, received {value}")
        self._marks = value

s = Student("Alice", 10, 85.0)
s.marks = 92.5  # Invokes setter
print(f"Student: {s._name} | Marks: {s.marks}")
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Method dispatch $\mathcal{O}(1)$ descriptor lookup time leta hai.
- **Space Complexity:** Memory footprint instance attributes aur class namespace par depend karta hai.
