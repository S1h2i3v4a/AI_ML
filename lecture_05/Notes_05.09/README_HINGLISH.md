# Lecture 05.09: Static Methods (@staticmethod): Decoupled Utility Routines (हिंग्लिश)

## 📌 Module Overview
`@staticmethod` decorator ka upyog, utility functions jo na instance ko access karte hain aur na class ko, aur teeno method types ka comparison.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Static Method Kya Hota Hai?
Static method ek normal helper function hota hai jise class ke andar organize karke rakha jata hai. Iske paas na `self` hota hai aur na `cls`. Yeh object ya class ke kisi attribute ko modify nahi karta.

### 2. Teeno Methods Ka Comparison
- **Instance Method (`self`):** Jab object ke data ko badalna ya padhna ho.
- **Class Method (`cls`):** Jab class-level data ya factory constructors banane ho.
- **Static Method (None):** Jab pure utility ya mathematical calculation karni ho jo bahar ke kisi state par depend na karti ho.

---

## 💻 Python Code Aur Implementation
```python
class SecurityValidator:
    MIN_PASSWORD_LENGTH = 8

    @staticmethod
    def is_valid_password(pwd: str) -> bool:
        has_min_len = len(pwd) >= SecurityValidator.MIN_PASSWORD_LENGTH
        has_upper = any(c.isupper() for c in pwd)
        has_digit = any(c.isdigit() for c in pwd)
        return has_min_len and has_upper and has_digit

print("Password 'Secret123':", SecurityValidator.is_valid_password("Secret123"))
print("Password 'weak':", SecurityValidator.is_valid_password("weak"))
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Method dispatch $\mathcal{O}(1)$ descriptor lookup time leta hai.
- **Space Complexity:** Memory footprint instance attributes aur class namespace par depend karta hai.
