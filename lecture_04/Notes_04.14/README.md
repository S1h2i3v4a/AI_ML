# 🚀 Lecture 04.14: Practice Problems (Part c) — Dictionary Inversion & Grouping

## 📌 Executive Architectural Summary
This lecture focuses on **Dictionary Inversion**: swapping keys and values such that $d[k] = v \implies d_{	ext{inv}}[v] = k$. When values are non-unique, the inverted dictionary must map each unique value to a list or set of original keys to prevent collision overwrites.

---

## 🔬 Core Engineering Mechanics

### 1. Inversion with Injective (1-to-1) Mapping
If every value in $d$ is distinct:
$$
d_{	ext{inv}} = \{v: k 	ext{ for } k, v \in d.	ext{items}()\}
$$

### 2. Inversion with Non-Injective (Grouping) Mapping
If values can collide, accumulate original keys in a collection:
$$
d_{	ext{grouped}}[v] = \{k \mid d[k] = v\}
$$

---

## 💻 Production Python Implementation

```python
# Inverting student grades: Grades -> List of Students
student_grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "A",
    "David": "C",
    "Eva": "B"
}

# Grouping Inversion
grade_roster = {}
for student, grade in student_grades.items():
    if grade not in grade_roster:
        grade_roster[grade] = []
    grade_roster[grade].append(student)

print("Inverted Grade Roster:")
for grade, students in sorted(grade_roster.items()):
    print(f"Grade {grade}: {students}")
```
