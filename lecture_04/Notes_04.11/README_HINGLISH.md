# 🚀 Lecture 04.11: Python Sets

## 📌 Executive Summary (Saransh)
Set unique elements ka **Unordered** collection hota hai. Isme duplicate elements allowed nahi hote aur data search karna $\mathcal{O}(1)$ speed par hota hai.

---

## 🔬 Deep Technical Concepts

### 1. Duplicates Khatam Karna
Agar aap kisi duplicate elements wali list ko `set()` mein pass kar dein, toh saare duplicates automatically remove ho jate hain.

### 2. Empty Set
Empty set banane ke liye `set()` likhna padta hai, kyunki `{}` likhne se empty dictionary ban jati hai.

---

## 💻 Code Example

```python
# Set banana
s = {1, 2, 2, 3, 4, 4, 5}
print("Set (No duplicates):", s) # {1, 2, 3, 4, 5}

# Fast membership check
print("3 in set?", 3 in s) # True
```
