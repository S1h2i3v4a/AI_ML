# 🚀 Lecture 04.05: List Ke Important Methods

## 📌 Executive Summary (Saransh)
List par kaam karne ke liye Python bahut saare built-in methods deta hai jo list ko modify karte hain.

---

## 🔬 Deep Technical Concepts

### 1. Most Used Methods
- `append(x)`: Aakhri mein ek item jodta hai ($O(1)$ time).
- `insert(idx, x)`: Kisi specific index par item insert karta hai.
- `pop()`: Aakhri item ko nikalta hai aur return karta hai.
- `remove(x)`: Pehle match hone wale element ko delete karta hai.
- `sort()`: Elements ko ascending order mein sort karta hai ($O(N \log N)$).
- `reverse()`: List ko ulta kar deta hai.

---

## 💻 Code Example

```python
numbers = [25, 10, 45, 5]

# Sort karna
numbers.sort()
print("Sorted:", numbers) # [5, 10, 25, 45]

# Append aur Pop
numbers.append(60)
print("Append ke baad:", numbers)

last = numbers.pop()
print("Popped item:", last)
```
