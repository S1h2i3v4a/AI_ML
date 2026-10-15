# Notes 01.06: Official Installation & Configuration Guide

## 1. Python Installation Walkthrough

### For Windows:
1. Visit the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest Python installer (e.g., Python 3.10+).
3. **CRITICAL STEP:** On the very first installer screen, check the box:
   $$\boxed{\checkmark \text{ Add python.exe to PATH}}$$
   *Failure to check this box prevents the command prompt and terminal from recognizing `python` and `pip` commands.*
4. Click **Install Now**.
5. Once completed, click **Disable path length limit** if prompted.

### For macOS:
1. Download the macOS 64-bit universal2 installer from python.org or install via Homebrew:
   ```bash
   brew install python
   ```
2. Run the `Install Certificates.command` file located in the Python folder inside Applications.

---

## 2. Verifying Installation & PATH Configuration

Open your terminal (PowerShell, Command Prompt, or Bash) and execute:
```bash
python --version
pip --version
```

If you receive `'python' is not recognized as an internal or external command`, it indicates Python was not registered to your operating system's `PATH` environment variable.

### Adding Python to PATH Manually on Windows:
1. Search for **Environment Variables** in Windows search.
2. Under **User variables**, select **Path** and click **Edit**.
3. Add the path to Python directory (e.g., `C:\Users\<Username>\AppData\Local\Programs\Python\Python312\`) and the Scripts directory (e.g., `...\Python312\Scripts\`).

---

## 3. Resolving PowerShell Script Execution Policy

On Windows, activating virtual environments in PowerShell may trigger:
`File ... Activate.ps1 cannot be loaded because running scripts is disabled on this system.`

Resolve this by executing PowerShell as Administrator and running:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
