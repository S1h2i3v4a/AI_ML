# Lecture 03: Practice Problems & Systems Engineering Suite

Welcome to the comprehensive practice suite for **Lecture 03: Python Fundamentals (Part 2 — Conditionals, Loops & Functions)**. This suite implements all 10 problems from official **Assignment 2** alongside 3 industrial-grade systems engineering case studies.

---

## 📂 Suite Architecture

```text
Practice_Problems/
├── Questions/
│   ├── README.md               # English Problem Specifications (Problems 1-10 + Case Studies 1-3)
│   ├── README_HINGLISH.md      # Hinglish Specifications with Deep Bullet Deconstructions
│   ├── questions.ipynb         # Interactive Problem Notebook (Starters & Test Cases)
│   └── questions.pdf           # Vector-Grade Printable Problem Set
├── Solutions/
│   ├── README.md               # English Rigorous Production Implementations & Proofs
│   ├── README_HINGLISH.md      # Hinglish Line-by-Line Breakdowns & Complexity Proofs
│   ├── solutions.ipynb         # Fully Executed Solution Notebook with Benchmarks
│   ├── solutions.pdf           # Vector-Grade Printable Master Solution Manual
│   ├── case1_control_flow_jump_graph.png         # 300 DPI Bytecode Jump Trajectory
│   ├── case2_loop_execution_speed_benchmark.png  # 300 DPI while vs for vs C-Accumulator
│   └── case3_call_stack_recursion_memory.png     # 300 DPI Recursion Call Stack Depth
├── README.md                   # English Suite Index & Syllabus Mapping
└── README_HINGLISH.md          # Hinglish Suite Overview & Roadmap
```

---

## 🎯 Syllabus & Problem Inventory

### Part I: Core Assignment 2 Problems

| # | Title | Core Focus | Algorithmic Complexity |
|---|---|---|---|
| **01** | Income Tax Bracket Calculator | Chained decision branching, boundary conditions | $\mathcal{O}(1)$ Time, $\mathcal{O}(1)$ Space |
| **02** | Even Numbers in Range $[a, b]$ | Modular arithmetic, inclusive range filtering | $\mathcal{O}(b - a)$ Time, $\mathcal{O}(1)$ Space |
| **03** | Integer Digit Deconstruction | Successive division, modulo-10 digit extraction | $\mathcal{O}(\log_{10} N)$ Time, $\mathcal{O}(1)$ Space |
| **04** | Integer Digit Cardinality Counter | Digit counting loop vs logarithmic formulation | $\mathcal{O}(\log_{10} N)$ Time, $\mathcal{O}(1)$ Space |
| **05** | Sum of Integer Digits | Modular digit extraction, cumulative accumulation | $\mathcal{O}(\log_{10} N)$ Time, $\mathcal{O}(1)$ Space |
| **06** | Dual Divisibility Filter ($3 \land 5$) | Least Common Multiple ($\\text{lcm}(3, 5) = 15$) | $\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Space |
| **07** | Sentinel-Controlled Input Poller | Indefinite `while True` loop, sentinel string exit | $\mathcal{O}(K)$ Time, $\mathcal{O}(1)$ Space |
| **08** | Arithmetic Dispatch Calculator | Multi-way dispatch, `match ... case`, zero guard | $\mathcal{O}(1)$ Time, $\mathcal{O}(1)$ Space |
| **09** | Primality Verifier Function | Trial division up to $\lfloor \sqrt{N} \rfloor$, loop `else` | $\mathcal{O}(\sqrt{N})$ Time, $\mathcal{O}(1)$ Space |
| **10** | Number Guessing Game Engine | Interactive loop, binary feedback search | $\mathcal{O}(\log_2(\text{Range}))$ Best Strategy |

### Part II: Systems Engineering Case Studies

| # | Systems Case Study | Core Focus | Deliverables |
|---|---|---|---|
| **Case 1** | Bytecode Branching & Jump Invariants | CPython `POP_JUMP_IF_FALSE`, disassembly | Instruction flow graph; 300 DPI plot |
| **Case 2** | Iteration Overhead: `while` vs `for` | `FOR_ITER` iterator vs variable rebinding | Empirical benchmark curves; 300 DPI plot |
| **Case 3** | Call Stack Depth & Frame Allocation | `PyFrameObject` stack growth, recursion limit | Stack frame memory analysis; 300 DPI plot |
