# 🚀 Lecture 02.12: Taking User Input (input())

## 📌 Executive Summary (Saransh)
User se console par data lene ke liye `input()` function ka use hota hai. Iska sabse zaroori rule yeh hai ki yeh hamesha data ko **String** format mein return karta hai.

---

## 🔬 Deep Technical Concepts

### 1. `input()` Ka Golden Rule
User chahe number type kare ya text, Python use string (`str`) hi samjhega. Agar aapko calculation karni hai, toh aapko use `int()` ya `float()` mein convert (type cast) karna padega.

---

## 💻 Code Example

```python
# Direct string input
name = "Shradha" # input("Enter name: ")

# Number input ke liye type casting
age_str = "21"   # input("Enter age: ")
age = int(age_str)

print(f"Hello {name}, you are {age} years old!")
print(f"Next year you will be {age + 1} years old.")
```
