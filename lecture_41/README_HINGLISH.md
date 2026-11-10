# Lecture 41 (Hinglish): Deep Learning (Part-6)
## Minor Project: Sentiment Analysis on IMDB Reviews with PyTorch RNN

Yeh **Lecture 41: Deep Learning (Part-6)** ka complete comprehensive master guide hai. Is lecture me Natural Language Processing (NLP) aur PyTorch ka ek practical minor project scratch se banaya gaya hai: **IMDB Movie Reviews ($50,000$ reviews)** par Recurrent Neural Network (RNN) train karke Positive vs Negative sentiment classify karna.

---

## 1. Directory Structure

```
lecture_41/
├── Lecture_Code/
│   ├── Codes.ipynb                        <- Complete executable PyTorch notebook
│   └── Resources/
│       ├── 00) Contents TEAMWORK.jpeg     <- Syllabus overview
│       ├── 9 Handwritten Digit Classification using CNN & RNN.png <- CNN vs RNN reference
│       └── 10 MNIST Dataset in PyTorch.png <- MNIST vision sequential reference
│
├── Notes_41.01/  <- Minor Project: Sentiment Analysis on IMDB Reviews with PyTorch RNN
├── Notes_41.02/  <- Text Normalization & Regex Preprocessing (Case Folding, URLs, Punctuations & HTML)
├── Notes_41.03/  <- Linguistic Tokenization & Stopwords Removal with NLTK
├── Notes_41.04/  <- Morphological Stemming vs Lemmatization & Vocabulary Construction
├── Notes_41.05/  <- Text Vectorization using TF-IDF (Term Frequency - Inverse Document Frequency)
├── Notes_41.06/  <- PyTorch Data Pipelines: TensorDataset, DataLoader, Batching & Splitting
├── Notes_41.07/  <- Designing the Recurrent Neural Network (RNN) Architecture in PyTorch
├── Notes_41.08/  <- Optimization, Loss Function & The Recurrent Training Loop
├── Notes_41.09/  <- Evaluation, Metrics & Real-World Inference on Unseen Reviews
├── Notes_41.10/  <- Comparative Study: Sequence Processing with RNNs vs Spatial Convolutions with CNNs
│
└── Practice_Problems/
    ├── README.md                          <- 15 High-Yield Technical Problems (English)
    ├── README_HINGLISH.md                 <- 15 High-Yield Technical Problems (Hinglish)
    ├── Solutions.md                       <- Full Mathematical & Code Solutions (English)
    └── Solutions_HINGLISH.md              <- Full Mathematical & Code Solutions (Hinglish)
```

---

## 2. Submodules Overview

1. **Notes_41.01:** Minor Project Overview, IMDB dataset ($50\text{K}$ reviews), EDA, null values check, aur deduplication ($50,000 \to 49,582$).
2. **Notes_41.02:** Text Normalization, Python `re` module se URLs hatana, non-greedy HTML tags stripping, aur caret negation se punctuations clean karna.
3. **Notes_41.03:** NLTK `word_tokenize`, English stopwords filtering, aur Zipf's Law ($f(w) \propto 1/r$).
4. **Notes_41.04:** Morphological Normalization, Porter Stemmer cascading rules, valid vs non-valid stems, over/under-stemming error modes.
5. **Notes_41.05:** Text Vectorization, TF-IDF formula, `max_features=5000` memory constraint, aur sparse-to-dense array conversion.
6. **Notes_41.06:** PyTorch Data Pipelines, Train/Test Split (80/20), FloatTensors, `TensorDataset`, aur `DataLoader(batch_size=64, shuffle=True)`.
7. **Notes_41.07:** Custom `nn.Module` RNN architecture, Hidden state recurrence, 3D tensor unsqueeze, Linear readout, aur $656,641$ parameters calculation.
8. **Notes_41.08:** Binary Cross-Entropy Loss (`BCELoss`), Sigmoid probability, Adam optimizer, aur 10-Epoch training loop.
9. **Notes_41.09:** Testing protocol, `model.eval()`, `torch.no_grad()`, 0.5 thresholding, $\approx 86\%-88\%$ accuracy, aur live inference function.
10. **Notes_41.10:** Comparative Study: 2D Spatial Convolutions (CNN) vs 1D Sequential Recurrence (RNN) on MNIST ($28 \times 28$) handwritten digits.

---

## 3. Notebook-Friendly Hand-Drawn Diagrams

Saare concepts ke liye hand-drawn notebook-style diagrams (`Comic Sans MS`, blue/black pen aesthetic, clean mathematical annotations) use kiye gaye hain. Instructor face/webcam images ko completely remove kar diya gaya hai.
