# 🚀 Lecture 04.04: Python Lists aur Memory Structure

## 📌 Executive Summary (Saransh)
List Python ka sabse versatile data structure hai. Yeh **Ordered** (sequence maintain karta hai), **Mutable** (badla ja sakta hai), aur **Heterogeneous** (alag-alag types ka data ek sath rakh sakta hai).

---

## 🔬 Deep Technical Concepts

### 1. List Memory Mein Kaise Rehti Hai?
Python ki list internally C language ke **pointer array** par based hoti hai. List ke andar direct data nahi hota, balki memory addresses (pointers) store hote hain. Isliye isme int, string, float sab ek sath aa sakte hain.

### 2. Mutability (Badlav)
List ke andar kisi bhi index ki value ko badla ja sakta hai (`my_list[0] = 50`), aur list ka memory address change nahi hota.

---

## 💻 Code Example

```python
# List banana
marks = [95, 82, 74, 91]
print("Pehle Marks:", marks)

# Value badalna (Mutate)
marks[1] = 88
print("Update ke baad:", marks)

# Naya item jodna
marks.append(100)
print("Append ke baad:", marks)
```
