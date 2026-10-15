# 🚀 Lecture 02.07: Relational (Comparison) Operators

## 📌 Executive Summary (Saransh)
Relational operators do values ko aapas mein compare karne ke liye use hote hain aur result hamesha Boolean (`True` ya `False`) return karte hain.

---

## 🔬 Deep Technical Concepts

### 1. Comparison Operators
- `==`: Barabar hai ya nahi
- `!=`: Barabar nahi hai
- `>`: Bada hai
- `<`: Chota hai
- `>=`: Bada ya barabar hai
- `<=`: Chota ya barabar hai

### 2. Chained Comparisons
Python mein aap math ki tarah seedhe likh sakte hain: `10 < x < 20`, jo internally check karta hai `(10 < x) and (x < 20)`.

---

## 💻 Code Example

```python
a = 10
b = 20

print("a == b:", a == b) # False
print("a != b:", a != b) # True
print("a < b:", a < b)   # True

# Chained comparison
age = 22
print("Eligible (18 <= age < 60):", 18 <= age < 60) # True
```
