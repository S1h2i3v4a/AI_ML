# Notes 01.06: Official Installation Guide (Windows & macOS) [Hinglish]

## 1. Python Kaise Install Karein?

### Windows Ke Liye Step-by-Step:
1. Official website par jayein: [python.org/downloads](https://www.python.org/downloads/)
2. Latest Python 3 installer download karein.
3. **SABSE ZAROORI STEP (Galti Mat Karna!):**  
   Installer open karte hi sabse niche ek checkbox hoga:
   $$\boxed{\checkmark \text{ Add python.exe to PATH}}$$
   Is box ko **zaroor check (tick) karein!** Agar aapne ise miss kar diya, toh terminal mein `python` command chalegi hi nahi aur error aayega.
4. **Install Now** par click karein. Setup complete hone ke baad close karein.

---

## 2. Check Karein Ki Python Sahi Install Hua Ya Nahi

Apne computer ka **Command Prompt (CMD)** ya **PowerShell** open karein aur type karein:
```bash
python --version
pip --version
```
Agar screen par `Python 3.12.x` aur `pip 24.x` likha aa raha hai, toh badhai ho! Aapka setup 100% successful ho chuka hai.

---

## 3. PowerShell "Running Scripts is Disabled" Error Fix

Windows PowerShell mein jab aap pehli baar virtual environment activate karenge, toh aksar security error aata hai:
`...Activate.ps1 cannot be loaded because running scripts is disabled...`

Iska instant fix:
Terminal mein bas yeh ek command run kar dein:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Iske baad `Activate.ps1` bina kisi rukawat ke chalega!
