# Lecture 04: Assignment 3 Master Solutions Aur Systems Manual (हिंग्लish)

Is document mein **Lecture 04: Strings, Lists, Tuples, Dictionaries, aur Sets** ke Assignment 3 ke sabhi 10 questions aur 3 systems engineering case studies ka line-by-line solution aur deep technical breakdown diya gaya hai.

Har solution ke andar do vishesh sections include kiye gaye hain:
1. `### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?` (Numbered bullet points)
2. `### 🔍 Har Ek Bullet Point Ka Detailed Explanation` (Deep algorithmic aur memory-level explanation)

---

## 📋 Table of Contents

- [Solution 01: Palindrome String Check](#solution-01-palindrome-string-check)
- [Solution 02: Integer List Ka Arithmetic Average](#solution-02-integer-list-ka-arithmetic-average)
- [Solution 03: Do Integer Lists Ko Merge Aur Sort Karna](#solution-03-do-integer-lists-ko-merge-aur-sort-karna)
- [Solution 04: Tuple Parity Partitioning](#solution-04-tuple-parity-partitioning)
- [Solution 05: Menu-Driven Student Gradebook Hash Table](#solution-05-menu-driven-student-gradebook-hash-table)
- [Solution 06: Lexical Word-Length Mapping](#solution-06-lexical-word-length-mapping)
- [Solution 07: Whitespace Character Counter](#solution-07-whitespace-character-counter)
- [Solution 08: Disjoint Set Verification](#solution-08-disjoint-set-verification)
- [Solution 09: Sequence Duplicate Detector](#solution-09-sequence-duplicate-detector)
- [Solution 10: Unique Character Extraction Aur Count](#solution-10-unique-character-extraction-aur-count)
- [Systems Case Study 1: String Immutability Aur Buffer Concatenation Complexity](#systems-case-study-1-string-immutability-aur-buffer-concatenation-complexity)
- [Systems Case Study 2: Dynamic Array Growth Geometry Aur List Amortized Complexity](#systems-case-study-2-dynamic-array-growth-geometry-aur-list-amortized-complexity)
- [Systems Case Study 3: CPython Hash Table Architecture Aur Perturbation Probing](#systems-case-study-3-cpython-hash-table-architecture-aur-perturbation-probing)

---

## Solution 01: Palindrome String Check

### Python Source Code

```python
def check_palindrome_slice(s: str) -> bool:
    """Slicing method: O(N) Time, O(N) Space"""
    return s == s[::-1]

def check_palindrome_two_pointers(s: str) -> bool:
    """Two-pointer method: O(N) Time, O(1) Aux Space"""
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Demonstration
if __name__ == "__main__":
    user_str = "radar"
    if check_palindrome_two_pointers(user_str):
        print(f"The string '{user_str}' is a Palindrome.")
    else:
        print(f"The string '{user_str}' is NOT a Palindrome.")
```

### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Humne do alag-alag algorithms implement kiye hain: Slicing (`s[::-1]`) aur Two-Pointer scan.
2. Two-pointer method mein `left = 0` aur `right = len(s) - 1` set karke string ke dono kinaro se center ki taraf convergence perform kiya hai.
3. Jab tak `left < right` hai, har step par check kiya hai ki kya `s[left] == s[right]` hai; agar ek bhi mismatched character mila toh seedhe `False` return kiya hai.
4. Loop poora complete hone par `True` return kiya hai aur formatted console message print kiya hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Slicing vs Two-Pointer Strategy
Slicing `s[::-1]` likhne mein bahut aasan hai aur CPython internal C loop mein fast execute hota hai, lekin yeh pure string ka ek naya reversed copy allocate karta hai jiski vajah se $\mathcal{O}(N)$ additional memory lagti hai. Production systems aur large text processing ke liye Two-pointer technique superior hoti hai kyunki yeh bina kisi naye string object ko create kiye $\mathcal{O}(1)$ auxiliary space mein execution karti hai.

#### 2. Two-Pointer Pointers Initialization
`left` pointer string ke start index $0$ par point karta hai aur `right` pointer last index $N - 1$ par point karta hai. Yeh pointers mirror reflection line ke symmetric indices represent karte hain.

#### 3. Character Matching Loop
Loop ke har iteration mein:
- `s[left]` aur `s[right]` ko direct compare kiya jata hai.
- Agar mismatch mila, toh execution immediately terminate ho jaata hai (early exit optimization).
- Agar match hua, toh `left += 1` karke pointer aage badhta hai aur `right -= 1` karke pointer peeche aata hai.

#### 4. Asymptotic Bounds
Time complexity dono algorithms ki linear hoti hai:

$$
T(N) = \mathcal{O}(N)
$$

Lekin Two-pointer approach strict constant space guarantee karti hai:

$$
S_{\text{twopointer}}(N) = \mathcal{O}(1)
$$

---

## Solution 02: Integer List Ka Arithmetic Average

### Python Source Code

```python
from typing import List, Optional

def calculate_list_average(nums: List[int]) -> Optional[float]:
    """Calculates arithmetic mean with ZeroDivisionError guard."""
    if not nums:
        return None
    return sum(nums) / len(nums)

# Demonstration
if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    avg = calculate_list_average(data)
    if avg is not None:
        print(f"List: {data}")
        print(f"Calculated Average: {avg:.2f}")
    else:
        print("List is empty! Cannot compute average.")
```

### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Guard condition `if not nums:` implement ki hai taaki empty list aane par program `ZeroDivisionError` se crash na ho.
2. Built-in `sum(nums)` ka upyog karke list ke sabhi integers ka linear accumulation sum calculate kiya hai.
3. Built-in `len(nums)` ka upyog karke total elements count kiye hain jo $\mathcal{O}(1)$ time mein size deta hai.
4. Resultant mean ko floating-point format specifier `{avg:.2f}` ke dwara clean 2 decimal places mein print kiya hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Zero Division Guard
Mathematics mein division by zero undefined hota hai. Agar list khali aati hai (`len(nums) == 0`), toh Python bina guard ke `ZeroDivisionError` throw karta hai. Humne `if not nums: return None` lagakar defensive programming ensure ki hai.

#### 2. Sum Accumulation
`sum(nums)` Python ke internal C implementation mein single continuous pass run karta hai jo sabhi elements ke pointers ko dereference karke aggregate sum calculate karta hai. Iski time complexity strictly:

$$
T_{\text{sum}}(N) = \mathcal{O}(N)
$$

hoti hai.

#### 3. O(1) Length Retrieval
CPython list object ek C struct `PyListObject` hota hai jisme `ob_size` field explicitly stored rehta hai. Jab hum `len(nums)` call karte hain, toh Python ko elements count nahi karne padte; woh seedhe memory se struct field read karta hai:

$$
T_{\text{len}}(N) = \mathcal{O}(1)
$$

#### 4. Formatting Output
Float precision issues (jaise $30.000000000000004$) ko prevent karne ke liye string formatting `{avg:.2f}` do decimal places par round karke professional output present karti hai.

---

## Solution 03: Do Integer Lists Ko Merge Aur Sort Karna

### Python Source Code

```python
from typing import List

def merge_and_sort(list1: List[int], list2: List[int]) -> List[int]:
    """Merges two lists and sorts them in ascending order via Timsort."""
    merged = list1 + list2
    merged.sort()
    return merged

# Demonstration
if __name__ == "__main__":
    l1 = [4, 1, 7]
    l2 = [9, 2, 5]
    res = merge_and_sort(l1, l2)
    print(f"L1: {l1} | L2: {l2}")
    print(f"Merged & Sorted: {res}")
```

### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Binary `+` operator ka use karke `list1` aur `list2` ke elements ko ek naye combined list buffer `merged` mein concatenate kiya hai.
2. In-place `.sort()` method call karke Python ke production sorting engine (Timsort) ko trigger kiya hai.
3. Function se completely sorted combined list return karwayi hai.
4. Console par clean f-string format mein input lists aur sorted outcome ko display kiya hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. List Concatenation Mechanics
Jab hum `list1 + list2` likhte hain, CPython pehle total length $N + M$ calculate karta hai, ek naya `PyListObject` allocate karta hai, aur dono lists ke element pointers ko naye buffer mein `memcpy` karta hai. Yeh step $\mathcal{O}(N + M)$ time leta hai.

#### 2. Timsort Algorithm
Python ka `.sort()` method Timsort algorithm use karta hai jo Tim Peters dwara design kiya gaya tha. Timsort real-world data mein natural sorted runs ko identify karta hai aur Merge Sort aur Insertion Sort ka optimal combination execute karta hai. Iski worst-case time complexity:

$$
T(N, M) = \mathcal{O}((N + M) \log(N + M))
$$

hoti hai, aur best-case (agar pehle se sorted ho) $\mathcal{O}(N + M)$ hoti hai.

#### 3. In-place vs New List
`.sort()` method in-place sort karta hai bina koi extra list banaye, jabki `sorted()` ek nayi list create karta. Kyunki humne `merged` list pehle hi create kar li thi, `.sort()` use karna memory-efficient rehta hai.

#### 4. Memory Footprint
Resulting list exactly $N + M$ element pointers ko store karti hai:

$$
S(N, M) = \mathcal{O}(N + M)
$$

---

## Solution 04: Tuple Parity Partitioning

### Python Source Code

```python
from typing import Tuple

def partition_tuple(numbers: Tuple[int, ...]) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
    """Separates an immutable tuple into even and odd component tuples."""
    evens = tuple(x for x in numbers if (x & 1) == 0)
    odds = tuple(x for x in numbers if (x & 1) != 0)
    return evens, odds

# Demonstration
if __name__ == "__main__":
    t = (10, 15, 22, 33, 40, 55, 62)
    evens, odds = partition_tuple(t)
    print(f"Source Tuple: {t}")
    print(f"Even Tuple:   {evens}")
    print(f"Odd Tuple:    {odds}")
```

### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Tuple elements par fast bitwise AND operator `(x & 1)` se parity evaluation perform kiya hai.
2. Generator expression aur `tuple()` constructor ka use karke do naye immutable tuples (`evens` aur `odds`) create kiye hain.
3. Original sequence order ko retain rakha hai.
4. Dono partitioned tuples ko ek single combined tuple pair ke roop mein return kiya hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Bitwise Parity Optimization
Standard modulo `x % 2 == 0` ke bajaye humne bitwise `(x & 1) == 0` use kiya hai. Binary representation mein kisi bhi even number ka Least Significant Bit (LSB) hamesha $0$ hota hai, aur odd number ka LSB $1$ hota hai. Bitwise operation direct CPU ALU instruction level par execute hoti hai.

#### 2. Immutable Packing Via `tuple()`
Tuples immutable hote hain, isliye list ki tarah unme `.append()` nahi kiya ja sakta. Humne generator expressions `(x for x in numbers if ...)` use kiye hain jo bina intermediate list create kiye directly `tuple()` constructor ko elements feed karte hain.

#### 3. Relative Order Preservation
Generator expressions left-to-right sequence mein stream karti hain, isliye numbers ka original sequence order perfectly maintain rehta hai.

#### 4. Asymptotic Complexity
Pure tuple par single pass filtration hone ke karan:

$$
T(N) = \mathcal{O}(N)
$$

$$
S(N) = \mathcal{O}(N)
$$

---

## Solution 05: Menu-Driven Student Gradebook Hash Table

### Python Source Code

```python
from typing import Dict

def run_gradebook_cli():
    gradebook: Dict[str, str] = {}
    
    menu = """
=== STUDENT GRADEBOOK MANAGEMENT ===
[A] Add Student
[B] Update Grade
[C] Search Student
[D] Display All Records
[E] Exit
Choose an option: """
    
    while True:
        choice = input(menu).strip().upper()
        
        if choice == 'A':
            name = input("Enter Student Name: ").strip().title()
            if name in gradebook:
                print(f"Warning: Student '{name}' already exists with grade '{gradebook[name]}'.")
            else:
                grade = input("Enter Letter Grade (A/B/C/D/F): ").strip().upper()
                gradebook[name] = grade
                print(f"Success: Added '{name}' -> '{grade}'.")
                
        elif choice == 'B':
            name = input("Enter Student Name to Update: ").strip().title()
            if name not in gradebook:
                print(f"Error: Student '{name}' not found in records.")
            else:
                new_grade = input("Enter New Letter Grade: ").strip().upper()
                gradebook[name] = new_grade
                print(f"Success: Updated '{name}' -> '{new_grade}'.")
                
        elif choice == 'C':
            name = input("Enter Student Name to Search: ").strip().title()
            grade = gradebook.get(name)
            if grade:
                print(f"Found: {name} has grade '{grade}'.")
            else:
                print(f"Not Found: No record for '{name}'.")
                
        elif choice == 'D':
            print("\n" + "-" * 35)
            print(f"{'Student Name':<20} | {'Grade':<10}")
            print("-" * 35)
            if not gradebook:
                print("No records found.")
            else:
                for s_name, s_grade in sorted(gradebook.items()):
                    print(f"{s_name:<20} | {s_grade:<10}")
            print("-" * 35)
            
        elif choice == 'E':
            print("Exiting Student Gradebook. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter A, B, C, D, or E.")

if __name__ == "__main__":
    # To run interactively, call run_gradebook_cli()
    print("Gradebook CLI module loaded.")
```

### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Dictionary `gradebook = {}` ko primary in-memory hash table storage banaya hai.
2. `while True` loop ke dwara 5 distinct console options (A, B, C, D, E) handle kiye hain.
3. String normalization `.strip().title()` aur `.upper()` ka use karke case-insensitive consistency banayi hai.
4. Lookups, updates, aur duplicate protections ensure ki hain $\mathcal{O}(1)$ average hash table operations ke saath.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Dictionary Hash Table Architecture
Python dictionary keys string identifiers par hash function calculate karti hai. Student name search karte waqt lookup time constant $\mathcal{O}(1)$ rehta hai, chahe gradebook mein 10 students ho ya 10,000.

#### 2. Input Sanitization
Agar koi user `" alice "` likhe aur doosra `"ALICE"` likhe, toh python bina normalization ke unhe alag keys treat karega. Humne `.strip().title()` lagakar name ko standard title-cased format (`"Alice"`) mein normalize kiya hai.

#### 3. Error Handling Aur Conflict Prevention
- Add karte waqt `if name in gradebook:` check kiya hai taaki purana grade bina warning ke overwrite na ho.
- Update karte waqt `if name not in gradebook:` se check kiya hai taaki non-existent key update attempt par clear error message mile.
- Search mein `.get(name)` method safe lookup karta hai bina `KeyError` raise kiye.

#### 4. Tabular Formatting
Option D mein string formatting specifiers (`{s_name:<20} | {s_grade:<10}`) se aligned, uniform columns print hoti hain.

---

## Solution 06: Lexical Word-Length Mapping

### Python Source Code

```python
from typing import List, Dict

def word_length_dict(words: List[str]) -> Dict[str, int]:
    """Generates word-to-length dictionary via comprehension."""
    return {w: len(w) for w in words}

# Demonstration
if __name__ == "__main__":
    words_list = ["apple", "banana", "kiwi", "cherry"]
    res_dict = word_length_dict(words_list)
    print(f"Words: {words_list}")
    print(f"Dictionary: {res_dict}")
```

### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Dictionary comprehension `{w: len(w) for w in words}` ka concise aur declarative implementation kiya hai.
2. List ke har word $w$ ko hash key aur uski length `len(w)` ko integer value banaya hai.
3. Linear scan mein dictionary build ki hai.
4. Output dictionary ko formatted display karwaya hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Dictionary Comprehension Mechanics
Dictionary comprehension Python bytecode level par direct `BUILD_MAP` instructions execute karti hai. Standard loop ke mukable comprehension C-level loops mein run karti hai jo runtime overhead ko reduce karti hai.

#### 2. String Length Introspection
Python strings internally `PyASCIIObject` ya `PyCompactUnicodeObject` struct ke form mein store hoti hain jisme length field (`length`) directly store hoti hai. Isliye `len(w)` calculation $\mathcal{O}(1)$ time mein hoti hai.

#### 3. Key Uniqueness Invariant
Agar input list mein duplicate words aate hain (jaise `["apple", "apple"]`), toh dictionary mapping property ke mutabiq duplicate word overwrite ho jaayega aur final dictionary mein single unique key maintain rahegi.

#### 4. Complexity
Poore list ke $N$ words process karne ke liye:

$$
T(N) = \mathcal{O}(N), \quad S(N) = \mathcal{O}(N)
$$

---

## Solution 07: Whitespace Character Counter

### Python Source Code

```python
def count_whitespaces(s: str) -> int:
    """Counts whitespace characters in O(N) time and O(1) space."""
    return sum(1 for ch in s if ch.isspace())

# Demonstration
if __name__ == "__main__":
    text = "Machine Learning\tLecture 04\nAssignment Suite"
    count = count_whitespaces(text)
    print(f"Input Text: {repr(text)}")
    print(f"Total Whitespaces: {count}")
```

### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Generator expression `(1 for ch in s if ch.isspace())` construct kiya hai.
2. Built-in `sum()` function ke dwara generator stream ko linearly accumulate kiya hai.
3. Single pass mein Bina kisi extra list ko memory mein store kiye count nikala hai.
4. Whitespace frequency ko integer result ke roop mein return aur print kiya hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Generator vs List Comprehension
Agar hum `sum([1 for ch in s if ch.isspace()])` likhte, toh brackets `[...]` ki vajah se memory mein ek poori nayi list banti. Jabki bina brackets ke generator expression lazy evaluation karti hai: har matching character par ek $1$ yield hota hai aur `sum()` use consume kar leta hai. Isse auxiliary memory $\mathcal{O}(1)$ banti hai.

#### 2. Unicode `.isspace()` Standard
Python ka `ch.isspace()` standard ASCII space ke alawa tab (`\t`), newline (`\n`), vertical tab (`\v`), carriage return (`\r`), aur Unicode whitespace characters (jaise non-breaking space `\u00A0`) sabhi ko accurately detect karta hai.

#### 3. Mathematical Indicator Sum
Count ko mathematical indicator function ke roop mein formulate kiya gaya hai:

$$
W(S) = \sum_{i=1}^{N} \mathbb{I}_{\text{whitespace}}(s_i)
$$

#### 4. Asymptotic Bounds
Time complexity string length ke proportional hai:

$$
T(N) = \mathcal{O}(N), \quad S(N) = \mathcal{O}(1)
$$

---

## Solution 08: Disjoint Set Verification

### Python Source Code

```python
from typing import List, Any

def check_disjoint(list1: List[Any], list2: List[Any]) -> bool:
    """Checks whether two lists have zero common elements using sets."""
    return set(list1).isdisjoint(list2)

# Demonstration
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [3, 4, 5]
    print(f"A={a}, B={b} -> Disjoint: {check_disjoint(a, b)}")
    print(f"A={a}, C={c} -> Disjoint: {check_disjoint(a, c)}")
```

### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Pehli list ko Python `set(list1)` mein cast kiya hai.
2. Built-in `.isdisjoint(list2)` method ko call karke shared elements ki absence test ki hai.
3. Boolean outcome (`True` ya `False`) return karwaya hai.
4. Positive aur negative dono test cases par verification output print kiya hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Set Theory Disjoint Definition
Do sets $S_1$ aur $S_2$ disjoint tab hote hain jab unka intersection empty ho:

$$
S_1 \cap S_2 = \emptyset \iff |S_1 \cap S_2| = 0
$$

Agar ek bhi common element milta hai, toh intersection non-empty ho jaata hai aur disjoint condition violate ho jaati hai.

#### 2. `.isdisjoint()` Internal Optimization
CPython ka `.isdisjoint()` implementation doosri list ke elements ko iterate karte hue check karta hai ki kya koi element pehle set ke hash table mein maujood hai. Jaise hi pehla common element milta hai, method immediately `False` return kar deta hai (early stopping).

#### 3. Complexity Comparison
- Naive nested loop: $\mathcal{O}(N \times M)$ time.
- Set disjoint lookup: $\mathcal{O}(N)$ set build + $\mathcal{O}(\min(N, M))$ lookup = $\mathcal{O}(N + M)$ total time.

#### 4. Space Tradeoff
Set build karne ke liye pehli list ke elements hash table mein store hote hain, isliye auxiliary space:

$$
S(N) = \mathcal{O}(N)
$$

---

## Solution 09: Sequence Duplicate Detector

### Python Source Code

```python
from typing import List, Set, Any

def find_duplicates(items: List[Any]) -> Set[Any]:
    """Finds duplicates in single pass using seen and duplicates sets."""
    seen: Set[Any] = set()
    duplicates: Set[Any] = set()
    
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
            
    return duplicates

# Demonstration
if __name__ == "__main__":
    data = [1, 2, 3, 2, 4, 5, 1, 6, 2]
    dups = find_duplicates(data)
    print(f"Data: {data}")
    print(f"Identified Duplicates: {dups}")
```

### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Do empty sets `seen` aur `duplicates` initialize kiye hain.
2. Input list ke upar single iterative pass run kiya hai.
3. Conditional logic `if item in seen:` se check kiya hai; agar item pehle se present hai toh use `duplicates` set mein add kiya hai, warna `seen` set mein add kiya hai.
4. Filtered duplicate elements ka unique set return kiya hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Two-Set Invariant
- `seen`: Yeh set tracking karta hai ki kaun-kaun se elements kam se kam ek baar encounter ho chuke hain.
- `duplicates`: Yeh set sirf unhi elements ko accumulate karta hai jo do ya do se zyada baar appear hote hain.

#### 2. Why Avoid `items.count()`
Beginners aksar `[x for x in items if items.count(x) > 1]` likh dete hain. List ka `.count()` method har iteration par poori list ko scan karta hai, jisse algorithm $\mathcal{O}(N^2)$ quadratic ban jaata hai. Humara two-set approach hash lookup $\mathcal{O}(1)$ use karta hai, jisse overall running time strictly linear rehta hai.

#### 3. Automatic Deduplication
Kyunki `duplicates` ek Python `set` hai, agar koi number (jaise `2`) teen ya chaar baar bhi appear hota hai, toh woh `duplicates` set mein sirf ek hi baar store hoga.

#### 4. Time and Space Bounds

$$
T(N) = \mathcal{O}(N)
$$

$$
S(N) = \mathcal{O}(N)
$$

---

## Solution 10: Unique Character Extraction Aur Count

### Python Source Code

```python
from typing import Tuple, Set

def extract_unique_chars(s: str) -> Tuple[Set[str], int]:
    """Extracts unique characters from string and returns set and length."""
    unique_set = set(s)
    return unique_set, len(unique_set)

# Demonstration
if __name__ == "__main__":
    word = "engineering"
    chars, count = extract_unique_chars(word)
    print(f"Original Word: {word}")
    print(f"Unique Characters Set: {sorted(chars)}")
    print(f"Total Unique Count: {count}")
```

### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. String ko direct `set(s)` constructor mein pass karke unique characters ka set construct kiya hai.
2. Built-in `len(unique_set)` function se set ki cardinality calculate ki hai.
3. Unique characters ka collection aur uska integer count ek tuple pair mein return kiya hai.
4. Formatted output print kiya hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Set Hash Deduplication
String Python mein iterable of single-character strings hoti hai. Jab `set(s)` call hota hai, CPython har character ka hash nikaal kar internal open-addressing table mein insert karta hai. Duplicate characters collision check ke baad drop ho jaate hain.

#### 2. Set Cardinality
Mathematical set $\mathcal{U} = \{ c \mid c \in S \}$ ki cardinality $K = |\mathcal{U}|$ built-in `len()` se $\mathcal{O}(1)$ time mein milti hai.

#### 3. Alphabet Upper Bound
Agar input string 10,000 characters ki bhi ho, toh unique characters ki maximum count English alphabet ke liye $26$ (ya case-sensitive $52$) se exceed nahi kar sakti. Isliye space complexity alphabet size $|\Sigma|$ se bounded rehti hai.

#### 4. Complexity Formulation

$$
T(N) = \mathcal{O}(N)
$$

$$
S(N) = \mathcal{O}(|\Sigma|) \le \mathcal{O}(N)
$$

---

## Systems Case Study 1: String Immutability Aur Buffer Concatenation Complexity

### Python Benchmark Implementation

```python
import time
from typing import Tuple

def benchmark_concatenation(n: int) -> Tuple[float, float]:
    # 1. Naive Repeated Concatenation
    start = time.perf_counter()
    s_naive = ""
    for _ in range(n):
        s_naive += "a"
    time_naive = time.perf_counter() - start
    
    # 2. Optimized str.join()
    start = time.perf_counter()
    parts = ["a"] * n
    s_join = "".join(parts)
    time_join = time.perf_counter() - start
    
    return time_naive, time_join

# Demonstration
if __name__ == "__main__":
    test_n = 20000
    t_naive, t_join = benchmark_concatenation(test_n)
    print(f"N = {test_n}:")
    print(f"  Naive '+':     {t_naive:.6f} seconds")
    print(f"  str.join():    {t_join:.6f} seconds")
    print(f"  Speedup:       {t_naive / max(t_join, 1e-9):.2f}x")
```

### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Naive repeated string concatenation (`s += "a"`) ko measure karne ke liye high-precision timer `time.perf_counter()` use kiya hai.
2. Preallocated list ko `str.join()` karne ka optimized execution time benchmark kiya hai.
3. Dono approaches ke asymptotic runtime equations formulate kiye hain.
4. 300 DPI high-resolution benchmark visualization plot embed kiya hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Why Naive `+` is Quadratic
Python strings immutable hote hain. Har `s += "a"` ke dauran CPython ek naya buffer allocate karta hai aur purani string ke $i$ characters ko naye buffer mein copy karta hai. Total character copies:

$$
T(N) = \sum_{i=1}^{N} i = \frac{N(N+1)}{2} = \Theta(N^2)
$$

$N = 50,000$ par yeh 1.25 billion byte operations ban jaata hai, jo system ko severely choke karta hai.

#### 2. `str.join()` Linear Engine
`str.join()` do passes mein execute hota hai:
- Pass 1: Total character length count karta hai.
- Pass 2: Single continuous memory block allocate karke direct `memcpy` se place karta hai.
Iska running time strictly linear hota hai:

$$
T(N) = \Theta(N)
$$

#### 3. 300 DPI Benchmark Visualization
Plot file `case1_string_concatenation_complexity.png` empirical CPU time aur theoretical curves ke difference ko visually demonstrate karti hai:

![Case 1 Visualization](case1_string_concatenation_complexity.png)

---

## Systems Case Study 2: Dynamic Array Growth Geometry Aur List Amortized Complexity

### Python Benchmark Implementation

```python
import sys
from typing import List, Tuple

def analyze_cpython_list_growth(max_n: int = 100) -> List[Tuple[int, int, int]]:
    lst = []
    growth_log = []
    prev_bytes = sys.getsizeof(lst)
    
    for i in range(max_n):
        lst.append(i)
        curr_bytes = sys.getsizeof(lst)
        if curr_bytes != prev_bytes or i == 0:
            # 64-bit CPython: Header 56 bytes, 8 bytes per pointer
            allocated_slots = (curr_bytes - 56) // 8
            growth_log.append((i + 1, curr_bytes, allocated_slots))
            prev_bytes = curr_bytes
            
    return growth_log

# Demonstration
if __name__ == "__main__":
    logs = analyze_cpython_list_growth(50)
    print(f"{'Size (len)':<12} | {'Bytes':<10} | {'Allocated Slots':<15}")
    print("-" * 42)
    for length, bytes_sz, slots in logs[:10]:
        print(f"{length:<12} | {bytes_sz:<10} | {slots:<15}")
```

### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. `sys.getsizeof()` ka prayog karke CPython dynamic list object ke memory growth ko track kiya hai.
2. CPython 3.12+ `list_resize()` over-allocation formula ka exact mathematical mapping formulate kiya hai.
3. Step function table derive kiya hai jo capacity expansion milestones ($0, 4, 8, 16, 25, 35, 46, \dots$) dikhata hai.
4. List growth geometry ka 300 DPI high-resolution visualization graph embed kiya hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. CPython Growth Formula
Dynamic array mein continuous reallocation overhead se bachne ke liye CPython extra slots allocate karta hai:

$$
\text{allocated} = \text{new\_size} + (\text{new\_size} \gg 3) + (3 \text{ if new\_size } < 9 \text{ else } 6)
$$

Yeh growth sequence exponential growth guarantee karti hai.

#### 2. Amortized $\mathcal{O}(1)$ Proof
Reallocation par $K$ elements copy hote hain, lekin agle $K$ appends tak reallocation cost bilkul $0$ hoti hai:

$$
\text{Amortized Cost per Append} = \frac{\mathcal{O}(K)}{K} = \mathcal{O}(1)
$$

#### 3. 300 DPI Growth Visualization
Graph `case2_list_overallocation_geometry.png` allocated slots aur current length ke step difference (waste factor) ko clearly visualize karta hai:

![Case 2 Visualization](case2_list_overallocation_geometry.png)

---

## Systems Case Study 3: CPython Hash Table Architecture Aur Perturbation Probing

### Python Benchmark Implementation

```python
from typing import List

def trace_cpython_probing(hash_code: int, table_size: int = 8, steps: int = 8) -> List[int]:
    mask = table_size - 1
    perturb = hash_code
    j = hash_code & mask
    path = [j]
    
    for _ in range(steps - 1):
        j = (5 * j + 1 + perturb) & mask
        perturb >>= 5
        path.append(j)
        
    return path

# Demonstration
if __name__ == "__main__":
    h = hash("data_science")
    probing_path = trace_cpython_probing(h, table_size=8, steps=6)
    print(f"Hash Code: {h}")
    print(f"Probing Trajectory (Table Size 8): {probing_path}")
```

### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. CPython hash table open-addressing lookup algorithm ka mathematical model build kiya hai.
2. Pseudo-random perturbation formula $j_{i+1} = (5 j_i + 1 + \text{perturb}) \pmod{2^k}$ ko trace kiya hai.
3. Load factor boundary $\alpha = 2/3$ ka mathematical threshold analyze kiya hai.
4. Probing trajectory aur load factor dynamics ka 300 DPI high-resolution plot embed kiya hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Open Addressing vs Linked Chaining
CPython flat compact array use karta hai jisme memory cache locality optimize rehti hai. Collisions ko resolve karne ke liye open addressing slots probe kiye jaate hain.

#### 2. Perturbation Probing Sequence
Linear probing clustering problems create karta hai. Isliye CPython hash code ke higher bits ko use karne ke liye `perturb >>= 5` shift karta hai jisse probe sequence uniform pseudo-random dispersion show karti hai:

$$
j_{i+1} = (5 j_i + 1 + \text{perturb}) \pmod{2^k}
$$

#### 3. Load Factor Threshold $\alpha = 2/3$
Jab hash table 66.6% full ho jaati hai, collision likelihood steeply badh jaati hai. CPython table size ko double ya quadruple karke rehashing perform karta hai taaki lookup speed $\mathcal{O}(1)$ bani rahe.

#### 4. 300 DPI Visualization
Graph `case3_hash_table_load_factor_probing.png` perturbation probing sequence aur collision frequency ko graphically demonstrate karta hai:

![Case 3 Visualization](case3_hash_table_load_factor_probing.png)
