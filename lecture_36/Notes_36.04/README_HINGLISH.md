# Submodule 36.04: Perceptron (In Depth) (Hinglish)

## 1. Perceptron ka Parichay

**Perceptron** Deep Learning aur Neural Networks ki sabse basic unit (single artificial neuron) hai. Ise 1958 mein **Frank Rosenblatt** ne invent kiya tha. Pura deep learning isi ek neuron ke mathematical formula par khada hai.

---

## 2. Perceptron ka Mathematical Architecture

Perceptron inputs leta hai, unhe weights se multiply karta hai, bias jodta hai, aur activation function se pass karke output banata hai:

```mermaid
flowchart LR
    subgraph Inputs
        X1["x1 (Feature 1)"]
        X2["x2 (Feature 2)"]
        X3["x3 (Feature 3)"]
        B["Bias (+1)"]
    end
    subgraph Weights
        W1["w1"]
        W2["w2"]
        W3["w3"]
        WB["b (Bias Weight)"]
    end
    subgraph Core Processing
        SUM["Summation Node (Σ)<br/>z = w1*x1 + w2*x2 + w3*x3 + b"]
        ACT["Activation Function f(z)<br/>Step / Sigmoid / ReLU"]
    end
    subgraph Final Result
        Y["Output (y_hat)"]
    end
    X1 -->|w1| SUM
    X2 -->|w2| SUM
    X3 -->|w3| SUM
    B -->|b| SUM
    SUM --> ACT
    ACT --> Y
```

### Formula ka Breakdown:

1. **Inputs ($x_1, x_2, \dots$)**: Model ko milne wale raw features.
2. **Weights ($w_1, w_2, \dots$)**: Har feature ki importance ko darshate hain. Jis feature ka weight zyada hoga, output par uska asar utna zyada hoga.
3. **Bias ($b$)**: Yeh ek constant value hoti hai jo sum me judti hai.
   - **Bias kyun zaroori hai?** Agar bias na ho ($b = 0$), toh decision boundary hamesha origin $(0,0)$ se pass hogi. Bias boundary ko shift karne ki azaadi deta hai taaki agar saare inputs zero bhi hon, tab bhi neuron activate ho sake.
4. **Weighted Sum ($z$)**:
$$z = \sum_{i=1}^n w_i x_i + b = w_1 x_1 + w_2 x_2 + \dots + w_n x_n + b$$
Vector form mein:
$$z = \mathbf{w}^T \mathbf{x} + b$$
5. **Activation Function ($f(z)$)**:
$$\hat{y} = f(z)$$

---

## 3. Activation Function ki Zaroorat Kyun Hai?

Agar hum activation function na lagayein, toh chahe aap 100 layers jod lo, mathematically wo ek single straight line (linear equation) hi rahegi:
$$W_2(W_1 x + b_1) + b_2 = W' x + b'$$
Real-world problems linear nahi hotin. **Activation functions non-linearity introduce karte hain**, jisse model complex curves aur shapes seekh pata hai.

---

## 4. Teen Mukhya Activation Functions

```mermaid
flowchart TD
    subgraph Activation Functions
        A1[1. Step Function<br/>Puraana tarika: agar z >= 0 toh 1, warna 0]
        A2[2. Sigmoid Function<br/>Output ko 0 aur 1 ke beech squash karta hai]
        A3[3. ReLU Function<br/>max 0, z - Modern Deep Learning ka gold standard]
    end
```

1. **Step Function**:
$$f(z) = 1 	ext{ agar } z \ge 0, 	ext{ warna } 0$$
   *(Iska derivative zero hota hai, isliye modern gradient descent isme kaam nahi karta).*
2. **Sigmoid Function**:
$$\sigma(z) = rac{1}{1 + e^{-z}}$$
   *(Output hamesha $0$ aur $1$ ke beech hota hai, probability nikalne ke liye perfect).*
3. **ReLU (Rectified Linear Unit)**:
$$f(z) = \max(0, z)$$
   *(Negative values ko zero kar deta hai aur positive ko as-it-is chhod deta hai. Sabse fast aur popular).*

---

## 5. Neural Network Seekhta Kaise Hai? (Training Loop)

```mermaid
flowchart LR
    A[Inputs x] -->|Forward Pass| B[Calculate z = w*x + b]
    B -->|Activation| C[Output y_hat]
    C -->|Error Check| D[Loss Function]
    D -->|Backward Pass| E[Backpropagation: Gradients ∂L/∂w]
    E -->|Weights Update| F[Optimizer: w = w - η*grad]
    F -.->|Naya Round| B
```

1. **Forward Pass**: Data inputs se start hokar formula ke zariye prediction $\hat{y}$ banata hai.
2. **Loss Function**: Check karta hai ki prediction sachai ($y$) se kitni door hai.
3. **Backpropagation**: Calculus ke chain rule se error ko peeche bhej kar gradients calculate karta hai.
4. **Optimizer**: Weights aur bias ko update karta hai taaki agle round me error kam ho:
$$w \leftarrow w - \eta rac{\partial L}{\partial w}$$

---

## 6. Visual Reference

![Perceptron in Depth](keyframe_01.png)
