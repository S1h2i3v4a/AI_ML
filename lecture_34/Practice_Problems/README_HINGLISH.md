# Day 34 Practice Problems: Terminal & Shell Operations (Hinglish)

Yeh practice suite teen production-grade engineering challenges provide karti hai taaki aap Day 34 mein seekhe gaye command-line concepts, path navigation, file lifecycle, aur safe deletion techniques ko master kar sakein.

---

## Challenge 1: Production Server Triage & Path Resolution

### Background & Context
Aapne SSH ke through ek remote Ubuntu GPU compute instance (`ai-prod-node-04`) par login kiya hai. Ek computer vision pipeline raat ke 02:30 AM par crash ho gayi kyunki dataset path galat tha. Aapko bina kisi graphical GUI ke sirf terminal commands se directory inspect karni hai, logs dhoondhne hain, aur hidden environment files verify karni hain.

### Tasks & Sawal
1. **Print Current Location**: Confirm karo ki abhi aap kis folder mein khade ho using standard print working directory command.
2. **Detailed Directory Listing**: Current directory ke sabhi contents list karo jisme hidden dotfiles (`.bashrc`, `.env`, `.git`), unke exact permissions, file size, aur timestamps visible hon.
3. **Absolute vs Relative Navigation**:
   - Server logs `/var/log/cv_pipeline/crash_dump.log` par store hain. Explain karo yeh absolute path hai ya relative path aur kyun?
   - `/var/log/cv_pipeline/` ke andar absolute path use karke navigate karo.
   - `/var/log/cv_pipeline/` ke andar se direct do level upar `/var/` mein jao ek single relative command use karke (bina `/var` explicitly type kiye).
4. **Home Directory Return**: Apne user home directory (`/home/engineer/`) mein single shortcut command se instantly wapas aao.

---

## Challenge 2: MLOps Project Workspace Scaffolding

### Background & Context
Aapko ek naya NLP sentiment analysis project `sentiment_llm` set up karna hai. Mouse ya File Explorer se folder banane ke bajaye aapko pura folder hierarchy terminal commands se banana hai.

### Tasks & Sawal
1. **Directory Tree Creation**:
   - Root project folder `sentiment_llm` banao aur uske andar jao.
   - Teen subdirectories banao: `data`, `src`, aur `checkpoints`.
   - `data` ke andar do separate folders banao: `raw` aur `processed`.
2. **File Initialization**:
   - `src` folder ke andar teen empty files create karo: `dataset.py`, `model.py`, aur `train.py`.
   - Root project folder `sentiment_llm` mein ek dependency manifest `requirements.txt` aur ek hidden `.env` file create karo.
3. **Timestamp Refresh**:
   - Maan lo `requirements.txt` pehle se bani hui hai. `touch` command ka use karke uski modification date-time ko current timestamp par update karo bina file ka content change kiye.
4. **Validation**:
   - Ek single command aur flags run karke verify karo ki saari files (including hidden `.env`) aur subdirectories properly ban gayi hain.

---

## Challenge 3: Defensive Disk Cleanup & Safe Deletion Governance

### Background & Context
Aapke server ka storage volume `/mnt/scratch_storage` 98% full ho chuka hai. Puraane training runs ne hazaaron temporary checkpoint files chhod di hain. Aapko safely disk space free karni hai bina kisi production model ya OS path ko delete kiye.

### Tasks & Sawal
1. **Empty vs Non-Empty Directory Deletion**:
   - Ek puraana empty folder hai `stale_cache/`. Kaunsi safe command se ise delete karoge jo check kare ki folder sach mein empty hai aur agar file ho toh delete na kare?
   - Ek puraana experiment folder hai `run_epoch_01/` jisme 50 model weights (`.pt`) aur log files bhari hain. Is pure non-empty directory tree ko kaise delete karoge?
2. **Dangerous Commands ka Risk Analysis**:
   - Agar koi junior engineer galti se yeh command run kar de:
     ```bash
     rm -rf / tmp/old_checkpoints
     ```
     *(Dhyan do `/` aur `tmp/old_checkpoints` ke beech space hai)*. Iska server par kya bhayanak asar padega?
   - Terminal deletion graphical Desktop GUI (Recycle Bin / Trash) se fundamentally alag kyun hai?
3. **Safe Deletion Protocol**:
   - Production server par recursive `rm` chalane se pehle kaunse 3 safety checks follow karne chahiye?

---

## Solutions Reference
Step-by-step verified bash commands aur full technical explanations ke liye [Solutions_HINGLISH.md](file:///c:/Users/Shivam%20Keshari/OneDrive/Desktop/AI-ML/lecture_34/Practice_Problems/Solutions_HINGLISH.md) check karein.\n