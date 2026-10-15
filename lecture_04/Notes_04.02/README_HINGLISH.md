# 🚀 Lecture 04.02: String Slicing (Tukde Nikalna)

## 📌 Executive Summary (Saransh)
Slicing ka matlab hai kisi string mein se ek hissa (substring) nikalna. Iska syntax hota hai: `string[start : stop : step]`.

---

## 🔬 Deep Technical Concepts

### 1. Slicing Ke 3 Parameters
- `start`: Kahan se shuru karna hai (inclusive).
- `stop`: Kahan par rukna hai (exclusive, yeh include nahi hota).
- `step`: Kitne steps aage badhna hai (by default $1$).

### 2. Reverse Karne Ka Trick
`s[::-1]` likhne se poori string ulti (reverse) ho jati hai, jo palindrome check karne mein sabse zyada kaam aati hai.

---

## 💻 Code Example

```python
text = "ApnaCollege"

# Starting 4 characters
print("text[0:4] ->", text[0:4]) # 'Apna'

# Reverse string
print("text[::-1] ->", text[::-1])

# Palindrome check
w = "madam"
print(f"'{w}' palindrome hai?", w == w[::-1]) # True
```
