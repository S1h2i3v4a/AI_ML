# Lecture 30: Practice Problems Suite (Questions - Hinglish)
## Supervised Machine Learning (Part 6) — Boosting & Advanced Ensembles

Is problem set mein **sirf aur sirf 3 case-based questions** diye gaye hain jo strictly Lecture 30 ke syllabus par based hain. Har question ko aasan shabdon mein practical scenario ke saath explain kiya gaya hai.

---

## 🩺 Case Study 1: NovaGen Research Labs — Healthcare Risk Triage

### 🎯 Scenario & Background
NovaGen Research Labs ne 9,549 patients ka health dataset collect kiya hai (`novagen_dataset.csv`).
- **Features (22 predictors)**:
  - Numerical indicators: `Age`, `BMI`, `Blood_Pressure`, `Cholesterol`, `Glucose_Level`, `Heart_Rate`, `Sleep_Hours`, `Exercise_Hours`, `Water_Intake`, `Stress_Level`.
  - Categorical/lifestyle indicators: `Smoking`, `Alcohol`, `Diet`, `MentalHealth`, `PhysicalActivity`, `MedicalHistory`, `Allergies`, `Diet_Type__Vegan`, `Diet_Type__Vegetarian`, `Blood_Group_AB`, `Blood_Group_B`, `Blood_Group_O`.
- **Target**: `Target` (Binary: `1` = Bimaar / High Risk Patient, `0` = Normal / Low Risk Patient).
- **Doctor's Requirement**: Medical diagnosis mein False Negative (bimaar patient ko healthy bol dena) sabse zyada dangerous hota hai. Isliye doctors ke liye **Recall (Sensitivity)** sabse important metric hai.

### 📝 Questions
1. **Baselines aur Ensembles ka Comparison**:
   - Data ko 80% train aur 20% test sets mein divide karein (`random_state=42`).
   - Numerical features ko `StandardScaler` se scale karein.
   - Yeh 4 models train karein:
     - `LogisticRegression(penalty='l2', solver='liblinear', max_iter=1000)`
     - `KNeighborsClassifier(n_neighbors=5)`
     - `RandomForestClassifier(n_estimators=200, random_state=42)`
     - `GradientBoostingClassifier(n_estimators=150, learning_rate=0.1, max_depth=3, random_state=42)`
   - Sabhi models ka test set par Recall score calculate karein.
   - Seedhe shabdon mein samjhayein: Tree ensemble models (Random Forest aur Gradient Boosting) ka Recall (> 94%) linear model (~82%) se itna zyada behtar kyun aata hai?
2. **Soft Voting Classifier Implementation**:
   - Ek `VotingClassifier` banayein jo Logistic Regression, KNN aur Decision Tree ko combine kare:
     ```python
     voting_clf = VotingClassifier(
         estimators=[
             ('lr', LogisticRegression(solver='liblinear', max_iter=1000)),
             ('knn', KNeighborsClassifier(n_neighbors=5)),
             ('dt', DecisionTreeClassifier(max_depth=5, random_state=42))
         ],
         voting='soft'
     )
     ```
   - Iska test recall aur accuracy check karein.
   - Simple tarike se batayein: **Soft Voting** (probabilities ka average lena) aur **Hard Voting** (sirf majority count karna) mein kya farak hota hai? Soft voting zyada reliable kyun hoti hai?
3. **Hospital Deployment Decision**:
   - NovaGen benchmark table dekhein:
     - Logistic Regression: 82.8% Recall
     - KNN: 88.3% Recall
     - Voting Classifier: 93.1% Recall
     - Gradient Boosting: 94.9% Recall
     - Random Forest: 95.8% Recall
   - Agar NovaGen ko hospital mein ek final model deploy karna ho, toh doctor kis model ko prefer karenge aur kyun?

---

## ⚙️ Case Study 2: AdaBoost Mein Sample Reweighting Kaise Kaam Karta Hai?

### 🎯 Scenario & Background
Ek chip manufacturing factory mein camera se microchips inspect ho rahe hain: Defective (`+1`) ya Normal (`-1`). Real-time speed ke liye hum chote 1-split decision stumps (`max_depth=1`) ko AdaBoost se jodh rahe hain (`adaboost.ipynb`).

### 📝 Questions
1. **Sample Weights ka Asli Logic**:
   - Maan lijiye hamare paas $N = 100$ microchips hain. Round 1 shuru hone par har microchip ka initial weight $w_i^{(1)}$ kya hota hai?
   - Round 1 mein Decision Stump 1 ne 10 microchips ko galat classify kar diya (error $\epsilon_1 = 0.10$).
   - Aasan bhasha mein explain karein:
     - Jo 10 microchips galat huye, unka weight agle round mein kaise badhta hai?
     - Jo 90 sahi huye, unka weight kaise kam hota hai?
     - Isse Round 2 mein agla Decision Stump 2 unhi 10 mushkil microchips par focus kyun karne lagta hai?
2. **Estimator Voting Power ($\alpha_m$)**:
   - Har model ke vote ka weight nikaalne ka formula:
     $$\alpha_m = \frac{1}{2} \ln\left(\frac{1 - \epsilon_m}{\epsilon_m}\right)$$
   - Stump 1 ($\epsilon_1 = 0.10$) ke liye $\alpha_1$ calculate karein.
   - Agar kisi stump ki accuracy coin toss jaisi ho ($\epsilon_m = 0.50$), toh uska $\alpha_m$ kya hoga?
   - Agar model 100% accurate ho jaye ($\epsilon_m \to 0$), toh $\alpha_m$ kahan jayega?
3. **Code aur Learning Rate**:
   - `AdaBoostClassifier(estimator=DecisionTreeClassifier(max_depth=1), n_estimators=50, learning_rate=0.5, random_state=42)` fit karein.
   - `learning_rate` ka kya role hai? Overfitting se bachne ke liye chota learning rate (e.g. 0.5) aur zyada estimators (e.g. 50 ya 100) kyun use kiye jaate hain?

---

## 🏗️ Case Study 3: Meta-Learning — Stacking vs Blending

### 🎯 Scenario & Background
Ek bank fraud detection engine alag-alag model families ko combine karna chahta hai (`ensemble_heterogenous.ipynb`):
- Random Forest (Bagging non-linear trees)
- Gradient Boosting (Boosting sequential trees)
- Logistic Regression (Linear model)

### 📝 Questions
1. **Stacking ko Simple Words Mein Samjhein**:
   - Stacking 2 levels par kaam karta hai:
     - **Level 0 (Base Models)**: Sabhi alag-alag models input data par apni predictions dete hain.
     - **Level 1 (Meta-Learner)**: Ek final model (jaise Logistic Regression) yeh seekhta hai ki kis case mein kis base model ki baat sunni hai.
   - Base models alag-alag type ke (heterogeneous) kyun hone chahiye? Sabhi models ek jaise hone se Stacking ka fayda kyun nahi hota?
2. **Stacking vs Blending ka Seedha Antar**:
   - **Blending**: Dataset ko do hisson mein baant ta hai (e.g. 70% Train, 30% Blend). Base models 70% par train hokar 30% par predict karte hain, aur Meta-model sirf unhi 30% predictions par train hota hai.
   - **Stacking**: K-Fold Out-of-Fold (OOF) cross-validation use karta hai taaki poore 100% training data par meta-predictions bina kisi target leakage ke mil sakein.
   - Dono mein trade-off kya hai? (Speed ke liye Blending kab chunenge aur Data efficiency ke liye Stacking kab chunenge?)
3. **Scikit-Learn Implementation**:
   - `StackingClassifier` implement karein:
     ```python
     from sklearn.ensemble import StackingClassifier

     stacking_clf = StackingClassifier(
         estimators=[
             ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
             ('gb', GradientBoostingClassifier(n_estimators=100, random_state=42))
         ],
         final_estimator=LogisticRegression(),
         cv=5
     )
     ```
   - Model train karke check karein ki meta-learning se accuracy individual models se behtar aati hai ya nahi.
