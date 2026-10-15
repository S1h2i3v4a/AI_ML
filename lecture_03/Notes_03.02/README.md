# Lecture 03.02: Practice Examples (Conditionals)

## 📌 Executive Summary
Real-world decision logic examples: Driving license eligibility, academic grading scales, and tax bracket calculations.

---

## 🔬 Theoretical Foundations & Principles
### 1. Complex Real-World Predicates
Combining multiple operational thresholds requires structured chained comparisons and range evaluations.

### 2. Multi-Tier Grading Bracket Model
Given numerical grade $G \in [0, 100]$:

$$
\text{Grade}(G) = \begin{cases}
'A' & \text{if } 90 \le G \le 100 \\
'B' & \text{if } 80 \le G < 90 \\
'C' & \text{if } 70 \le G < 80 \\
'D' & \text{if } 60 \le G < 70 \\
'F' & \text{otherwise}
\end{cases}
$$

### 3. Short-Circuit Evaluation Efficiency
When testing composite conditions with `and` / `or`, place cheap, highly selective conditions first to minimize expensive sub-expression evaluations.

---

## 💻 Production Implementation & Code
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

## ⚙️ Algorithmic Complexity & Systems Analysis
- **Time Complexity:** Detailed in respective algorithmic operations.
- **Auxiliary Space:** Memory bounds and CPython frame management.
