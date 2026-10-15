# 🚀 Lecture 02.01: Hamara Pehla Program aur Output Mechanics

## 📌 Executive Summary (Saransh)
Kisi bhi programming language ki shuruat screen par data display karne se hoti hai. Python mein yeh task hum built-in `print()` function ke zariye karte hain. Yeh function internally computer ki memory se data lekar OS console screen par print karta hai.

---

## 🔬 Deep Technical Concepts

### 1. `print()` Function Ka Anatomy
Python mein `print()` ka full signature hota hai:
```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```
- `*objects`: Jo bhi data ya values aap comma dekar pass karte hain, Python unhe string mein convert karke print karta hai.
- `sep`: Multiple values ke beech mein aane wala separator (by default single space `' '`).
- `end`: Sabse aakhri value print hone ke baad aane wala character (by default newline `'\n'`).
- `flush`: Agar `True` ho toh buffer ko bina wait kiye turant screen par bhej deta hai.

### 2. Python Character Set
Python 3 natively **Unicode (UTF-8)** character set follow karta hai:
- **Letters:** Capital $A-Z$ aur Small $a-z$
- **Digits:** $0$ se $9$
- **Special Symbols:** $+$, $-$, $*$, $/$, $\%$, brackets, etc.
- **Escape Characters:** `\n` (nayee line), `\t` (tab space).

---

## 💻 Code Example

```python
# Pehla print statement
print("Hello World!")

# Custom separator aur custom end character ke saath
print("Python", "AI", "ML", sep=" | ", end=" ===> [DONE]\n")

# Math calculations print karna
print("2 + 3 =", 2 + 3)
```
