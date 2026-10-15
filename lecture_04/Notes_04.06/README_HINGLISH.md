# 🚀 Lecture 04.06: Lists Ke Saath Loops Chalana

## 📌 Executive Summary (Saransh)
List ke sabhi elements par baar-baar koi operation chalane ke liye loops use hote hain. Python mein `for ... in` loop aur List Comprehension sabse zyada popular hain.

---

## 🔬 Deep Technical Concepts

### 1. `enumerate()` aur `zip()`
- `enumerate(list)`: Loop mein element ke sath uska index bhi deta hai.
- `zip(list1, list2)`: Do lists ko ek sath parallel loop karne ke kaam aata hai.

### 2. List Comprehension
Ek line mein list banane ka elegant tarika: `[x**2 for x in nums if x % 2 == 0]`.

---

## 💻 Code Example

```python
fruits = ["apple", "banana", "mango"]

# Index ke sath loop
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")

# Comprehension: sabhi ko capital karna
upper_fruits = [f.upper() for f in fruits]
print("Upper Fruits:", upper_fruits)
```
