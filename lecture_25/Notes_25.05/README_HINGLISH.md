# Notes_25.05: Naive Bayes Ka Intuition Aur Independence Assumption [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_25_05.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 25 Overview](../README_HINGLISH.md)

---

## 📌 Executive Summary
Classification mein Bayes Theorem aur 'Naive' conditional independence assumption ka intuition.

---

## 🎯 Mathematical Formulations

Bayes' Theorem for Classification:

$$
P(y \mid \mathbf{x}) = \frac{P(\mathbf{x} \mid y) P(y)}{P(\mathbf{x})} = \frac{P(x_1, x_2, \dots, x_d \mid y) P(y)}{P(\mathbf{x})}
$$

The 'Naive' Conditional Independence Assumption:

$$
P(x_1, x_2, \dots, x_d \mid y) = \prod_{j=1}^d P(x_j \mid y) = P(x_1 \mid y) \cdot P(x_2 \mid y) \cdots P(x_d \mid y)
$$

MAP Decision Rule:

$$
\hat{y} = \arg\max_y P(y) \prod_{j=1}^d P(x_j \mid y)
$$

---

## 💡 Concept Intuition & Key Insights (Desi Style)

### Isko 'Naive' Kyu Bolte Hain?
'Naive' ka matlab hota hai 'bholapan'. Yeh algorithm assume karta hai ki target class $y$ ke given hone par saare features aapas mein 100% independent hain!
Jaise email spam detection mein: word `"Free"` aane par word `"Money"` aane se koi connection nahi hai. Real world mein yeh assumption sach nahi hota (words aksar correlated hote hain), lekin fir bhi Naive Bayes practically text classification aur spam filtering mein bohot tezi se aur zabardast accuracy ke sath perform karta hai!

---

## 💻 Python Production Implementation

```python
# Naive Bayes conceptual probability multiplication
P_spam = 0.3
P_free_given_spam = 0.8
P_win_given_spam = 0.7

P_ham = 0.7
P_free_given_ham = 0.1
P_win_given_ham = 0.05

score_spam = P_spam * P_free_given_spam * P_win_given_spam
score_ham = P_ham * P_free_given_ham * P_win_given_ham

print(f"Posterior Spam Score: {score_spam:.4f}")
print(f"Posterior Ham Score : {score_ham:.4f}")
print("Predicted Class:", "Spam" if score_spam > score_ham else "Ham")
```
