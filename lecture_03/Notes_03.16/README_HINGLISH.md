# Lecture 03.16: Types of Functions Aur Parameter Semantics (हिंग्लिश)

## 📌 Module Overview
Functions ke types: Built-in vs User-defined, Positional vs Keyword args, Default parameter mutable trap, aur variadic `*args`, `**kwargs`.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Parameter Passing Modes
- Positional: Arguments jis order mein pass hote hain usi order mein parameters ko milte hain.
- Keyword: Name assign karke pass karna (`func(age=25, name="Bob")`).
- `*args`: Multiple extra positional arguments ko tuple ke form mein accept karna.
- `**kwargs`: Multiple extra keyword arguments ko dictionary ke form mein accept karna.

### 2. The Mutable Default Trap (Common Bug)
Kabhi bhi default value ke roop mein empty list `[]` ya empty dict `{}` na dein! Kyunki default value function definition ke waqt ek hi baar allocate hoti hai, isliye har call mein wahi purani list share hone lagti hai.

---

## 💻 Python Code Aur Implementation
```python
# Variadic function demonstration
def flexible_logger(level: str, *messages: str, **metadata: str) -> None:
    combined = " ".join(messages)
    meta_str = " | ".join(f"{k}={v}" for k, v in metadata.items())
    print(f"[{level.upper()}] {combined} ({meta_str})")

flexible_logger("info", "Server started", "Listening on port 8080", env="production", host="0.0.0.0")
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Har operation ki asymptotic execution limits.
- **Space Complexity:** Memory footprint aur call stack activation analysis.
