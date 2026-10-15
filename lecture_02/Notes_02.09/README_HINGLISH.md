# 🚀 Lecture 02.09: Logical Operators

## 📌 Executive Summary (Saransh)
Logical operators (`and`, `or`, `not`) conditions ko aapas mein jodne ke liye use hote hain. Python short-circuit evaluation follow karta hai jisse unnecessary calculations bach jati hain.

---

## 🔬 Deep Technical Concepts

### 1. The Three Operators
1. **`and`:** Agar dono conditions `True` hain, tabhi `True` aayega.
2. **`or`:** Agar koi bhi ek condition `True` hai, toh `True` aayega.
3. **`not`:** Ulta kar deta hai (`True` ko `False`, `False` ko `True`).

### 2. Short-Circuit Evaluation
- `A and B`: Agar pehla part hi `False` hai, toh Python doosre part ko check hi nahi karta.
- `A or B`: Agar pehla part hi `True` hai, toh Python doosre part ko check hi nahi karta.

---

## 💻 Code Example

```python
age = 20
has_license = True

# Dono true hone chahiye
can_drive = (age >= 18) and has_license
print("Can Drive:", can_drive)

# Short circuit example
x = 0
# 10 / x error deta agar evaluate hota, par x != 0 False hone se short circuit ho gaya
safe = (x != 0) and (10 / x > 1)
print("Safe Check:", safe)
```
