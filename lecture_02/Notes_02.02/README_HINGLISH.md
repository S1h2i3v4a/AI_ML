# 🚀 Lecture 02.02: Python Variables aur Memory Architecture

## 📌 Executive Summary (Saransh)
C ya C++ mein variable ek fixed memory dabba hota hai, lekin Python mein variable ek **tag ya label** hota hai jo heap memory mein bane object ki taraf point karta hai.

---

## 🔬 Deep Technical Concepts

### 1. Identifier (Variable Naam) Ke Niyam
1. **Shuruat:** Naam hamesha letter ($a-z, A-Z$) ya underscore (`_`) se shuru hona chahiye.
2. **Numbers:** Shuruat mein number nahi aa sakta (`2name` galat hai, par `name2` sahi hai).
3. **Keywords:** Python ke reserved words jaise `if`, `for`, `class` ko variable ka naam nahi bana sakte.
4. **Case Sensitive:** `age`, `Age`, aur `AGE` teeno alag-alag variables hain.

### 2. Memory Binding
Jab aap likhte hain `a = 10`, toh Python memory mein ek integer object banata hai `10`, aur `a` ko uska address de deta hai.

---

## 💻 Code Example

```python
# Variables define karna
name = "Shradha"
age = 30
is_active = True

print("Student:", name, "| Age:", age)

# Case-sensitivity check
x = 10
X = 20
print("x =", x, "aur X =", X) # Dono alag hain!
```
