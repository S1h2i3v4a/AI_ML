# Module 24.05: Underfitting Kya Hoti Hai? (High Bias) (Hinglish)

## 1. Underfitting Ka Matlab

Jab koi machine learning model itna simple ya kamzor hota hai ki wo training data ke basic pattern ko bhi samajh nahi pata, to use **Underfitting** kehte hain.

Jaise agar data parabola ya curved wave jaisa hai, aur hum zabardasti ek seedhi straight line khinch kar bolte hain ki ye model hai:
- **Training Error:** Bohot high hota hai (Training data par hi fail ho jata hai).
- **Test Error:** Wo bhi bohot high hota hai (Naye data par bhi fail rehta hai).

---

## 2. High Bias Ka Concept

Ise statistics mein **High Bias** kehte hain:
- Model ne pehle se hi rigid assumption bana rakha hai ki "data linear hi hoga", chahe data kitna bhi complex kyu na ho.
- Chahe aap model ko 10 lakh training examples bhi de dein, agar uske paas curve sikhne ki mathematical capacity hi nahi hai, to wo improve nahi hoga!

---

## 3. Underfitting Hone Ki Wajah

1. **Model Bahut Simple Hai:** Non-linear data par linear model fit karna.
2. **Kaam Ke Features Gayab Hain:** Data mein zaroori signals hi nahi diye gaye.
3. **Regularization Bahut Zyada Hai:** Penalty parameter $\lambda$ itna bada kar diya ki saare weights zero ho gaye.
4. **Under-training:** Gradient descent ko bohot kam iterations par rok diya.
