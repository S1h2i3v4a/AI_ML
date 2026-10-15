# Lecture 03.09: Break Aur Continue: Loop Control Flow (हिंग्लिश)

## 📌 Module Overview
Loop control statements: break (immediate exit), continue (skip iteration), pass, aur Python ka unique loop-else construct.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Loop Control Keywords
- `break`: Loop ko turant band (terminate) karke bahar nikal deta hai.
- `continue`: Current iteration ko wahin chhodkar agle round par jump kar jaata hai.
- `pass`: Khaali block (placeholder) ke liye use hota hai jaha syntax code maangta hai par hume kuch nahi karna.

### 2. Python Ka Unique `else` On Loops
Python mein `for` aur `while` loop ke saath bhi `else` lag sakta hai! Yeh `else` tabhi execute hota hai jab loop poora complete ho jaye bina kisi `break` statement ke hit hue. Agar loop ke beech mein `break` chal gaya, toh `else` execute nahi hota.

---

## 💻 Python Code Aur Implementation
```python
# Prime search demonstrating loop-else
def is_prime_search(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            break  # Divisor found, break out
    else:
        # Executed ONLY if loop completed without break
        return True
    return False

for num in [2, 7, 9, 13, 25, 29]:
    print(f"Number {num:2d} is Prime? {is_prime_search(num)}")
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Har operation ki asymptotic execution limits.
- **Space Complexity:** Memory footprint aur call stack activation analysis.
