# Notes_25.06: Naive Bayes Solved Example Aur Laplace Smoothing [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_25_06.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 25 Overview](../README_HINGLISH.md)

---

## 📌 Executive Summary
Table se probability calculate karne ka example aur Zero Frequency problem ka Laplace solution.

---

## 🎯 Mathematical Formulations

Zero Frequency Problem & Additive Laplace Smoothing ($\alpha = 1$):

$$
P(w_i \mid y) = \frac{\text{Count}(w_i, y) + \alpha}{\sum_{w \in V} \text{Count}(w, y) + \alpha |V|}
$$

Jahan $|V|$ vocabulary size (unique words ki sankhya) hai aur $\alpha = 1$ smoothing parameter hai.

---

## 💡 Concept Intuition & Key Insights (Desi Style)

### Zero Frequency Problem Kya Hai?
Maan lijiye training data mein word `"Bitcoin"` kabhi Ham email mein nahi aaya. Toh $P(\text{"Bitcoin"} \mid \text{Ham}) = 0$.
Jab test email aayegi jisme `"Bitcoin"` likha hoga, toh probability multiply hokar:
$P(\mathbf{x} \mid \text{Ham}) = P(x_1 \mid \text{Ham}) \times \dots \times 0 = 0$!
Ek naye word ki wajah se poori probability zero ho gayi!
### Solution: Laplace Smoothing
Hum numerator mein $+1$ aur denominator mein $+|V|$ add kar dete hain. Isse kisi bhi word ki probability kabhi exactly zero nahi hoti.

---

## 💻 Python Production Implementation

```python
# Laplace smoothing example
count_word = 0
total_words_in_class = 500
vocab_size = 1000
alpha = 1.0

prob_without_smoothing = count_word / total_words_in_class
prob_with_smoothing = (count_word + alpha) / (total_words_in_class + alpha * vocab_size)

print(f"Without smoothing : {prob_without_smoothing}")
print(f"With smoothing    : {prob_with_smoothing:.6f}")
```
