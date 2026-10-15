# Lecture 05: Object-Oriented Programming (OOP) in Python (हिंग्लिश)

**Lecture 05: Object-Oriented Programming (OOP)** ke master curriculum document mein aapka swagat hai. Yeh module Python ke core OOP principles: Classes, Objects, Constructors (`__init__`), Class vs Instance attributes, Encapsulation (Private, Protected, Name Mangling, `@property`), Inheritance (Single, Multiple, Multilevel, C3 Linearization MRO), Abstraction (`abc.ABC`), Polymorphism (Method Overriding, Duck Typing, Operator Overloading), aur official **Assignment 4** ke 10 questions aur chat system mini-project ko first-principles se cover karta hai.

---

## 📂 Module Ki Sanrachna (Folder Architecture)

```text
lecture_05/
├── Notes_05.01/ to Notes_05.16/    # 16 Granular Submodules (README.md, README_HINGLISH.md, notes.pdf, .ipynb)
├── Practice_Problems/             # Assignment 4 & Systems Engineering Suite
│   ├── Questions/                 # Problem Statements (README.md, README_HINGLISH.md, questions.ipynb, questions.pdf)
│   └── Solutions/                 # Master Solutions (README.md, README_HINGLISH.md, solutions.ipynb, solutions.pdf, 300DPI plots)
├── Python_Fundamentals_Assignment4.pdf # Official Assignment Sheet
├── Python_Fundamentals_Part4.pdf       # Official Slide Deck
├── Chat_System_Code.pdf               # Official Chat System Reference Project
├── README.md                          # English Master Overview
└── README_HINGLISH.md                 # Hinglish Master Overview (Yeh File)
```

---

## 🧭 Submodules Ka Complete Index

| # | Topic Title | Core Concepts | Quick Links |
|---|---|---|---|
| **05.01** | What is Object-Oriented Programming | Paradigm shift, Procedural vs OOP, State & Behavior, 4 Pillars | [Notes](Notes_05.01/README_HINGLISH.md) \| [PDF](Notes_05.01/notes.pdf) \| [Notebook](Notes_05.01/lecture_05_01.ipynb) |
| **05.02** | Classes & Objects | Blueprints vs heap instances, identity (`id`), type, memory allocation | [Notes](Notes_05.02/README_HINGLISH.md) \| [PDF](Notes_05.02/notes.pdf) \| [Notebook](Notes_05.02/lecture_05_02.ipynb) |
| **05.03** | Attributes & Methods | Dot notation, internal `__dict__`, method binding, dynamic attributes | [Notes](Notes_05.03/README_HINGLISH.md) \| [PDF](Notes_05.03/notes.pdf) \| [Notebook](Notes_05.03/lecture_05_03.ipynb) |
| **05.04** | Constructor — \`__init__()\` Method | `__new__` vs `__init__`, `self` parameter, instance initialization | [Notes](Notes_05.04/README_HINGLISH.md) \| [PDF](Notes_05.04/notes.pdf) \| [Notebook](Notes_05.04/lecture_05_04.ipynb) |
| **05.05** | Types of Constructors | Default vs parameterized constructors, simulating overloading with `@classmethod` | [Notes](Notes_05.05/README_HINGLISH.md) \| [PDF](Notes_05.05/notes.pdf) \| [Notebook](Notes_05.05/lecture_05_05.ipynb) |
| **05.06** | Attributes — Class vs Instance | Class attributes (shared) vs instance attributes (unique), shadowing trap | [Notes](Notes_05.06/README_HINGLISH.md) \| [PDF](Notes_05.06/notes.pdf) \| [Notebook](Notes_05.06/lecture_05_06.ipynb) |
| **05.07** | Instance Methods | `self` pointer binding, mutating instance state, method chaining patterns | [Notes](Notes_05.07/README_HINGLISH.md) \| [PDF](Notes_05.07/notes.pdf) \| [Notebook](Notes_05.07/lecture_05_07.ipynb) |
| **05.08** | Class Methods (\`@classmethod\`) | `@classmethod` decorator, `cls` binding, factory constructors | [Notes](Notes_05.08/README_HINGLISH.md) \| [PDF](Notes_05.08/notes.pdf) \| [Notebook](Notes_05.08/lecture_05_08.ipynb) |
| **05.09** | Static Methods (\`@staticmethod\`) | `@staticmethod` decorator, decoupled utility helpers, namespace scoping | [Notes](Notes_05.09/README_HINGLISH.md) \| [PDF](Notes_05.09/notes.pdf) \| [Notebook](Notes_05.09/lecture_05_09.ipynb) |
| **05.10** | Practice Problem (Banking System) | Encapsulated bank account, deposit/withdrawal validation, audit logs | [Notes](Notes_05.10/README_HINGLISH.md) \| [PDF](Notes_05.10/notes.pdf) \| [Notebook](Notes_05.10/lecture_05_10.ipynb) |
| **05.11** | Encapsulation in OOPs | Public, protected `_`, private `__`, name mangling, `@property` getters/setters | [Notes](Notes_05.11/README_HINGLISH.md) \| [PDF](Notes_05.11/notes.pdf) \| [Notebook](Notes_05.11/lecture_05_11.ipynb) |
| **05.12** | Inheritance in OOPs | IS-A relationship, base & derived classes, code reuse, `super()` proxy | [Notes](Notes_05.12/README_HINGLISH.md) \| [PDF](Notes_05.12/notes.pdf) \| [Notebook](Notes_05.12/lecture_05_12.ipynb) |
| **05.13** | Types of Inheritance & MRO | Single, multiple, multilevel, hierarchical, hybrid; C3 Linearization MRO | [Notes](Notes_05.13/README_HINGLISH.md) \| [PDF](Notes_05.13/notes.pdf) \| [Notebook](Notes_05.13/lecture_05_13.ipynb) |
| **05.14** | Abstraction in Python | Abstract Base Classes, `abc` module, `@abstractmethod`, interface contracts | [Notes](Notes_05.14/README_HINGLISH.md) \| [PDF](Notes_05.14/notes.pdf) \| [Notebook](Notes_05.14/lecture_05_14.ipynb) |
| **05.15** | Polymorphism — Method Overriding | Runtime dynamic dispatch, method overriding, shape area hierarchy | [Notes](Notes_05.15/README_HINGLISH.md) \| [PDF](Notes_05.15/notes.pdf) \| [Notebook](Notes_05.15/lecture_05_15.ipynb) |
| **05.16** | Polymorphism — Duck Typing & Dunder | Duck typing philosophy, dunder methods (`__str__`, `__repr__`, `__add__`) | [Notes](Notes_05.16/README_HINGLISH.md) \| [PDF](Notes_05.16/notes.pdf) \| [Notebook](Notes_05.16/lecture_05_16.ipynb) |

---

## 🎯 Practice Problems & Systems Engineering Suite

Assignment 4 ke sabhi 10 questions, Chat System mini project, aur 3 systems engineering case studies:
- **Questions Suite:** [Hinglish Guide](Practice_Problems/Questions/README_HINGLISH.md) \| [English Guide](Practice_Problems/Questions/README.md) \| [PDF](Practice_Problems/Questions/questions.pdf) \| [Notebook](Practice_Problems/Questions/questions.ipynb)
- **Solutions Suite:** [Hinglish Guide](Practice_Problems/Solutions/README_HINGLISH.md) \| [English Guide](Practice_Problems/Solutions/README.md) \| [PDF](Practice_Problems/Solutions/solutions.pdf) \| [Executed Notebook](Practice_Problems/Solutions/solutions.ipynb)
