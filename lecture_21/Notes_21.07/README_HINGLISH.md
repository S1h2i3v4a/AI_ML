# Notes_21.07: Vectors (Magnitude Aur Direction) [Hinglish]

## 📌 Topic Overview
Is lecture mein Shraddha ma'am ne **Vectors** ka fundamental concept samjhaya hai: Vector ke paas Magnitude (lambai) aur Direction (disha) dono hote hain, component form $\vec{v} = v_1\hat{i} + v_2\hat{j} + v_3\hat{k}$ kaise likha jata hai, aur Unit Vector kaise banta hai.

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- Scalar vs Vector ka farq (Magnitude vs Magnitude + Direction).
- Basis vectors $\hat{i}, \hat{j}, \hat{k}$ ka role.
- Vector ka Magnitude (Length): $\|\vec{v}\| = \sqrt{x^2 + y^2 + z^2}$.
- Shraddha ma'am ka blackboard vector $\vec{A} = (2, 1, 3) = 2\hat{i} + \hat{j} + 3\hat{k}$.
- Unit Vector ($\hat{v} = \frac{\vec{v}}{\|\vec{v}\|}$) nikalna.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

#### 1. Vector Kya Hai?
- **Scalar:** Sirf ek number hota hai (jaise Speed $= 50\text{ km/h}$, Temperature $= 30^\circ\text{C}$). Isme koi disha nahi hoti.
- **Vector:** Isme number ke sath **Disha (Direction)** bhi hoti hai (jaise Velocity $= 50\text{ km/h}$ North ki taraf).

#### 2. Component Form ($\hat{i}, \hat{j}, \hat{k}$):
Origin $(0, 0, 0)$ se shuru hokar point $(2, 1, 3)$ par jaane waale vector ko hum likhte hain:

$$
\vec{A} = 2\hat{i} + 1\hat{j} + 3\hat{k}
$$

- $\hat{i}$: X-axis ki unit direction
- $\hat{j}$: Y-axis ki unit direction
- $\hat{k}$: Z-axis ki unit direction

#### 3. Magnitude (Lambai):

$$
\|\vec{A}\| = \sqrt{2^2 + 1^2 + 3^2} = \sqrt{4 + 1 + 9} = \sqrt{14} \approx 3.74
$$

---

### 📊 Blackboard Diagram: 3D Vector Decomposition

```mermaid
flowchart TD
    Origin["Origin (0, 0, 0)"] -->|2 units along X-axis (2î)| X["(2, 0, 0)"]
    X -->|1 unit along Y-axis (1ĵ)| Y["(2, 1, 0)"]
    Y -->|3 units along Z-axis (3k̂)| Z["Point A (2, 1, 3)"]
    Origin -.->|Resultant Vector Arrow Ā| Z
```

---

### 💻 Python Code Implementation

```python
import numpy as np

def analyze_vector_properties(v=(2, 1, 3)):
    """
    Analyzes mathematical properties of a vector v:
    - Component form: v1*i + v2*j + v3*k
    - Euclidean magnitude (L2 Norm): ||v|| = sqrt(v1^2 + v2^2 + v3^2)
    - Unit vector: v_hat = v / ||v||
    
    Parameters:
        v (tuple or list): Vector components.
        
    Returns:
        dict: Components, magnitude, and unit vector components.
    """
    v_arr = np.array(v, dtype=float)
    
    # Euclidean magnitude (norm)
    magnitude = float(np.linalg.norm(v_arr))
    
    # Unit vector (normalized direction)
    unit_v = (v_arr / magnitude).tolist()
    
    return {
        "components": list(v),
        "notation_str": f"{v[0]}i + {v[1]}j + {v[2]}k",
        "magnitude_||v||": magnitude,
        "unit_vector_v_hat": unit_v,
        "unit_vector_norm_check": float(np.linalg.norm(unit_v))
    }

# --- Execution & Verification ---
# Shraddha ma'am's chalkboard vector A = (2, 1, 3)
res = analyze_vector_properties(v=(2, 1, 3))
print(f"Vector Components : {res['components']}")
print(f"Component Notation: {res['notation_str']}")
print(f"Magnitude ||v||   : sqrt(2² + 1² + 3²) = sqrt(4 + 1 + 9) = sqrt(14) ≈ {res['magnitude_||v||']:.4f}")
print(f"Unit Vector v_hat : {[round(x, 4) for x in res['unit_vector_v_hat']]}")
print(f"Unit Vector Norm  : {res['unit_vector_norm_check']:.1f}")

```

---

### 🎯 Key Takeaways:
1. Vector ka magnitude Pythagoras theorem se nikalta hai: $\sqrt{x^2 + y^2 + z^2}$.
2. AI embeddings mein unit vector ($\|\hat{v}\| = 1$) banakar cosine similarity calculate ki jaati hai.
