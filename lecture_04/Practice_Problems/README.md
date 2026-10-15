# Lecture 04: Practice Problems & Systems Engineering Suite

Welcome to the comprehensive practice suite for **Lecture 04: Strings, Lists, Tuples, Dictionaries, and Sets**. This suite bridges fundamental Python data structures with production-grade computational complexity and CPython memory models.

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
│   ├── case1_string_concatenation_complexity.png  # 300 DPI Empirical vs Theoretical Benchmarks
│   ├── case2_list_overallocation_geometry.png     # 300 DPI CPython Dynamic Array Growth Steps
│   └── case3_hash_table_load_factor_probing.png   # 300 DPI Perturbation Probing & Collision Dynamics
├── README.md                   # English Suite Index & Syllabus Mapping
└── README_HINGLISH.md          # Hinglish Suite Overview & Roadmap
```

---

## 🎯 Syllabus & Problem Inventory

### Part I: Core Assignment 3 Problems

| # | Title | Core Focus | Algorithmic Complexity |
|---|---|---|---|
| **01** | Palindrome String Verifier | Two-Pointer Symmetric Invariance & Slicing | $\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Aux Space |
| **02** | Arithmetic Mean of Integer List | Accumulation, Vector Aggregation & Type Casts | $\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Space |
| **03** | Sorted Merge of Two Sequences | Dual Ingestion & Adaptive Timsort | $\mathcal{O}((N+M) \log(N+M))$ Time |
| **04** | Tuple Parity Partitioning | Modulo Arithmetic & Immutable Sequence Packing | $\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space |
| **05** | Student Gradebook Record System | Dynamic CRUD via Hash Map Key Invariants | $\mathcal{O}(1)$ Amortized Operations |
| **06** | Word-to-Length Lexical Map | Dictionary Comprehension & String Introspection | $\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space |
| **07** | Whitespace Character Counter | Unicode Code-Point Inspection & Generators | $\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Aux Space |
| **08** | Disjoint Sequence Verification | Hash Set Intersection & Set Theory Invariants | $\mathcal{O}(\min(N, M))$ Average Time |
| **09** | Sequence Duplicate Element Detector | Uniqueness Filtering & Cardinality Comparison | $\mathcal{O}(N)$ Average Time, $\mathcal{O}(N)$ Space |
| **10** | Unique Character Ingestion & Count | Character Set Cardinality $|\mathcal{U}|$ | $\mathcal{O}(N)$ Time, $\mathcal{O}(|\Sigma|)$ Space |

### Part II: Systems Engineering Case Studies

| # | Systems Case Study | Core Focus | Key Concepts & Deliverables |
|---|---|---|---|
| **Case 1** | String Immutability & Buffer Concatenation | CPython `PyASCIIObject`, Interning, Allocations | $\mathcal{O}(N^2)$ quadratic degradation vs $\mathcal{O}(N)$ `str.join()`; 300 DPI plot |
| **Case 2** | Dynamic Array Growth & Memory Geometry | `list_resize()` over-allocation formula | Empirical memory footprint tracking; 300 DPI growth plot |
| **Case 3** | Hash Table Architecture & Set Dynamics | Open Addressing Perturbation Probing | Load factor threshold $\alpha = 2/3$; probing trajectory plot |

---

## 🛠️ Verification & Execution

To execute the solution benchmark suite locally:

```bash
jupyter execute Solutions/solutions.ipynb
```
