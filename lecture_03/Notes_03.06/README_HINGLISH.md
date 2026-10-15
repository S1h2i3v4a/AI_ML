# Lecture 03.06: While Loops: Iteration Aur Termination (हिंग्लिश)

## 📌 Module Overview
While loops ka architecture, loop invariants, state update, aur infinite loop se bachne ke rules.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. While Loop Ka Concept
Jab hume pehle se pata na ho ki loop kitni baar chalega, balki kisi condition ke False hone tak chalana ho, tab hum `while` loop use karte hain.

### 2. Loop Termination Ka Niyam
Har while loop ke andar teen cheezein hona zaroori hain:
1. **Initialization:** Loop shuru hone se pehle counter ya state variable declare karna.
2. **Condition:** Check karna ki kya loop aage badhna chahiye.
3. **Update / Mutation:** Har iteration mein variable ko aage badhana taaki condition kabhi na kabhi False ho sake.

Agar update statement bhool gaye, toh loop **infinite loop** ban jaata hai aur CPU 100% consume hone lagta hai.

---

## 💻 Python Code Aur Implementation
```python
# Monotonic termination example: binary search counter
def countdown_and_sum(n: int) -> int:
    total = 0
    curr = n
    while curr > 0:
        total += curr
        curr -= 1  # Monotonic decrement ensures termination
    return total

print("Sum of 10 down to 1:", countdown_and_sum(10))
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Har operation ki asymptotic execution limits.
- **Space Complexity:** Memory footprint aur call stack activation analysis.
