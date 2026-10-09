# Module 23.13: Hands-On Linear Regression (Insurance Dataset)

## 1. Real-World End-to-End Pipeline

Is module mein hum real-world medical `insurance.csv` dataset par Linear Regression ka complete production-grade pipeline banate hain:

1. **Data Loading & Inspection:** Columns, data types, missing values check karna.
2. **Preprocessing:** Categorical text columns (`sex`, `smoker`, `region`) ko numbers mein convert karna (One-Hot Encoding).
3. **Train-Test Split:** 80% data training ke liye aur 20% unseen data evaluation ke liye alag karna.
4. **Model Training:** Scikit-Learn ke `LinearRegression` model ko fit karna.
5. **Coefficient Analysis:** Har feature ka learned weight dekhna (jaise smoking ka bill par kya asar padta hai).

---

## 2. Insurance Dataset Ka Structure

- `age`: Primary person ki umar.
- `sex`: Gender (`female`, `male`).
- `bmi`: Body Mass Index.
- `children`: Kitne bachhe dependent hain.
- `smoker`: Smoker hai ya nahi (`yes`, `no`).
- `region`: Kis area mein rehta hai.
- **Target `charges`:** Health insurance ka final medical bill ($).

---

## 3. Categorical Encoding (Dummy Variable Trap)

Linear Regression sirf numerical values samajhta hai. Isliye hum `pd.get_dummies(drop_first=True)` use karte hain:
- `drop_first=True` kyu? Agar 2 categories hain (`yes`, `no`), to sirf 1 column `smoker_yes` kaafi hai ($1 = \text{yes}, 0 = \text{no}$). Agar dono columns rakh lenge to multicollinearity ho jayegi jise **Dummy Variable Trap** kehte hain.

---

## 4. Learned Coefficients Ka Matlab

Model train hone ke baad hume milta hai:

$$
\hat{y} = b + w_1 \cdot \text{age} + w_2 \cdot \text{bmi} + w_3 \cdot \text{smoker\_yes} + \dots
$$

- **Smoker Coefficient:** Smoker hone par medical charges mein lagbhag $+\$23,800$ ka massive increase hota hai!
- **Age Coefficient:** Har saal umar badhne par lagbhag $+\$250$ bill badh jata hai.
