# Notes 01.05: Core Development Tools & Ecosystem Setup

## 1. Essential Toolchain for AI Engineering

An enterprise-ready AI development environment comprises three foundational components:
1. **The Python Runtime Engine:** The CPython interpreter that parses and executes bytecode. (Recommended version: Python 3.10 to 3.12).
2. **The Package Manager (`pip`):** The standard package installer connecting to the Python Package Index (PyPI) hosting >500,000 open-source libraries.
3. **Environment Isolation Engine (`venv`):** Sandboxing tool preventing dependency version collision across distinct projects.

---

## 2. Why Virtual Environments are Mandatory in AI

In machine learning engineering, different projects frequently depend on conflicting versions of critical libraries:
- **Project Alpha (Computer Vision):** Requires `torch==2.0.1` and `torchvision==0.15.2`.
- **Project Beta (Legacy NLP):** Requires `torch==1.12.1` and `transformers==4.21.0`.

Installing packages globally to the root operating system directory corrupts the global site-packages, causing unrecoverable dependency breakages (`pip dependency hell`).

### Creating an Isolated Virtual Environment:
```bash
# 1. Navigate to your project directory
cd my_ai_project

# 2. Create an isolated virtual environment named 'aiml_env'
python -m venv aiml_env

# 3. Activate the environment
# Windows (PowerShell):
.\aiml_env\Scripts\Activate.ps1
# Windows (CMD):
.\aiml_env\Scripts\activate.bat
# macOS / Linux:
source aiml_env/bin/activate

# 4. Verify that python points to the isolated sandbox
which python   # macOS/Linux
where.exe python   # Windows
```
