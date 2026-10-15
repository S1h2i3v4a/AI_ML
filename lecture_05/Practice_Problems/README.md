# Lecture 05: Practice Problems & Systems Engineering Suite

Welcome to the comprehensive practice suite for **Lecture 05: Object-Oriented Programming (OOP) in Python**. This suite implements all 10 problems from official **Assignment 4**, the reference OOP Chat System, and 3 advanced systems engineering case studies.

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
│   ├── case1_object_memory_slots_anatomy.png     # 300 DPI __dict__ vs __slots__ Memory Comparison
│   ├── case2_c3_linearization_mro_graph.png      # 300 DPI C3 Linearization MRO Resolution Graph
│   └── case3_attribute_lookup_dispatch_flow.png  # 300 DPI CPython Attribute Lookup Hierarchy
├── README.md                   # English Suite Index & Syllabus Mapping
└── README_HINGLISH.md          # Hinglish Suite Overview & Roadmap
```

---

## 🎯 Syllabus & Problem Inventory

### Part I: Core Assignment 4 Problems

| # | Title | Core Concept | Algorithmic Complexity |
|---|---|---|---|
| **01** | BankAccount Ledger System | Classes & Objects, State Mutation | $\mathcal{O}(1)$ Deposits/Withdrawals |
| **02** | Book Review Catalog Entity | Dynamic Attribute Lists, Aggregation | $\mathcal{O}(1)$ Appends, $\mathcal{O}(N)$ Display |
| **03** | Encapsulated Student Record | Validation Setters, Information Hiding | $\mathcal{O}(1)$ Access & Invariant Guards |
| **04** | Polymorphic Shape Hierarchy | Method Overriding, Geometric Equations | $\mathcal{O}(1)$ Area Evaluation |
| **05** | Vehicle Taxonomy Inheritance | Base/Derived Inheritance, `super()` | $\mathcal{O}(1)$ Construction & Delegation |
| **06** | Abstract Employee Payroll Engine | Abstract Base Classes (`abc`), Contracts | $\mathcal{O}(1)$ Polymorphic Salary Dispatch |
| **07** | Simulated Constructor Overloading | Default Arguments, Lifecycle Initialization | $\mathcal{O}(1)$ Construction |
| **08** | Global Game Player Tracker | Class vs Instance Attributes, Counters | $\mathcal{O}(1)$ Static Tracking |
| **09** | Multiple Inheritance & Omnivore Diet | Multiple Inheritance, Diamond MRO | $\mathcal{O}(1)$ Method Resolution |
| **10** | Mini-Project: OOP Chat System | Multi-Class Object System (`User`, `Room`) | $\mathcal{O}(1)$ Messaging, $\mathcal{O}(K)$ Broadcast |

### Part II: Systems Engineering Case Studies

| # | Systems Case Study | Core Focus | Deliverables |
|---|---|---|---|
| **Case 1** | Object Memory & `__slots__` Anatomy | `PyObject` header, `__dict__` vs `__slots__` | Empirical memory footprint curves; 300 DPI plot |
| **Case 2** | Multiple Inheritance & C3 Linearization | Method Resolution Order (MRO), Diamond graph | Topological linearization tree; 300 DPI plot |
| **Case 3** | Dynamic Dispatch & Descriptor Protocol | `__getattribute__` resolution hierarchy | Full attribute dispatch flow chart; 300 DPI plot |
