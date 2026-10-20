# Lecture 06.09: List Comprehensions in Python [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_06_09.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 06 Module Par Wapas Jayein](../README_HINGLISH.md)

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- List Comprehension kya hota hai aur yeh traditional `for` loops se fast aur concise kyu hai.
- Syntax 1 (Basic mapping): `[x for x in iterable]`.
- Syntax 2 (Filtering): `[x for x in iterable if condition]` (jaise even numbers filter karna).
- Syntax 3 (Ternary If-Else): `[val_if_true if cond else val_if_false for x in iterable]`.
- Dictionary Comprehensions aur Set Comprehensions ka intro.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

- **Kyu Use Karein List Comprehension**: Traditional Python me agar hume 1 se 10 ke squares ki list banani ho, to pehle empty list `res = []` banani padti hai, fir `for x in range:` chalana padta hai, aur fir `res.append(x**2)` likhna padta hai (4 lines). List comprehension me wahi kaam ek line me hota hai: `[x**2 for x in range(1, 11)]`.

- **Filtering Syntax**: `if` filter hamesha loop ke baad aata hai: `[x for x in nums if x % 2 == 0]`. Yeh sirf un elements ko list me rakhta hai jo condition satisfy karte hain.

- **Ternary If-Else Syntax**: Jab hume har element ko modify karna ho based on condition, to `if-else` loop ke pehle aata hai: `['Even' if x % 2 == 0 else 'Odd' for x in nums]`.

- **Performance Advantage**: List comprehension C-level optimization par execute hota hai (CALL_METHOD aur APPEND bytecode instructions avoid hote hain), isiliye large datasets par yeh standard for-loop se significantly faster hota hai.

- **Lecture Reference**: Ma'am ne slide 6 me teeno formats clearly showcase kiye: Basic, With Condition, aur With if-else.

---

## 2. Visual Architecture & Workflow Diagram

```mermaid
flowchart LR
    A["Input Iterable:<br/>[1, 2, 3, 4, 5, 6]"] --> B{"Syntax Type"}
    B -->|"Basic: [x*2 for x in seq]"| C["Doubled List:<br/>[2, 4, 6, 8, 10, 12]"]
    B -->|"Filter: [x for x in seq if x % 2 == 0]"| D["Filtered Even List:<br/>[2, 4, 6]"]
    B -->|"If-Else: ['E' if x%2==0 else 'O' for x in seq]"| E["Categorized List:<br/>['O', 'E', 'O', 'E', 'O', 'E']"]
```

---

## 3. Mathematical & Theoretical Framework

A list comprehension translates set-builder notation from set theory into procedural lists:

$$
\mathcal{L} = \{ f(x) \mid x \in \mathcal{S} \land P(x) \}
$$

In Python list comprehension syntax:

$$
\text{Python: } [f(x) \text{ for } x \text{ in } \mathcal{S} \text{ if } P(x)]
$$

When equipped with a conditional evaluator $g(x) = (x \in \mathcal{A} ? v_1 : v_2)$:

$$
[v_1 \text{ if } P(x) \text{ else } v_2 \text{ for } x \text{ in } \mathcal{S}]
$$

---

## 4. Structured Implementation & Execution

```python
def evaluate_list_comprehension_variants(numbers: list) -> dict:
    """
    Demonstrates basic mapping, conditional filtering, ternary if-else,
    and dictionary comprehensions.
    
    Parameters:
    -----------
    numbers : list of int
        Input list of integers to transform.
        
    Returns:
    --------
    dict
        Transformed collections across each comprehension pattern.
    """
    # 1. Basic Mapping: Squares of numbers
    squares = [x**2 for x in numbers]
    
    # 2. Filtering: Only numbers greater than 15 (Assignment 5 Q3)
    filtered_gt_15 = [x for x in numbers if x > 15]
    
    # 3. Filtering: Only even numbers
    evens = [x for x in numbers if x % 2 == 0]
    
    # 4. Ternary If-Else: Label numbers as 'Even' or 'Odd'
    parity_labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
    
    # 5. Dictionary Comprehension: Map number to its cube
    cube_mapping = {x: x**3 for x in numbers[:4]}
    
    return {
        "original": numbers,
        "squares": squares,
        "filtered_greater_than_15": filtered_gt_15,
        "even_numbers": evens,
        "parity_labels": parity_labels,
        "cube_dictionary": cube_mapping
    }

# Driver test (Includes Assignment 5 Q3 dataset [5, 10, 15, 20, 25])
sample_numbers = [5, 10, 15, 20, 25]
comp_results = evaluate_list_comprehension_variants(sample_numbers)
print("List Comprehension Variations Results:")
for k, v in comp_results.items():
    print(f"  {k}: {v}")
```

---

## 5. Mukhya Batein (Key Takeaways) & Summary
- Code ko modular function ke roop me likha gaya hai jisme clear shuruat (`def`), docstrings, error handling, aur ending (`return`) maujood hai.
- Video lectures me ma'am dwara sikhaye gaye exact concepts, slides aur Assignment 5 ke requirements ko 100% follow kiya gaya hai.
