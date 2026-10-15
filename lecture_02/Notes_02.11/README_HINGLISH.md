# 🚀 Lecture 02.11: Type Conversion aur Type Casting

## 📌 Executive Summary (Saransh)
Data ko ek type se doosre type mein badalna Type Conversion kehlata hai. Yeh do tareeqe se hota hai: Implicit (jo Python khud karta hai) aur Explicit (jo hum code mein karte hain).

---

## 🔬 Deep Technical Concepts

### 1. Implicit Conversion (Automatic)
Jab aap `int` aur `float` ko add karte hain, toh Python precision bachane ke liye answer ko automatically `float` bana deta hai (`5 + 2.0 = 7.0`).

### 2. Explicit Casting (Manual)
Hum functions use karte hain:
- `int("45")` $	o$ integer $45$
- `float(10)` $	o$ decimal $10.0$
- `str(25)` $	o$ string `"25"`
- `bool(1)` $	o$ `True`

---

## 💻 Code Example

```python
# String se number banana
s = "100"
n = int(s)
print(n + 50) # 150

# Float se integer (point ke baad ka data hat jata hai)
val = 15.89
print("Truncated Int:", int(val)) # 15
```
