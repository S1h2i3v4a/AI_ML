# Solutions: Day 33 Practice Problems Suite (Hinglish)

## Solution to Case Study 1: Feature Transformation & RFM Pipeline

### 1. Raw Timestamps aur Birth Years ka Mathematical Flaw
Euclidean distance formula:
$$
d(u, v) = \sqrt{\sum_{i=1}^{p} (u_i - v_i)^2}
$$
1. **Birth Year**: Raw birth year (1955 vs 1995) ek arbitrary calendar point hai. Iska squared difference $(1995 - 1955)^2 = 1600$ distance matrix ko corrupt karta hai. `Age = 2026 - Year_Birth` banane se yeh direct consumer life-stage feature ban jata hai.
2. **Timestamp String**: Strings par distance calculate nahi ho sakti. Agar raw UNIX seconds ($1.6 \times 10^9$) use karein toh scale itna bada ho jayega ki baki features ka effect khatam ho jayega. `Customer_Tenure_Days = ref_date - Dt_Customer` loyalty duration ka meaningful metric deta hai.

### 2. Reproducibility Anchor Date
- Agar hum `datetime.now()` use karein toh har mahine code run karne par customers ke tenure days badal jayenge aur cluster centroids shift ho jayenge.
- **Solution**: Reference date hamesha dataset ki maximum joining date honi chahiye:
$$
\text{Reference Date} = \max(\text{Dt\_Customer})
$$
$$
\text{Customer\_Tenure\_Days} = (\text{Reference Date} - \text{Dt\_Customer})
$$

### 3. Clustering mein `drop_first=True` Kyun Galat Hai?
- OLS regression mein matrix inversion $(X^T X)^{-1}$ hota hai. Perfect multicollinearity se bachne ke liye ek column drop karna padta hai.
- Unsupervised clustering mein matrix inversion nahi hota, balki spatial geometric distance calculate hoti hai:
$$
d(D_A, D_B) = \sqrt{(1 - 0)^2 + (0 - 1)^2} = \sqrt{2}
$$
Agar hum category 1 drop kar dein, toh category 1 ka vector $(0, 0, \dots, 0)$ ban jayega. Uska category 2 se distance $\sqrt{(0-1)^2} = 1$ ho jayega (jo $\sqrt{2}$ nahi hai). Isse geometric symmetry toot jati hai. Isliye clustering mein **saari categories retain** ki jaati hain (`drop=None`).

---

## Solution to Case Study 2: Optimal K Selection

### 1. WCSS Formula aur Monotonicity
Within-Cluster Sum of Squares (Inertia):
$$
\text{WCSS} = \sum_{k=1}^{K} \sum_{x_i \in C_k} \| x_i - \mu_k \|^2
$$
Jab $K$ badhta hai, toh data points naye sub-centroids ke aur kareeb aate hain. Extreme case mein jab $K = N$ ho jaye, toh har point apna centroid ban jata hai aur $\text{WCSS} = 0$ ho jata hai. Isliye WCSS monotonically decrease hota hai.

### 2. `KneeLocator` ka Mathematical Logic
`KneeLocator` $K$ aur WCSS dono ko $[0, 1]$ par normalize karta hai aur first point se last point tak ek straight chord draw karta hai. Curve se chord ka perpendicular distance jahan maximum hota hai:
$$
k^* = \arg\max_k \left( \text{Chord}(k) - y_{\text{norm}}(k) \right)
$$
wahi optimal elbow point hota hai.

### 3. Evaluation aur Optimal K

| $K$ | WCSS | $\Delta \text{WCSS}$ | Silhouette Score |
| :---: | :---: | :---: | :---: |
| 2 | 24,500 | — | 0.38 |
| 3 | 16,800 | 7,700 | 0.42 |
| **4** | **11,200** | **5,600** | **0.45 (Peak)** |
| 5 | 9,900 | 1,300 (Sharp decline) | 0.41 |
| 6 | 8,900 | 1,000 | 0.39 |

- $K=3 \to 4$ par 5,600 ka drop hua, lekin $K=4 \to 5$ par sirf 1,300 ka drop hua (diminishing returns).
- Silhouette score exactly $K=4$ par maximum ($0.45$) hai.
- Isliye **$K^* = 4$** mathematically aur commercially optimal choice hai.

---

## Solution to Case Study 3: Personas aur Marketing Optimization

### 1. Persona Assignment
1. **Alpha**: *"Family Shoppers / Thrifty Couples"* — Low income (\$38.5k), low spend (\$210), 1.35 kids, high web browsing, low response (6.5%).
2. **Beta**: *"Affluent Couples / Established Spenders"* — High income (\$74.2k), highest spend (\$1,280), few kids (0.42), store/catalog buyers, good response (17.2%).
3. **Gamma**: *"Budget Singles / Window Shoppers"* — Lowest income (\$35.8k), lowest spend (\$155), single parents (1.40 kids), highest web visits (7.1), moderate response (13.8%).
4. **Delta**: *"Affluent Singles / Golden Cluster"* — High income (\$71.9k), high spend (\$1,210), 0.38 kids, **unprecedented 33.5% response rate**!

### 2. Delta "Golden Cluster" Kyun Hai?
Per-contact expected revenue:
$$
E[\text{Revenue}] = \text{Response Rate} \times \text{Mean Spending}
$$
- **Alpha**: $0.065 \times \$210 = \mathbf{\$13.65}$
- **Beta**: $0.172 \times \$1,280 = \mathbf{\$220.16}$
- **Gamma**: $0.138 \times \$155 = \mathbf{\$21.39}$
- **Delta**: $0.335 \times \$1,210 = \mathbf{\$405.35}$

Delta ka expected revenue Beta se **1.84 guna** aur Alpha se **nearly 30 guna** zyada hai! Is highest marketing ROI ki wajah se Delta "Golden Cluster" kehlata hai.

### 3. Budget Allocation (\$100,000 Total Budget)
1. **Cluster Delta (\$45,000 / 45%)**: Personalized luxury concierge, private member drops, gourmet food subscriptions.
2. **Cluster Beta (\$35,000 / 35%)**: VIP loyalty rewards, premium catalog mailings, milestone gifts.
3. **Cluster Alpha (\$12,000 / 12%)**: Weekend grocery bundles, family-pack coupons, automated email marketing.
4. **Cluster Gamma (\$8,000 / 8%)**: Clearance flash sales, abandoned cart discount vouchers, BNPL zero-interest payment options.
