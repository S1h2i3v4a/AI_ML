# 🚀 Lecture 04.13: Class Practice Problems (Part a & b)

## 📌 Executive Summary (Saransh)
Is lecture mein do real-world coding problems solve kiye gaye hain: Common elements dhoondna aur words ki frequency count karna.

---

## 🔬 Deep Technical Concepts

### 1. Problem A: Common Elements
Do lists mein common items dhoondne ke liye dono ko `set` bana kar intersection (`&`) lena sabse fast tarika hai.

### 2. Problem B: Word Frequency
Sentence ke har word ko dictionary ki key banakar uski counting ko update karte hain `dict.get(w, 0) + 1` se.

---

## 💻 Code Example

```python
# Common elements
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
common = set(l1) & set(l2)
print("Common:", list(common))

# Frequency count
text = "apple banana apple orange apple banana"
freq = {}
for w in text.split():
    freq[w] = freq.get(w, 0) + 1
print("Frequencies:", freq)
```
