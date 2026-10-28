# Day 36 Practice Problems: Deep Learning Foundations & Perceptrons (Hinglish)

Yeh practice suite teen production-grade engineering challenges provide karti hai taaki aap Day 36 mein seekhe gaye artificial neuron mathematics, non-linear decision boundaries, PyTorch tensor forward pass, aur deep learning frameworks ko master kar sakein.

---

## Challenge 1: Diagnostic Neuron ka Manual Calculation aur PyTorch Proof

### Background & Context
Aap ek hospital ke liye cardiovascular risk prediction model bana rahe ho. Ek single artificial neuron patient ke 4 normalized health parameters process karta hai:
1. Normalized Age ($x_1 = 0.60$)
2. Normalized Blood Pressure ($x_2 = 0.75$)
3. Normalized Cholesterol ($x_3 = 0.80$)
4. Normalized Max Heart Rate ($x_4 = 0.50$)

Neuron ke trained weights aur bias diye gaye hain:
$$\mathbf{w} = \begin{bmatrix} 0.40 \\ 0.70 \\ 0.50 \\ -0.60 \end{bmatrix}, \quad b = -0.15$$

### Tasks & Sawal
1. **Manual Linear Sum ($z$)**:
   - Weighted sum ka formula likhein aur exact step-by-step value calculate karein:
$$z = \sum_{i=1}^4 w_i x_i + b$$
2. **Sigmoid Activation Se Probability ($\hat{y}$)**:
   - Value $z$ ko Sigmoid function mein pass karke predicted probability nikaalein:
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$
   - Agar threshold $0.50$ hai, toh kya patient high risk par classified hoga?
3. **PyTorch Code Implementation**:
   - PyTorch ke `nn.Linear(in_features=4, out_features=1)` ka use karke yahi neuron banayein.
   - Is layer ke `.weight` aur `.bias` ko manual values se initialize karein.
   - Input tensor `[0.60, 0.75, 0.80, 0.50]` pass karein aur verify karein ki PyTorch ka output aapke manual calculation se exact match karta hai.

---

## Challenge 2: Non-Linearity aur XOR Problem (Perceptron ki Limit)

### Background & Context
1969 mein Marvin Minsky aur Seymour Papert ne prove kiya tha ki ek akela Perceptron **XOR gate** ko kabhi solve nahi kar sakta kyunki XOR non-linear hota hai aur ek single seedhi line se divide nahi ho sakta.

### XOR Truth Table:
| $x_1$ | $x_2$ | Target Output $y$ | Point $(x_1, x_2)$ |
| :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | $(0, 0)$ |
| 0 | 1 | 1 | $(0, 1)$ |
| 1 | 0 | 1 | $(1, 0)$ |
| 1 | 1 | 0 | $(1, 1)$ |

### Tasks & Sawal
1. **Mathematical Contradiction Proof**:
   - Charon points ke liye equations banakar mathematically prove karo ki aisi koi weights $w_1, w_2$ aur bias $b$ exist nahi karte jo charon equations ko ek sath satisfy kar sakein.
2. **Multi-Layer Architecture (MLP)**:
   - Ek 2-layer neural network (2 inputs, 2 hidden neurons, 1 output neuron) design karo jo XOR problem ko solve kare.
   - Har neuron ke weights aur bias clearly define karo.

---

## Challenge 3: Industrial Framework Sizing & Architecture

### Background & Context
Ek e-commerce company 10 million industrial product images ke liye automated quality inspection pipeline build kar rahi hai ($1024 \times 1024 \times 3$ RGB images).

### Tasks & Sawal
1. **ML vs Deep Learning Selection**:
   - 3 solid engineering reasons dijiye ki traditional machine learning (SIFT + SVM) is scale par kyun fail ho jayegi aur Deep Learning kyun zaroori hai.
2. **PyTorch vs TensorFlow vs Keras**:
   - Agar R&D team ko naye custom attention layers banane hain aur deployment team ko edge devices par model chalana hai, toh kaunsa framework chunna chahiye aur kyun?
3. **GPU VRAM Calculation**:
   - Batch size 32 ke ek single forward pass batch ka raw memory footprint calculate karein (`float32` precision). Training ke waqt raw data se 3x-4x zyada VRAM kyun chahiye hoti hai?

---

## Solutions Reference
Step-by-step verified calculations aur PyTorch code ke liye [Solutions_HINGLISH.md](file:///c:/Users/Shivam%20Keshari/OneDrive/Desktop/AI-ML/lecture_36/Practice_Problems/Solutions_HINGLISH.md) check karein.
