# 🚀 Lecture 02.10: Operator Precedence (Prathmikta)

## 📌 Executive Summary (Saransh)
Jab ek hi line mein multiple operators aa jate hain, toh kaun pehle solve hoga yeh **Operator Precedence** decide karta hai (jaise school mein BODMAS rule hota tha).

---

## 🔬 Deep Technical Concepts

### 1. Priority Order
1. `()`: Brackets sabse pehle solve hote hain.
2. `**`: Power doosre number par.
3. `*`, `/`, `//`, `%`: Multiplication aur division teesre number par.
4. `+`, `-`: Addition aur subtraction uske baad.
5. Comparisons: `<`, `>`, `==`.
6. Logical: `not`, `and`, `or`.

---

## 💻 Code Example

```python
# Step-by-step solve
res = 10 + 3 * 2 ** 2
# 1. 2 ** 2 = 4
# 2. 3 * 4 = 12
# 3. 10 + 12 = 22
print("Result:", res)

# Brackets use karke order badalna
res2 = (10 + 3) * 4
print("Bracketed Result:", res2) # 52
```
