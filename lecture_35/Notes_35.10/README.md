# Submodule 35.10: The Git Push Command

## 1. What is Pushing?

When you run `git commit`, your changes are saved strictly on your local machine's disk. To share these commits with your team, back them up in the cloud, or update your production server, you must **push** them to the remote repository on GitHub.

```mermaid
flowchart LR
    A[Local Machine Repository<br/>Committed Inodes / HEAD] -->|git push origin main| B[Remote GitHub Repository<br/>Cloud Sync & Visibility]
```

---

## 2. Command Syntax & Upstream Configuration

```bash
git push <remote_name> <branch_name>
```

### Standard Command:
```bash
git push origin main
```
- **`origin`**: The default alias given to your remote repository URL on GitHub.
- **`main`**: The target branch on the remote repository receiving your local commits.

### Setting Upstream Tracking (`-u` flag):
The first time you push a newly initialized branch to GitHub, use the `-u` (or `--set-upstream`) flag:
```bash
git push -u origin main
```
- **What `-u` Does**: Establishes a permanent tracking link between your local `main` branch and `origin/main` on GitHub.
- **Subsequent Pushes**: Once configured, you can simply type `git push` without specifying `origin main` each time.

---

## 3. GitHub Authentication

When pushing commits, GitHub verifies write permissions:
- **Personal Access Tokens (PAT)**: GitHub has deprecated raw account passwords for CLI operations. You generate a token under GitHub **Settings** $	o$ **Developer Settings** $	o$ **Personal Access Tokens** with `repo` scope.
- **Git Credential Manager (GCM)**: On modern Windows/macOS installations, Git automatically opens a browser window for a one-click OAuth login, saving your credentials securely in the OS credential vault.
