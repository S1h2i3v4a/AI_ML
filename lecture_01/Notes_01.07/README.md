# Notes 01.07: Mastering Visual Studio Code for AI/ML Engineering

## 1. Why Visual Studio Code is the Premier AI Editor

Microsoft Visual Studio Code (VS Code) has become the gold-standard code editor in data science and AI engineering. It seamlessly combines:
- A lightning-fast, lightweight text editor.
- Built-in interactive **Jupyter Notebook (`.ipynb`)** execution engine.
- Integrated multi-shell terminal (PowerShell, Bash, WSL).
- Rich debugging with variable inspection and memory inspection.
- Native Git source control integration.

---

## 2. Essential Extensions for AI Engineers

Search and install from the VS Code Extensions Marketplace (`Ctrl+Shift+X`):
1. **Python (by Microsoft):** Provides IntelliSense, linting, code formatting, and debugging.
2. **Pylance:** Fast, feature-rich language support with type checking.
3. **Jupyter (by Microsoft):** Enables running interactive notebook cells directly inside VS Code without launching a separate browser server.

---

## 3. Selecting the Correct Python Interpreter

When working inside VS Code with virtual environments, you must tell the editor which Python binary to use:
1. Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on Mac) to open the Command Palette.
2. Type and select: `Python: Select Interpreter`.
3. Choose the interpreter located inside your project's `.venv` or `aiml_env` directory (e.g., `./aiml_env/Scripts/python.exe`).
4. The selected environment will now display in the bottom-right status bar.

---

## 4. Script (`.py`) vs Notebook (`.ipynb`) Workflow

| Feature | Python Script (`.py`) | Jupyter Notebook (`.ipynb`) |
| :--- | :--- | :--- |
| **Execution Model** | Entire file executes top-to-bottom | Interactive cell-by-cell execution |
| **State Persistence**| Memory cleared when process exits | Variables, models, and data remain in RAM |
| **Best Used For** | Production pipelines, microservices, classes | Exploratory Data Analysis, model tuning, plotting |
