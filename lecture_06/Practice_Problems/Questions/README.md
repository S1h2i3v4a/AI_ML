# Lecture 06: Practice Problems & Assignment 5 — Problem Statements

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](questions.ipynb)
[![PDF](https://img.shields.io/badge/PDF-questions.pdf-red.svg)](questions.pdf)

🌐 **Language / भाषा:** **English** | [हिंदी / Hinglish](README_HINGLISH.md) | [⬅️ Back to Lecture 06 Module](../../README.md)

---

## Overview & Official Curriculum
This practice suite contains the official problems from **Assignment 5** (Python Fundamentals Part 5) covering File I/O, Exception Handling, List Comprehensions, and the JSON module, alongside enterprise systems engineering extensions.

---

## 📋 Problem Catalog

### Problem 1: Name Registry Persistence (Assignment 5 Q1)
Create a program that:
1. Opens a file `names.txt` in write mode (`"w"`).
2. Writes 5 names (one per line).
3. Then opens the same file in read mode (`"r"`) and prints all names to standard output.

### Problem 2: Audit Event Logging (Assignment 5 Q2)
Create a program that:
1. Opens a file `log.txt` in append mode (`"a"`).
2. Adds a new timestamped log entry (e.g. `"Program run successfully"`).
3. Opens the file in read mode and prints all historical logs.

### Problem 3: Numeric Threshold Filtering (Assignment 5 Q3)
Create a program that:
1. Initializes a list of numbers: `[5, 10, 15, 20, 25]`.
2. Uses a **list comprehension** to construct a new list containing only numbers strictly greater than 15.
3. Prints the resulting filtered list.

### Problem 4: Municipal Demographic JSON Store (Assignment 5 Q4)
Create a program that:
1. Initializes a dictionary of 3 cities and their population figures.
2. Serializes and saves it to `cities.json` using `json.dump()` with `indent=4`.
3. Loads the JSON file back into Python and prints each city alongside its population.
4. Accepts a new city and population entry, dynamically updates the data structure, and persists the updated JSON file.

### Problem 5: Missing Resource Exception Guard (Assignment 5 Q5)
Create a program that:
1. Attempts to open a file `data.txt` in read mode.
2. If the file does not exist, catches `FileNotFoundError` gracefully and displays `"File not found!"` without terminating the process abruptly.

### Problem 6: Enterprise Server Log Incident Analyzer (Systems Engineering)
Build a log analysis engine that reads an application access log, parses HTTP response codes (`200`, `404`, `500`), filters server anomalies using list comprehensions, and outputs a diagnostic summary to `audit_report.json`.

---

## Reference Official Documents
- [Python_Fundamentals_Part5.pdf](../../Python_Fundamentals_Part5.pdf) — Official Slide Deck
- [Python_Fundamentals_Assignment5.pdf](../../Python_Fundamentals_Assignment5.pdf) — Official Assignment Sheet
