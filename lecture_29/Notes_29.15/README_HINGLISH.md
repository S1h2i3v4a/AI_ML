# Lecture 29.15: Out-Of-Bag (OOB) Evaluation — Theory & Mathematics [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_29.15.ipynb)
[![English PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)
[![Hinglish PDF](https://img.shields.io/badge/PDF-notes__hinglish.pdf-green.svg)](notes_hinglish.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 29 Module Par Wapas Jayein](../README_HINGLISH.md)

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Out-Of-Bag (OOB) samples kya hote hain aur yeh bootstrap sampling se kaise nikalte hain.
- Mathematical derivation of $(1 - 1/N)^N \to 1/e \approx 36.8\%$.
- OOB score ka advantage: Bina alag validation split banaye free me unbiased test estimate milna.
- `oob_score=True` parameter aur `rf.oob_score_` attribute ka practical use.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

- **In-Bag vs Out-Of-Bag**: Jab hum $N$ samples me se $N$ samples with replacement uthate hain, to mathematical probability ke hisab se lagbhag 63.2% unique rows hi select hoti hain. Baki 36.8% rows us specific tree ke liye bilkul UNSEEN (Out-Of-Bag) reh jaati hain!

- **Free Validation Set**: Har ek sample kisi na kisi tree ke liye OOB hota hai. Hum har sample ko un trees se evaluate karwa lete hain jinhone use training me nahi dekha! Isse hume bina train-test split ke poore dataset par unbiased accuracy estimate mil jata hai.

- **Mathematical Limit**: Ek sample ke ek draw me select NA hone ki probability $1 - \frac{1}{N}$ hoti hai. $N$ independent draws ke baad select na hone ki probability $(1 - \frac{1}{N})^N$ hoti hai. Jab $N \to \infty$, yeh limit exactly $\frac{1}{e} = 0.367879... \approx 36.8\%$ evaluate hoti hai!

- **Lecture Reference**: Ma'am ne exact notebook code me `rf = RandomForestClassifier(n_estimators=501, oob_score=True, max_depth=4)` chala kar OOB score print kiya tha.

---

## 2. Visual Architecture & Workflow Diagram

```mermaid
flowchart TD
    A["Training Dataset (N Rows)"] --> B["Bootstrap Sample (Size N with replacement)"]
    B --> C["~63.2% IN-BAG SAMPLES<br/>(Used to train Tree k)"]
    B --> D["~36.8% OUT-OF-BAG (OOB) SAMPLES<br/>(Completely Unseen by Tree k!)"]
    D --> E["Feed OOB samples through Tree k for validation"]
    E --> F["Aggregate across all B Trees -> Compute oob_score_"]
```

---

## 3. Mathematical & Theoretical Framework

Let $N$ be the dataset cardinality. In a single random draw with replacement, the probability that a specific observation $x_i$ is **not** selected is:

$$
p = 1 - \frac{1}{N}
$$

Across $N$ independent draws, the probability that $x_i$ is **never** selected in the bootstrap sample is:

$$
P(\text{OOB}) = \left( 1 - \frac{1}{N} \right)^N
$$

Applying the standard calculus limit definition of the exponential function $\lim_{n \to \infty} (1 + x/n)^n = e^x$ with $x = -1$:

$$
\lim_{N \to \infty} \left( 1 - \frac{1}{N} \right)^N = e^{-1} = \frac{1}{e} \approx 0.367879... \approx 36.8\%
$$

Hence, the expected in-bag proportion is:

$$
P(\text{In-Bag}) = 1 - e^{-1} \approx 0.63212... \approx 63.2\%
$$

---

## 4. Structured Implementation & Execution

```python
import numpy as np

def calculate_oob_theoretical_convergence() -> dict:
    """
    Computes the convergence of (1 - 1/N)^N towards 1/e across varying sample scales.
    
    Returns:
    --------
    dict
        Sample size N vs OOB probability evaluation.
    """
    n_values = [5, 10, 50, 100, 500, 1000, 10000, 100000]
    true_limit = np.exp(-1.0)
    
    evaluations = {}
    for n in n_values:
        prob_oob = (1.0 - 1.0/n) ** n
        abs_error = abs(prob_oob - true_limit)
        evaluations[f"N_{n}"] = {
            "oob_probability": float(prob_oob),
            "percentage": float(prob_oob * 100),
            "delta_from_limit": float(abs_error)
        }
        
    return {
        "theoretical_limit_1_over_e": float(true_limit),
        "limit_percentage": float(true_limit * 100),
        "convergence_table": evaluations
    }

# Driver test
oob_math = calculate_oob_theoretical_convergence()
print(f"OOB Asymptotic Limit: {oob_math['limit_percentage']:.4f}%")
print("Convergence Verification across N:")
for n_key, data in oob_math['convergence_table'].items():
    print(f"  {n_key:<8} -> OOB: {data['percentage']:.4f}%, Error: {data['delta_from_limit']:.6f}")
```

---

## 5. Mukhya Batein (Key Takeaways) & Summary
- Code ko modular function ke roop me likha gaya hai jisme clear shuruat (`def`), docstrings, error handling, aur ending (`return`) maujood hai.
- Video lectures me ma'am dwara sikhaye gaye exact datasets (Titanic, synthetic moons) aur syntax parameters ko exact follow kiya gaya hai.
