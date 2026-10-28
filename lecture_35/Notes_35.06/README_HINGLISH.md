# Submodule 35.06: VS Code ke Sath Git Use Karna (Hinglish)

## 1. Integrated Terminal ka Fayda

Code likhte waqt bar-bar bahar ja kar alag terminal window kholne ki zaroorat nahi hoti. **Visual Studio Code (VS Code)** ke andar hi terminal integrate hota hai, jisse aap ek hi screen par code bhi likh sakte ho aur Git commands bhi chala sakte ho.

---

## 2. VS Code mein Terminal Kaise Kholein?

1. **Keyboard Shortcut**: Keyboard par ``Ctrl + ` `` (backtick) dabayein.
2. **Top Menu**: Menu bar mein **Terminal** $	o$ **New Terminal** par click karein.
3. Screen ke bottom mein terminal panel open ho jayega jo directly aapke open project folder par set hoga.

---

## 3. Windows par Git Bash ko Default Profile Banana

Windows par VS Code aksar default mein PowerShell kholta hai. Git Bash ko default karne ke liye:
1. Terminal panel ke top-right mein `+` ke paas dropdown arrow par click karein.
2. **Select Default Profile** chunein.
3. List mein se **Git Bash** select karein.
4. Ab naya terminal kholne par hamesha Git Bash open hoga jisme saari Linux/Bash commands smoothly chalengi.

---

## 4. Verification

Terminal mein command chala kar check karein:
```bash
git --version
```
Ab aap VS Code ke andar se hi `git status`, `git add`, `git commit` aasaani se execute kar sakte hain.
