# Lecture 03.02: Conditionals Ke Practical Examples (हिंग्लिश)

## 📌 Module Overview
Practical conditional problems: Driving license eligibility, academic grade assignment, aur tax bracket calculations.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Real-World Decision Architecture
Jab hum real-world systems build karte hain, toh hume multiple ranges aur conditions ko combine karna hota hai.

### 2. Grading System Ka Mathematical Mapping

$$
\text{Grade}(G) = \begin{cases}
'A' & \text{if } 90 \le G \le 100 \\
'B' & \text{if } 80 \le G < 90 \\
'C' & \text{if } 70 \le G < 80 \\
'D' & \text{if } 60 \le G < 70 \\
'F' & \text{otherwise}
\end{cases}
$$

Python chained comparisons jaise `90 <= marks <= 100` ko cleanly support karta hai jo mathematical notation ke exact barabar hai.

### 3. Defensive Input Validation
Koi bhi decision lene se pehle input bounds check karna zaroori hota hai taaki out-of-range data (jaise negative marks ya $>100$) system ko corrupt na kare.

---

## 💻 Python Code Aur Implementation
```python
def calculate_grade(marks: float) -> str:
    if not (0 <= marks <= 100):
        raise ValueError(f"Invalid marks {marks}: must be between 0 and 100")
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

for score in [95, 82, 74, 61, 45]:
    print(f"Marks: {score} -> Grade: {calculate_grade(score)}")
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Har operation ki asymptotic execution limits.
- **Space Complexity:** Memory footprint aur call stack activation analysis.
