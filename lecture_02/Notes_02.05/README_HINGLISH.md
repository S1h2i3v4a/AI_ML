# 🚀 Lecture 02.05: PEP 8 Style Guide aur Best Practices

## 📌 Executive Summary (Saransh)
Python mein code ka clean aur readable hona sabse important maana jata hai. **PEP 8** Python ka official style guide hai jo batata hai ki indentation, naming conventions aur spacing kaise honi chahiye.

---

## 🔬 Deep Technical Concepts

### 1. 4-Spaces Indentation
Python mein curly braces `{}` nahi hote, block of code ko represent karne ke liye **4 spaces** ki indentation zaroori hoti hai. Tabs aur spaces ko mix nahi karna chahiye.

### 2. Naming Rules (PEP 8)
- **Variables & Functions:** `snake_case` (jaise `user_name`, `total_price`).
- **Constants:** Capital letters `UPPER_CASE` (jaise `PI = 3.14`).
- **Classes:** `PascalCase` (jaise `StudentProfile`).

---

## 💻 Code Example

```python
# Sahi PEP 8 tarika
user_age = 21
is_authenticated = True

def greet_user(name):
    # 4-space indentation
    message = f"Namaste, {name}!"
    return message

print(greet_user("Shradha"))
```
