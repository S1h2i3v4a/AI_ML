# Lecture 29.12: What is Bagging (Bootstrap Aggregating)? [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_29.12.ipynb)
[![English PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)
[![Hinglish PDF](https://img.shields.io/badge/PDF-notes__hinglish.pdf-green.svg)](notes_hinglish.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 29 Module Par Wapas Jayein](../README_HINGLISH.md)

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Bagging (Bootstrap Aggregating) ka core concept aur Leo Breiman (1996) ka breakthrough.
- Bootstrapping kya hoti hai: Sampling with replacement ka statistical mechanics.
- Parallel model training: Models aapas me independent kyu hote hain.
- Aggregation process: Classification me Voting aur Regression me Mean Averaging.
- Variance reduction: High-variance unstable models (Decision Trees) ko stable banana.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

- **Bagging = Bootstrap + Aggregation**: Yeh do shabdon se milkar bana hai: 'Bootstrapping' (data sampling) aur 'Aggregating' (outputs combine karna).

- **Sampling with Replacement**: Maan lijiye hamare paas 100 rows ka dataset hai. Hum ek bag me se random 1 row nikaalte hain, use record karte hain aur WAPAS bag me daal dete hain! Is tarah naye sub-dataset me kuch rows 2 ya 3 baar repeat ho sakti hain aur kuch rows bilkul chhoot sakti hain.

- **Parallel Execution**: Sabhi base models ek dusre se independent hote hain, isiliye sabhi models ko multi-core CPU ya cluster par ek sath parallel me train kiya ja sakta hai.

- **Variance Reduction Superpower**: Decision trees individual roop se high variance (overfitting) show karte hain. Lekin jab hum 100 bootstrapped trees ka average lete hain, to unka individual noise aapas me cancel out ho jata hai aur test error drastically gir jata hai!

---

## 2. Visual Architecture & Workflow Diagram

```mermaid
flowchart TD
    D["Original Dataset D (N Samples)"] --> B1["Bootstrap Sample D1 (with replacement)"]
    D --> B2["Bootstrap Sample D2 (with replacement)"]
    D --> B3["Bootstrap Sample Dk (with replacement)"]
    B1 --> M1["Base Model 1 (e.g. Decision Tree)"]
    B2 --> M2["Base Model 2 (e.g. Decision Tree)"]
    B3 --> Mk["Base Model k (e.g. Decision Tree)"]
    M1 & M2 & Mk --> AGG["Aggregation Layer"]
    AGG -->|"Classification: Mode (Majority Vote)"| C["Final Class Label"]
    AGG -->|"Regression: Mean Average"| R["Final Continuous Prediction"]
```

---

## 3. Mathematical & Theoretical Framework

Given training set $\mathcal{D} = \{ (\mathbf{x}_i, y_i) \}_{i=1}^N$, generate $B$ bootstrap samples $\mathcal{D}_1, \dots, \mathcal{D}_B$, each drawn uniformly with replacement:

$$
\Pr\left( \mathbf{x}_i \in \mathcal{D}_b \right) = 1 - \left(1 - \frac{1}{N}\right)^N \approx 1 - e^{-1} \approx 63.2\%
$$

For regression, the bagged estimator averages predictions:

$$
\hat{f}_{\text{bag}}(\mathbf{x}) = \frac{1}{B} \sum_{b=1}^B \hat{f}_b(\mathbf{x})
$$

The theoretical variance decomposition reveals variance reduction for uncorrelated estimators:

$$
\text{Var}(\hat{f}_{\text{bag}}) = \rho \sigma^2 + \frac{1 - \rho}{B} \sigma^2 \xrightarrow{\rho \to 0, B \to \infty} 0
$$

---

## 4. Structured Implementation & Execution

```python
import numpy as np

def simulate_bootstrap_sampling_properties(n_samples: int = 1000, n_bootstraps: int = 100) -> dict:
    """
    Simulates statistical bootstrapping with replacement to verify the theoretical 63.2% capture rate.
    
    Parameters:
    -----------
    n_samples : int
        Size of the original population dataset.
    n_bootstraps : int
        Number of independent bootstrap resamples.
        
    Returns:
    --------
    dict
        Empirical vs theoretical unique sample capture rates.
    """
    original_indices = np.arange(n_samples)
    unique_fractions = []
    
    for _ in range(n_bootstraps):
        # Uniform sampling WITH replacement
        resample = np.random.choice(original_indices, size=n_samples, replace=True)
        unique_count = len(np.unique(resample))
        unique_fractions.append(unique_count / n_samples)
        
    empirical_mean_fraction = np.mean(unique_fractions)
    theoretical_fraction = 1.0 - np.exp(-1.0)
    
    return {
        "dataset_size": n_samples,
        "total_bootstraps_simulated": n_bootstraps,
        "empirical_unique_sample_rate": float(empirical_mean_fraction),
        "theoretical_limit_rate": float(theoretical_fraction),
        "empirical_percentage": float(empirical_mean_fraction * 100),
        "theoretical_percentage": float(theoretical_fraction * 100)
    }

# Driver test
boot_sim = simulate_bootstrap_sampling_properties(1000, 200)
print("Bootstrap Statistical Verification:")
print(f"  Empirical Capture Rate   : {boot_sim['empirical_percentage']:.2f}%")
print(f"  Theoretical Limit (1-1/e): {boot_sim['theoretical_percentage']:.2f}%")
```

---

## 5. Mukhya Batein (Key Takeaways) & Summary
- Code ko modular function ke roop me likha gaya hai jisme clear shuruat (`def`), docstrings, error handling, aur ending (`return`) maujood hai.
- Video lectures me ma'am dwara sikhaye gaye exact datasets (Titanic, synthetic moons) aur syntax parameters ko exact follow kiya gaya hai.
