# Module 24.01: Feature Engineering — Categorical Encoding (Hinglish)

## 1. Encoding Ki Zaroorat Kyu Hoti Hai?

Machine Learning ke sabhi algorithms (Linear Regression, Logistic Regression, Neural Networks) numbers aur matrix multiplication ($\mathbf{X} \mathbf{w}$) par kaam karte hain. Computer strings jaise `"Red"`, `"Male"`, ya `"Bachelors"` ko mathematically multiply ya subtract nahi kar sakta.

Isliye hume categorical text data ko numbers mein convert karna padta hai, jise **Categorical Encoding** kehte hain.

Categorical features 2 tarah ke hote hain:
1. **Nominal Data:** Jisme koi order ya ranking nahi hoti (e.g. `["Red", "Blue", "Green"]` ya `["India", "USA", "UK"]`).
2. **Ordinal Data:** Jisme ek natural hierarchy ya order hota hai (e.g. `["Poor", "Average", "Good"]` ya `["High School", "Bachelors", "Masters", "PhD"]`).

---

## 2. Encoding Ke Tareeqe

### 1. Label / Ordinal Encoding
Har category ko ek integer number de diya jata hai:
`"High School" -> 0, "Bachelors" -> 1, "Masters" -> 2, "PhD" -> 3`.

**Khatra:** Agar ise Nominal data par laga diya (`"Red" -> 0, "Blue" -> 1, "Green" -> 2`), to Linear Regression sochega ki Green, Red se do guna bada hai ($2 > 0$), jo bilkul galat assumption hai!

### 2. One-Hot Encoding (OHE)
Har category ke liye ek naya binary ($0$ ya $1$) column banaya jata hai:
- Agar 3 colors hain to 3 naye columns banenge: `is_red`, `is_blue`, `is_green`.
- Red ke liye vector hoga `[1, 0, 0]`.
- Isme saari categories mutually orthogonal hoti hain aur koi jhoothi ranking create nahi hoti!
