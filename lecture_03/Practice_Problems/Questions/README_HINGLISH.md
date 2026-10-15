# Lecture 03: Assignment 2 Questions Aur Systems Case Studies (हिंग्लिश)

Is document mein **Lecture 03: Python Fundamentals (Part 2 — Conditionals, Loops Aur Functions)** ke official **Assignment 2** ke sabhi 10 questions aur 3 systems engineering case studies ka detailed Hinglish explanation diya gaya hai.

Har question ke andar do vishesh sections hain:
1. `### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?` (Numbered bullet points)
2. `### 🔍 Har Ek Bullet Point Ka Detailed Explanation` (Deep conceptual aur practical breakdown)

---

## 📋 Table of Contents

- [Question 01: Income Tax Bracket Calculator](#question-01-income-tax-bracket-calculator)
- [Question 02: Range Ke Beech Ke Even Numbers Print Karna](#question-02-range-ke-beech-ke-even-numbers-print-karna)
- [Question 03: Number Ke Digits Alag-Alag Print Karna](#question-03-number-ke-digits-alag-alag-print-karna)
- [Question 04: Number Ke Total Digits Count Karna](#question-04-number-ke-total-digits-count-karna)
- [Question 05: Number Ke Digits Ka Sum Nikalna](#question-05-number-ke-digits-ka-sum-nikalna)
- [Question 06: 3 Aur 5 Dono Se Divisible Numbers (1 Se 100)](#question-06-3-aur-5-dono-se-divisible-numbers-1-se-100)
- [Question 07: Sentinel-Controlled Loop (Quit Bolne Tak Chalo)](#question-07-sentinel-controlled-loop-quit-bolne-tak-chalo)
- [Question 08: Simple Arithmetic Calculator Function](#question-08-simple-arithmetic-calculator-function)
- [Question 09: Prime Number Verifier Function](#question-09-prime-number-verifier-function)
- [Question 10: Number Guessing Game](#question-10-number-guessing-game)
- [Systems Case Study 1: Control Flow Branching Aur Bytecode Jump Offsets](#systems-case-study-1-control-flow-branching-aur-bytecode-jump-offsets)
- [Systems Case Study 2: Loop Execution Speed Aur VM Interpreter Overhead](#systems-case-study-2-loop-execution-speed-aur-vm-interpreter-overhead)
- [Systems Case Study 3: Call Stack Frame Allocation Aur Recursion Limits](#systems-case-study-3-call-stack-frame-allocation-aur-recursion-limits)

---

## Question 01: Income Tax Bracket Calculator

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. User se console par uski annual salary ek floating-point ya integer number ke roop mein input leni hai.
2. Conditional statements (`if`, `elif`, `else`) ka upyog karke check karna hai ki salary kis tax bracket slab mein aati hai:
   - Agar salary 30,000 se kam hai, toh tax rate 5% hoga.
   - Agar salary 30,000 se 70,000 ke beech hai (inclusive), toh tax rate 15% hoga.
   - Agar salary 70,000 se zyada hai, toh tax rate 25% hoga.
3. Total calculated tax amount formula $\text{Tax} = \text{Salary} \times \text{Rate}$ se calculate karna hai.
4. Screen par applicable tax percentage aur final tax amount ko professional 2 decimal places ke format mein print karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Salary input lena aur data type conversion
User se console par `input()` ke zariye salary enter karwayi jaati hai. Kyunki `input()` hamesha string return karta hai, hume use `float(input())` ya `int(input())` mein convert karna padta hai. Saath hi defensive check lagana hota hai ki salary negative ($S < 0$) na ho.

#### 2. Conditional Tax Slabs Ki Logic
Decision boundaries mathematical piecewise function ke mutabiq decide hoti hain:

$$
R(S) = \begin{cases}
0.05 & \text{if } S < 30,000 \\
0.15 & \text{if } 30,000 \le S \le 70,000 \\
0.25 & \text{if } S > 70,000
\end{cases}
$$

Python mein `elif 30000 <= salary <= 70000:` likhna chained comparison syntax ke karan bohot clean hota hai.

#### 3. Total Tax Liability Calculation
Applicable rate milne ke baad actual payable tax amount calculate kiya jata hai:

$$
T(S) = S \cdot R(S)
$$

For example, agar salary $50,000$ hai, toh rate $15\%$ hoga aur tax $50,000 \times 0.15 = 7,500.00$ banega.

#### 4. Formatted Display
Final result ko f-string formatting `{tax:.2f}` ke dwara clean currency format mein print kiya jata hai.

---

## Question 02: Range Ke Beech Ke Even Numbers Print Karna

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek function banana hai jo do integer arguments $a$ aur $b$ accept kare.
2. Range $[a, b]$ ke andar ke sabhi numbers ko inspect karke sirf unhi numbers ko filter karna hai jo even (sam) hain.
3. Range ke dono ends ($a$ aur $b$) inclusive hone chahiye (yaani agar $a$ ya $b$ khud even hain toh woh bhi print hone chahiye).
4. Sabhi filtered even numbers ko console par sequence mein print karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Function signature aur parameters
Function ka signature `def print_even_numbers(a: int, b: int) -> None:` hoga. Agar user ulta range de de (jaise $a = 20$ aur $b = 10$), toh function ko automatically identify karna chahiye taaki crash na ho.

#### 2. Even Number Filter Logic
Kisi bhi integer $x$ ke liye parity condition modulo arithmetic se check hoti hai:

$$
x \pmod 2 = 0
$$

Agar $x \pmod 2 == 0$ evaluate hota hai, tabhi number even maana jaayega. Bitwise operator `(x & 1) == 0` se bhi check kiya ja sakta hai.

#### 3. Inclusive Range Generation
Python ka built-in `range(start, stop)` function `stop` boundary ko include nahi karta. Isliye $b$ ko include karne ke liye hume loop `range(a, b + 1)` tak chalana hota hai.

#### 4. Output Display
Numbers ko ek line mein clean format mein display karne ke liye `print(num, end=" ")` ka use kiya jaata hai.

---

## Question 03: Number Ke Digits Alag-Alag Print Karna

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Function mein ek integer $N$ (jaise $N = 312$) input lena hai.
2. Number ke ek-ek digit ko isolate karke alag-alag print karna hai ($3, 1, 2$).
3. Problem sheet ke hint ke mutabiq mathematical operations ($N \pmod{10}$ aur $N // 10$) ka upyog karna hai, bina `str(N)` string conversion kiye.
4. Digits ko unke original left-to-right natural reading order mein display karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Input number $N$
Koi bhi positive integer $N$, jaise $312$, $5049$, ya $7$.

#### 2. Mathematical Modulo & Floor Division Mechanism
Decimal base-10 number system mein kisi bhi number ka sabse rightmost (last) digit modulo-10 se milta hai:

$$
\text{last\_digit} = N \pmod{10}
$$

Aur us rightmost digit ko number se hatane ke liye integer floor division kiya jata hai:

$$
N = \lfloor N / 10 \rfloor = N // 10
$$

Jaise $312 \pmod{10} = 2$, aur $312 // 10 = 31$.

#### 3. Left-to-Right Order Preservation
Kyunki modulo arithmetic peeche se (units place se) digits nikaalta hai, agar hum direct print karenge toh order reverse ($2, 1, 3$) aayega. Natural left-to-right ($3, 1, 2$) order lane ke liye hum digits ko collect karke reverse karte hain ya divisor $10^{k-1}$ se divide karte hain.

#### 4. Pure Arithmetic Constraint
Hum string casting `for ch in str(n)` use nahi karenge; pure arithmetic loops $\mathcal{O}(\log_{10} N)$ se execute karenge.

---

## Question 04: Number Ke Total Digits Count Karna

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek function `count_digits(n: int) -> int` banana hai jo kisi bhi integer $N$ ko accept kare.
2. Number ke andar total kitne digits hain unhe count karna hai.
3. Negative numbers aur single-digit zero ($N = 0$) ke edge cases ko safely handle karna hai.
4. Total digit count integer value ke roop mein return karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Problem Definition
Agar $N = 312$ hai toh answer $3$ hona chahiye. Agar $N = 7$ hai toh $1$. Agar $N = 0$ hai toh $1$.

#### 2. Loop Counting Algorithm
Ek counter `count = 0` rakhte hain. Jab tak $N > 0$ rehta hai, hum $N //= 10$ karte hain aur `count += 1` badhate hain. Har step par number 10 guna chota hota jata hai.

#### 3. Mathematical Logarithmic Bound
Base-10 number mein digits ki sankhya seedhe logarithm se related hoti hai:

$$
K = \lfloor \log_{10} |N| \rfloor + 1
$$

Loop theek $\lfloor \log_{10} N \rfloor + 1$ iterations chalta hai.

#### 4. Edge Cases: Zero Aur Negative Numbers
- Agar $N = 0$ ho, toh `while n > 0:` loop chalega hi nahi! Isliye pehle hi check karte hain `if n == 0: return 1`.
- Agar $N$ negative ho, toh pehle `n = abs(n)` karke sign discard karte hain.

---

## Question 05: Number Ke Digits Ka Sum Nikalna

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek function `sum_of_digits(n: int) -> int` likhna hai.
2. Diye gaye integer $N$ ke sabhi digits ko aapas mein add karna hai.
3. Example: Agar $N = 312$ hai, toh result $3 + 1 + 2 = 6$ aana chahiye.
4. Negative numbers ko absolute value lekar safely compute karna hai aur final sum return karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Input Processing
Input $N$ ko pehle absolute value `abs(n)` mein convert karte hain taaki negative numbers (jaise $-456$) ka sum bhi $4 + 5 + 6 = 15$ sahi nikle.

#### 2. Running Sum Accumulator
Ek accumulator variable `total_sum = 0` initialize kiya jaata hai.

#### 3. Mathematical Summation Loop
Loop ke har iteration mein:
- Last digit extract karte hain: $d = N \pmod{10}$
- Accumulator mein add karte hain: $\text{total\_sum} += d$
- Truncate karte hain: $N = N // 10$

Ganit ke roop mein:

$$
\Sigma(N) = \sum_{i=0}^{k-1} d_i
$$

#### 4. Loop Exit Aur Return
Jab $N = 0$ ho jaata hai, loop terminate hota hai aur `total_sum` function se return ho jaata hai.

---

## Question 06: 3 Aur 5 Dono Se Divisible Numbers (1 Se 100)

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Range 1 se 100 tak ke sabhi integers ko scan karna hai.
2. Check karna hai ki kaunse numbers 3 aur 5 dono se poori tarah divide (bina kisi remainder ke) hote hain.
3. Number theory ke LCM principle ($\\text{lcm}(3, 5) = 15$) ka concept samajhna hai.
4. Matching numbers (jaise 15, 30, 45, 60, 75, 90) ko screen par print karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Range Specification
Range $[1, 100]$ closed interval hai, yaani $1$ aur $100$ dono inclusive hain.

#### 2. Divisibility Condition
Ek number $x$ 3 aur 5 dono se divide tabhi hoga jab:

$$
x \pmod 3 = 0 \quad \land \quad x \pmod 5 = 0
$$

Number theory ke mutabiq, kyunki 3 aur 5 coprime hain (hcf = 1), isliye unka common divisor unke product (LCM = 15) se divide hoga:

$$
x \pmod{15} = 0
$$

#### 3. Brute Force vs Step Range
- Brute force approach: `for x in range(1, 101): if x % 3 == 0 and x % 5 == 0:` (100 checks).
- Optimized step approach: `for x in range(15, 101, 15):` (sirf 6 steps direct jump).

#### 4. Output Display
Resulting sequence $\{15, 30, 45, 60, 75, 90\}$ ko terminal par print kiya jata hai.

---

## Question 07: Sentinel-Controlled Loop (Quit Bolne Tak Chalo)

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek continuous looping console program banana hai jo baar-baar user se number input maange.
2. Har entered number ke liye evaluate karke batana hai ki number **Positive**, **Negative**, ya **Zero** hai.
3. Agar user number ke bajaye string `"Quit"` enter kare, toh program ko gracefully terminate ho jana chahiye.
4. Invalid string inputs ko handle karna hai taaki program crash na ho.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Indefinite while True loop
Jab tak termination condition hit na ho, program `while True:` loop mein chalta rehta hai.

#### 2. Sentinel Token Detection
User input ko normalize karte hain `raw = input().strip().lower()`. Agar `raw == "quit"` hai, toh loop se turant `break` ho jaate hain.

#### 3. Numeric Parsing Aur Sign Evaluation
Agar user ne quit nahi kaha, toh input ko `float(raw)` mein convert karke check karte hain:
- `if num > 0: print("Positive")`
- `elif num < 0: print("Negative")`
- `else: print("Zero")`

#### 4. Error Handling
Agar user ne koi aisi string likh di jo na "quit" hai aur na number (jaise "hello"), toh `try ... except ValueError` laga kar error message print karte hain aur loop continue rakhte hain.

---

## Question 08: Simple Arithmetic Calculator Function

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek function `calculator(a, b, operation)` design karna hai jo teen parameters accept kare.
2. `operation` parameter ke basis par char standard arithmetic calculations perform karni hain: `+`, `-`, `*`, `/`.
3. Multi-way decision logic ke liye Python 3.10+ ke `match ... case` statement ka prayog karna hai.
4. Division by zero ($b = 0$ jab `operation == '/'`) ki critical edge case ko handle karna hai aur invalid operations par error raise karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Parameters Specification
- `a`: Pehla operand (float/int).
- `b`: Doosra operand (float/int).
- `operation`: String token (`'+'`, `'-'`, `'*'`, `'/'`).

#### 2. Structural Pattern Matching
Python 3.10 ke `match operation:` syntax se clean dispatch banaya jaata hai:
- `case '+': return a + b`
- `case '-': return a - b`
- `case '*': return a * b`
- `case '/': ...`

#### 3. Division By Zero Guard
Agar $b = 0$ hai aur operation `'/'` hai:

$$
\frac{a}{0} = \text{Undefined}
$$

Python native division `ZeroDivisionError` throw kar dega. Hum guard lagate hain `if b == 0: raise ZeroDivisionError(...)`.

#### 4. Wildcard Default
`case _:` fallback lagate hain jo kisi bhi unexpected operator (jaise `'%'` ya `'^'`) par `ValueError` return karta hai.

---

## Question 09: Prime Number Verifier Function

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek function `is_prime(n: int) -> bool` banana hai jo check kare ki number prime (abhyajya) hai ya nahi.
2. Agar number prime hai toh `True` return karna hai, warna `False`.
3. Loop ka use karke divisors test karne hain.
4. Base conditions ($N \le 1$ prime nahi hote, $2$ sabse chota prime hai) aur mathematical upper bound $\lfloor \sqrt{n} \rfloor$ ka dhyan rakhna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Prime Number Ki Definition
Ek integer $N > 1$ prime hota hai agar uske factors sirf 1 aur $N$ khud ho. $0, 1$, aur negative numbers prime nahi hote. $2$ ekmatra even prime number hai.

#### 2. Sub-Linear $\mathcal{O}(\sqrt{N})$ Upper Bound
Agar koi number composite hai, toh uska kam se kam ek divisor zaroor $\le \sqrt{N}$ hoga. Isliye loop ko $2$ se $N-1$ tak chalana inefficient hai; hum sirf $2$ se lekar $\lfloor \sqrt{N} \rfloor$ tak hi check karte hain:

$$
d \le \lfloor \sqrt{N} \rfloor
$$

Agar $\sqrt{N}$ tak koi divisor nahi mila, toh aage kisi divisor ke milne ki probability mathematically impossible hai.

#### 3. Loop Execution Aur Early Exit
Jaise hi koi divisor milta hai (`if n % d == 0:`), function turant `return False` kar deta hai. Agar poora loop bina kisi divisor ke khatam ho gaya, toh `return True`.

#### 4. Asymptotic Running Time
Standard trial division $N$ steps leta hai, jabki square-root bound sirf $\mathcal{O}(\sqrt{N})$ steps leta hai. Agar $N = 1,000,000$ hai, toh loop sirf $1,000$ iterations chalega!

---

## Question 10: Number Guessing Game

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek secret number (jaise 1 se 100 ke beech) program mein fix ya randomly choose karna hai.
2. User se repeatedly guess input lena hai.
3. User ke guess ko secret number se compare karke teen tarah ke feedbacks dene hain:
   - Agar guess secret number se bada hai: `"Too high"`.
   - Agar guess secret number se chota hai: `"Too low"`.
   - Agar guess exact match kar gaya: `"Correct!"` aur game terminate karna hai.
4. Total attempts count karke success par congratulatory message print karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Game State Setup
Ek integer `secret_number` set kiya jata hai aur ek counter `attempts = 0` rakha jata hai.

#### 2. Comparison Logic
Har input par evaluation hota hai:

$$
\text{Feedback}(g) = \begin{cases}
\text{"Too high"} & \text{if } g > S \\
\text{"Too low"} & \text{if } g < S \\
\text{"Correct!"} & \text{if } g = S
\end{cases}
$$

#### 3. Binary Search Optimal Strategy
Agar user binary search strategy use kare (har step par midpoint guess kare), toh 1 se 100 tak ke kisi bhi number ko maximum:

$$
K = \lceil \log_2 100 \rceil = 7 \text{ guesses}
$$

mein guarantee ke saath guess kiya ja sakta hai.

#### 4. Termination Aur Score
Jab user ka guess match ho jaata hai, `break` statement execute hota hai aur terminal par total attempts print hoti hain.

---

## Systems Case Study 1: Control Flow Branching Aur Bytecode Jump Offsets

### 📋 Is Case Study Mein Aapse Kya Pucha Gaya Hai?
1. Python ke `if/elif/else` aur `match/case` statements ko CPython virtual machine bytecode level par inspect karna.
2. `dis` module se bytecode opcodes (`POP_JUMP_IF_FALSE`, `JUMP_FORWARD`, `COMPARE_OP`) ko disassemble karna.
3. Control flow graph (CFG) aur jump address offsets ko analyze karna.
4. 300 DPI high-resolution bytecode jump trajectory visualizer render karna.

---

## Systems Case Study 2: Loop Execution Speed Aur VM Interpreter Overhead

### 📋 Is Case Study Mein Aapse Kya Pucha Gaya Hai?
1. CPython ke andar `while` loop, `for` loop, aur C-level accumulator primitives (`sum(range())`) ke running times ko benchmark karna.
2. Explain karna ki kyu `while` loop virtual machine interpreter overhead ke karan slow hota hai (`COMPARE_OP` aur dynamic pointer rebinding).
3. Prove karna ki kyu `for` loop ka `FOR_ITER` opcode C-level par fast iterate karta hai.
4. Benchmark curves ka 300 DPI high-resolution graph plot karna.

---

## Systems Case Study 3: Call Stack Frame Allocation Aur Recursion Limits

### 📋 Is Case Study Mein Aapse Kya Pucha Gaya Hai?
1. CPython runtime ke call stack allocation model (`PyFrameObject`) ka structure analyze karna.
2. Measure karna ki har recursive function call stack par kitne bytes allocate karti hai.
3. Explain karna ki Python default recursion limit `sys.getrecursionlimit() = 1000` kyu enforce karta hai.
4. Stack memory growth aur recursion limit boundary ka 300 DPI visualization graph plot karna.
