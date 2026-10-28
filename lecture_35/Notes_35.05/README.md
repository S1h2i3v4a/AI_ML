# Submodule 35.05: Configuring Git (Identity & Settings)

## 1. First-Time Setup Requirements

Before creating commits, Git requires you to configure your **author identity**. Every commit you create is permanently stamped with your name and email address. This ensures full accountability and correct authorship attribution across collaborative teams.

---

## 2. Essential Configuration Commands

Set your identity globally across your entire system using the `--global` flag:

### 1. Setting Author Name:
```bash
git config --global user.name "Your Name"
```
*Example:*
```bash
git config --global user.name "Shivam Keshari"
```

### 2. Setting Author Email:
```bash
git config --global user.email "your.email@example.com"
```
*Example:*
```bash
git config --global user.email "shivamkeshari@gmail.com"
```

> [!IMPORTANT]
> The email configured in `user.email` should match the primary email address registered on your GitHub account. This ensures that GitHub correctly maps your local commits to your online profile and lights up your contribution heatmap.

---

## 3. Inspecting Git Configurations

To verify your configuration values at any time, execute:

```bash
# View all active configurations
git config --list

# Or query specific keys
git config user.name
git config user.email
```

### Where Configurations are Stored:
- **Global**: Stored in `~/.gitconfig` (applies to all repositories for the current operating system user).
- **Local**: Stored in `.git/config` inside a specific repository (overrides global settings for that specific project).
