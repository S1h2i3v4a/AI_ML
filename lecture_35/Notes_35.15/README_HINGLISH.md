# Submodule 35.15: Git Branch Commands (Hinglish)

## 1. Branch Commands ka Overview

Git branches ko create karne, dekhne, switch karne, aur delete karne ke liye dedicated commands hoti hain.

---

## 2. Mukhya Commands ki List

### 1. Saari Branches Dekhna:
```bash
git branch
```
- Project ki saari local branches list karta hai.
- Star (`*`) aur green color batata hai ki aap abhi kis branch par khade ho.

### 2. Nayi Branch Banana:
```bash
git branch feature-login
```
*(Nayi branch ban jati hai par aap abhi usi purani branch par rehte ho).*

### 3. Branch Change (Switch) Karna:
```bash
# Puraani command
git checkout feature-login

# Nayi modern command
git switch feature-login
```
- Aapka working directory target branch ke code par update ho jata hai aur `HEAD` pointer wahan shift ho jata hai.

### 4. Nayi Branch Banakar Turant Switch Karna (Short Command):
```bash
git checkout -b feature-login
# Ya:
git switch -c feature-login
```
Yeh sabse popular command hai jo 1 second mein branch banakar usme enter bhi kar deti hai.

### 5. Branch Rename Karna:
```bash
git branch -M main
```

### 6. Branch Delete Karna:
```bash
# Safe deletion (agar code merge ho chuka hai)
git branch -d feature-login

# Force deletion (bina merge kiye forcefully delete)
git branch -D feature-login
```

> [!CAUTION]
> Jis branch par aap khade ho, use delete nahi kar sakte. Pehle `git checkout main` karein, phir doosri branch delete karein.
