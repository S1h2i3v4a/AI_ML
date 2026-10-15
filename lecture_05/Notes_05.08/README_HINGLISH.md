# Lecture 05.08: Class Methods (@classmethod): Factory Pattern Aur Cls Binding (हिंग्लिश)

## 📌 Module Overview
`@classmethod` decorator ka use, `cls` parameter binding, class state ko manage karna, aur alternative constructor factories banana.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Class Method Kya Hota Hai?
Class method kisi individual object ke bajaye poori Class se juda hota hai. Iske upar `@classmethod` decorator lagta hai aur pehla parameter `cls` hota hai (jo class object ko refer karta hai).

### 2. Factory Pattern Mein Use
Jab hume alag-alag formats (jaise JSON data, dictionary, ya CSV line) se object instantiate karna ho, toh class methods sabse clean solution provide karte hain.

---

## 💻 Python Code Aur Implementation
```python
class User:
    total_users = 0

    def __init__(self, username: str, role: str):
        self.username = username
        self.role = role
        User.total_users += 1

    @classmethod
    def create_admin(cls, username: str):
        """Factory method to create an admin user."""
        return cls(username, role="ADMINISTRATOR")

    @classmethod
    def get_user_count(cls) -> int:
        return cls.total_users

u1 = User("Alice", "MEMBER")
u2 = User.create_admin("Bob")
print(f"Total Users: {User.get_user_count()} | Bob's Role: {u2.role}")
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Method dispatch $\mathcal{O}(1)$ descriptor lookup time leta hai.
- **Space Complexity:** Memory footprint instance attributes aur class namespace par depend karta hai.
