# Lecture 06.07: Exception Handling Fundamentals (`try`, `except`) [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_06_07.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 06 Module Par Wapas Jayein](../README_HINGLISH.md)

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Syntax Errors vs Runtime Exceptions ke beech ka farq.
- Exceptions kyu hoti hain: `ZeroDivisionError`, `ValueError`, `FileNotFoundError`, `TypeError`, `NameError`.
- Basic `try...except` block ka control flow aur graceful degradation.
- Specific exception catching kyu best practice hai (broad bare `except:` avoid karna).

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

- **Exception Kya Hai**: Exception ek runtime error hota hai jo program chalte waqt kisi unexpected condition (jaise zero se divide karna ya missing file kholna) ki wajah se raise hota hai. Agar ise handle na karein to program crash ho jata hai.

- **`try` Block**: Woh code jisme error aane ki sambhavna ho, use `try` block ke andar likha jata hai.

- **`except` Block**: Agar `try` block me koi error aata hai, to Python execution crash hone ke bajay `except` block me jump karta hai jahan hum alternate action ya error message display karte hain.

- **Specific vs Bare Except**: Hamesha specific exception catch karna chahiye (e.g. `except ZeroDivisionError:`). Bare `except:` use karne se `KeyboardInterrupt` (Ctrl+C) aur system errors bhi catch ho jate hain jo debugging ko mushkil banate hain.

- **Lecture Examples**: Ma'am ne 4 common errors sikhaye: `10 / 0` (`ZeroDivisionError`), `int('abc')` (`ValueError`), missing file (`FileNotFoundError`), aur wrong operation on type (`TypeError`).

---

## 2. Visual Architecture & Workflow Diagram

```mermaid
flowchart TD
    A["Normal Program Execution"] --> B["Enter try Block"]
    B --> C{"Did an error occur?"}
    C -->|No| D["Complete try Block Smoothly"]
    C -->|Yes| E{"Does error match specific except type?"}
    E -->|Yes| F["Execute except Handler<br/>(Program Continues Without Crashing)"]
    E -->|No| G["Propagate Exception up the Stack<br/>(Program Terminates)"]
    D & F --> H["Resume Rest of Code Normally"]
```

---

## 3. Mathematical & Theoretical Framework

Let program execution state be $S \in \mathcal{S}$. A protected operation $f: \mathcal{S} \to \mathcal{S} \cup \mathcal{E}$ maps either to a valid state or an error $\epsilon \in \mathcal{E}$:

$$
\text{try-catch}(f, S) = \begin{cases} 
f(S) & \text{if } f(S) \in \mathcal{S} \\
\text{handler}(\epsilon) & \text{if } f(S) = \epsilon \in \mathcal{E}_{\text{caught}} \\
\text{crash}(\epsilon) & \text{if } \epsilon \notin \mathcal{E}_{\text{caught}}
\end{cases}
$$

---

## 4. Structured Implementation & Execution

```python
def safe_division_and_conversion(dividend: str, divisor: str) -> dict:
    """
    Demonstrates specific exception handling covering ValueError, ZeroDivisionError,
    and unexpected type mismatches.
    
    Parameters:
    -----------
    dividend : str
        Numerator input string to convert and divide.
    divisor : str
        Denominator input string.
        
    Returns:
    --------
    dict
        Computed quotient or structured error diagnosis.
    """
    result = {
        "success": False,
        "quotient": None,
        "error_type": None,
        "error_message": None
    }
    
    try:
        num = float(dividend)
        den = float(divisor)
        quotient = num / den
        
        result["success"] = True
        result["quotient"] = quotient
        
    except ValueError as ve:
        result["error_type"] = "ValueError"
        result["error_message"] = f"Invalid numeric format: {ve}"
        
    except ZeroDivisionError as zde:
        result["error_type"] = "ZeroDivisionError"
        result["error_message"] = "Cannot divide by zero in standard arithmetic."
        
    except Exception as general_err:
        result["error_type"] = type(general_err).__name__
        result["error_message"] = str(general_err)
        
    return result

# Driver test cases
cases = [
    ("100", "4"),       # Valid division
    ("50", "0"),        # ZeroDivisionError
    ("hello", "5"),     # ValueError
    ("25", "2.5")       # Valid float division
]

print("Exception Handling Test Suite:")
for div, den in cases:
    res = safe_division_and_conversion(div, den)
    status_str = f"Quotient={res['quotient']}" if res['success'] else f"Caught {res['error_type']} ({res['error_message']})"
    print(f"  Inputs ({div} / {den}) -> {status_str}")
```

---

## 5. Mukhya Batein (Key Takeaways) & Summary
- Code ko modular function ke roop me likha gaya hai jisme clear shuruat (`def`), docstrings, error handling, aur ending (`return`) maujood hai.
- Video lectures me ma'am dwara sikhaye gaye exact concepts, slides aur Assignment 5 ke requirements ko 100% follow kiya gaya hai.
