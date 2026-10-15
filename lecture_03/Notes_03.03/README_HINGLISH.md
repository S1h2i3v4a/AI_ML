# Lecture 03.03: Odd Ya Even: Parity Checking Ka Logic (हिंग्लिश)

## 📌 Module Overview
Number even hai ya odd, iska mathematical aur bitwise hardware analysis.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Parity Ki Paribhasha
Kisi bhi integer $x$ ke liye parity test define hota hai:

$$
x \pmod 2 = 0 \iff x \text{ is Even}
$$

Agar $x \pmod 2 \neq 0$ hai, toh number Odd hota hai.

### 2. Modulo vs Bitwise AND (`& 1`)
Modulo operator division circuitry use karta hai, jabki bitwise AND `(x & 1)` direct binary bits par operate karta hai. Har even number ka last binary bit hamesha $0$ hota hai aur odd number ka $1$ hota hai. Isliye bitwise check hardware level par ultra-fast hota hai.

---

## 💻 Python Code Aur Implementation
```python
def check_parity_modulo(n: int) -> str:
    return "Even" if n % 2 == 0 else "Odd"

def check_parity_bitwise(n: int) -> str:
    return "Even" if (n & 1) == 0 else "Odd"

for val in [0, 14, 27, -8, -13]:
    print(f"Number: {val:4d} | Modulo: {check_parity_modulo(val):4s} | Bitwise: {check_parity_bitwise(val):4s}")
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Har operation ki asymptotic execution limits.
- **Space Complexity:** Memory footprint aur call stack activation analysis.
