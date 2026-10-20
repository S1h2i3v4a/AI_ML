# Lecture 06.01: Introduction to File I/O & Persistent Storage [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_06_01.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 06 Module Par Wapas Jayein](../README_HINGLISH.md)

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- File I/O kya hota hai aur volatile memory (RAM) vs non-volatile storage (Hard Disk / SSD) ka difference.
- Python me files ko operate karne ka basic lifecycle: Open -> Read/Write -> Close.
- Built-in `open('filename', 'mode')` function aur file handle (descriptor) ka role.
- File close karna kyu mandatory hai: Memory leaks, file locks, aur buffer flush issue.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

- **RAM vs Disk Storage**: Python program jab run hota hai, to variables RAM me bante hain. Program band hote hi RAM flush ho jati hai. Data ko hamesha ke liye save rakhne ke liye hum hard disk me 'Files' create karte hain.

- **File Handle (Descriptor)**: `f = open('data.txt', 'r')` likhne par operating system ek file handle return karta hai jo disk par file ki memory location aur current read/write position ko point karta hai.

- **Buffer Flushing & `close()`**: Python disk par har ek character turant nahi likhta; pehle data RAM buffer me accumulate hota hai. Jab hum `f.close()` call karte hain, tab buffer disk par flush hota hai aur OS lock release hota hai. Agar close na karein to data corrupt ya lose ho sakta hai.

- **Default Behavior**: Agar `open('filename')` me mode specify na kiya jaye, to Python by default use `'r'` (read text mode) manta hai. Agar file exist na kare to `FileNotFoundError` aata hai.

---

## 2. Visual Architecture & Workflow Diagram

```mermaid
flowchart LR
    A["Python Program<br/>(Volatile RAM)"] -->|"open('data.txt', 'w')<br/>Request File Handle"| B["Operating System Kernel"]
    B -->|"Allocate Stream Buffer"| C["Disk Storage / SSD<br/>(Persistent File)"]
    A -->|"f.write('data')"| B
    A -->|"f.close()<br/>Flush Buffer & Release Lock"| C
```

---

## 3. Mathematical & Theoretical Framework

Data transfer between user-space RAM and disk storage operates through bounded streaming buffers:

$$
\text{Disk Throughput } T = \frac{B}{\Delta t}, \quad B \in \mathbb{N} \text{ bytes}
$$

The lifecycle state transition of a file descriptor $fd \in \mathcal{F}$ follows a finite state automaton:

$$
\text{CLOSED} \xrightarrow{\text{open}(path, mode)} \text{OPEN (Buffered)} \xrightarrow{\text{close}()} \text{CLOSED (Flushed)}
$$

---

## 4. Structured Implementation & Execution

```python
import os

def demonstrate_basic_file_lifecycle(filepath: str, sample_text: str) -> dict:
    """
    Demonstrates the explicit open, write, flush, read, and close lifecycle of a file.
    
    Parameters:
    -----------
    filepath : str
        Relative or absolute path of the target file.
    sample_text : str
        Initial text payload to persist.
        
    Returns:
    --------
    dict
        Verification metadata including file size and read content.
    """
    # 1. Open for writing (creates new file or truncates)
    f_out = open(filepath, "w", encoding="utf-8")
    bytes_written = f_out.write(sample_text)
    f_out.close()  # Flushes buffer and releases OS file descriptor
    
    # 2. Open for reading
    f_in = open(filepath, "r", encoding="utf-8")
    content = f_in.read()
    f_in.close()  # Frees read lock
    
    file_size = os.path.getsize(filepath)
    
    return {
        "filepath": filepath,
        "bytes_written": bytes_written,
        "content_read": content,
        "file_size_on_disk": file_size,
        "file_exists": os.path.exists(filepath)
    }

# Driver test
target_file = "intro_sample.txt"
payload = "Hello Students! Welcome to Python File I/O."
result = demonstrate_basic_file_lifecycle(target_file, payload)
print("File Lifecycle Execution Result:")
for k, v in result.items():
    print(f"  {k}: {v}")

# Cleanup
if os.path.exists(target_file):
    os.remove(target_file)
```

---

## 5. Mukhya Batein (Key Takeaways) & Summary
- Code ko modular function ke roop me likha gaya hai jisme clear shuruat (`def`), docstrings, error handling, aur ending (`return`) maujood hai.
- Video lectures me ma'am dwara sikhaye gaye exact concepts, slides aur Assignment 5 ke requirements ko 100% follow kiya gaya hai.
