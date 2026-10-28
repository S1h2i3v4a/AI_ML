# Day 35 Practice Problems: Git & GitHub Engineering Suite (Hinglish)

Yeh practice suite teen real-world industry challenges provide karti hai taaki aap Day 35 mein seekhe gaye branching strategies, merge conflict resolution, pull request lifecycles, aur disaster recovery techniques ko thoroughly master kar sakein.

---

## Challenge 1: Production Hotfix & Branch Isolation Pipeline

### Background & Context
Aap ek fintech startup mein AI engineer ho. Aap apne local computer par `feature-fraud-v2` branch par ek naya fraud detection model develop kar rahe ho. Achanak DevOps team ka message aata hai ki production `main` branch mein ek critical authentication security bug aa gaya hai jise turant theek karna zaroori hai.

### Tasks & Sawal
1. **Status Check**:
   - Kaunsi command se check karoge ki aap abhi kis branch par ho aur kaunsi files modified hain?
2. **Safe Branch Switching**:
   - Agar aap adhe-adhure code ke sath seedhe `git checkout main` karoge toh kya problem aa sakti hai?
   - Apne `feature-fraud-v2` branch ke current kaam ko commit karke kaise safe karoge?
3. **Hotfix Branch Creation & Fix**:
   - `main` branch par switch karke GitHub se latest code pull karo.
   - `main` se ek nayi branch `hotfix-auth-patch` banao aur usme switch karo.
   - `auth.py` file fix karke commit karo with message `"Patch CVE auth token bypass"`.
4. **Merge & Cleanup**:
   - `main` branch mein wapas aakar is hotfix ko merge karo aur GitHub par push karo.
   - Kaam khatam hone par local `hotfix-auth-patch` branch ko delete karo.
   - Wapas apni original `feature-fraud-v2` branch mein jakar apna puraana development resume karo.

---

## Challenge 2: Multi-Developer Merge Conflict Resolution

### Background & Context
Aap aur aapka teammate (Engineer B) dono ek hi file `database.py` par kaam kar rahe the:
- Engineer B ne GitHub `origin/main` par push kar diya jisme database port `5432` aur connection pool `20` set tha.
- Same time par aapne apne local machine ke `main` branch par wahi exact line change karke port `5433` aur connection pool `50` kar diya.

Jab aapne `git pull origin main` chalaya, toh Git ne error diya:
```text
CONFLICT (content): Merge conflict in database.py
Automatic merge failed; fix conflicts and then commit the result.
```

### Tasks & Sawal
1. **Conflict Markers ka Anatomy**:
   - Git file ke andar jo conflict markers lagata hai (`<<<<<<< HEAD`, `=======`, `>>>>>>>`), unka exact structure likhkar samjhao ki aapka code kaunsa hai aur doosre ka kaunsa.
2. **Conflict Resolve Karna**:
   - Maan lo team ka decision hai ki port `5432` (Engineer B ka) rahega, par connection pool `50` (aapka) rahega. Final clean file bina kisi marker ke kaise dikhegi?
3. **Final Merge Sequence**:
   - File edit karne ke baad use stage karne, merge commit banane, aur GitHub par push karne ka complete terminal command sequence likho.

---

## Challenge 3: Disaster Recovery & Accidental Secret Commit Mitigation

### Background & Context
Ek naye developer ne galti se `.env` file ke andar live OpenAI API Key aur AWS password likh kar yeh chala diya:
```bash
git add .
git commit -m "Add API endpoints and keys"
git push origin main
```
Yeh repository GitHub par public hai, aur web bots ne wo secret key scan kar li hai.

### Tasks & Sawal
1. **Pehla Emergency Action**:
   - Git command chalane se pehle sabse pehla aur sabse critical action kya lena chahiye?
2. **File ko Local Par Rakh kar Git se Hatana**:
   - Agar developer `rm .env` chalata hai toh computer se hi file delete ho jati hai jisse local project chalna band ho jata hai. Kaunsi Git command se file disk par bachi rahegi par Git ke index se delete ho jayegi?
3. **`.gitignore` Rules**:
   - `.gitignore` ke andar kya likhein taaki aage se `.env` ya `.env.local` kabhi bhi galti se Git mein track na hon?
4. **`git revert` vs `git reset` Analysis**:
   - Public repository ke case mein `git revert` aur `git reset --hard` ka kya impact hota hai? Secret leaked hone ke baad API key rotate/invalidate karna kyun mandatory hai?

---

## Solutions Reference
Complete step-by-step verified bash commands aur full explanations ke liye [Solutions_HINGLISH.md](file:///c:/Users/Shivam%20Keshari/OneDrive/Desktop/AI-ML/lecture_35/Practice_Problems/Solutions_HINGLISH.md) check karein.
