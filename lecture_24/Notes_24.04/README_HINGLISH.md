# Module 24.04: Overfitting Kya Hoti Hai? (High Variance) (Hinglish)

## 1. Overfitting Ka Matlab

Jab koi machine learning model training data ko samajhne ke bajaye usko **ratta maar leta hai (memorize kar leta hai)**, to us condition ko **Overfitting** kehte hain.

Model data ke real patterns ke saath-saath uske random noise aur kachre ko bhi seekh leta hai:
- **Training Error:** Lagbhag $0$ ho jata hai (Model training par 100% marks laata hai).
- **Test Error:** Bohot zyada kharab ho jata hai (Naye unseen data par model fail ho jata hai).

---

## 2. High Variance Ka Concept

Statistics mein ise **High Variance** kehte hain:
- Model itna flexible aur sensitive ban jata hai ki agar hum training data mein 2 points badal dein, to model ka poora graph hil jata hai!
- Training points par line har point ko touch karne ke liye ajeeb-o-gareeb jumps karti hai.

---

## 3. Overfitting Hone Ki Wajah

1. **Model Bahut Complex Hai:** Data simple linear tha lekin humne degree 15 ka polynomial fit kar diya.
2. **Data Bahut Kam Hai:** Features $100$ hain lekin training rows sirf $20$ hain ($d > m$).
3. **Data Mein Noise Hai:** Kuch outliers ko fit karne ke chashme mein model ne poori prediction bigad di.
4. **Weights Bahut Bade Ho Gaye:** Weights $w_j$ ki values hazaron mein chali gayi hain.
