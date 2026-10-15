# Lecture 03: Python Fundamentals (Part 2 — Conditional Statements, Loops & Functions)

Welcome to the definitive, first-principles curriculum module for **Lecture 03: Python Fundamentals (Part 2)**. This module establishes complete mastery over Python's control flow branching, looping mechanics, iterator protocols, function activations, modular architecture, and algorithmic problem-solving.

---

## 📂 Module Architecture

```text
lecture_03/
├── Notes_03.01/ to Notes_03.18/    # 18 Granular Submodules (README.md, README_HINGLISH.md, notes.pdf, .ipynb)
├── Practice_Problems/             # Comprehensive Assignment 2 & Systems Engineering Suite
│   ├── Questions/                 # Problem Statements (README.md, README_HINGLISH.md, questions.ipynb, questions.pdf)
│   └── Solutions/                 # Rigorous Solutions (README.md, README_HINGLISH.md, solutions.ipynb, solutions.pdf, 300DPI plots)
├── Python_Fundamentals_Assignment2.pdf # Official Assignment Sheet
├── Python_Fundamentals_Part2.pdf       # Official Course Slide Deck
├── Topic_List.jpg                     # Official Lecture Visual Index
├── README.md                          # English Master Overview (This Document)
└── README_HINGLISH.md                 # Hinglish Master Overview
```

---

## 🧭 Submodule Inventory & Topic Roadmap

| # | Topic Title | Core Concepts | Quick Links |
|---|---|---|---|
| **03.01** | Conditional Statements in Python | Control flow branching, if/elif/else syntax, truth value testing, Boolean lattices | [Notes](Notes_03.01/README.md) \| [PDF](Notes_03.01/notes.pdf) \| [Notebook](Notes_03.01/lecture_03_01.ipynb) |
| **03.02** | Practice Examples (Conditionals) | Driving license eligibility, academic grading brackets, tax threshold boundaries | [Notes](Notes_03.02/README.md) \| [PDF](Notes_03.02/notes.pdf) \| [Notebook](Notes_03.02/lecture_03_02.ipynb) |
| **03.03** | Odd or Even (Parity Checking) | Parity invariants, modulo arithmetic ($x \pmod 2$), low-level bitwise masking ($x \mathbin{\&} 1$) | [Notes](Notes_03.03/README.md) \| [PDF](Notes_03.03/notes.pdf) \| [Notebook](Notes_03.03/lecture_03_03.ipynb) |
| **03.04** | Nesting (Decision Trees) | Hierarchical branching, cyclomatic complexity $M = E - N + 2P$, guard clause refactoring | [Notes](Notes_03.04/README.md) \| [PDF](Notes_03.04/notes.pdf) \| [Notebook](Notes_03.04/lecture_03_04.ipynb) |
| **03.05** | Match Case in Python | PEP 634 Structural Pattern Matching, literal/capture/wildcard patterns, pattern guards | [Notes](Notes_03.05/README.md) \| [PDF](Notes_03.05/notes.pdf) \| [Notebook](Notes_03.05/lecture_03_05.ipynb) |
| **03.06** | Loops Using While | Indefinite iteration, loop invariants, state mutations, monotonic termination proofs | [Notes](Notes_03.06/README.md) \| [PDF](Notes_03.06/notes.pdf) \| [Notebook](Notes_03.06/lecture_03_06.ipynb) |
| **03.07** | Practice Examples (Loops) | Counter-controlled loops, accumulators, sentinel loops, successive division digit extraction | [Notes](Notes_03.07/README.md) \| [PDF](Notes_03.07/notes.pdf) \| [Notebook](Notes_03.07/lecture_03_07.ipynb) |
| **03.08** | Multiplication Table of N | Arithmetic progressions $a_i = N \cdot i$, columnar formatting, range iteration | [Notes](Notes_03.08/README.md) \| [PDF](Notes_03.08/notes.pdf) \| [Notebook](Notes_03.08/lecture_03_08.ipynb) |
| **03.09** | Break & Continue Control Flow | Early loop exit (`break`), iteration skip (`continue`), syntactic placeholder (`pass`), loop `else` | [Notes](Notes_03.09/README.md) \| [PDF](Notes_03.09/notes.pdf) \| [Notebook](Notes_03.09/lecture_03_09.ipynb) |
| **03.10** | Loops Using For (Iterator Protocol) | Definite iteration, iterable vs iterator distinction, `iter()`, `next()`, `StopIteration` | [Notes](Notes_03.10/README.md) \| [PDF](Notes_03.10/notes.pdf) \| [Notebook](Notes_03.10/lecture_03_10.ipynb) |
| **03.11** | Vowel Count (Stream Filtering) | Character stream traversal, vowel set membership testing, case normalization | [Notes](Notes_03.11/README.md) \| [PDF](Notes_03.11/notes.pdf) \| [Notebook](Notes_03.11/lecture_03_11.ipynb) |
| **03.12** | The range() Function | Immutable sequence arithmetic progression, lazy generation, constant $\mathcal{O}(1)$ space | [Notes](Notes_03.12/README.md) \| [PDF](Notes_03.12/notes.pdf) \| [Notebook](Notes_03.12/lecture_03_12.ipynb) |
| **03.13** | Sum of N Numbers | Loop accumulation $\mathcal{O}(N)$ vs Gauss closed-form formula $\frac{N(N+1)}{2}$ in $\mathcal{O}(1)$ | [Notes](Notes_03.13/README.md) \| [PDF](Notes_03.13/notes.pdf) \| [Notebook](Notes_03.13/lecture_03_13.ipynb) |
| **03.14** | Functions in Python | Function definition, parameters vs arguments, return values, call stack `PyFrameObject` | [Notes](Notes_03.14/README.md) \| [PDF](Notes_03.14/notes.pdf) \| [Notebook](Notes_03.14/lecture_03_14.ipynb) |
| **03.15** | Practice Examples (Functions) | Modular decomposition, pure deterministic functions, side-effect elimination | [Notes](Notes_03.15/README.md) \| [PDF](Notes_03.15/notes.pdf) \| [Notebook](Notes_03.15/lecture_03_15.ipynb) |
| **03.16** | Types of Functions & Arguments | Built-in vs user-defined, positional/keyword arguments, default values, `*args`, `**kwargs` | [Notes](Notes_03.16/README.md) \| [PDF](Notes_03.16/notes.pdf) \| [Notebook](Notes_03.16/lecture_03_16.ipynb) |
| **03.17** | Lambda Functions (Anonymous) | Alonzo Church $\lambda$-calculus, single-expression syntax, inline callbacks (`map`, `filter`) | [Notes](Notes_03.17/README.md) \| [PDF](Notes_03.17/notes.pdf) \| [Notebook](Notes_03.17/lecture_03_17.ipynb) |
| **03.18** | Factorial of N (Iterative vs Recursive) | Factorial definition $N!$, iterative product $\mathcal{O}(1)$ vs recursive call stack $\mathcal{O}(N)$ | [Notes](Notes_03.18/README.md) \| [PDF](Notes_03.18/notes.pdf) \| [Notebook](Notes_03.18/lecture_03_18.ipynb) |

---

## 🎯 Practice Problems & Systems Engineering Suite

Explore the official Assignment 2 suite along with 3 systems engineering case studies:
- **Questions Suite:** [English Guide](Practice_Problems/Questions/README.md) \| [Hinglish Guide](Practice_Problems/Questions/README_HINGLISH.md) \| [PDF](Practice_Problems/Questions/questions.pdf) \| [Notebook](Practice_Problems/Questions/questions.ipynb)
- **Solutions Suite:** [English Guide](Practice_Problems/Solutions/README.md) \| [Hinglish Guide](Practice_Problems/Solutions/README_HINGLISH.md) \| [PDF](Practice_Problems/Solutions/solutions.pdf) \| [Executed Notebook](Practice_Problems/Solutions/solutions.ipynb)
