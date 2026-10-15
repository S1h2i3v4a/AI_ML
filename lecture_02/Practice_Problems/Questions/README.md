# 📋 Lecture 02: Practice Problems — Technical Problem Specifications

[![Language: English](https://img.shields.io/badge/Language-English-blue.svg)](#)
[![Status: Compliant](https://img.shields.io/badge/MathJax-100%25_Compliant-brightgreen.svg)](#)

This document contains the complete problem specifications for **Lecture 02: Python Fundamentals (Part-1)**, including the 10 Official Assignment Problems from Apna College and 3 Systems Engineering Case Studies.

---

## 📝 Part 1: Official Assignment Problems (Q1 - Q10)

---

### 📌 Problem 1: User Greeting String Formatting
Write a program that prompts the user for their name and age, then constructs and prints a formatted greeting sentence:
`"Hello <name>, you are <age> years old!"`

#### Input / Output Contract:
- **Input:** String `name`, String `age`.
- **Output:** Formatted sentence printed to `sys.stdout`.

---

### 📌 Problem 2: Two Numbers Basic Arithmetic Calculator
Take two numeric values as user input and compute their Sum, Difference, Product, and Quotient.

#### Mathematical Invariant:
For $a, b \in \mathbb{R}$ with $b \ne 0$:

$$
\text{Sum} = a + b, \quad \text{Diff} = a - b, \quad \text{Prod} = a \times b, \quad \text{Quot} = \frac{a}{b}
$$

---

### 📌 Problem 3: Heterogeneous Numbers Float Average
Prompt the user for two integers and one floating-point number. Explicitly cast all three operands to `float` and compute their arithmetic mean.

#### Mathematical Invariant:
For $x_1, x_2 \in \mathbb{Z}$ and $x_3 \in \mathbb{R}$:

$$
\mu = \frac{\text{float}(x_1) + \text{float}(x_2) + x_3}{3.0}
$$

---

### 📌 Problem 4: String Number Ingestion & Multi-Type Casting
Prompt the user for a numeric string (e.g., `"45"`). Convert the value sequentially:
1. To an integer (`int`)
2. To a float (`float`)
3. Back to a string (`str`)
Display each transformed value alongside its runtime type signature (`type()`).

---

### 📌 Problem 5: Operator Precedence Evaluation Trace
Evaluate the expression `x = 10 + 3 * 2 ** 2` in Python. Explain step-by-step why the emitted result is $22$ according to CPython's Abstract Syntax Tree operator binding hierarchy.

#### Mathematical Precedence Chain:

$$
\text{Step 1: } 2^2 = 4 \quad (\text{Exponentiation Priority})
$$

$$
\text{Step 2: } 3 \times 4 = 12 \quad (\text{Multiplication Priority})
$$

$$
\text{Step 3: } 10 + 12 = 22 \quad (\text{Addition Priority})
$$

---

### 📌 Problem 6: Variable Value Swapping
Implement value swapping between two variables without allocating a third intermediate temporary variable. Contrast Python's tuple unpacking with arithmetic and bitwise methods.

#### Algebraic Invariant:

$$
a \gets a + b, \quad b \gets a - b, \quad a \gets a - b
$$

---

### 📌 Problem 7: Celsius to Fahrenheit Converter
Prompt the user for temperature in Celsius (string input), parse it into a floating-point number, and calculate temperature in Fahrenheit.

#### Mathematical Transformation:

$$
T_F = \left(T_C \times \frac{9}{5}\right) + 32
$$

---

### 📌 Problem 8: Circle Area Geometric Calculation
Take circle radius $r$ as input and compute the total disk surface area assuming $\pi = 3.14$.

#### Mathematical Formulation:

$$
A = \pi r^2 = 3.14 \times r^2
$$

---

### 📌 Problem 9: Simple Interest Financial Calculation
Prompt for Principal ($P$), Annual Rate ($R$), and Time ($T$). Convert all to float and compute Simple Interest and final maturity balance.

#### Mathematical Formulation:

$$
\text{SI} = \frac{P \times R \times T}{100}, \quad A = P + \text{SI}
$$

---

### 📌 Problem 10: Decimal Integer & Fractional Part Separation
Take a decimal number as input (e.g., `45.78`) and separate it into its integer component $\lfloor x \rfloor$ and fractional component $x - \lfloor x \rfloor$.

#### Mathematical Decomposition:

$$
x_{\text{int}} = \lfloor x \rfloor, \quad x_{\text{frac}} = x - \lfloor x \rfloor
$$

---

## 🔬 Part 2: Advanced Systems Engineering Case Studies

---

### 📌 Case Study 1: Numerical Stability & IEEE-754 Precision Mechanics
1. Analyze why $0.1 + 0.2 \ne 0.3$ in 64-bit IEEE-754 binary floating-point representation.
2. Define Machine Epsilon $\epsilon_{\text{mach}} = 2^{-52} \approx 2.22 \times 10^{-16}$.
3. Demonstrate Catastrophic Cancellation in naive loss formulations:

$$
f_{\text{naive}}(x) = \sqrt{x+1} - \sqrt{x}
$$

4. Derive the algebraically conjugate stable formulation:

$$
f_{\text{stable}}(x) = \frac{1}{\sqrt{x+1} + \sqrt{x}}
$$

---

### 📌 Case Study 2: CPython Integer Memory Optimization & Object Identity
1. Explain CPython's `small_ints` array singleton caching architecture for integers in the range $[-5, 256]$.
2. Formalize pointer identity equality (`is`) vs value equality (`==`).
3. Describe arbitrary-precision integer representation (`PyLongObject` digit arrays base $2^{30}$).

---

### 📌 Case Study 3: Short-Circuit Logical Evaluation & Branch Prediction
1. Formalize Boolean short-circuit evaluation for $A \land B$ and $A \lor B$.
2. Implement defensive guarded access patterns (`obj is not None and obj.is_valid()`).
3. Analyze CPU pipeline branch misprediction penalty ($15-20$ clock cycles) and derive the expected evaluation cost:

$$
\mathbb{E}[C_{A \land B}] = C_A + P(A = \text{True}) \cdot C_B
$$
