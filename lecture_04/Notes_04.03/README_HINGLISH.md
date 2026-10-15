# 🚀 Lecture 04.03: String Formatting (f-strings)

## 📌 Executive Summary (Saransh)
String ke andar variables ki value inject karne ke liye **f-strings** Python ka sabse powerful aur fast tareeqa hai.

---

## 🔬 Deep Technical Concepts

### 1. F-Strings Ka Upyog
String ke aage `f` lagakar curly braces `{}` ke andar direct variable ya math calculations likhe ja sakte hain: `f"Name: {name}"`.

### 2. Decimal Precision aur Spacing
- `{val:.2f}`: Decimal ke baad sirf 2 digits print karega.
- `{val:,}`: Badi numbers mein commas lagayega (jaise `1,000,000`).

---

## 💻 Code Example

```python
student = "Aman"
marks = 85.6789

# 2 decimal places tak print karna
print(f"Student: {student}, Marks: {marks:.2f}")

# Calculation inside f-string
print(f"Marks + Grace: {marks + 5:.2f}")
```
