# Lecture 03.04: Nesting (Hierarchical Decision Trees)

## 📌 Executive Summary
Nested conditionals, cyclomatic complexity management, guard clauses, and early return patterns.

---

## 🔬 Theoretical Foundations & Principles
### 1. Hierarchical Branching
Nesting occurs when a conditional statement is located within the suite of another conditional.

### 2. Cyclomatic Complexity ($M$)
Thomas McCabe's cyclomatic complexity metric measures the number of linearly independent paths through a program's source code:

$$
M = E - N + 2P
$$

Where $E$ is the number of edges, $N$ is nodes, and $P$ is connected components. Excessive nesting dramatically increases $M$, impairing maintainability.

### 3. The Guard Clause Refactoring Pattern
Replace deep nested pyramids with flat guard clauses that exit early upon failure conditions.

---

## 💻 Production Implementation & Code
```python
# Poor: Deeply nested pyramid
def verify_access_nested(user, authenticated, active, role):
    if authenticated:
        if active:
            if role == "ADMIN":
                return "FULL_ACCESS"
            else:
                return "LIMITED_ACCESS"
        else:
            return "ACCOUNT_INACTIVE"
    else:
        return "UNAUTHENTICATED"

# Production: Flat Guard Clauses
def verify_access_guarded(user, authenticated, active, role):
    if not authenticated:
        return "UNAUTHENTICATED"
    if not active:
        return "ACCOUNT_INACTIVE"
    if role == "ADMIN":
        return "FULL_ACCESS"
    return "LIMITED_ACCESS"

print("Guarded Access:", verify_access_guarded("Alice", True, True, "ADMIN"))
```

---

## ⚙️ Algorithmic Complexity & Systems Analysis
- **Time Complexity:** Detailed in respective algorithmic operations.
- **Auxiliary Space:** Memory bounds and CPython frame management.
