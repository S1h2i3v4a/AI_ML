# Lecture 40 Practice Problems (Hinglish): Deep Learning (Part-5)
## CIFAR-10 CNN, NLP Foundations, Word Embeddings, RNN & LSTM

Yeh problem set aapke theoretical, mathematical, aur PyTorch implementation concepts ko rigorously test karega.

---

### Problem 1: CIFAR-10 Normalization Math
PyTorch me hum CIFAR-10 images ko normalize karte hain:
```python
transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
```
1. `transforms.ToTensor()` raw pixels $[0, 255]$ ko $[0.0, 1.0]$ me convert karta hai. Prove karo ki `Normalize` ke baad values kis range $[-1.0, 1.0]$ me convert hoti hain.
2. Neural networks me inputs ko $[0, 1]$ me chhodne ke bajaye zero-centered $[-1, 1]$ banana gradient descent ke liye kyu critical hota hai?

---

### Problem 2: ConvNet Spatial Dimension Calculation
Ek 3-block CNN architecture par consider karo:
- **Input:** `(Batch, 3, 32, 32)`
- **Block 1:** `Conv2d(3, 32, kernel_size=3, padding=1)` $\to$ `ReLU()` $\to$ `MaxPool2d(2, 2)`
- **Block 2:** `Conv2d(32, 64, kernel_size=3, padding=1)` $\to$ `ReLU()` $\to$ `MaxPool2d(2, 2)`
- **Block 3:** `Conv2d(64, 128, kernel_size=3, padding=1)` $\to$ `ReLU()` $\to$ `MaxPool2d(2, 2)`

Har block ke baad output feature map ka height, width aur channel count calculate karo. Block 3 ke baad jab hum flatten karte hain, toh total kitne nodes bante hain?

---

### Problem 3: ConvNet ke Learnable Parameters ka Exact Calculation
Problem 2 ke network me aage do fully connected layers hain:
- `Linear(2048, 256)` followed by `ReLU()`
- `Linear(256, 10)`

In sabhi layers ke weights aur biases ke parameters calculate karo aur pura model ka total parameter count nikalo.

---

### Problem 4: Model.eval() aur torch.no_grad()
PyTorch testing loop me:
```python
model.eval()
with torch.no_grad():
```
1. `model.eval()` call karne se Dropout aur Batch Normalization layers ke behavior me kya farak padta hai?
2. `with torch.no_grad()` ka purpose kya hai? Agar isko omit kar diya jaye toh memory aur compute par kya asar padega?

---

### Problem 5: VGG Factorization & Receptive Field
VGG network me $5 \times 5$ filter ke bajaye do consecutive $3 \times 3$ filters use kiye jaate hain.
1. Prove karo ki do $3 \times 3$ filters ka effective receptive field ek $5 \times 5$ filter ke barabar hota hai.
2. Dono approaches ke weights/parameters ka ratio calculate karo. Chhote filters stack karne ka kya fayda hai?

---

### Problem 6: ResNet Residual Connection & Math
1. ResNet ka residual connection equation $\mathbf{y} = \mathcal{F}(\mathbf{x}) + \mathbf{x}$ likho.
2. Gradient flow equation $\frac{\partial \mathcal{E}}{\partial \mathbf{x}} = \frac{\partial \mathcal{E}}{\partial \mathbf{y}} \left( \frac{\partial \mathcal{F}}{\partial \mathbf{x}} + \mathbf{I} \right)$ derive karo.
3. Identity matrix $\mathbf{I}$ vanishing gradient problem ko 100+ layers me kaise prevent karta hai?

---

### Problem 7: Stemming vs Lemmatization
1. Words `"running"`, `"better"`, `"flies"`, `"corpora"` par Stemming aur Lemmatization apply karo.
2. Over-stemming aur under-stemming kya hota hai? Concrete example do.

---

### Problem 8: One-Hot Encoding ki Limitations
Ek corpus me vocabulary size $|\mathcal{V}| = 100,000$ hai.
1. Ek 500-word document ko One-Hot matrix me store karne ke liye 32-bit floats me kitne Megabytes (MB) memory lagegi?
2. Prove karo ki One-Hot vectors me "king" aur "queen" ka cosine similarity zero hota hai aur ye semantic meaning capture kyu nahi kar pata.

---

### Problem 9: Bag-of-Words Document-Term Matrix (DTM)
Corpus:
- $D_1$: `"deep learning models learn patterns"`
- $D_2$: `"deep neural models learn deep patterns"`

1. Sorted vocabulary nikalo.
2. $2 \times |\mathcal{V}|$ Document-Term Matrix banao.
3. Agar test time par naya word `"transformers"` aata hai, toh BoW model use kaise handle karta hai?

---

### Problem 10: N-Grams se Negation Handling
Do sentences:
- $S_1$: `"The film was not good, it was bad."`
- $S_2$: `"The film was not bad, it was good."`

1. Explain karo ki Bag-of-Words (Unigrams) in dono sentences ka sentiment differentiate kyu nahi kar pata.
2. Bigrams ($n=2$) likho aur dikhao ki kaun sa feature classifier ko positive vs negative distinguish karne me help karta hai.

---

### Problem 11: Step-by-Step TF-IDF Calculation
Corpus ($N=4$ documents):
- $D_1$: `"cat sat mat"`
- $D_2$: `"cat cat cat"`
- $D_3$: `"dog bark loud"`
- $D_4$: `"cat dog friends"`

$\text{TF}$ aur $\text{IDF} = \log_{10}(N / \text{DF})$ formulas use karke:
1. $\text{TF}(\text{"cat"}, D_2)$ aur $\text{TF}(\text{"cat"}, D_1)$ calculate karo.
2. $\text{IDF}(\text{"cat"})$ aur $\text{IDF}(\text{"mat"})$ calculate karo.
3. Unnormalized $\text{TF-IDF}$ weights compute karo.

---

### Problem 12: Word2Vec: CBOW vs Skip-Gram
1. CBOW aur Skip-Gram ke objective me kya antar hota hai?
2. Vectors $\mathbf{u} = [0.8, 0.6, 0.0]$ aur $\mathbf{v} = [0.6, 0.8, 0.0]$ ka exact Cosine Similarity calculate karo.
3. Word2Vec me vector algebra $\vec{v}_{\text{King}} - \vec{v}_{\text{Man}} + \vec{v}_{\text{Woman}} \approx \vec{v}_{\text{Queen}}$ kaise kaam karti hai?

---

### Problem 13: RNN Parameter Count & Time Unrolling
Ek vanilla RNN me $d_x = 100$ (input), $d_h = 256$ (hidden state), aur $d_y = 10$ (classes) hain.
1. $\mathbf{W}_{xh}, \mathbf{W}_{hh}, \mathbf{b}_h, \mathbf{W}_{hy}, \mathbf{b}_y$ ke shapes aur parameters count karo.
2. Total parameters kitne hain?
3. Agar sequence length $T=10$ se badhakar $T=1,000$ ho jaye, toh kya weights ka count badhega? Kyu ya kyu nahi?

---

### Problem 14: BPTT Vanishing Gradients & Gradient Clipping
1. BPTT me gradient formulation $\prod_{j=k+1}^t \frac{\partial \mathbf{h}_j}{\partial \mathbf{h}_{j-1}}$ me $\mathbf{W}_{hh}^T$ ki powers kyu aati hain?
2. $\tanh(z)$ function vanishing gradient ko aur kyu badha deta hai?
3. Agar gradient norm $\|\mathbf{g}\| = 25.0$ hai aur clipping threshold $\theta = 5.0$ hai, toh clipped gradient formula aur scaled value kya hogi?

---

### Problem 15: LSTM Cell Gates & CEC Proof
1. LSTM ke 4 main steps (Forget, Input/Candidate, Cell State update, Output) ki equations likho.
2. Cell state update $\mathbf{C}_t = \mathbf{f}_t \odot \mathbf{C}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{C}}_t$ ka derivative $\frac{\partial \mathbf{C}_t}{\partial \mathbf{C}_{t-1}}$ nikalo.
3. Prove karo ki yeh derivative LSTM me Constant Error Carousel (CEC) create karke vanishing gradient problem ko kaise solve karta hai.
