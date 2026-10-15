# Lecture 04: Practice Problems Aur Systems Engineering Suite (हिंग्लिश)

**Lecture 04: Strings, Lists, Tuples, Dictionaries, aur Sets** ke complete practice problem suite mein aapka swagat hai. Yeh suite standard assignment problems ko CPython ke internal memory mechanics aur asymptotic complexity ke saath deeply explain karta hai.

---

## 📂 Suite Ki Directory Sanrachna

```text
Practice_Problems/
├── Questions/
│   ├── README.md               # English Problem Statements (10 Problems + 3 Case Studies)
│   ├── README_HINGLISH.md      # Hinglish Statements with Comprehensive Bullet Explanations
│   ├── questions.ipynb         # Interactive Jupyter Notebook for Testing
│   └── questions.pdf           # Printable PDF Problem Sheet
├── Solutions/
│   ├── README.md               # English Production-Grade Solutions & Mathematical Proofs
│   ├── README_HINGLISH.md      # Hinglish Line-by-Line Breakdown & Complexity Analysis
│   ├── solutions.ipynb         # Fully Executed Solutions Notebook with Live Outputs
│   ├── solutions.pdf           # Printable Master Solution Manual
│   ├── case1_string_concatenation_complexity.png  # 300 DPI String Concatenation Benchmark
│   ├── case2_list_overallocation_geometry.png     # 300 DPI List Dynamic Resize Steps
│   └── case3_hash_table_load_factor_probing.png   # 300 DPI Perturbation Probing Visualizer
├── README.md                   # English Index & Syllabus Mapping
└── README_HINGLISH.md          # Hinglish Suite Overview
```

---

## 🎯 Questions Ka Complete Index

### Bhaag 1: Official Assignment 3 Problems

1. **Problem 1 (Palindrome String Check):** Check karein ki string aage aur peeche dono taraf se barabar hai ya nahi ($s = s[::-1]$).
2. **Problem 2 (Average of Integer List):** Diye gaye integer list ke sabhi elements ka mathematical mean (average) calculate karein.
3. **Problem 3 (Merge and Sort Two Lists):** Do user-provided integer lists ko merge karein aur ascending order mein sort karein.
4. **Problem 4 (Tuple Parity Partition):** Ek integer tuple ko do alag tuples mein baantein — even numbers aur odd numbers.
5. **Problem 5 (Menu-Driven Gradebook):** Dictionary ka use karke student records add, update, search aur display karne ka interactive console program banayein.
6. **Problem 6 (Word to Length Dictionary):** Words ki list se ek aisi dictionary generate karein jisme keys words ho aur values unki lengths ho.
7. **Problem 7 (Whitespace Counter):** Diye gaye string ke andar kul kitne whitespace characters (spaces, tabs, newlines) hain unhe count karein.
8. **Problem 8 (Disjoint Sets Check):** Verify karein ki do lists mein koi bhi common element nahi hai ($S_1 \cap S_2 = \emptyset$).
9. **Problem 9 (Duplicate Detector):** List ke andar duplicates dhoondhe aur identify karein set data structure ka use karke.
10. **Problem 10 (Unique Characters Extractor):** User string se unique characters ka set banayein aur unka total count print karein.

### Bhaag 2: Systems Case Studies

- **Case Study 1:** Python string immutability, interning, aur iterative `+` concatenation ki $\mathcal{O}(N^2)$ quadratic slow-down vs $\mathcal{O}(N)$ `str.join()`.
- **Case Study 2:** CPython `list_resize()` dynamic over-allocation formula, growth geometry ($0, 4, 8, 16, 25, 35, 46, \dots$), aur amortized $\mathcal{O}(1)$ time.
- **Case Study 3:** Hash tables open addressing perturbation probing ($j = (5j + 1 + \text{perturb}) \pmod{2^k}$), collision resolution, aur load factor resize boundary $\alpha = 2/3$.
