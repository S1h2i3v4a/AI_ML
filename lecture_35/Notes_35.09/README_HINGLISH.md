# Submodule 35.09: Git Add aur Commit Commands (Hinglish)

## 1. Do-Step Commit Process

Git mein file save karna aam text editor ke `Ctrl + S` se alag hota hai. Git **2-Step Process** follow karta hai:

```mermaid
flowchart LR
    A[Working Directory<br/>Modified Files] -->|git add| B[Staging Area<br/>Prepared Box]
    B -->|git commit -m| C[Repository<br/>Permanent Snapshot]
```

Is do-step structure ka fayda yeh hai ki aap chun sakte ho ki kaunse files ka ek group bana kar commit karna hai.

---

## 2. `git add` Command (Staging)

`git add` command aapke changes ko Working Directory se nikaal kar Staging Area mein le aati hai:

```bash
# Kisi specific file ko stage karna
git add index.html

# Ek sath multiple files stage karna
git add app.js style.css

# Project ke saare modified aur new files ko ek sath stage karna
git add .
```

---

## 3. `git commit` Command (Permanent Save)

Staging area mein aayi files ko repository mein permanently record karne ke liye `git commit` chalate hain:

```bash
git commit -m "Aapka descriptive commit message"
```

*Example:*
```bash
git commit -m "Add navigation bar and login button"
```

### Commit mein kya-kya save hota hai?
- Ek unique 40-character **SHA Hash ID** (jaise `e082e89`).
- Author ka naam aur email address.
- Exact date aur time.
- Aapka likha hua message jo batata hai ki kya change hua.

### Short Command (`-am`):
Agar koi nayi file create nahi hui hai, sirf puraani files modify hui hain, toh aap add aur commit ek sath kar sakte ho:
```bash
git commit -am "Fix typo in login heading"
```
