# Lecture 03.05: Match Case In Python: Structural Pattern Matching (हिंग्लिश)

## 📌 Module Overview
Python 3.10 ka powerful feature: match ... case statements, wildcards (`_`), pattern guards (`if`), aur structural destructuring.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Match Case Kya Hai?
Python 3.10 mein introduce hua `match ... case` C ya Java ke simple `switch` statement se kahi zyada advance hai. Yeh sirf values ko match nahi karta, balki data structure ke internal shape ko bhi inspect aur unpack kar sakta hai.

### 2. Key Components
- `match expression:` Subject jise match karna hai.
- `case pattern:` Pattern jo check karna hai.
- `case _:` Default / Fallback wildcard pattern jo sab kuch catch karta hai.
- Guards `case pattern if condition:` Extra condition lagane ke liye.

### 3. Pattern Evaluation Logic

$$
P_i(s) \land G_i(s)
$$

Pehla match hote hi code execute hota hai aur automatic break ho jata hai (C-style fallthrough nahi hota).

---

## 💻 Python Code Aur Implementation
```python
def process_command(cmd: str) -> str:
    match cmd.strip().lower().split():
        case ["quit"] | ["exit"]:
            return "TERMINATING_ENGINE"
        case ["load", filename]:
            return f"LOADING_FILE: {filename}"
        case ["move", ("left" | "right" | "up" | "down") as direction, steps] if steps.isdigit():
            return f"MOVING_{direction.upper()}_BY_{steps}_UNITS"
        case _:
            return "UNKNOWN_COMMAND"

print(process_command("load dataset.csv"))
print(process_command("move right 5"))
print(process_command("quit"))
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Har operation ki asymptotic execution limits.
- **Space Complexity:** Memory footprint aur call stack activation analysis.
