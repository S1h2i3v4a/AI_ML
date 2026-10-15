# 🎯 Lecture 02: Practice Problems & Systems Engineering Suite

[![Course](https://img.shields.io/badge/Course-Apna_College_Prime_AI_ML-red.svg)](#)
[![Module](https://img.shields.io/badge/Module-Python_Foundations-blue.svg)](#)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

🌐 **Language Navigation:** [English Guide](README.md) | [हिंदी / Hinglish Guide](README_HINGLISH.md)

---

## 📌 Suite Architecture & Navigation

This practice suite provides end-to-end problems bridging the gap between basic Python syntax and production systems engineering. It includes the complete **10 Official Assignment Problems** from Apna College plus **3 Advanced Engineering Case Studies**.

```plaintext
Practice_Problems/
├── README.md                             # Suite Overview (English)
├── README_HINGLISH.md                    # Suite Overview (Hinglish)
├── Questions/
│   ├── README.md                         # English Problem Statements
│   ├── README_HINGLISH.md                # Hinglish Problem Statements & Clear Deliverables
│   ├── questions.ipynb                   # Executable Starter Notebook
│   └── questions.pdf                     # Vector-Grade Printable PDF
└── Solutions/
    ├── README.md                         # Exhaustive English Solutions Guide
    ├── README_HINGLISH.md                # Exhaustive Hinglish Guide + Formal Proofs
    ├── solutions.ipynb                   # Fully Executed & Populated Solutions Notebook
    ├── solutions.pdf                     # Vector-Grade Printable PDF
    ├── case1_floating_point_cancellation_error.png # 300 DPI IEEE-754 Precision Analysis
    ├── case2_small_int_caching_and_identity.png    # 300 DPI CPython Integer Caching Plot
    └── case3_short_circuit_branch_evaluation.png   # 300 DPI Short-Circuit & Branch Optimization
```

---

## 📊 Problem Inventory & Classification

| ID | Title | Domain | Core Challenge |
| :--- | :--- | :--- | :--- |
| **Q1** | User Greeting String Formatting | I/O & Formatting | F-string interpolation with dynamic type casting |
| **Q2** | Basic Arithmetic Calculator | Arithmetic Operators | Multi-operator pipeline ($+$, $-$, $*$, $/$) with float division |
| **Q3** | Heterogeneous Float Average | Type Promotion | Casting 2 ints and 1 float to calculate exact arithmetic mean |
| **Q4** | String Number Ingestion & Casting | Type Invariants | Parsing string `"45"`, converting across types, type introspection |
| **Q5** | Operator Precedence Evaluation | AST Hierarchy | Tracing $10 + 3 \times 2^2$ step-by-step according to Python precedence |
| **Q6** | Variable Value Swapping | Memory Semantics | Swapping values via tuple unpacking vs algebraic vs XOR |
| **Q7** | Celsius to Fahrenheit Converter | Formula Translation | Implementing $F = (C \times 9/5) + 32$ with precision guarantees |
| **Q8** | Circle Area Geometric Engine | Geometry & Constants | Computing $A = \pi r^2$ with explicit type handling |
| **Q9** | Simple Interest Financial Kernel | Financial Mathematics | Evaluating $\text{SI} = (P \times R \times T) / 100$ |
| **Q10** | Decimal Integer & Fractional Split | Number Theory | Separating $\lfloor x \rfloor$ and fractional offset $x - \lfloor x \rfloor$ |
| **Case 1** | IEEE-754 Precision & Cancellation | Numerical Analysis | Floating-point error analysis and algebraic conjugation |
| **Case 2** | CPython Small Int Caching | Memory Architecture | Pre-allocated `[-5, 256]` singleton cache and `is` vs `==` semantics |
| **Case 3** | Short-Circuit Logic & Branch Evaluation | Boolean Algebra | Short-circuit evaluation guarantees and guarded execution patterns |
