# Lecture 03.11: Vowel Count: String Traversal Aur Membership Testing (हिंग्लिश)

## 📌 Module Overview
String ke characters ko traverse karke vowels count karna, case normalization, aur set lookup.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Vowel Counting Problem
Kisi bhi text ke andar vowels ($a, e, i, o, u$) ki sankhya nikalne ke liye hum string ko iterate karte hain aur check karte hain ki character vowel set ka member hai ya nahi:

$$
V(S) = \sum_{i=1}^{N} \mathbb{I}_{\mathcal{V}}(\text{lower}(c_i))
$$

### 2. Hash Set Optimization
String ke bajaye set `{'a', 'e', 'i', 'o', 'u'}` ka use karne se membership check $\mathcal{O}(1)$ average time mein execute hota hai.

---

## 💻 Python Code Aur Implementation
```python
def count_vowels(text: str) -> dict[str, int]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    counts = {v: 0 for v in vowels}
    for char in text.lower():
        if char in vowels:
            counts[char] += 1
    return counts

sample = "Artificial Intelligence & Deep Learning 2026"
print("Vowel Frequencies:", count_vowels(sample))
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Har operation ki asymptotic execution limits.
- **Space Complexity:** Memory footprint aur call stack activation analysis.
