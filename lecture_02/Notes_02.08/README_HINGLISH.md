# 🚀 Lecture 02.08: Assignment Operators

## 📌 Executive Summary (Saransh)
Assignment operators variable mein value store ya update karne ke kaam aate hain. Short-cut compound assignment operators (`+=`, `-=`, etc.) code ko chota aur clean banate hain.

---

## 🔬 Deep Technical Concepts

### 1. Compound Operators
- `x += 5` ka matlab hai `x = x + 5`
- `x -= 3` ka matlab hai `x = x - 3`
- `x *= 2` ka matlab hai `x = x * 2`
- `x /= 4` ka matlab hai `x = x / 4` (result float ban jata hai)
- `x **= 2` ka matlab hai `x = x ** 2`

---

## 💻 Code Example

```python
score = 50
print("Initial Score:", score)

score += 10 # 50 + 10 = 60
print("Bonus add hone ke baad:", score)

score *= 2  # 60 * 2 = 120
print("Double bonus:", score)
```
