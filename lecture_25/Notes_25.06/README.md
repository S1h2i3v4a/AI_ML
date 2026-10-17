# Lecture 25.06: Naive Bayes Step-by-Step Example (Weather & Play)

## 📌 Topic Overview
In this lecture, Shraddha ma'am works through a manual blackboard calculation of **Naive Bayes** using the classic **Weather & Wind -> Play** decision problem.

---

## 📋 Classroom Blackboard Dataset

| Day | Weather | Wind | Play |
| :---: | :---: | :---: | :---: |
| D1 | Sunny | Strong | No |
| D2 | Sunny | Weak | Yes |
| D3 | Overcast | Weak | Yes |
| D4 | Rainy | Strong | No |
| D5 | Rainy | Weak | Yes |

---

## 🧮 Step-by-Step Manual Calculation

We want to predict for a new day: **$X = (\text{Weather} = \text{Sunny}, \text{Wind} = \text{Strong})$**.

### Step 1: Calculate Priors

$$
P(\text{Play = Yes}) = \frac{3}{5} = 0.60, \quad P(\text{Play = No}) = \frac{2}{5} = 0.40
$$

### Step 2: Compute Conditional Likelihoods

$$
P(\text{Sunny} \mid \text{Yes}) = \frac{1}{3}, \quad P(\text{Strong} \mid \text{Yes}) = \frac{1}{3}
$$

$$
P(\text{Sunny} \mid \text{No}) = \frac{1}{2}, \quad P(\text{Strong} \mid \text{No}) = \frac{1}{2}
$$

### Step 3: Compute Numerator Scores

$$
\text{Score}(\text{Yes}) = P(\text{Yes}) \cdot P(\text{Sunny} \mid \text{Yes}) \cdot P(\text{Strong} \mid \text{Yes}) = \frac{3}{5} \times \frac{1}{3} \times \frac{1}{3} = \frac{1}{15} \approx 0.0667
$$

$$
\text{Score}(\text{No}) = P(\text{No}) \cdot P(\text{Sunny} \mid \text{No}) \cdot P(\text{Strong} \mid \text{No}) = \frac{2}{5} \times \frac{1}{2} \times \frac{1}{2} = \frac{1}{10} = 0.1000
$$

### Step 4: Decision Rule

Since $\text{Score}(\text{No}) = 0.1000 > \text{Score}(\text{Yes}) = 0.0667$:
$$\mathbf{\hat{y} = \text{Play = No}}$$

---

## 📊 Visual Flowchart: Decision Computation

```mermaid
flowchart TD
    Test["New Day: Sunny + Strong Wind"] --> BranchYes["Path: Play = Yes"]
    Test --> BranchNo["Path: Play = No"]

    BranchYes --> CalcYes["P(Yes) * P(Sunny|Yes) * P(Strong|Yes)<br/>3/5 * 1/3 * 1/3 = 0.0667"]
    BranchNo --> CalcNo["P(No) * P(Sunny|No) * P(Strong|No)<br/>2/5 * 1/2 * 1/2 = 0.1000"]

    CalcYes --> CompareCompare Scores
    CalcNo --> Compare

    Compare --> Decision["0.1000 > 0.0667<br/>Final Prediction: Play = No!"]
```

---

## 💻 Python Implementation

```python
def naive_bayes_weather_predict(weather_val, wind_val):
    """
    Demonstrates manual Naive Bayes step-by-step probability calculation
    using Shraddha ma'am's Weather/Wind -> Play Tennis blackboard dataset.
    
    Dataset Breakdown:
    - Total Days = 5
    - Play = Yes (3 days), Play = No (2 days)
    
    Calculates P(Yes|X) vs P(No|X) and returns predicted class with scores.
    """
    # 1. Class Priors
    p_yes = 3 / 5
    p_no  = 2 / 5

    # 2. Likelihood tables from blackboard
    # Weather given Class:
    likelihood_weather = {
        'Yes': {'Sunny': 1/3, 'Overcast': 1/3, 'Rainy': 1/3},
        'No':  {'Sunny': 1/2, 'Overcast': 0/2, 'Rainy': 1/2}
    }

    # Wind given Class:
    likelihood_wind = {
        'Yes': {'Strong': 1/3, 'Weak': 2/3},
        'No':  {'Strong': 1/2, 'Weak': 1/2}
    }

    # 3. Calculate Numerator (Posterior Score)
    score_yes = p_yes * likelihood_weather['Yes'][weather_val] * likelihood_wind['Yes'][wind_val]
    score_no  = p_no  * likelihood_weather['No'][weather_val]  * likelihood_wind['No'][wind_val]

    # 4. ArgMax Decision
    prediction = "Play = Yes" if score_yes > score_no else "Play = No"

    return {
        'Score_Yes': score_yes,
        'Score_No': score_no,
        'Prediction': prediction
    }

# --- Function Call & Testing ---
result = naive_bayes_weather_predict(weather_val='Sunny', wind_val='Strong')
print("Weather = Sunny, Wind = Strong:")
print(f"  Posterior Score (Yes): {result['Score_Yes']:.4f}")
print(f"  Posterior Score (No) : {result['Score_No']:.4f}")
print(f"  Final Decision       : {result['Prediction']}")
```

---

## 🔑 Key Takeaways
1. We do not need the evidence $P(X)$ when comparing classes because it is identical for both $Yes$ and $No$.
2. Frequency counts from training data directly yield likelihoods.
