# Lecture 03.01: Python Mein Conditional Statements (if, elif, else) (हिंग्लिश)

## 📌 Module Overview
Control flow branching ka poora concept, if/elif/else syntax, truthiness rules, Boolean conditions, aur CPython bytecode branching execution.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Conditional Statements Ka Buniyadi Concept
Program standard flow mein upar se neeche (line-by-line) sequentially execute hota hai. Lekin real-world programs aur machine learning algorithms mein decisions lene padte hain: "Agar data clean hai toh train karo, warna preprocess karo."

Is decision branching ke liye Python hume teen keywords provide karta hai:
- `if`: Yeh pehli condition check karta hai. Agar condition True hai, toh iska code block execute hota hai.
- `elif` (else if): Agar pehli `if` condition False ho gayi, tabhi agla `elif` check hota hai.
- `else`: Agar upar ki saari conditions False ho gayi, tab yeh fallback block execute hota hai.

### 2. Decision Logic Ka Ganit
Decision branch ek predicate function hota hai jo state $\mathbf{x}$ ko Boolean outcome $\{0, 1\}$ mein map karta hai:

$$
f: \mathcal{X} \to \{0, 1\}
$$

Chain ke andar har condition tabhi evaluate hoti hai jab pichli saari conditions False hoti hain:

$$
P_i \iff \left(\bigwedge_{j=1}^{i-1} \neg f_j(\mathbf{x})\right) \land f_i(\mathbf{x})
$$

### 3. Truthiness Aur Falsy Values
Python mein har object ki apni "truthiness" hoti hai. Agar kisi value ko `if` statement mein daala jaaye:
- Falsy values: `0`, `0.0`, `""` (empty string), `[]` (empty list), `()` (empty tuple), `{}` (empty dict), `None`, `False`.
- Truthy values: Koi bhi non-zero number, non-empty string ya collection.

---

## 💻 Python Code Aur Implementation
```python
# Production Conditional Demonstration
def evaluate_admission_status(score: float, age: int) -> str:
    """Determines university admission qualification based on score and age."""
    if score >= 90.0:
        if age >= 18:
            return "DIRECT_ADMISSION_HONORS"
        else:
            return "PROVISIONAL_ADMISSION_UNDERAGE"
    elif score >= 75.0:
        return "STANDARD_ADMISSION"
    elif score >= 60.0:
        return "WAITLIST_REVIEW"
    else:
        return "ADMISSION_REJECTED"

print("Score 92, Age 20:", evaluate_admission_status(92, 20))
print("Score 84, Age 19:", evaluate_admission_status(84, 19))
print("Score 52, Age 21:", evaluate_admission_status(52, 21))
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Har operation ki asymptotic execution limits.
- **Space Complexity:** Memory footprint aur call stack activation analysis.
