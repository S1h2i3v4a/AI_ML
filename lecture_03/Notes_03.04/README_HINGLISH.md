# Lecture 03.04: Nesting: Hierarchical Decision Trees (हिंग्लिश)

## 📌 Module Overview
Nested if-else statements, cyclomatic complexity, aur guard clauses ka use karke clean code likhna.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Nested Conditionals Kya Hote Hain?
Jab ek `if` ya `else` ke andar doosra `if-else` block likha jata hai, toh use nesting kehte hain. Yeh hierarchical decisions (jaise country $\to$ state $\to$ city) ke liye use hota hai.

### 2. Cyclomatic Complexity Ka Khatra
Zyada deep nesting code ko padhna aur debug karna mushkil bana deti hai. McCabe cyclomatic complexity:

$$
M = E - N + 2P
$$

Bataata hai ki code mein kitne alag-alag execution paths hain.

### 3. Guard Clauses Ka Best Practice
Deep nesting ke bajaye "Guard Clauses" (Early Return) use karna chahiye: pehle invalid conditions par exit kar jao taaki main code flat aur readable rahe.

---

## 💻 Python Code Aur Implementation
```python
# Poor: Deeply nested pyramid
def verify_access_nested(user, authenticated, active, role):
    if authenticated:
        if active:
            if role == "ADMIN":
                return "FULL_ACCESS"
            else:
                return "LIMITED_ACCESS"
        else:
            return "ACCOUNT_INACTIVE"
    else:
        return "UNAUTHENTICATED"

# Production: Flat Guard Clauses
def verify_access_guarded(user, authenticated, active, role):
    if not authenticated:
        return "UNAUTHENTICATED"
    if not active:
        return "ACCOUNT_INACTIVE"
    if role == "ADMIN":
        return "FULL_ACCESS"
    return "LIMITED_ACCESS"

print("Guarded Access:", verify_access_guarded("Alice", True, True, "ADMIN"))
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Har operation ki asymptotic execution limits.
- **Space Complexity:** Memory footprint aur call stack activation analysis.
