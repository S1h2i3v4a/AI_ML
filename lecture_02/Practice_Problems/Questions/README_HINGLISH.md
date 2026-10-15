# 📋 Lecture 02: Practice Problems — Sawal aur Detailed Specifications

[![Language: Hinglish](https://img.shields.io/badge/Language-Hinglish-orange.svg)](#)
[![Status: Compliant](https://img.shields.io/badge/MathJax-100%25_Compliant-brightgreen.svg)](#)

Yeh document **Lecture 02: Python Fundamentals (Part-1)** ke saare questions (10 Official Assignment Problems + 3 Advanced Systems Case Studies) ko cover karta hai. Har question mein aapse kya manga gaya hai, usse pehle bullet points mein clear kiya gaya hai, phir har point ko explain kiya gaya hai, aur sabhi formulas genuine math textbook style mein likhe gaye hain.

---

## 📝 Part 1: Official Assignment Problems (Q1 - Q10)

---

### 📌 Question 1: User Greeting String Formatting

#### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. User se console par uska naam (`name`) aur umar (`age`) input lena hai.
2. Uske baad console par ek formatted sentence print karna hai jismein exact format ho: `"Hello <name>, you are <age> years old!"`.
3. Input string handling aur f-string interpolation ka sahi use demonstrate karna hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (User Input Lena):** User se `input()` function ke zariye uska naam aur age poochiye. Dhyaan rahe ki `input()` hamesha text (string) return karta hai.
- **Point 2 (Formatted Sentence Banana):** Humko naam aur age ko ek specific sentence ke andar rakhkar print karna hai. Jaise agar user ne `"Shradha"` aur `"21"` enter kiya, toh output `"Hello Shradha, you are 21 years old!"` aana chahiye.
- **Point 3 (String Interpolation):** Iske liye sabse modern aur fast tarika Python ka f-string (`f"Hello {name}, you are {age} years old!"`) use karna hai.

#### 📐 Mathematical & Algorithmic Formulation
String concatenation function:

$$
S(\text{name}, \text{age}) = \text{"Hello "} \oplus \text{name} \oplus \text{", you are "} \oplus \text{str}(\text{age}) \oplus \text{" years old!"}
$$

---

### 📌 Question 2: Two Numbers Basic Arithmetic Calculator

#### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. User se do numbers (`a` aur `b`) input lene hain aur unhe appropriate numeric data type (`float` ya `int`) mein convert karna hai.
2. Dono numbers ka Sum (jod), Difference (ghatana), Product (guna), aur Quotient (bhaag) calculate karna hai.
3. Charo arithmetic results ko clearly label ke saath print karna hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Do Numbers Ka Input):** User se do alag-alag prompts par numbers maangne hain. Kyunki numbers decimal bhi ho sakte hain, isliye `float(input())` use karna behtar hai.
- **Point 2 (Arithmetic Operations):** Python ke binary arithmetic operators use karne hain: Sum ke liye `+`, Difference ke liye `-`, Product ke liye `*`, aur Division ke liye `/`.
- **Point 3 (Output Display):** Har calculation ka answer ek saaf line mein print karein taaki user ko pata chale ki kaunsa answer sum ka hai aur kaunsa quotient ka.

#### 📐 Mathematical & Algorithmic Formulation
Given $a, b \in \mathbb{R}$ with $b \ne 0$:

$$
\text{Sum} = a + b
$$

$$
\text{Difference} = a - b
$$

$$
\text{Product} = a \times b
$$

$$
\text{Quotient} = \frac{a}{b}
$$

---

### 📌 Question 3: Heterogeneous Numbers Ka Average

#### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. User se teen numbers input lene hain: pehle do integers aur teesra floating-point number.
2. Teeno values ko explicitly `float` data type mein type cast karna hai.
3. Teeno numbers ka Arithmetic Mean (Average) calculate karke print karna hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Teen Inputs):** User se pehla number integer, doosra integer aur teesra float ke roop mein input lijiye.
- **Point 2 (Explicit Type Casting):** Integers ko `float()` function laga kar floating-point representation mein convert kijiye taaki teeno variables ek common numeric domain mein aa jayein.
- **Point 3 (Average Formula):** Teeno ko add karke $3.0$ se divide kijiye. Dhyaan rahe ki operator precedence ki wajah se brackets zaroori hain: `(num1 + num2 + num3) / 3`.

#### 📐 Mathematical & Algorithmic Formulation
Given $x_1, x_2 \in \mathbb{Z}$ and $x_3 \in \mathbb{R}$:

$$
x_1' = \text{float}(x_1), \quad x_2' = \text{float}(x_2), \quad x_3' = x_3
$$

$$
\mu = \frac{x_1' + x_2' + x_3'}{3}
$$

---

### 📌 Question 4: String Number Ingestion & Multi-Type Casting

#### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek string input lijiye jismein number ho (jaise `"45"`).
2. Is string ko pehle `int` mein convert kijiye, phir `float` mein convert kijiye, aur phir wapas `str` mein convert kijiye.
3. Teeno converted values ko unke data type (`type()`) ke saath console par print kijiye.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (String Input):** Ek string variable banayein jismein numeric characters hon (jaise `"45"`).
- **Point 2 (Type Conversion Steps):** Type constructors use karein: integer ke liye `int("45")`, decimal ke liye `float("45")`, aur wapas string banane ke liye `str(45)`.
- **Point 3 (Type Inspection):** Built-in `type()` function ka use karke verify kijiye ki har step par data type sahi badla hai ya nahi (e.g., `<class 'int'>`, `<class 'float'>`, `<class 'str'>`).

#### 📐 Mathematical & Algorithmic Formulation
Type casting mapping:

$$
s \in \Sigma^* \xrightarrow{\text{int()}} n \in \mathbb{Z} \xrightarrow{\text{float()}} f \in \mathbb{R} \xrightarrow{\text{str()}} s' \in \Sigma^*
$$

---

### 📌 Question 5: Operator Precedence Evaluation Trace

#### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Mathematical expression `x = 10 + 3 * 2 ** 2` ko Python mein evaluate karke uska result print karna hai.
2. Python ke operator precedence rules ke mutabik step-by-step explain karna hai ki yeh output kyu aaya.
3. Kis operator ki priority zyada hai aur execution tree kaise bana, yeh batana hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Expression Run Karna):** Code mein `10 + 3 * 2 ** 2` calculate karein aur result dekhein.
- **Point 2 (Step-by-step Evaluation):** Batayein ki pehle power (`**`) solve hoti hai, phir multiplication (`*`), aur sabse aakhri mein addition (`+`).
- **Point 3 (AST Hierarchy):** Explain karein ki bina brackets ke Python kaise decide karta hai ki kaunsa operand kis operator ke saath bind hoga.

#### 📐 Mathematical & Algorithmic Formulation
Evaluation hierarchy:

$$
\text{Step 1: Exponentiation } \implies 2^2 = 4
$$

$$
\text{Step 2: Multiplication } \implies 3 \times 4 = 12
$$

$$
\text{Step 3: Addition } \implies 10 + 12 = 22
$$

---

### 📌 Question 6: Variable Value Swapping Without Temporary Variable

#### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. User se do numbers (`a` aur `b`) input lene hain.
2. Dono ki values ko aapas mein badalna (swap karna) hai.
3. Pythonic tuple unpacking (`a, b = b, a`) aur mathematical arithmetic method dono se swap karke dikhana hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Input Lena):** Maan lijiye user ne $a = 10$ aur $b = 20$ diya.
- **Point 2 (Value Swap Karna):** Swapping ke baad $a$ ki value $20$ honi chahiye aur $b$ ki value $10$.
- **Point 3 (Bina Extra Variable Ke Methods):** Ek Pythonic tarika hai tuple unpacking (`a, b = b, a`). Doosra mathematical tarika hai addition aur subtraction use karke bina teesre variable ke swap karna.

#### 📐 Mathematical & Algorithmic Formulation
Arithmetic Swap Proof:

$$
a_1 = a_0 + b_0
$$

$$
b_1 = a_1 - b_0 = (a_0 + b_0) - b_0 = a_0
$$

$$
a_2 = a_1 - b_1 = (a_0 + b_0) - a_0 = b_0
$$

---

### 📌 Question 7: Celsius to Fahrenheit Temperature Converter

#### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. User se Celsius mein temperature input lena hai (string format mein).
2. Input string ko floating-point number mein convert karna hai.
3. Conversion formula apply karke temperature ko Fahrenheit mein calculate aur display karna hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Celsius Input):** User se prompt karke Celsius value maangiye.
- **Point 2 (Float Parsing):** `float()` function se use decimal number banayein.
- **Point 3 (Formula Application):** Standard formula $F = (C \times 9/5) + 32$ lagayein aur temperature degree Fahrenheit ($^\circ\text{F}$) mein print karein.

#### 📐 Mathematical & Algorithmic Formulation
Linear affine temperature transformation:

$$
T_F = \left(T_C \times \frac{9}{5}\right) + 32
$$

---

### 📌 Question 8: Circle Area Geometric Calculation

#### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. User se circle ka radius ($r$) input lena hai aur use float mein cast karna hai.
2. Circle ke area ka formula $A = \pi r^2$ use karke area nikalna hai (jahan $\pi = 3.14$).
3. Area ko properly format karke console par display karna hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Radius Input):** User se radius $r$ lijiye aur verify kijiye ki radius non-negative ho ($r \ge 0$).
- **Point 2 (Formula Calculation):** Power operator `r ** 2` use karein aur use constant $3.14$ se multiply karein.
- **Point 3 (Output):** Calculated area ko do decimal places tak format karke print karein.

#### 📐 Mathematical & Algorithmic Formulation
Area of a circular disk of radius $r$:

$$
A = \pi r^2 = 3.14 \times r^2
$$

---

### 📌 Question 9: Simple Interest Financial Calculation

#### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. User se teen financial values input leni hain: Principal ($P$), Annual Interest Rate ($R$), aur Time in years ($T$).
2. Sabhi inputs ko floating-point format mein parse karna hai.
3. Simple Interest calculate karna hai formula $\text{SI} = \frac{P \times R \times T}{100}$ se aur Total Amount ($A = P + \text{SI}$) print karna hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (3 Inputs Lena):** Mool-dhan ($P$), Byaaj dar ($R$), aur Samay ($T$) user se alag-alag prompts par lijiye.
- **Point 2 (Float Casting):** Teeno values ko `float()` mein convert karein taaki paise ya percentage decimal mein bhi calculate ho sakein.
- **Point 3 (Formula Evaluation):** Pehle $P \times R \times T$ ko multiply karein aur phir $100$ se divide karein. Final Amount ke liye Principal mein SI add karke print karein.

#### 📐 Mathematical & Algorithmic Formulation
Financial interest formulation:

$$
\text{SI} = \frac{P \times R \times T}{100}
$$

$$
A_{\text{total}} = P + \text{SI} = P \left(1 + \frac{R \times T}{100}\right)
$$

---

### 📌 Question 10: Decimal Number Integer & Fractional Part Separation

#### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. User se ek decimal number (jaise `45.78`) input lena hai aur use `float` mein convert karna hai.
2. Us number ka Integer Part (poora hissa, jaise `45`) alag nikalna hai.
3. Us number ka Fractional Part (decimal ke baad ka hissa, jaise `0.78` ya `.78`) alag nikalna hai aur dono ko print karna hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Decimal Input):** Decimal floating-point number user se input lijiye.
- **Point 2 (Integer Part Nikalna):** `int(num)` use karne se Python point ke baad ka hissa hata deta hai aur integer part de deta hai.
- **Point 3 (Fractional Part Nikalna):** Original number mein se integer part ko minus kar dijiye (`num - int(num)`), jisse bacha hua fractional hissa mil jayega.

#### 📐 Mathematical & Algorithmic Formulation
Floor and fractional decomposition:

$$
x_{\text{int}} = \lfloor x \rfloor = \text{int}(x)
$$

$$
x_{\text{frac}} = x - \lfloor x \rfloor
$$

---

## 🔬 Part 2: Advanced Systems & AI Engineering Case Studies

---

### 📌 Case Study 1: Numerical Stability & IEEE-754 Precision Mechanics

#### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. **IEEE-754 Representation Breakdown:** Mathematically explain kijiye ki binary floating point mein $0.1 + 0.2 \ne 0.3$ kyu hota hai.
2. **Machine Epsilon Definition:** 64-bit double precision float ke mantissa bits aur machine epsilon $\epsilon_{\text{mach}}$ ka formula aur value analyze kijiye.
3. **Catastrophic Cancellation Analysis:** AI/ML loss functions mein jab do lagbhag barabar numbers minus hote hain ($f(x) = \sqrt{x+1} - \sqrt{x}$ jab $x \gg 1$), toh precision collapse kyu hota hai?
4. **Stable Conjugation Reformulation:** Is loss function ko algebraically conjugate karke numerically stable form mein convert kijiye aur relative error verify kijiye.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Binary Floating Point ki Seema):** Jaise base-10 mein $1/3 = 0.3333\dots$ non-terminating hota hai, waise hi base-2 mein $0.1 = 1/10$ ek non-terminating repeating fraction hota hai ($0.0001100110011\dots_2$). Is wajah se roundoff error aata hai.
- **Point 2 (Machine Epsilon):** 64-bit float mein 52 bits mantissa ke hote hain. $\epsilon_{\text{mach}} = 2^{-52} \approx 2.22 \times 10^{-16}$ woh smallest difference hai jo 1.0 ke baad represent ho sakta hai.
- **Point 3 (Catastrophic Cancellation):** Jab $x = 10^{16}$ ho, toh $\sqrt{x+1}$ aur $\sqrt{x}$ ke starting ke saare digits same hote hain. Minus karne par significant digits udd jaate hain aur zero ya garbage bachta hai.
- **Point 4 (Numerically Stable Formula):** Numerator aur denominator ko $(\sqrt{x+1} + \sqrt{x})$ se multiply karke subtraction ko division mein badal diya jata hai, jisse floating point arithmetic $100\%$ accurate rehti hai.

#### 📐 Mathematical & Algorithmic Formulation
Catastrophic cancellation in naive formulation:

$$
f_{\text{naive}}(x) = \sqrt{x + 1} - \sqrt{x}
$$

Conjugate algebraic stable formulation:

$$
f_{\text{stable}}(x) = \frac{(\sqrt{x+1} - \sqrt{x})(\sqrt{x+1} + \sqrt{x})}{\sqrt{x+1} + \sqrt{x}} = \frac{(x + 1) - x}{\sqrt{x+1} + \sqrt{x}} = \frac{1}{\sqrt{x+1} + \sqrt{x}}
$$

Machine Epsilon definition:

$$
\epsilon_{\text{mach}} = 2^{-52} \approx 2.2204 \times 10^{-16}
$$

Relative error:

$$
\text{Relative Error}(x) = \frac{|f_{\text{naive}}(x) - f_{\text{stable}}(x)|}{f_{\text{stable}}(x)}
$$

---

### 📌 Case Study 2: CPython Integer Memory Optimization & Object Identity Dynamics

#### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. **Small Integer Caching Architecture:** CPython ke `small_ints` array range $[-5, 256]$ ki memory architecture aur pre-allocation logic explain kijiye.
2. **`is` vs `==` Semantics:** Pointer memory identity (`is`) aur value equality (`==`) ke mathematical fark ko formalize kijiye.
3. **Arbitrary Precision Representation:** Python 3 ke `PyLongObject` mein bade integers ($> 2^{64}$) kaise store hote hain (30-bit digit arrays, base $2^{30}$).
4. **Memory Verification:** CPython runtime par script likh kar prove kijiye ki $256$ tak `is` true rehta hai aur $257$ par naya heap object banta hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Small Int Cache):** Python interpreter jab boot hota hai, toh woh $-5$ se lekar $256$ tak ke integers ke liye 262 singleton objects pehle se memory mein bana kar rakh leta hai taaki loop indexers aur counters baar-baar naye object na banayein.
- **Point 2 (`is` vs `==`):** `a == b` check karta hai ki dono dabbon ke andar rakhi value barabar hai ya nahi. `a is b` check karta hai ki kya $a$ aur $b$ dono memory ke ek hi address (`id(a) == id(b)`) ki taraf point kar rahe hain.
- **Point 3 (Bade Integers Ka Structure):** C language mein integer 32 ya 64 bits par overflow ho jata hai, par Python mein integer arbitrary-precision hota hai jo multiple 30-bit limbs (digits) ko chain karke unlimited bada number store kar sakta hai.
- **Point 4 (Runtime Verification):** `a = 256; b = 256; print(a is b)` True aayega, lekin `a = 257; b = 257; print(a is b)` False aayega (interactive terminal mein), jo CPython ke cache boundary ko prove karta hai.

#### 📐 Mathematical & Algorithmic Formulation
Memory identity condition:

$$
a \equiv b \iff \text{id}(a) == \text{id}(b) \implies a \text{ is } b
$$

Value equivalence condition:

$$
a = b \iff \text{val}(a) == \text{val}(b) \implies a == b
$$

Cache membership predicate:

$$
\text{Cached}(n) = \begin{cases} 
\text{True} & \text{if } -5 \le n \le 256 \\
\text{False} & \text{otherwise}
\end{cases}
$$

---

### 📌 Case Study 3: Short-Circuit Logical Evaluation & Branch Prediction Mechanics

#### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. **Boolean Lattice & Short-Circuit Theorem:** Formal Boolean algebra mein $A \land B$ aur $A \lor B$ ke short-circuit evaluation rules ko define kijiye.
2. **Defensive Guarded Execution Pattern:** Python mein `obj is not None and obj.is_valid()` pattern `AttributeError` aur `ZeroDivisionError` se kaise bachata hai, explain kijiye.
3. **CPU Pipeline Branch Prediction Impact:** Modern superscalar CPU pipelines mein short-circuit branches ke misprediction penalty ($15-20$ cycles) aur speculative execution dynamics ko evaluate kijiye.
4. **Bypass Efficiency Metric:** Agar first predicate ke true hone ki probability $P(A)$ ho, toh second expensive predicate ke bypass hone ka mathematical rate calculate kijiye.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Short-Circuit Ka Niyam):** `A and B` mein agar $A$ false ho gaya, toh result hamesha false hi hoga chahe $B$ kuch bhi ho, isliye Python $B$ ko run hi nahi karta. Isi tarah `A or B` mein agar $A$ true hai, toh $B$ ko check nahi kiya jata.
- **Point 2 (Defensive Coding):** Agar koi object `None` ho sakta hai, toh pehle check karein `obj is not None and obj.method()`. Agar object `None` hua, toh doosra part run hi nahi hoga aur code crash hone se bach jayega.
- **Point 3 (Hardware Pipeline Impact):** CPU pehle se andaza lagata hai ki condition True hogi ya False (Branch Prediction). Agar CPU ka andaza galat nikla, toh poora pipeline flush karna padta hai jismein 15 se 20 clock cycles barbaad hote hain.
- **Point 4 (Bypass Savings):** Agar fast condition pehle laga di jaye jiska bypass probability high ho, toh expensive database ya network calls ko $90\%+$ cases mein execute hone se roka ja sakta hai.

#### 📐 Mathematical & Algorithmic Formulation
Conditional execution probability under short-circuit evaluation:

$$
P(\text{eval}(B) \mid A \land B) = P(A = \text{True})
$$

$$
P(\text{bypass}(B) \mid A \land B) = P(A = \text{False}) = 1 - P(A = \text{True})
$$

For disjunction ($A \lor B$):

$$
P(\text{eval}(B) \mid A \lor B) = P(A = \text{False})
$$

$$
P(\text{bypass}(B) \mid A \lor B) = P(A = \text{True})
$$

Expected execution cost given operational latencies $C_A, C_B$:

$$
\mathbb{E}[C_{A \land B}] = C_A + P(A = \text{True}) \cdot C_B
$$
