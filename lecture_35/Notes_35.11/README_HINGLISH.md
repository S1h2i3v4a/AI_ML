# Submodule 35.11: Git Init Command (Hinglish)

## 1. `git init` kya karta hai?

`git init` command kisi bhi aam normal folder ko ek active **Git Repository** mein convert kar deti hai.

### Clone aur Init ka Farak:
- **`git clone`**: Jab project pehle se GitHub par bana hua hai, tab use apne computer par laane ke liye clone karte hain.
- **`git init`**: Jab aap apne computer par bilkul scratch se naya project shuru kar rahe ho aur chahte ho ki Git is folder ke changes track kare.

---

## 2. Command Execution

Terminal mein project folder ke andar jakar run karein:

```bash
git init
```

### Output:
```text
Initialized empty Git repository in C:/Users/Engineer/my_ml_project/.git/
```

### Parde ke peeche kya hota hai?
Git is folder ke andar ek hidden `.git/` folder create karta hai:
- Is `.git/` folder ke andar Git ka pura internal database hota hai (objects, commits, branches, config).
- **Caution**: Is hidden `.git/` folder ko kabhi manual delete mat karna, warna project ka pura commit history gayab ho jayega!
