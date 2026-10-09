# Module 24.10: Hands-On Lasso Regression & Shrinkage Paths (Hinglish)

## 1. Regularization Lagane Ka Sahi Tareeqa

Regularization lagane se pehle **StandardScaler** lagana 100% zaroori hota hai:
- Kyunki formula saare weights par barabar penalty lagata hai. Agar ek feature Salary (lakhs) hai aur doosra Age (tens), to penalty unke scale se confuse ho jayegi.
- Scaling karne se sabhi features barabar level par aa jate hain!

---

## 2. Regularization Shrinkage Path Kya Hota Hai?

Jab hum $\alpha$ (penalty) ko $0$ se badha kar $100$ tak le jaate hain:
- Shuruat mein saare weights OLS jaise bade hote hain.
- Jaise-jaise $\alpha$ badhta hai, sabse pehle faltu aur kamzor features ke weights zero ho jaate hain.
- Aakhir mein sirf sabse zaroori features (jaise Smoker ya BMI) bachte hain!
