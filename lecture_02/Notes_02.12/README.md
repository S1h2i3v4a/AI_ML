# 🚀 Lecture 02.12: Standard Input Stream & Parsing Pipelines

## 📌 Executive Architectural Summary
Interactive applications require ingest from external streams (`stdin`). In Python, this is handled by `input()`, which reads a line from the standard input console and returns it strictly as an immutable `str` (string).

---

## 🔬 Core Engineering Mechanics

### 1. The `input()` Contract
```python
val = input(prompt)
```
- Outputs the optional `prompt` to `stdout` without a trailing newline.
- Reads bytes from `sys.stdin` until encountering a newline (`\n`).
- Strips the trailing newline and returns the content as a `str` object.
- **Critical Invariant:** Regardless of what the user types (even digits), `input()` **ALWAYS returns a string**.

### 2. Type Parsing Pipelines
Because input is a string, mathematical processing requires explicit conversion:
```python
user_int = int(input("Enter integer: "))
user_float = float(input("Enter float: "))
```

---

## 💻 Production Python Implementation

```python
# Simulated Input Processing Pipeline

# 1. Parsing user inputs safely
def process_user_metrics(raw_name: str, raw_age: str, raw_height: str):
    name = raw_name.strip()
    age = int(raw_age)
    height_m = float(raw_height)
    
    print(f"Processed User: {name}, Age: {age}, Height: {height_m:.2f}m")
    return {"name": name, "age": age, "height": height_m}

# Demonstration
sample_data = process_user_metrics("  Shradha Khapra  ", "25", "1.65")
print("Structured Output:", sample_data)
```
