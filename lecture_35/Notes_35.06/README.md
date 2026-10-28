# Submodule 35.06: Git with Visual Studio Code

## 1. The Integrated Development Environment Workflow

Rather than switching back and forth between an external terminal window (like Git Bash) and your code editor, **Visual Studio Code (VS Code)** provides an integrated terminal environment. This allows you to write code, review diffs, and issue Git commands inside a single consolidated workspace.

---

## 2. Accessing the Integrated Terminal

1. **Keyboard Shortcut**: Press ``Ctrl + ` `` (Backtick) on Windows/Linux or ``Cmd + ` `` on macOS.
2. **Top Menu**: Navigate to **Terminal** $	o$ **New Terminal**.
3. **Bottom Panel**: The terminal panel opens at the bottom of the editor workspace, already anchored to your currently opened project folder.

---

## 3. Configuring Git Bash as Default Terminal on Windows

By default, Windows VS Code may launch PowerShell or Command Prompt (`cmd.exe`). To ensure POSIX Bash compatibility:
1. Open the terminal dropdown menu in the top-right corner of the terminal pane.
2. Click **Select Default Profile**.
3. Choose **Git Bash** from the available shell list.
4. Open a new terminal tab; it will now launch directly in Git Bash with full Unix syntax support.

---

## 4. Verifying Git Inside VS Code

Run the verification command directly in the integrated terminal:
```bash
git --version
```
Once verified, you can execute all Git commands (`git status`, `git add`, `git commit`, `git push`) seamlessly without ever leaving your editor.
