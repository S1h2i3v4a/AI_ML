# Submodule 36.03: What are Neural Networks?

## 1. Biological Inspiration: The Human Brain

The foundational architecture of Deep Learning is inspired by the human neurological system. The human brain contains approximately **86 to 100 billion biological neurons**, each interconnected through thousands of synapses, forming a massively parallel information processing network.

### Biological vs Artificial Neuron Mapping:

```mermaid
flowchart LR
    subgraph Biological Neuron
        A[Dendrites<br/>Receive incoming chemical signals] --> B[Cell Body / Soma<br/>Sums incoming electrical impulses]
        B --> C[Axon<br/>Conducts output action potential]
        C --> D[Synapse<br/>Connects to downstream neurons]
    end
    subgraph Artificial Neuron
        E[Inputs x1, x2, ... xn<br/>Input feature signals] --> F[Summation Node Σ<br/>Weighted sum: w1*x1 + ... + b]
        F --> G[Activation Function f<br/>Non-linear thresholding]
        G --> H[Output y-hat<br/>Transmitted to next layer]
    end
```

| Biological Component | Artificial Neural Network Equivalent | Computational Role |
| :--- | :--- | :--- |
| **Dendrites** | **Input Features ($x_1, x_2, \dots, x_n$)** | Receives data inputs from preceding nodes |
| **Synaptic Weights** | **Weights ($w_1, w_2, \dots, w_n$)** | Controls the amplification/attenuation strength of each connection |
| **Cell Body (Soma)** | **Summation Node ($\sum w_i x_i + b$)** | Accumulates all weighted inputs plus bias offset |
| **Action Potential Threshold** | **Activation Function ($f(z)$)** | Decides whether and with what magnitude the neuron should fire |
| **Axon** | **Neuron Output ($\hat{y}$)** | Transmits computed activation signal to downstream layers |

---

## 2. Artificial Neural Network (ANN) Architecture

An **Artificial Neural Network (ANN)** is organized into discrete sequential groups of artificial neurons called **Layers**:

```mermaid
flowchart LR
    subgraph Input Layer
        I1((x1))
        I2((x2))
        I3((x3))
    end
    subgraph Hidden Layer
        H1((h1))
        H2((h2))
        H3((h3))
        H4((h4))
    end
    subgraph Output Layer
        O1((y_hat))
    end
    I1 --> H1 & H2 & H3 & H4
    I2 --> H1 & H2 & H3 & H4
    I3 --> H1 & H2 & H3 & H4
    H1 --> O1
    H2 --> O1
    H3 --> O1
    H4 --> O1
```

### The Three Fundamental Layer Types:
1. **Input Layer**:
   - The entry point of the network.
   - Contains exactly one node for every input feature (e.g., if predicting house prices using 3 features: `square_feet`, `bedrooms`, `age`, the input layer has 3 nodes).
   - Performs no mathematical transformations; simply passes values forward.
2. **Hidden Layer(s)**:
   - Intermediate layers situated between input and output layers.
   - Perform mathematical dot-products, bias addition, and non-linear activation functions.
   - Extract increasingly abstract feature representations.
   - Networks with multiple hidden layers are called **Deep Neural Networks**.
3. **Output Layer**:
   - The final layer responsible for producing the model's prediction.
   - Node count and activation depend on the problem type:
     - *Binary Classification*: 1 node with **Sigmoid** activation (probability $\in [0, 1]$).
     - *Multi-Class Classification*: $K$ nodes with **Softmax** activation (probability distribution summing to 1).
     - *Regression*: 1 node with **Linear** (no) activation (continuous real number).
