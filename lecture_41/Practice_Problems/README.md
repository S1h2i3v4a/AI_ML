# Lecture 41 Practice Problems: Deep Learning (Part-6)
## Minor Project: Sentiment Analysis on IMDB Reviews with PyTorch RNN

This problem set tests your conceptual, mathematical, and implementation mastery across NLP data preprocessing, regular expressions, linguistic tokenization, stopwords filtering, morphological stemming, statistical text vectorization, PyTorch DataLoaders, Recurrent Neural Network architectures, Binary Cross-Entropy optimization, and paradigm comparisons (CNN vs RNN).

---

### Problem 1: Exploratory Data Analysis & Deduplication
In the IMDB dataset of $50,000$ movie reviews:
1. Explain the statistical concept of "data leakage" and why failing to remove duplicate reviews before performing train/test splitting leads to overly optimistic evaluation metrics.
2. If $418$ duplicate rows are dropped from a balanced dataset of $25,000$ positive and $25,000$ negative reviews, what is the new dataset size? Does dropping duplicates significantly alter the $50/50$ class balance?

---

### Problem 2: Lowercasing & Case Folding
1. Why is case normalization considered an essential first step in text processing?
2. Consider the sentence: `"The director did a Good job, but GOOD was not enough."` Explain what happens to vocabulary size and term frequency if lowercasing is omitted versus applied.

---

### Problem 3: Regex URL Removal
In text preprocessing, URLs are removed using:
```python
re.sub(r"http\S+", "", text)
```
1. Detail the exact regex mechanics of `http`, `\S`, and `+`.
2. Why is `\S+` used instead of `.*` or `\w+`? What would happen if `.*` were used instead?

---

### Problem 4: Regex Greedy vs Non-Greedy HTML Tag Stripping
Consider the raw string:
```text
"<br />This was an incredible movie!<br />Loved the plot."
```
1. What is the output of the non-greedy regex `re.sub(r"<.*?>", "", text)`?
2. What is the disastrous output if the greedy regex `re.sub(r"<.*>", "", text)` is used instead? Explain why this occurs.

---

### Problem 5: Punctuation Stripping via Caret Negation
Consider the regex function:
```python
re.sub(r"[^A-Za-z0-9\s]", "", text)
```
1. Explain the role of the caret `^` symbol when placed inside square brackets `[...]`.
2. Apply this regex to the string: `"Wow!! The actor's performance was 10/10 #CinematicMasterpiece :)"` and write out the exact resulting string.

---

### Problem 6: Word Tokenization with NLTK Punkt
1. Why is Python's native string splitting method `text.split(" ")` inadequate for tokenizing natural language corpora?
2. How does NLTK's `word_tokenize()` handle the contraction `"didn't"` and punctuation like `"movie!"`?

---

### Problem 7: Stopwords Removal & Zipf's Law
1. State **Zipf's Law** mathematically and explain why the top 100 most frequent English words account for $\approx 50\%$ of all tokens in an uncleaned corpus.
2. In the context of binary sentiment analysis, explain why functional stopwords ("the", "is", "at", "which") possess near-zero mutual information with the target sentiment label.

---

### Problem 8: Morphological Stemming vs Lemmatization
1. What is the fundamental operational difference between the **Porter Stemmer** and the **WordNet Lemmatizer**?
2. Define **over-stemming** and **under-stemming** with concrete word examples.
3. Why was the Porter Stemmer selected over Lemmatization for preprocessing $50,000$ IMDB reviews?

---

### Problem 9: TF-IDF Dimensionality & Memory Constraints
In Scikit-Learn, we instantiate:
```python
TfidfVectorizer(max_features=5000)
```
1. Calculate the theoretical memory footprint (in Megabytes) required to store a dense NumPy float32 matrix for $49,582$ documents with an unconstrained vocabulary of $60,000$ words versus the constrained $5,000$ words.
2. Explain the mathematical formula for Scikit-Learn's smooth Inverse Document Frequency:
   $$\text{IDF}(t) = \log\left(\frac{1 + N}{1 + \text{DF}(t)}\right) + 1$$
   What value does $\text{IDF}(t)$ take if a word appears in every single document ($\text{DF}(t) = N$)?

---

### Problem 10: PyTorch DataLoader & Shuffling Dynamics
A training set contains $39,665$ samples and is wrapped with `DataLoader(train_set, batch_size=64, shuffle=True)`.
1. Calculate the exact number of mini-batches yielded in one training epoch. How many samples are in the final batch?
2. What statistical assumption is violated during mini-batch gradient descent if `shuffle=False` is set for training?

---

### Problem 11: 3D Input Tensor Reshaping for PyTorch RNN
A batch of TF-IDF vectors has shape `(64, 5000)`. In the training loop, the input is reshaped:
```python
Xb = Xb.unsqueeze(1)
```
1. State the exact shape of `Xb` after this operation.
2. What do the three dimensions of `(Batch, Seq_Len, Input_Dim)` represent in this specific NLP model formulation?

---

### Problem 12: Exact Parameter Count Derivation for PyTorch RNN
Consider the model:
```python
class RNN(nn.Module):
    def __init__(self, input_size=5000, hidden_size=128):
        super().__init__()
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)
```
Calculate the exact number of learnable parameters (weights and biases) for:
1. The recurrent layer `self.rnn`.
2. The readout linear layer `self.fc`.
3. The entire model in total.

---

### Problem 13: Binary Cross-Entropy Loss & Sigmoid Activation
1. Write down the mathematical formula for the Binary Cross-Entropy Loss over a mini-batch of size $B=64$.
2. Suppose the ground truth is $y = 1$ (Positive). Compare the loss incurred when the model outputs a confident correct probability $\hat{p} = 0.99$ versus an incorrect confident probability $\hat{p} = 0.01$.

---

### Problem 14: PyTorch Model Evaluation Protocol
During evaluation on the $9,917$ test samples:
```python
model.eval()
with torch.no_grad():
    # evaluation loop
```
1. What internal operations are deactivated by `model.eval()`?
2. What is the explicit technical consequence of `with torch.no_grad()` on memory and computational graph construction?
3. If the model outputs logit $z = -1.386$, what is the Sigmoid probability $\hat{p}$, and what is the predicted class under threshold $\tau = 0.5$?

---

### Problem 15: Comparative Paradigm Study: CNN vs RNN on MNIST
In Lecture 41 reference materials, image classification on MNIST ($28 \times 28$) is studied using both CNN and RNN architectures:
1. Explain how a 2D image is formulated as an input sequence for a Recurrent Neural Network (specify sequence length $T$ and feature dimension $d_x$).
2. Why does a Convolutional Neural Network achieve higher accuracy ($>99.2\%$) with fewer parameters compared to an RNN ($\approx 97\%$) on image data? Compare their inductive biases.
