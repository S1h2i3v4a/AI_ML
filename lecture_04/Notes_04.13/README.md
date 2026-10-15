# 🚀 Lecture 04.13: Practice Problems (Part a & b) — Common Elements & Frequencies

## 📌 Executive Architectural Summary
This lecture tackles hands-on algorithmic problems synthesizing lists, sets, and dictionaries: finding common elements across collections using set intersection, and computing word frequencies using dictionary hash tables.

---

## 🔬 Core Engineering Mechanics

### 1. Problem A: Common Elements Extraction
Given two lists $L_1$ and $L_2$, find all elements present in both:
$$
	ext{Common} = 	ext{list}(	ext{set}(L_1) \cap 	ext{set}(L_2))
$$
Time Complexity: $\mathcal{O}(|L_1| + |L_2|)$ compared to naive nested loops $\mathcal{O}(|L_1| 	imes |L_2|)$.

### 2. Problem B: Word Frequency Histogram
Given a corpus string, count the frequency of each unique word using a dictionary accumulator pattern.

---

## 💻 Production Python Implementation

```python
# Part A: Common Elements via Set Intersection
list1 = [1, 2, 2, 3, 4, 5]
list2 = [2, 4, 6, 8]
common = list(set(list1) & set(list2))
print("Common Elements:", sorted(common))

# Part B: Word Frequency Counter
sentence = "python is great and python is fast and python is dynamic"
word_counts = {}
for word in sentence.split():
    word_counts[word] = word_counts.get(word, 0) + 1

print("
Word Frequencies:")
for w, c in word_counts.items():
    print(f"'{w}': {c}")
```
