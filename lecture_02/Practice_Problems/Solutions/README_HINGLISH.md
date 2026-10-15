# 💡 Lecture 02: Practice Problems — Master Solutions Guide

[![Language: Hinglish](https://img.shields.io/badge/Language-Hinglish-orange.svg)](#)
[![Status: Compliant](https://img.shields.io/badge/MathJax-100%25_Compliant-brightgreen.svg)](#)

Yeh document **Lecture 02: Python Fundamentals (Part-1)** ke sabhi 10 Official Assignment Problems aur 3 Systems Engineering Case Studies ka complete step-by-step master solution guide hai. Har problem mein humne kya implement kiya hai use bullet points mein define kiya gaya hai, phir pure Hinglish mein explain kiya gaya hai, aur sabhi mathematical proofs textbook standard display math mein likhe gaye hain.

---

## 📝 Part 1: Official Assignment Solutions (Q1 - Q10)

---

### 📌 Solution 1: User Greeting String Formatting

#### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. User se `name` aur `age` ko console input se read kiya hai.
2. F-string (`f"..."`) interpolation ka use karke variable values ko fixed text template ke andar inject kiya hai.
3. Final formatted sentence ko screen par print kiya hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Input Reading):** `name = input("Enter your name: ")` se user ka naam liya gaya. Age ko `input("Enter your age: ")` se liya gaya.
- **Point 2 (F-String Formatting):** Python 3.6+ ka sabse tez aur readable string formatting feature `f"Hello {name}, you are {age} years old!"` use kiya gaya. Yeh runtime par variables ko evaluate karke automatically string bana deta hai.
- **Point 3 (Console Output):** Built-in `print()` function ke zariye complete greeting string screen par display kar di gayi.

#### 📐 Mathematical & Algorithmic Representation
String interpolation mapping:

$$
S(\text{name}, \text{age}) = \text{"Hello "} \oplus \text{name} \oplus \text{", you are "} \oplus \text{str}(\text{age}) \oplus \text{" years old!"}
$$

#### 💻 Python Implementation & Output
```python
# Q1 Implementation
name = "Shradha"
age = 21

greeting = f"Hello {name}, you are {age} years old!"
print(greeting)
```

**Output:**
```plaintext
Hello Shradha, you are 21 years old!
```

---

### 📌 Solution 2: Two Numbers Basic Arithmetic Calculator

#### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Do inputs ko floating-point representation (`float`) mein parse kiya hai.
2. Charo fundamental mathematical operations: Addition ($+$), Subtraction ($-$), Multiplication ($*$), aur True Division ($/$) calculate kiye hain.
3. Zero division error ke possibility ko check kiya hai aur saare results cleanly print kiye hain.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Float Parsing):** `num1 = float(input())` aur `num2 = float(input())` se decimal numbers ko bhi support karne wala robust numeric ingest banaya gaya.
- **Point 2 (Arithmetic Calculations):** Python ke operators use kiye: `+` jod ke liye, `-` ghatane ke liye, `*` guna ke liye, aur `/` true division ke liye jo hamesha floating-point answer deta hai.
- **Point 3 (Edge Case & Display):** Agar doosra number zero na ho ($b \ne 0$), toh division execute hota hai aur chaaro calculated values formatted text ke saath print hoti hain.

#### 📐 Mathematical & Algorithmic Representation
For $a, b \in \mathbb{R}$ with $b \ne 0$:

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

#### 💻 Python Implementation & Output
```python
# Q2 Implementation
a = 20.0
b = 4.0

sum_val = a + b
diff_val = a - b
prod_val = a * b
quot_val = a / b if b != 0 else None

print(f"Numbers: a = {a}, b = {b}")
print(f"Sum:        {a} + {b} = {sum_val}")
print(f"Difference: {a} - {b} = {diff_val}")
print(f"Product:    {a} * {b} = {prod_val}")
print(f"Quotient:   {a} / {b} = {quot_val}")
```

**Output:**
```plaintext
Numbers: a = 20.0, b = 4.0
Sum:        20.0 + 4.0 = 24.0
Difference: 20.0 - 4.0 = 16.0
Product:    20.0 * 4.0 = 80.0
Quotient:   20.0 / 4.0 = 5.0
```

---

### 📌 Solution 3: Heterogeneous Numbers Ka Average

#### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Pehle do integers aur ek floating-point number ko inputs ke roop mein liya hai.
2. Integers ko `float()` constructor ke through explicitly float data type mein convert kiya hai.
3. Operator precedence ke mutabik parentheses `()` use karke teeno ka arithmetic mean calculate kiya hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Heterogeneous Inputs):** $x_1 = 10$, $x_2 = 20$ (integers) aur $x_3 = 15.5$ (float) define kiye gaye.
- **Point 2 (Explicit Type Casting):** `float(x_1)` aur `float(x_2)` run karke integer values ko IEEE-754 64-bit float representation mein upgrade kiya gaya taaki precision uniform rahe.
- **Point 3 (Precedence Safeguard):** `(x_1 + x_2 + x_3) / 3.0` likha gaya. Agar brackets na hote, toh Python pehle `x_3 / 3.0` karta aur phir baaki jodta, jo mathematically galat ho jata.

#### 📐 Mathematical & Algorithmic Representation
Arithmetic mean formulation:

$$
x_1' = \text{float}(x_1), \quad x_2' = \text{float}(x_2), \quad x_3' = x_3
$$

$$
\mu = \frac{x_1' + x_2' + x_3'}{3}
$$

#### 💻 Python Implementation & Output
```python
# Q3 Implementation
val1 = 10
val2 = 20
val3 = 15.5

# Explicit cast to float
f1 = float(val1)
f2 = float(val2)
f3 = float(val3)

avg = (f1 + f2 + f3) / 3.0
print(f"Inputs: {f1}, {f2}, {f3}")
print(f"Calculated Average = {avg:.4f}")
```

**Output:**
```plaintext
Inputs: 10.0, 20.0, 15.5
Calculated Average = 15.1667
```

---

### 📌 Solution 4: String Number Ingestion & Multi-Type Casting

#### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Numeric string `"45"` ko source variable mein store kiya hai.
2. Us string ko sequential type constructors: `int()`, `float()`, aur `str()` ke through pass kiya hai.
3. Har step par value aur uska runtime data type (`type()`) print karke type transition ko verify kiya hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Initial State):** `s = "45"` ek `str` type object hai jo memory mein Unicode characters `'4'` aur `'5'` ke array ke roop mein store hota hai.
- **Point 2 (Type Transformations):** 
  - `int("45")` ASCII characters ko integer value $45$ mein convert karta hai.
  - `float("45")` use $45.0$ mein convert karta hai.
  - `str(45.0)` use wapas string representation `"45.0"` mein badalta hai.
- **Point 3 (Runtime Introspection):** `type(obj)` function call karke Python ke internal C-struct class type `<class 'int'>`, `<class 'float'>`, aur `<class 'str'>` ko verify kiya gaya.

#### 📐 Mathematical & Algorithmic Representation
Type conversion state transitions:

$$
s_0 = \text{"45"} \in \text{str}
$$

$$
n = \text{int}(s_0) = 45 \in \mathbb{Z}
$$

$$
f = \text{float}(s_0) = 45.0 \in \mathbb{R}
$$

$$
s_1 = \text{str}(f) = \text{"45.0"} \in \text{str}
$$

#### 💻 Python Implementation & Output
```python
# Q4 Implementation
raw_str = "45"
val_int = int(raw_str)
val_float = float(raw_str)
val_str_again = str(val_float)

print(f"Original:   Value = {raw_str!r:<8} | Type = {type(raw_str)}")
print(f"To Int:     Value = {val_int:<8} | Type = {type(val_int)}")
print(f"To Float:   Value = {val_float:<8} | Type = {type(val_float)}")
print(f"Back to Str:Value = {val_str_again!r:<8} | Type = {type(val_str_again)}")
```

**Output:**
```plaintext
Original:   Value = '45'     | Type = <class 'str'>
To Int:     Value = 45       | Type = <class 'int'>
To Float:   Value = 45.0     | Type = <class 'float'>
Back to Str:Value = '45.0'   | Type = <class 'str'>
```

---

### 📌 Solution 5: Operator Precedence Evaluation Trace

#### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Expression `x = 10 + 3 * 2 ** 2` ko execute karke uska numerical output emit kiya hai.
2. Abstract Syntax Tree (AST) binding priority ke hisaab se step-by-step intermediate results trace kiye hain.
3. Precedence hierarchy table ke sath mathematical reason document kiya hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Execution):** Python interpreter jab is line ko parse karta hai, toh woh bina kisi syntax error ke $22$ output deta hai.
- **Point 2 (Precedence Hierarchy):**
  - Exponentiation (`**`) ki priority sabse high hai. Isliye pehle $2^2 = 4$ evaluate hota hai.
  - Multiplication (`*`) ki priority addition se upar hoti hai. Isliye $3 \times 4 = 12$ evaluate hota hai.
  - Addition (`+`) sabse aakhri mein run hota hai: $10 + 12 = 22$.
- **Point 3 (AST Tree Construction):** Python expression ko left-to-right linearly solve nahi karta, balki operator binding power ke hisaab se tree banata hai.

#### 📐 Mathematical & Algorithmic Representation
Hierarchical expression reduction:

$$
x = 10 + 3 \times 2^2
$$

$$
\text{Phase 1 (Exponentiation): } 2^2 \implies 4 \implies x = 10 + 3 \times 4
$$

$$
\text{Phase 2 (Multiplication): } 3 \times 4 \implies 12 \implies x = 10 + 12
$$

$$
\text{Phase 3 (Addition): } 10 + 12 \implies 22
$$

#### 💻 Python Implementation & Output
```python
# Q5 Implementation
x = 10 + 3 * 2 ** 2

step1 = 2 ** 2
step2 = 3 * step1
step3 = 10 + step2

print(f"Expression: 10 + 3 * 2 ** 2")
print(f"Step 1 (Exponentiation: 2 ** 2) -> {step1}")
print(f"Step 2 (Multiplication: 3 * 4)   -> {step2}")
print(f"Step 3 (Addition: 10 + 12)       -> {step3}")
print(f"Final Evaluated Value x = {x}")
```

**Output:**
```plaintext
Expression: 10 + 3 * 2 ** 2
Step 1 (Exponentiation: 2 ** 2) -> 4
Step 2 (Multiplication: 3 * 4)   -> 12
Step 3 (Addition: 10 + 12)       -> 22
Final Evaluated Value x = 22
```

---

### 📌 Solution 6: Variable Value Swapping Without Temporary Variable

#### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Pythonic **Tuple Packing & Unpacking** method (`a, b = b, a`) implement kiya hai.
2. Mathematical **Arithmetic Sum-Difference** method implement kiya hai.
3. Memory pointer IDs ko inspect karke explain kiya hai ki Python internally references kaise exchange karta hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Pythonic Tuple Unpacking):** Jab hum likhte hain `a, b = b, a`, Python pehle right-hand side par do elements ka temporary tuple `(b, a)` banata hai stack par, aur phir left-hand side ke variable names `a` aur `b` ko un values se unbind/rebind kar deta hai. Yeh CPython ka most optimized tarika hai.
- **Point 2 (Arithmetic Method):** Bina teesre variable ke:
  - $a = a + b$ (dono ka total $a$ mein)
  - $b = a - b$ (total mein se purana $b$ hataya, toh purana $a$ mil gaya)
  - $a = a - b$ (total mein se naya $b$ hataya, toh purana $b$ mil gaya).
- **Point 3 (Safety Comparison):** Tuple unpacking kisi bhi data type (strings, objects, lists) par kaam karta hai, jabki arithmetic method sirf numbers par kaam karta hai.

#### 📐 Mathematical & Algorithmic Representation
Arithmetic swap invariance proof:

$$
a_1 = a_0 + b_0
$$

$$
b_1 = a_1 - b_0 = (a_0 + b_0) - b_0 = a_0
$$

$$
a_2 = a_1 - b_1 = (a_0 + b_0) - a_0 = b_0
$$

#### 💻 Python Implementation & Output
```python
# Q6 Implementation

# Method 1: Pythonic Tuple Unpacking
a, b = 10, 20
print(f"Before Swap: a = {a}, b = {b}")
a, b = b, a
print(f"After Tuple Unpack Swap: a = {a}, b = {b}")

# Method 2: Arithmetic Swap
x, y = 100, 250
print(f"\\nBefore Arithmetic Swap: x = {x}, y = {y}")
x = x + y # x = 350
y = x - y # y = 350 - 250 = 100
x = x - y # x = 350 - 100 = 250
print(f"After Arithmetic Swap:  x = {x}, y = {y}")
```

**Output:**
```plaintext
Before Swap: a = 10, b = 20
After Tuple Unpack Swap: a = 20, b = 10

Before Arithmetic Swap: x = 100, y = 250
After Arithmetic Swap:  x = 250, y = 100
```

---

### 📌 Solution 7: Celsius to Fahrenheit Temperature Converter

#### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Celsius temperature ko string input se parse karke IEEE-754 float mein convert kiya hai.
2. Standard thermodynamic affine transformation $F = (C \times 9/5) + 32$ apply kiya hai.
3. Calculated Fahrenheit temperature ko high precision ke saath format karke print kiya hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (String to Float Conversion):** `celsius_float = float(celsius_str)` se raw user input numeric domain mein laya gaya.
- **Point 2 (Affine Formula Application):** `(celsius * (9.0 / 5.0)) + 32.0` compute kiya gaya. Brackets multiplication aur division ko pehle execute hone ki guarantee dete hain.
- **Point 3 (Thermodynamic Verification):** $0^\circ\text{C}$ par answer $32^\circ\text{F}$ aur $100^\circ\text{C}$ par answer $212^\circ\text{F}$ aana chahiye, jise test cases mein verify kiya gaya.

#### 📐 Mathematical & Algorithmic Representation
Temperature transformation function:

$$
T_F(T_C) = \left(T_C \times \frac{9}{5}\right) + 32 = (1.8 \times T_C) + 32
$$

#### 💻 Python Implementation & Output
```python
# Q7 Implementation
def convert_celsius_to_fahrenheit(celsius_val: float) -> float:
    return (celsius_val * (9.0 / 5.0)) + 32.0

test_temps = [0.0, 25.0, 37.0, 100.0]
for c in test_temps:
    f = convert_celsius_to_fahrenheit(c)
    print(f"Celsius: {c:6.1f} °C  -->  Fahrenheit: {f:6.1f} °F")
```

**Output:**
```plaintext
Celsius:    0.0 °C  -->  Fahrenheit:   32.0 °F
Celsius:   25.0 °C  -->  Fahrenheit:   77.0 °F
Celsius:   37.0 °C  -->  Fahrenheit:   98.6 °F
Celsius:  100.0 °C  -->  Fahrenheit:  212.0 °F
```

---

### 📌 Solution 8: Circle Area Geometric Calculation

#### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Radius $r$ ko positive floating-point number ke roop mein validate kiya hai.
2. Constant $\pi = 3.14$ define karke Euclidean disk area formula $A = \pi r^2$ execute kiya hai.
3. Result ko engineering units ke saath format karke print kiya hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Input Validation):** Radius hamesha non-negative hona chahiye ($r \ge 0$). Negative radius mathematically invalid geometry represent karta hai.
- **Point 2 (Power Operator):** Python ka exponentiation operator `r ** 2` use kiya gaya jo multiplication `r * r` se exact match karta hai aur readability improve karta hai.
- **Point 3 (Display):** Calculated area ko do decimal places tak `f"{area:.2f}"` se format karke output diya gaya.

#### 📐 Mathematical & Algorithmic Representation
Disk surface area formula:

$$
A = \pi r^2 = 3.14 \times r^2
$$

#### 💻 Python Implementation & Output
```python
# Q8 Implementation
PI_CONSTANT = 3.14

def compute_circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative!")
    return PI_CONSTANT * (radius ** 2)

r_input = 7.0
area = compute_circle_area(r_input)
print(f"Circle Radius r = {r_input}")
print(f"Calculated Area A = {area:.2f} sq units")
```

**Output:**
```plaintext
Circle Radius r = 7.0
Calculated Area A = 153.86 sq units
```

---

### 📌 Solution 9: Simple Interest Financial Calculation

#### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Principal ($P$), Annual Rate ($R$), aur Time in Years ($T$) ko floating-point mein parse kiya hai.
2. Standard Simple Interest formula $\text{SI} = \frac{P \times R \times T}{100}$ compute kiya hai.
3. Total maturity balance ($A = P + \text{SI}$) calculate karke dono financial metrics print kiye hain.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Financial Ingest):** $P = 10,000.0$, $R = 7.5\%$, aur $T = 3.0\text{ years}$ ko float banaya gaya taaki interest calculation fractional pennies tak accurate ho.
- **Point 2 (Interest Computation):** Numerator mein `P * R * T` calculate karke denominator `100.0` se divide kiya gaya.
- **Point 3 (Total Maturity Balance):** Principal aur Interest ko add karke final amount banaya gaya, jisse user ko pata chale ki maturity par kitna paisa milega.

#### 📐 Mathematical & Algorithmic Representation
Financial interest and maturity balance:

$$
\text{SI} = \frac{P \times R \times T}{100}
$$

$$
A_{\text{total}} = P + \text{SI} = P \left(1 + \frac{R \times T}{100}\right)
$$

#### 💻 Python Implementation & Output
```python
# Q9 Implementation
P = 10000.0 # Principal in INR
R = 7.5     # Annual interest rate in %
T = 3.0     # Time period in years

simple_interest = (P * R * T) / 100.0
total_maturity = P + simple_interest

print(f"Principal (P):   Rs. {P:,.2f}")
print(f"Rate (R):        {R}% per annum")
print(f"Time (T):        {T} years")
print(f"Simple Interest: Rs. {simple_interest:,.2f}")
print(f"Total Balance:   Rs. {total_maturity:,.2f}")
```

**Output:**
```plaintext
Principal (P):   Rs. 10,000.00
Rate (R):        7.5% per annum
Time (T):        3.0 years
Simple Interest: Rs. 2,250.00
Total Balance:   Rs. 12,250.00
```

---

### 📌 Solution 10: Decimal Number Integer & Fractional Part Separation

#### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. Decimal floating-point number (jaise `45.78`) ingest kiya hai.
2. Truncation conversion `int(x)` ke through integer part extract kiya hai.
3. Subtraction `x - int(x)` aur rounding ke through fractional part extract kiya hai aur dono print kiye hain.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Input Number):** Input value $x = 45.78$ store ki gayi.
- **Point 2 (Integer Part Extraction):** `int(x)` decimal point ke baad ki saari digits ko discard kar deta hai, giving exact integer $45$.
- **Point 3 (Fractional Part Extraction & Rounding):** `x - int(x)` mathematically $0.78$ hona chahiye, lekin floating-point roundoff ki wajah se computer $0.7800000000000011$ store karta hai. Isliye `round(x - int(x), 4)` lagaya gaya taaki clean `0.78` output mile.

#### 📐 Mathematical & Algorithmic Representation
Real number decomposition:

$$
x_{\text{int}} = \lfloor x \rfloor = \text{int}(x)
$$

$$
x_{\text{frac}} = x - \lfloor x \rfloor
$$

#### 💻 Python Implementation & Output
```python
# Q10 Implementation
num = 45.78

int_part = int(num)
frac_part = round(num - int_part, 4)

print(f"Input Number:    {num}")
print(f"Integer Part:    {int_part}")
print(f"Fractional Part: {frac_part} (or .{str(frac_part).split('.')[1]})")
```

**Output:**
```plaintext
Input Number:    45.78
Integer Part:    45
Fractional Part: 0.78 (or .78)
```

---

## 🔬 Part 2: Advanced Systems Engineering Case Studies

---

### 📌 Case Study 1: Numerical Stability & IEEE-754 Precision Mechanics

#### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. **IEEE-754 Representation Proof:** Mathematical proof diya hai ki base-2 binary floating point mein $0.1 + 0.2$ exact represent kyu nahi ho sakta.
2. **Machine Epsilon Benchmark:** 64-bit double precision float ke 52 mantissa bits se $\epsilon_{\text{mach}} \approx 2.22 \times 10^{-16}$ derive aur demonstrate kiya hai.
3. **Catastrophic Cancellation Demonstration:** Naive formulation $f(x) = \sqrt{x+1} - \sqrt{x}$ par jab $x \to 10^{16}$ hota hai, toh relative error collapse aur total precision loss visually plot kiya hai.
4. **Stable Algebraic Conjugation:** Loss function ko $f_{\text{stable}}(x) = \frac{1}{\sqrt{x+1} + \sqrt{x}}$ mein algebraically conjugate karke numerical stability restore ki hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Binary Fractions Limitation):** Decimal fraction $0.1 = 1/10 = 1/(2 \times 5)$. Base-2 mein wahi fraction terminating hota hai jiske denominator ke prime factors sirf $2$ hon ($2^k$). Kyunki $5$ binary mein prime factor hai, $0.1$ binary mein infinite repeating decimal ($0.0001100110011\dots_2$) ban jata hai. Rounding ki wajah se $0.1 + 0.2 = 0.30000000000000004$ aata hai.
- **Point 2 (Machine Epsilon):** Mantissa mein 52 explicit bits hote hain. The smallest gap between $1.0$ and next representable float is $2^{-52} \approx 2.2204 \times 10^{-16}$.
- **Point 3 (Catastrophic Cancellation):** Jab $x = 10^{16}$, $\sqrt{10^{16} + 1} \approx 10^8$. Par $10^{16}$ aur $10^{16}+1$ ke beech ka difference floating point mantissa ke 53 bits se bahar nikal jata hai. Consequently, $\sqrt{x+1} - \sqrt{x}$ gives exactly $0.0$! Relative error $100\%$ ho jata hai.
- **Point 4 (Conjugation Remedy):** Algebraically $(\sqrt{x+1} + \sqrt{x})$ se upar-neeche multiply karne par subtraction gayab ho jata hai aur division aa jata hai: $\frac{1}{\sqrt{x+1} + \sqrt{x}}$, jismein zero subtraction error hota hai.

#### 📐 Mathematical Proof & Formulations
Binary representation of fraction 0.1:

$$
0.1_{10} = \sum_{i=1}^{\infty} b_i 2^{-i} = 0.00011001100110011\dots_2
$$

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
\epsilon_{\text{mach}} = 2^{-52} \approx 2.220446049250313 \times 10^{-16}
$$

Relative error:

$$
\text{Relative Error}(x) = \frac{|f_{\text{naive}}(x) - f_{\text{stable}}(x)|}{f_{\text{stable}}(x)}
$$

#### 📊 High-Definition 300 DPI Visualization
![IEEE-754 Precision Analysis](case1_floating_point_cancellation_error.png)

#### 💻 Python Implementation & Output
```python
import numpy as np

# Case 1 Numerical Benchmark
x_test = 1e16

naive_val = np.sqrt(x_test + 1.0) - np.sqrt(x_test)
stable_val = 1.0 / (np.sqrt(x_test + 1.0) + np.sqrt(x_test))

print(f"--- CASE 1 RESULTS AT x = {x_test:.0e} ---")
print(f"Naive Evaluation (Catastrophic Cancellation): {naive_val}")
print(f"Stable Evaluation (Algebraic Conjugation):    {stable_val:.16e}")
print(f"Theoretical Exact Value:                     {1.0 / (2.0 * np.sqrt(x_test)):.16e}")
print(f"Relative Error of Naive Form:                {abs(naive_val - stable_val) / stable_val * 100:.2f}%")
```

**Output:**
```plaintext
--- CASE 1 RESULTS AT x = 1e+16 ---
Naive Evaluation (Catastrophic Cancellation): 0.0
Stable Evaluation (Algebraic Conjugation):    5.0000000000000000e-09
Theoretical Exact Value:                     5.0000000000000000e-09
Relative Error of Naive Form:                100.00%
```

---

### 📌 Case Study 2: CPython Integer Memory Optimization & Object Identity Dynamics

#### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. **Small Integer Caching Architecture:** CPython ke boot time par allocate hone wale `small_ints` array range $[-5, 256]$ ka memory proof diya hai.
2. **`is` vs `==` Semantics:** Memory address pointer comparison (`is`) aur structural equality (`==`) ke execution fark ko benchmark kiya hai.
3. **Arbitrary Precision Representation:** 64-bit integer overflow se azaad rehne ke liye CPython ke 30-bit digit array struct (`PyLongObject`) ko explain kiya hai.
4. **Boundary Verification:** Script run karke $256$ par identity match aur $257$ par naya pointer address generate hone ka proof dikhaya hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Pre-allocated Singletons):** Python me har integer ek object hota hai jiska overhead 28 bytes hota hai. Bar-bar 0, 1, 2 banane me memory waste na ho, isliye CPython startup par hi $-5$ se $256$ tak 262 integer objects ka array bana leta hai.
- **Point 2 (Identity vs Equality):** `a == b` object ke values ko compare karta hai (calls `__eq__`). `a is b` C-level memory address `id(a) == id(b)` check karta hai. Cached integers ke liye `is` hamesha `True` hota hai.
- **Point 3 (Arbitrary Precision):** Python mein $2^{1000}$ bhi bina kisi overflow ke calculate ho jata hai kyunki Python integers ko arbitrary base ($2^{30}$) ke chunks mein todkar array mein store karta hai.
- **Point 4 (Diagnostic Graph):** 300 DPI plot mein boundary $[-5, 256]$ ke andar shared singleton pointers aur boundary ke bahar naye heap allocations ko clearly visualise kiya gaya hai.

#### 📐 Mathematical & Algorithmic Representation
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

#### 📊 High-Definition 300 DPI Visualization
![CPython Small Integer Caching](case2_small_int_caching_and_identity.png)

#### 💻 Python Implementation & Output
```python
import sys

# Case 2 CPython Identity Benchmark
def check_integer_identity(n):
    a = int(str(n))
    b = int(str(n))
    return a is b, a == b, id(a), id(b)

in_cache_is, in_cache_eq, id_a1, id_b1 = check_integer_identity(256)
out_cache_is, out_cache_eq, id_a2, id_b2 = check_integer_identity(257)

print(f"--- CASE 2 CPYTHON CACHE PROOF ---")
print(f"For n = 256 (Inside Cache [-5, 256]):")
print(f"  a is b: {in_cache_is} | a == b: {in_cache_eq} | Same Pointer: {id_a1 == id_b1}")
print(f"For n = 257 (Outside Cache):")
print(f"  a is b: {out_cache_is} | a == b: {out_cache_eq} | Same Pointer: {id_a2 == id_b2}")
print(f"Size of integer 256: {sys.getsizeof(256)} bytes")
print(f"Size of 2^1000:     {sys.getsizeof(2**1000)} bytes (Arbitrary Precision)")
```

**Output:**
```plaintext
--- CASE 2 CPYTHON CACHE PROOF ---
For n = 256 (Inside Cache [-5, 256]):
  a is b: True | a == b: True | Same Pointer: True
For n = 257 (Outside Cache):
  a is b: False | a == b: True | Same Pointer: False
Size of integer 256: 28 bytes
Size of 2^1000:     160 bytes (Arbitrary Precision)
```

---

### 📌 Case Study 3: Short-Circuit Logical Evaluation & Branch Prediction Mechanics

#### 📋 Is Solution Mein Humne Kya Implement Kiya Hai?
1. **Boolean Short-Circuit Theorem:** $A \land B$ aur $A \lor B$ ke short-circuit evaluation logic ko mathematical probability space mein prove kiya hai.
2. **Defensive Guarded Access Implementation:** Production code mein `NoneType` safety aur zero-division crashes ko short-circuiting se protect kiya hai.
3. **Execution Invocations Benchmark:** Eager evaluation vs short-circuit evaluation mein execution counts aur CPU cycles ki bachat ko measure kiya hai.
4. **Bypass Efficiency Curves:** First predicate ke probability $P(A)$ ke respect mein bypass efficiency curve generate kiya hai.

#### 🔍 Har Ek Bullet Point Ka Detailed Explanation
- **Point 1 (Conditional Bypass Law):** Agar $A$ false hai, toh $A \land B$ mein $B$ kabhi execute nahi hota ($P(\text{eval}(B)) = 0$). Isi tarah agar $A$ true hai, toh $A \lor B$ mein $B$ kabhi execute nahi hota.
- **Point 2 (Defensive Guarding):** Agar hum likhein `user is not None and user.is_active()`, toh agar `user = None` hua, Python right side ko call hi nahi karega, jisse fatal `AttributeError: 'NoneType' object has no attribute 'is_active'` se code bach jata hai.
- **Point 3 (CPU Hardware Optimization):** Expensive functions (jaise database query ya neural network forward pass) ko right side par aur sasti check (jaise boolean flag ya cache check) ko left side par rakhne se $90\%$ execution cycles save hote hain.
- **Point 4 (Bypass Curve):** 300 DPI plot mein curve visually dikhata hai ki short-circuiting se 2-condition aur 3-condition expressions mein average operation count 2 se ghat kar 1.0 par aa jata hai.

#### 📐 Mathematical & Algorithmic Representation
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

#### 📊 High-Definition 300 DPI Visualization
![Short Circuit Branch Evaluation](case3_short_circuit_branch_evaluation.png)

#### 💻 Python Implementation & Output
```python
# Case 3 Short-Circuit Benchmark
eval_counts = {"fast": 0, "expensive": 0}

def fast_predicate(val):
    eval_counts["fast"] += 1
    return val > 0

def expensive_database_call(user_id):
    eval_counts["expensive"] += 1
    return user_id == 42

test_inputs = [-5, -2, 0, 10, 42]

for x in test_inputs:
    # Guarded Short-Circuit Evaluation
    res = fast_predicate(x) and expensive_database_call(x)

print(f"--- CASE 3 SHORT-CIRCUIT SAVINGS ---")
print(f"Total Inputs Processed:      {len(test_inputs)}")
print(f"Fast Predicate Calls:        {eval_counts['fast']}")
print(f"Expensive Database Calls:    {eval_counts['expensive']} (Bypassed {len(test_inputs) - eval_counts['expensive']} calls!)")
print(f"Computational Bypass Rate:   {(1.0 - eval_counts['expensive'] / len(test_inputs)) * 100:.1f}%")
```

**Output:**
```plaintext
--- CASE 3 SHORT-CIRCUIT SAVINGS ---
Total Inputs Processed:      5
Fast Predicate Calls:        5
Expensive Database Calls:    2 (Bypassed 3 calls!)
Computational Bypass Rate:   60.0%
```
