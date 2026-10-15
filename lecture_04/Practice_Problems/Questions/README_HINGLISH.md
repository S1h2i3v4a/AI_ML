# Lecture 04: Assignment 3 Questions Aur Systems Case Studies (हिंग्लिश)

Is document mein **Lecture 04: Strings, Lists, Tuples, Dictionaries, aur Sets** ke Assignment 3 ke sabhi 10 questions aur 3 systems engineering case studies ka detailed Hinglish explanation diya gaya hai.

Har question ke andar do vishesh sections include kiye gaye hain:
1. `### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?` (Numbered bullet points)
2. `### 🔍 Har Ek Bullet Point Ka Detailed Explanation` (Deep conceptual aur practical breakdown)

---

## 📋 Table of Contents

- [Question 01: Palindrome String Check](#question-01-palindrome-string-check)
- [Question 02: Integer List Ka Arithmetic Average](#question-02-integer-list-ka-arithmetic-average)
- [Question 03: Do Integer Lists Ko Merge Aur Sort Karna](#question-03-do-integer-lists-ko-merge-aur-sort-karna)
- [Question 04: Tuple Ko Even Aur Odd Mein Partition Karna](#question-04-tuple-ko-even-aur-odd-mein-partition-karna)
- [Question 05: Menu-Driven Student Gradebook Dictionary](#question-05-menu-driven-student-gradebook-dictionary)
- [Question 06: Words Se Word-Length Dictionary Banana](#question-06-words-se-word-length-dictionary-banana)
- [Question 07: String Ke Andar Whitespaces Count Karna](#question-07-string-ke-andar-whitespaces-count-karna)
- [Question 08: Do Lists Disjoint Hain Ya Nahi Check Karna](#question-08-do-lists-disjoint-hain-ya-nahi-check-karna)
- [Question 09: List Ke Andar Duplicate Elements Identify Karna](#question-09-list-ke-andar-duplicate-elements-identify-karna)
- [Question 10: String Se Unique Characters Aur Count Nikalna](#question-10-string-se-unique-characters-aur-count-nikalna)
- [Systems Case Study 1: String Immutability Aur Buffer Concatenation Complexity](#systems-case-study-1-string-immutability-aur-buffer-concatenation-complexity)
- [Systems Case Study 2: Dynamic Array Growth Geometry Aur List Amortized Complexity](#systems-case-study-2-dynamic-array-growth-geometry-aur-list-amortized-complexity)
- [Systems Case Study 3: CPython Hash Table Architecture Aur Perturbation Probing](#systems-case-study-3-cpython-hash-table-architecture-aur-perturbation-probing)

---

## Question 01: Palindrome String Check

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. User se console par ek string input ke roop mein lena hai.
2. Us string ko aage se (forward order) aur peeche se (reverse order) check karke dekhna hai ki kya dono patterns exact same hain.
3. String slicing (`[::-1]`) ya two-pointer technique ka use karke palindrome property test karni hai.
4. Screen par saaf message print karna hai ki string palindrome hai ya nahi.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. User se console par ek string input ke roop mein lena
Jab program start hoga, toh Python ke built-in `input()` function ka use karke user se koi bhi word ya text maangna hai. User `"madam"`, `"racecar"`, `"radar"`, ya `"python"` jaisa koi bhi word de sakta hai. Humara pehla step user input ko ek variable mein safely store karna hai.

#### 2. Forward aur reverse reading ko compare karna
Palindrome ka mathematical niyam yeh hota hai ki sequence aage se padhne par aur peeche se padhne par exact same character order produce kare. Ganit ke roop mein:

$$
\forall i \in \{0, 1, \dots, \lfloor N/2 \rfloor\}, \quad S[i] = S[N - 1 - i]
$$

Agar har index $i$ par character apne symmetric opposite index $N - 1 - i$ se match karta hai, tabhi string ko palindrome maana jaayega. Agar ek bhi character match nahi karta, toh string non-palindrome ghoshit ho jaati hai.

#### 3. Slicing ya Two-Pointer algorithm ka prayog
Python mein string ko reverse karne ka sabse fast aur idiomatic tareeqa slicing notation `s[::-1]` hota hai. Yeh internal C-level par pure string buffer ka reverse copy banata hai. Agar memory optimize karni ho, toh hum do pointers ($L=0$ aur $R=N-1$) rakh kar center ki taraf badhte hue comparison kar sakte hain jisse koi additional memory allocate nahi hoti.

#### 4. Screen par result display karna
Conditional statement `if ... else` laga kar terminal par formatted string (f-string) ki madad se output dikhana hai, jaise:
- `"The string 'radar' is a Palindrome."`
- `"The string 'hello' is NOT a Palindrome."`

---

## Question 02: Integer List Ka Arithmetic Average

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. User se integers ki ek list input ke roop mein accept karni hai.
2. List ke sabhi numbers ka total sum aur total elements ki count ($N$) calculate karni hai.
3. Ganitiya formula $\mu = \frac{\sum x_i}{N}$ ka upyog karke average (mean) nikalna hai.
4. Average ko terminal par 2 decimal places ke floating-point format mein print karna hai aur empty list ki edge case ko handle karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Integers ki list input accept karna
User se space-separated numbers liye jaate hain, jaise `"10 20 30 40 50"`. Inhe `.split()` method se individual substrings mein convert kiya jaata hai aur phir list comprehension ya `map(int, ...)` ke dwara actual Python integers mein cast karke list banayi jaati hai: `nums = [10, 20, 30, 40, 50]`.

#### 2. Total sum aur element count nikalna
Python ke built-in `sum(nums)` function se hum single pass mein list ke sabhi elements ka addition karte hain. Element count nikalne ke liye `len(nums)` ka use kiya jaata hai jo CPython mein $\mathcal{O}(1)$ time mein result deta hai kyunki list object ke header mein uska size pehle se stored rehta hai (`ob_size`).

#### 3. Mathematical mean formula apply karna
Average ka formula simple arithmetic mean hota hai:

$$
\mu = \frac{1}{N} \sum_{i=1}^{N} x_i
$$

Agar list khali ho ($N = 0$), toh direct division karne par Python `ZeroDivisionError` raise kar dega. Isliye pehle condition check karni hoti hai `if len(nums) == 0:` jisse program crash na ho.

#### 4. Formatted float output dikhana
Calculation ke baad result ko format specifier `{avg:.2f}` ke dwara print kiya jaata hai taaki agar answer repeating decimal bhi ho (jaise $14.333333$), toh screen par clean `14.33` display ho.

---

## Question 03: Do Integer Lists Ko Merge Aur Sort Karna

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. User se do alag-alag integer lists input karwani hain.
2. Dono lists ko aapas mein jod kar ek single concatenated list taiyar karni hai.
3. Resulting combined list ke sabhi numbers ko ascending order (chote se bade kram) mein sort karna hai.
4. Final sorted list ko output console par print karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Do separate lists user se input lena
User se pehli list maangi jaati hai (jaise `[4, 1, 7]`) aur fir doosri list (jaise `[9, 2, 5]`). Dono ko standard input ingestion pipeline se integer lists ke form mein parse kiya jaata hai.

#### 2. Dono lists ko concatenate karna
Python mein lists ko combine karne ke do tareeqe hote hain:
- Binary operator `+`: Yeh ek nayi list create karta hai jisme dono lists ke elements copy hote hain ($L_{\text{merged}} = L_1 + L_2$).
- In-place `.extend()`: Yeh pehli list ke buffer ko resize karke doosri list ke elements ko peeche append karta hai.

Dono ka theoretical time $\mathcal{O}(N + M)$ hota hai jaha $N$ aur $M$ dono lists ke sizes hain.

#### 3. Combined list ko sort karna
Combined list par Python ka standard sorting algorithm Timsort execute hota hai. Python mein `sorted(merged_list)` ya `merged_list.sort()` ka use kiya jata hai. Timsort real-world data ke runs ko identify karta hai aur iski time complexity:

$$
T(N, M) = \mathcal{O}((N + M) \log(N + M))
$$

hoti hai, jo information-theoretic comparison sort ka optimal bound hai.

#### 4. Final sorted list display karna
Sorted list ko cleanly terminal par print kiya jata hai, jaise `Merged and Sorted List: [1, 2, 4, 5, 7, 9]`.

---

## Question 04: Tuple Ko Even Aur Odd Mein Partition Karna

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. User se ya program definition mein ek integers ka tuple lena hai.
2. Har integer element par modulo 2 test ($x \pmod 2$) apply karke uski parity (even ya odd) jaanch karni hai.
3. Even numbers ko ek alag tuple mein aur odd numbers ko doosre alag tuple mein collect karna hai.
4. Original tuple ke sequence order ko preserve karte hue dono resulting tuples ko print karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Integers ka tuple lena
Tuple ek immutable sequence data type hai jo memory mein fixed array of pointer reference ke roop mein allocate hota hai. Example input: `(10, 15, 22, 33, 40, 55, 62)`.

#### 2. Parity check ($x \pmod 2$) lagana
Har number $t_i$ ke liye parity condition check ki jaati hai:

$$
\text{parity}(t_i) = \begin{cases} \text{even} & \text{if } t_i \pmod 2 = 0 \\ \text{odd} & \text{if } t_i \pmod 2 \neq 0 \end{cases}
$$

Bitwise operator `(t_i & 1) == 0` se bhi even test kiya ja sakta hai jo direct hardware level par fast parity check karta hai.

#### 3. Alag tuples generate karna
Kyunki tuples immutable hote hain, hum existing tuple ke andar dynamically naye items append nahi kar sakte. Isliye hum generator expressions ya list comprehensions ka use karte hain aur fir unhe `tuple()` constructor mein pass karke final tuples banate hain:
- `even_tuple = tuple(x for x in data if x % 2 == 0)`
- `odd_tuple = tuple(x for x in data if x % 2 != 0)`

#### 4. Elements ka order preserve karna aur display karna
Comprehensions sequence ko left-to-right iterate karti hain, isliye original order retain rehta hai. Final results ko console par output kar diya jaata hai.

---

## Question 05: Menu-Driven Student Gradebook Dictionary

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek continuous looping menu-driven console program banana hai jo student gradebook maintain kare.
2. Option A ke dwara naye student ka name aur grade add karne ki suvidha deni hai.
3. Option B ke dwara existing student ka grade update karne ki suvidha deni hai.
4. Option C ke dwara kisi student ka name search karke uska grade print karna hai.
5. Option D ke dwara poori gradebook tabular form mein display karni hai aur Option E par loop exit karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Continuous loop aur dictionary structure
Program ek `while True:` loop mein chalega jo baar-baar user ke samne options present karega jab tak user exit command select na kare. Data ko store karne ke liye ek hash map (dictionary) `gradebook = {}` banaya jaata hai jaha student name unique key hoti hai aur grade uski value hoti hai.

#### 2. Option A: Add Student Record
Jab user 'A' select kare, toh student ka name aur grade input liya jaata hai. Check kiya jata hai ki agar student pehle se exist karta hai (`if name in gradebook:`), toh user ko warning di jaaye taaki accidental overwrite na ho, ya seedhe `gradebook[name] = grade` assign kiya jaaye.

#### 3. Option B: Update Student Grade
Jab user 'B' select kare, toh pehle verify kiya jata hai ki kya student record mein maujood hai. Agar maujood hai, toh naya grade assign kiya jata hai. Agar student record mein nahi hai, toh appropriate error message (`"Student not found!"`) print kiya jata hai.

#### 4. Option C: Search Student Record
Dictionary indexing ya `.get(name)` method ka prayog karke $\mathcal{O}(1)$ average time mein student ka grade retrieve kiya jaata hai.

#### 5. Option D & E: Display Table aur Exit
Option D par dictionary ke `.items()` ko iterate karke clean tabular layout mein Roll/Name aur Grade print hota hai. Option E par `break` statement execute karke program terminate ho jata hai.

---

## Question 06: Words Se Word-Length Dictionary Banana

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Words ki ek given list lena hai, jaise `["apple", "banana", "kiwi", "cherry"]`.
2. Har word ko key banakar aur us word ki string length (`len(word)`) ko value banakar ek dictionary banani hai.
3. Is task ko standard `for` loop aur dictionary comprehension dono tareeqon se demonstrate karna hai.
4. Generated dictionary ko output screen par print karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Words ki input list
List of strings represent karta hai humare input corpus ko: `words = ["apple", "banana", "kiwi", "cherry"]`.

#### 2. Word-to-length mapping
Har string $w$ ke andar characters ki sankhya $|w|$ hoti hai. Hume ek mathematical relation build karna hai:

$$
w \mapsto |w|
$$

#### 3. Loop approach vs Comprehension
- Standard loop mein ek empty dict `res = {}` banakar `for w in words: res[w] = len(w)` kiya jaata hai.
- Dictionary comprehension mein single line declarative syntax use hota hai: `{w: len(w) for w in words}`. Comprehension internal Python bytecode level par direct optimized map instructions use karta hai.

#### 4. Output verification
Terminal par output dikhana hai: `{'apple': 5, 'banana': 6, 'kiwi': 4, 'cherry': 6}`.

---

## Question 07: String Ke Andar Whitespaces Count Karna

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. User se ek string input lena hai jisme text, spaces, tabs (`\t`), aur newlines (`\n`) ho sakte hain.
2. String ke ek-ek character ko check karke identify karna hai ki kitne characters whitespace category mein aate hain.
3. Python ke string method `.isspace()` ya direct character set comparison ka use karna hai.
4. Total whitespace count ko terminal par display karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. User string input
String mein multiple words, sentences aur formatting escape sequences ho sakte hain. Example: `"Machine Learning 2026\tLab\n"`

#### 2. Whitespace identification logic
Python ka `char.isspace()` method Unicode standard ke sabhi whitespace code-points ko cover karta hai:
- Space `' '` (ASCII 32)
- Tab `'\t'` (ASCII 9)
- Newline `'\n'` (ASCII 10)
- Carriage return `'\r'` (ASCII 13)
- Form feed `'\f'` (ASCII 12)
- Vertical tab `'\v'` (ASCII 11)

#### 3. Counting algorithm
Hum generator expression `sum(1 for c in s if c.isspace())` ka use karte hain jo bina kisi intermediate list ko memory mein banaye single linear pass $\mathcal{O}(N)$ time aur $\mathcal{O}(1)$ aux memory mein count calculate kar leta hai.

#### 4. Screen par result print karna
Final count integer ko clean format mein print kiya jaata hai: `Whitespace count: 4`.

---

## Question 08: Do Lists Disjoint Hain Ya Nahi Check Karna

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. User se do alag-alag lists input karwani hain.
2. Determine karna hai ki kya dono lists mein koi bhi shared ya common element maujood hai ya nahi.
3. Set theory ke disjoint concept ($S_1 \cap S_2 = \emptyset$) ka upyog karke efficiently check karna hai.
4. Output mein Boolean result aur descriptive text print karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Do lists input lena
Example inputs:
- Case A: `L1 = [1, 2, 3]`, `L2 = [4, 5, 6]`
- Case B: `L1 = [1, 2, 3]`, `L2 = [3, 4, 5]`

#### 2. Disjoint sets ka mathematical meaning
Agar do sets $S_1$ aur $S_2$ ke beech ka intersection set poori tarah empty ho:

$$
S_1 \cap S_2 = \emptyset \iff |S_1 \cap S_2| = 0
$$

toh unhe disjoint sets kaha jaata hai. Agar unke beech ek bhi common member milta hai, toh woh disjoint nahi hote.

#### 3. Efficient set method `.isdisjoint()`
Naive nested loop se check karne par time complexity $\mathcal{O}(N \times M)$ hoti hai jo extremely slow hai. Jabki list ko set mein convert karke `set(L1).isdisjoint(L2)` call karne par CPython smaller set ke elements ko hash table mein probe karta hai jisse time complexity drops to:

$$
\mathcal{O}(\min(|S_1|, |S_2|))
$$

#### 4. Output presentation
Terminal par clear message aana chahiye ki lists disjoint hain ya nahi, aur agar disjoint nahi hain toh kaunse elements common hain.

---

## Question 09: List Ke Andar Duplicate Elements Identify Karna

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Integers ya strings ki ek list accept karni hai jisme duplicate values ho sakti hain.
2. List ko scan karke un sabhi elements ko dhoondhna hai jo ek se zyada baar appear hue hain.
3. Set data structure ka upyog karke tracking karni hai taaki duplicate detection fast aur efficient ho.
4. Sabhi duplicate elements ka ek unique set print karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Input list containing duplicates
Example input: `[1, 2, 3, 2, 4, 5, 1, 6]`

#### 2. Fast tracking with two sets
Ek standard approach mein do sets maintain kiye jaate hain:
- `seen`: Har us element ko store karta hai jo pehli baar encounter hua.
- `duplicates`: Har us element ko store karta hai jo `seen` mein pehle se maujood tha jab humne use dobara dekha.

#### 3. Mathematical multiplicity
Har element ki frequency $m(v)$ define hoti hai:

$$
\mathcal{D} = \{ v \in X \mid m(v) > 1 \}
$$

Single loop pass $\mathcal{O}(N)$ mein chalte hue hum hash lookups $\mathcal{O}(1)$ se verify kar lete hain. Hume list ke built-in `.count()` ko loop ke andar call karne se bachna chahiye kyunki woh $\mathcal{O}(N^2)$ complexity create kar deta hai.

#### 4. Result display
Final output mein terminal par filtered duplicates dikhaye jaate hain: `Duplicates: {1, 2}`.

---

## Question 10: String Se Unique Characters Aur Count Nikalna

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. User se ek string input lena hai (jaise `"engineering"`).
2. String ke sabhi unique characters ko filter karke unka collection taiyar karna hai.
3. Total unique characters ki sankhya (cardinality) count karni hai.
4. Unique characters ka set aur unka total count print karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. User input ingestion
String input lena: `s = "engineering"`.

#### 2. Set construction se uniqueness filter karna
Set data structure mathematically identical elements ko discard kar deta hai. Jab hum string ko `set(s)` mein cast karte hain, toh CPython internal hash table allocate karta hai aur duplicate characters automatically drop ho jaate hain.

#### 3. Set cardinality calculate karna
Unique character set $\mathcal{U} = \{ c \mid c \in S \}$ ki cardinality nikalne ke liye built-in `len(unique_set)` function call kiya jaata hai:

$$
K = |\mathcal{U}|
$$

#### 4. Result display
Console par characters ka set aur total count display hota hai:
- `Unique characters: {'e', 'n', 'g', 'i', 'r'}`
- `Total unique count: 5`

---

## Systems Case Study 1: String Immutability Aur Buffer Concatenation Complexity

### 📋 Is Case Study Mein Aapse Kya Pucha Gaya Hai?
1. Python ke immutable string memory model (`PyUnicodeObject`) ka structure analyze karna.
2. Prove karna ki loop ke andar `+` operator se string concatenate karne par $\mathcal{O}(N^2)$ quadratic slowdown kyu aata hai.
3. Compare karna preallocated list aur `str.join()` method ki linear $\mathcal{O}(N)$ performance ke saath.
4. Dono methods ke CPU execution times ko benchmark karna aur 300 DPI high-resolution graph plot karna.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Python String Immutability
Python mein strings immutable objects hote hain. Jab string create hoti hai, toh uska memory buffer fix ho jata hai. Agar hum `s = s + char` likhte hain, toh Python purani string ko modify nahi karta; balki ek poora naya memory buffer allocate karta hai aur purane characters ko naye buffer mein copy karta hai.

#### 2. $\mathcal{O}(N^2)$ Quadratic Complexity Ka Mathematical Proof
Loop ke $i$-th iteration mein $i$ characters naye buffer mein copy hote hain. Total characters copied across $N$ iterations:

$$
T(N) = \sum_{i=1}^{N} i = \frac{N(N+1)}{2} = \frac{1}{2} N^2 + \frac{1}{2} N = \Theta(N^2)
$$

Yeh quadratic curve large $N$ par catastrophic performance drop laata hai.

#### 3. `str.join()` Ki Linear $\mathcal{O}(N)$ Architecture
`str.join()` do passes mein kaam karta hai:
- Pass 1: Sabhi strings ki lengths ko sum karke exact required total buffer size calculate karta hai.
- Pass 2: Ek single continuous memory block allocate karke sabhi strings ke bytes ko direct memory copy (`memcpy`) se place kar deta hai.
Iska running time strictly $\mathcal{O}(N)$ hota hai.

#### 4. Empirical Benchmark Aur Visualization
$N = 1,000$ se $N = 50,000$ tak benchmarks run karke time curves ko matplotlib par plot kiya gaya hai aur `case1_string_concatenation_complexity.png` ke roop mein save kiya gaya hai.

---

## Systems Case Study 2: Dynamic Array Growth Geometry Aur List Amortized Complexity

### 📋 Is Case Study Mein Aapse Kya Pucha Gaya Hai?
1. CPython ke dynamic list growth formula (`list_resize()` in `listobject.c`) ka mathematical analysis karna.
2. List ki allocated capacity vs current size ko `sys.getsizeof()` se step-by-step measure karna.
3. Prove karna ki kyu individual reallocations slow hone ke bawajood `list.append()` ki amortized time complexity $\mathcal{O}(1)$ hoti hai.
4. Capacity growth steps ka 300 DPI visualization graph generate karna.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. CPython Growth Formula
CPython list resize hone par agle kuch appends ke liye extra empty slots over-allocate karta hai taaki har append par `realloc` na bulana pade. Formula:

$$
\text{allocated} = \text{new\_size} + (\text{new\_size} \gg 3) + (3 \text{ if new\_size } < 9 \text{ else } 6)
$$

Is formula ke mutabiq capacity steps $0, 4, 8, 16, 25, 35, 46, 58, 72, 88, 106, \dots$ bante hain.

#### 2. Capacity Measurement Via `sys.getsizeof()`
Hum ek loop chalate hain jo $N = 0$ se $100$ tak numbers append karta hai aur har step par bytes size inspect karta hai. 64-bit architecture par list ka base header 56 bytes ka hota hai aur har element pointer 8 bytes leta hai.

#### 3. Amortized $\mathcal{O}(1)$ Ka Accounting Proof
Jab capacity double hoti hai, reallocation cost $\mathcal{O}(K)$ lagti hai. Lekin agle $K$ appends tak reallocation cost $0$ hoti hai. Agar hum total cost ko $K$ appends par divide karein:

$$
\text{Amortized Cost} = \frac{\mathcal{O}(K)}{K} = \mathcal{O}(1)
$$

Is tarah average append cost constant rehti hai.

#### 4. 300 DPI Visualization
Graph `case2_list_overallocation_geometry.png` mein step function plot kiya gaya hai jo allocated capacity aur current length ke gap (waste factor) ko clearly illustrate karta hai.

---

## Systems Case Study 3: CPython Hash Table Architecture Aur Perturbation Probing

### 📋 Is Case Study Mein Aapse Kya Pucha Gaya Hai?
1. Python dictionary aur set ke hash table open-addressing lookup algorithm ko analyze karna.
2. Collision resolution ke liye CPython ke pseudo-random perturbation formula ka study karna.
3. Explain karna ki load factor $\alpha = 2/3$ par dictionary table resize kyu hoti hai.
4. Probing trajectory aur collision avoidance ka 300 DPI high-resolution visualization generate karna.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Open Addressing vs Chaining
Java ya traditional hash tables linked-list chaining use karte hain. CPython cache locality ko optimize karne ke liye flat array open addressing use karta hai, jisme sabhi key-value entries direct array slots mein rehti hain.

#### 2. Perturbation Probing Formula
Jab do keys ka hash index same slot par collide hota hai, toh CPython linear probing use nahi karta (kyunki linear probing primary clustering create karta hai). CPython higher-order bits ko mix karne ke liye perturbation sequence use karta hai:

$$
j_{i+1} = (5 j_i + 1 + \text{perturb}) \pmod{2^k}
$$

Har step par `perturb >>= 5` shift hota hai jisse poori table uniformly explore hoti hai bina kisi infinite loop ke.

#### 3. Load Factor Threshold $\alpha = 2/3$
Hash table ka load factor hota hai:

$$
\alpha = \frac{\text{used}}{\text{table\_size}}
$$

Agar $\alpha > 0.66$ ho jaaye, toh collision probability exponentially badhne lagti hai aur lookup time $\mathcal{O}(1)$ se degrade hokar linear search banne lagta hai. Isliye CPython $\alpha = 2/3$ reach hone par table size ko double ya quadruple kar deta hai.

#### 4. Probing Trajectory Visualization
Visual figure `case3_hash_table_load_factor_probing.png` perturbation probing sequence, slot occupancy, aur load factor transition dynamics ko graphically render karti hai.
