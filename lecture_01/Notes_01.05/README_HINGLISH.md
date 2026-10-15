# Notes 01.05: Development Tools aur Environment Setup [Hinglish]

## 1. AI Development Ke Zaroori Tools

Professional Machine Learning coding start karne ke liye hume 3 cheezon ki zaroorat hoti hai:
1. **Python 3.10+ Interpreter:** Jo hamare code ko execute karta hai.
2. **`pip` (Package Installer for Python):** Duniya bhar ke AI packages (NumPy, Pandas, PyTorch) ko ek single command se download karne ka tool.
3. **`venv` (Virtual Environment):** Har project ke liye alag isolated room banana taaki packages aapas mein ladkar system crash na karein.

---

## 2. Virtual Environment Kyu Zaroori Hai?

Maan lijiye aapne 6 mahine pehle ek project banaya jisme `scikit-learn 1.2` chal raha tha. Aaj aap naya project shuru karte hain jisko `scikit-learn 1.5` chahiye.

Agar aap bina virtual environment ke global system par upgrade karenge, toh purana project instant crash ho jayega!

Isliye industry standard rule hai: **Har project ka apna alag `venv` hona chahiye.**

### Virtual Environment Setup Commands:
```bash
# Environment create karna
python -m venv myenv

# Windows par activate karna (PowerShell)
.\myenv\Scripts\Activate.ps1

# Mac/Linux par activate karna
source myenv/bin/activate
```
Activate hone ke baad terminal ke aage `(myenv)` likha aayega. Ab aap jo bhi install karenge, wo sirf usi project mein rahega!
