# Module 24.12: ElasticNet Ka Parichay (L1 + L2 Ka Combination) (Hinglish)

## 1. Lasso Aur Ridge Ki Kami

- **Lasso Ki Kami:** Agar 4 features aapas mein bohot correlated hain, to Lasso unme se kisi 1 random feature ko rakh leta hai aur baaki 3 ko zero kar deta hai!
- **Ridge Ki Kami:** Ridge saare features ko retain karta hai, wo kisi ko zero nahi karta (Feature selection nahi kar pata).

---

## 2. ElasticNet Ka Hybrid Formula

Zou aur Hastie ne dono ko milakar **ElasticNet** banaya:

$$
J(\mathbf{w}, b) = \text{MSE} + \alpha \left[ \rho \|\mathbf{w}\|_1 + \frac{1 - \rho}{2} \|\mathbf{w}\|_2^2 \right]
$$

Yaha `l1_ratio` ($\rho$) decide karta hai ki kitna Lasso aur kitna Ridge hoga:
- $\rho = 1.0$: Poora Lasso.
- $\rho = 0.0$: Poora Ridge.
- $\rho = 0.5$: 50% Lasso + 50% Ridge!

---

## 3. Grouping Effect Ka Fayda

ElasticNet correlated features ko ek **Group** ki tarah treat karta hai:
- Ya to poora group retain hoga aur unke weights smoothly share honge (Ridge property).
- Ya phir bekaar feature groups ek saath zero ho jayenge (Lasso property)!
