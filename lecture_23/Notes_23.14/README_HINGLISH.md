# Module 23.14: Regression Evaluation Metrics (MAE, MSE, RMSE, $R^2$ & Adjusted $R^2$)

## 1. Regression Mein Accuracy Kyu Kaam Nahi Karti?

Classification mein answer "Yes" ya "No" hota hai, to hum accuracy ($\frac{\text{Correct}}{\text{Total}}$) nikaal lete hain.
Lekin Regression mein target ek continuous decimal number hota hai (jaise $\hat{y} = 25000.45$). Exact match hone ki probability mathematically zero hoti hai. Isliye regression mein hum errors ki doori (distance) aur explained variance calculate karte hain.

---

## 2. Distance-Based Error Metrics

### 1. Mean Absolute Error (MAE):
$$
\text{MAE} = \frac{1}{m} \sum_{i=1}^m |y_i - \hat{y}_i|
$$
- **Unit:** Same as target (jaise Dollars ya Rupees).
- **Outliers Par Asar:** Kam hota hai, sabhi errors ko linearly count karta hai.

### 2. Mean Squared Error (MSE):
$$
\text{MSE} = \frac{1}{m} \sum_{i=1}^m (y_i - \hat{y}_i)^2
$$
- **Unit:** Squared unit ($\$^{2}$ ya $\text{Rs}^2$).
- **Outliers Par Asar:** Bohot zyada hota hai. Agar ek point ka error 10 hai to square hokar 100 ho jayega.

### 3. Root Mean Squared Error (RMSE):
$$
\text{RMSE} = \sqrt{\frac{1}{m} \sum_{i=1}^m (y_i - \hat{y}_i)^2}
$$
- **Unit:** Wapas normal currency unit mein aa jata hai.
- Large errors ko strong penalty deta hai aur interpret karna easy hota hai.

---

## 3. $R^2$ Score (Coefficient of Determination)

$R^2$ ye batata hai ki hamare model ne data ke kitne percent variance ko explain kar liya hai:

$$
R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}} = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$

- $R^2 = 1.0$: Perfect model (zero error).
- $R^2 = 0.80$: Model ne data ke 80% variation ko capture kar liya hai, 20% unexplained noise hai.
- $R^2 = 0.0$: Baseline mean predictor jaisa bekaar model.
- $R^2 < 0.0$: Mean predict karne se bhi zyada kharab model!

---

## 4. $R^2$ Ki Kami Aur Adjusted $R^2$ Ka Solution

### $R^2$ Ka Sabse Bada Dhokha:
Agar aap model mein 50 bekaar useless columns (jaise employee ka shoe size ya phone number) bhi add kar denge, tab bhi $R^2$ ya to badh jayega ya same rahega. $R^2$ kabhi kam nahi hota chahe feature kitna bhi bekaar ho!

### Adjusted $R^2$ Ka Formula:
$$
R^2_{\text{adj}} = 1 - \left[ \frac{(1 - R^2)(m - 1)}{m - p - 1} \right]
$$
Yaha $m$ dataset ke samples hain aur $p$ total features ki count hai.
- Agar naya feature kaam ka hai: $R^2_{\text{adj}}$ badhega.
- Agar naya feature faltu/useless hai: $p$ badhne ki wajah se penalty lagegi aur $R^2_{\text{adj}}$ kam ho jayega!
