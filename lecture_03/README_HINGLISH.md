# Lecture 03: Python Fundamentals (Part 2 — Conditionals, Loops Aur Functions) (हिंग्लिश)

**Lecture 03: Python Fundamentals (Part 2)** ke master curriculum document mein aapka swagat hai. Yeh module Python ke control flow branching (`if/elif/else`, `match/case`), indefinite aur definite looping (`while`, `for`, `range`), iterator protocol, functions architecture (`def`, scope, `PyFrameObject`), aur modular coding ko first-principles se cover karta hai.

---

## 📂 Module Ki Sanrachna (Folder Architecture)

```text
lecture_03/
├── Notes_03.01/ to Notes_03.18/    # 18 Detailed Submodules (README.md, README_HINGLISH.md, notes.pdf, .ipynb)
├── Practice_Problems/             # Assignment 2 & Systems Engineering Case Studies Suite
│   ├── Questions/                 # Problem Statements (README.md, README_HINGLISH.md, questions.ipynb, questions.pdf)
│   └── Solutions/                 # Master Solutions (README.md, README_HINGLISH.md, solutions.ipynb, solutions.pdf, 300DPI plots)
├── Python_Fundamentals_Assignment2.pdf # Official Assignment Sheet
├── Python_Fundamentals_Part2.pdf       # Official Slide Deck
├── Topic_List.jpg                     # Official Lecture Index Image
├── README.md                          # English Master Overview
└── README_HINGLISH.md                 # Hinglish Master Overview (Yeh File)
```

---

## 🧭 Submodules Ka Complete Index

| # | Topic Title | Core Concepts | Quick Links |
|---|---|---|---|
| **03.01** | Conditional Statements in Python | Control flow branching, if/elif/else syntax, truthiness rules, Boolean conditions | [Notes](Notes_03.01/README_HINGLISH.md) \| [PDF](Notes_03.01/notes.pdf) \| [Notebook](Notes_03.01/lecture_03_01.ipynb) |
| **03.02** | Practice Examples (Conditionals) | Driving license check, grading scheme, tax bracket slabs calculation | [Notes](Notes_03.02/README_HINGLISH.md) \| [PDF](Notes_03.02/notes.pdf) \| [Notebook](Notes_03.02/lecture_03_02.ipynb) |
| **03.03** | Odd or Even (Parity Checking) | Modulo $x \pmod 2$ vs hardware bitwise mask $x \mathbin{\&} 1$ speedup | [Notes](Notes_03.03/README_HINGLISH.md) \| [PDF](Notes_03.03/notes.pdf) \| [Notebook](Notes_03.03/lecture_03_03.ipynb) |
| **03.04** | Nesting (Decision Trees) | Hierarchical if-else, cyclomatic complexity, guard clauses pattern | [Notes](Notes_03.04/README_HINGLISH.md) \| [PDF](Notes_03.04/notes.pdf) \| [Notebook](Notes_03.04/lecture_03_04.ipynb) |
| **03.05** | Match Case in Python | Python 3.10+ Pattern Matching, wildcards (`_`), pattern guards (`if`) | [Notes](Notes_03.05/README_HINGLISH.md) \| [PDF](Notes_03.05/notes.pdf) \| [Notebook](Notes_03.05/lecture_03_05.ipynb) |
| **03.06** | Loops Using While | While loop, loop invariants, state mutations, infinite loop prevention | [Notes](Notes_03.06/README_HINGLISH.md) \| [PDF](Notes_03.06/notes.pdf) \| [Notebook](Notes_03.06/lecture_03_06.ipynb) |
| **03.07** | Practice Examples (Loops) | Counters, running accumulators, sentinel loops, digit extraction ($N \pmod{10}$, $N // 10$) | [Notes](Notes_03.07/README_HINGLISH.md) \| [PDF](Notes_03.07/notes.pdf) \| [Notebook](Notes_03.07/lecture_03_07.ipynb) |
| **03.08** | Multiplication Table of N | Arithmetic progression $a_i = N \cdot i$, columnar f-string formatting | [Notes](Notes_03.08/README_HINGLISH.md) \| [PDF](Notes_03.08/notes.pdf) \| [Notebook](Notes_03.08/lecture_03_08.ipynb) |
| **03.09** | Break & Continue Control Flow | `break`, `continue`, `pass`, aur Python ka unique loop `else` construct | [Notes](Notes_03.09/README_HINGLISH.md) \| [PDF](Notes_03.09/notes.pdf) \| [Notebook](Notes_03.09/lecture_03_09.ipynb) |
| **03.10** | Loops Using For (Iterator Protocol) | Definite iteration, `iter()`, `next()`, `StopIteration` exception | [Notes](Notes_03.10/README_HINGLISH.md) \| [PDF](Notes_03.10/notes.pdf) \| [Notebook](Notes_03.10/lecture_03_10.ipynb) |
| **03.11** | Vowel Count (Stream Filtering) | String character traversal, set membership testing in $\mathcal{O}(1)$ time | [Notes](Notes_03.11/README_HINGLISH.md) \| [PDF](Notes_03.11/notes.pdf) \| [Notebook](Notes_03.11/lecture_03_11.ipynb) |
| **03.12** | The range() Function | Immutable sequence arithmetic progression, lazy evaluation, 48 bytes $\mathcal{O}(1)$ memory | [Notes](Notes_03.12/README_HINGLISH.md) \| [PDF](Notes_03.12/notes.pdf) \| [Notebook](Notes_03.12/lecture_03_12.ipynb) |
| **03.13** | Sum of N Numbers | Loop sum $\mathcal{O}(N)$ vs Gauss closed formula $\frac{N(N+1)}{2}$ in $\mathcal{O}(1)$ | [Notes](Notes_03.13/README_HINGLISH.md) \| [PDF](Notes_03.13/notes.pdf) \| [Notebook](Notes_03.13/lecture_03_13.ipynb) |
| **03.14** | Functions in Python | Function definition (`def`), arguments vs parameters, call stack activation frames | [Notes](Notes_03.14/README_HINGLISH.md) \| [PDF](Notes_03.14/notes.pdf) \| [Notebook](Notes_03.14/lecture_03_14.ipynb) |
| **03.15** | Practice Examples (Functions) | Modular code, pure deterministic functions, elimination of side effects | [Notes](Notes_03.15/README_HINGLISH.md) \| [PDF](Notes_03.15/notes.pdf) \| [Notebook](Notes_03.15/lecture_03_15.ipynb) |
| **03.16** | Types of Functions & Arguments | Built-in vs user-defined, positional/keyword args, default arguments mutable trap, `*args`, `**kwargs` | [Notes](Notes_03.16/README_HINGLISH.md) \| [PDF](Notes_03.16/notes.pdf) \| [Notebook](Notes_03.16/lecture_03_16.ipynb) |
| **03.17** | Lambda Functions (Anonymous) | Single-expression anonymous closures, inline callbacks (`map`, `filter`, `sorted`) | [Notes](Notes_03.17/README_HINGLISH.md) \| [PDF](Notes_03.17/notes.pdf) \| [Notebook](Notes_03.17/lecture_03_17.ipynb) |
| **03.18** | Factorial of N (Iterative vs Recursive) | Factorial $N!$, iterative loop $\mathcal{O}(1)$ memory vs recursion call stack $\mathcal{O}(N)$ limits | [Notes](Notes_03.18/README_HINGLISH.md) \| [PDF](Notes_03.18/notes.pdf) \| [Notebook](Notes_03.18/lecture_03_18.ipynb) |

---

## 🎯 Practice Problems & Systems Engineering Suite

Assignment 2 ke sabhi 10 questions aur 3 systems engineering case studies:
- **Questions Suite:** [Hinglish Guide](Practice_Problems/Questions/README_HINGLISH.md) \| [English Guide](Practice_Problems/Questions/README.md) \| [PDF](Practice_Problems/Questions/questions.pdf) \| [Notebook](Practice_Problems/Questions/questions.ipynb)
- **Solutions Suite:** [Hinglish Guide](Practice_Problems/Solutions/README_HINGLISH.md) \| [English Guide](Practice_Problems/Solutions/README.md) \| [PDF](Practice_Problems/Solutions/solutions.pdf) \| [Executed Notebook](Practice_Problems/Solutions/solutions.ipynb)
