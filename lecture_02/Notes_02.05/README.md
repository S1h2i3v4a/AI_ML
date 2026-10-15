# 🚀 Lecture 02.05: PEP 8 Style Guide & Architectural Standards

## 📌 Executive Architectural Summary
Readability is a foundational pillar of the Python philosophy ("Readability counts" - The Zen of Python, PEP 20). **PEP 8** is the official style guide for Python code, standardizing indentation, whitespace, naming conventions, and file structures.

---

## 🔬 Core Engineering Mechanics

### 1. Strict Indentation Standard
- Python uses whitespace indentation instead of curly braces `{}` to delimit code blocks.
- **The Standard:** Exactly **4 spaces per indentation level**. Never mix physical tabs and spaces (`TabError`).

### 2. Naming Conventions (PEP 8)
- **Variables & Functions:** `snake_case` (lowercase words separated by underscores, e.g., `learning_rate`, `calculate_loss`).
- **Constants:** `UPPER_SNAKE_CASE` (e.g., `MAX_ITERATIONS`, `PI_VALUE`).
- **Classes:** `PascalCase` / `CapWords` (e.g., `NeuralNetwork`, `DataPreprocessor`).
- **Private Attributes:** Leading underscore (e.g., `_internal_cache`, `__private_key`).

---

## 💻 Production Python Implementation

```python
# PEP 8 Compliant Code Structure

# 1. Constants at module level
DEFAULT_BATCH_SIZE = 64
MAX_EPOCHS = 100

# 2. Function definition with 4-space indentation and clean spacing
def calculate_linear_activation(weight: float, feature: float, bias: float) -> float:
    # 4 spaces indentation
    linear_output = (weight * feature) + bias
    return linear_output

# Execution
w, x, b = 2.5, 4.0, 1.2
activation = calculate_linear_activation(w, x, b)
print(f"Activation Result: {activation:.4f}")
```
