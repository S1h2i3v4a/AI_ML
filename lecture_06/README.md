# Lecture 06: Python Fundamentals (Part 5) — File I/O, Exceptions, Comprehensions & JSON

Welcome to the comprehensive, first-principles curriculum module for **Lecture 06: Python Fundamentals (Part 5)**. This module covers core systems programming and data interchange in Python: persistent File I/O stream mechanics, open modes (`r`, `w`, `a`, `x`, `r+`, `w+`, `a+`, `b`), Context Managers (`with` keyword) and deterministic resource management, filesystem manipulation (`os.remove`, `os.path.exists`), algorithmic text processing, structured Exception Handling (`try`, `except`, `else`, `finally`, `raise`), high-performance List Comprehensions, data serialization with the JSON module (`dump`, `load`, `dumps`, `loads`), and the complete implementation of official **Assignment 5**.

---

## 📂 Module Architecture

```text
lecture_06/
├── Notes_06.01/ to Notes_06.10/    # 10 Granular Submodules (README.md, README_HINGLISH.md, notes.pdf, .ipynb)
├── Practice_Problems/             # Comprehensive Assignment 5 & Systems Engineering Suite
│   ├── Questions/                 # Problem Statements (README.md, README_HINGLISH.md, questions.ipynb, questions.pdf)
│   └── Solutions/                 # Master Solutions (README.md, README_HINGLISH.md, solutions.ipynb, solutions.pdf)
├── Python_Fundamentals_Assignment5.pdf # Official Assignment Sheet
├── Python_Fundamentals_Part5.pdf       # Official Course Slide Deck
├── README.md                          # English Master Overview (This Document)
└── README_HINGLISH.md                 # Hinglish Master Overview
```

---

## 🧭 Submodule Inventory & Topic Roadmap

| # | Topic Title | Core Concepts | Quick Links |
|---|---|---|---|
| **06.01** | Introduction to File I/O & Persistent Storage | RAM vs Disk persistence, Stream buffers, `open()`, `close()`, OS file handles | [Notes](Notes_06.01/README.md) \| [PDF](Notes_06.01/notes.pdf) \| [Notebook](Notes_06.01/lecture_06_01.ipynb) |
| **06.02** | File Operations — Reading & Writing Methods | `read()`, `readline()`, `readlines()`, `write()`, `writelines()`, stream cursor | [Notes](Notes_06.02/README.md) \| [PDF](Notes_06.02/notes.pdf) \| [Notebook](Notes_06.02/lecture_06_02.ipynb) |
| **06.03** | Modes in File Operations | `r`, `w`, `a`, `x`, `r+`, `w+`, `a+`, `b` binary vs text, truncation dynamics | [Notes](Notes_06.03/README.md) \| [PDF](Notes_06.03/notes.pdf) \| [Notebook](Notes_06.03/lecture_06_03.ipynb) |
| **06.04** | Context Managers & The \`with\` Keyword | Auto-closure guarantee, RAII pattern, `__enter__` and `__exit__` dunder protocol | [Notes](Notes_06.04/README.md) \| [PDF](Notes_06.04/notes.pdf) \| [Notebook](Notes_06.04/lecture_06_04.ipynb) |
| **06.05** | Deleting & Managing Files | `os.remove()`, `os.path.exists()`, safe unlinking, `pathlib.Path` | [Notes](Notes_06.05/README.md) \| [PDF](Notes_06.05/notes.pdf) \| [Notebook](Notes_06.05/lecture_06_05.ipynb) |
| **06.06** | Practice Problems on File I/O | Word frequency Counter, keyword search, in-place find and replace, line counting | [Notes](Notes_06.06/README.md) \| [PDF](Notes_06.06/notes.pdf) \| [Notebook](Notes_06.06/lecture_06_06.ipynb) |
| **06.07** | Exception Handling Fundamentals | `try`, `except`, `ZeroDivisionError`, `ValueError`, `FileNotFoundError`, `TypeError` | [Notes](Notes_06.07/README.md) \| [PDF](Notes_06.07/notes.pdf) \| [Notebook](Notes_06.07/lecture_06_07.ipynb) |
| **06.08** | The Complete Exception Flow | `try`, `except`, `else`, `finally`, `raise`, custom exception classes | [Notes](Notes_06.08/README.md) \| [PDF](Notes_06.08/notes.pdf) \| [Notebook](Notes_06.08/lecture_06_08.ipynb) |
| **06.09** | List Comprehensions in Python | Mapping, filtering with `if`, ternary `if-else`, performance optimization | [Notes](Notes_06.09/README.md) \| [PDF](Notes_06.09/notes.pdf) \| [Notebook](Notes_06.09/lecture_06_09.ipynb) |
| **06.10** | Working with the JSON Module | `dumps()`, `loads()`, `dump()`, `load()`, indentation formatting `indent=4` | [Notes](Notes_06.10/README.md) \| [PDF](Notes_06.10/notes.pdf) \| [Notebook](Notes_06.10/lecture_06_10.ipynb) |

---

## 🎯 Practice Problems & Assignment 5 Suite

Explore the official Assignment 5 suite along with systems engineering case studies:
- **Questions Suite:** [English Guide](Practice_Problems/Questions/README.md) \| [Hinglish Guide](Practice_Problems/Questions/README_HINGLISH.md) \| [PDF](Practice_Problems/Questions/questions.pdf) \| [Notebook](Practice_Problems/Questions/questions.ipynb)
- **Solutions Suite:** [English Guide](Practice_Problems/Solutions/README.md) \| [Hinglish Guide](Practice_Problems/Solutions/README_HINGLISH.md) \| [PDF](Practice_Problems/Solutions/solutions.pdf) \| [Notebook](Practice_Problems/Solutions/solutions.ipynb)
