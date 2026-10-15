# 🚀 Lecture 04.12: Set Operations (Union, Intersection)

## 📌 Executive Summary (Saransh)
Sets ke paas math ki tarah Union ($\cup$), Intersection ($\cap$), aur Difference nikalne ke direct operators aur methods hote hain.

---

## 🔬 Deep Technical Concepts

### 1. Char Mukhya Operations
1. **Union (`|`):** Dono sets ke saare elements mila deta hai.
2. **Intersection (`&`):** Sirf common elements nikalta hai.
3. **Difference (`-`):** Pehle set mein jo hai par doosre mein nahi hai.
4. **Disjoint (`isdisjoint`):** Agar dono sets mein kuch bhi common na ho toh `True` deta hai.

---

## 💻 Code Example

```python
a = {1, 2, 3}
b = {3, 4, 5}

print("Union (sab milakar):", a | b)          # {1, 2, 3, 4, 5}
print("Intersection (common):", a & b)         # {3}
print("Difference (a mein par b mein nahi):", a - b) # {1, 2}
```
