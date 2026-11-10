# Lecture 41 Practice Problems (Hinglish): Deep Learning (Part-6)
## Minor Project: Sentiment Analysis on IMDB Reviews with PyTorch RNN

Yeh problem set aapke NLP text preprocessing, regular expressions, tokenization, stemming, TF-IDF vectorization, PyTorch DataLoaders, Recurrent Neural Networks, BCELoss optimization, aur CNN vs RNN comparison ko rigorously test karega.

---

### Problem 1: Exploratory Data Analysis & Deduplication
1. "Data Leakage" kya hota hai? Agar train/test split karne se pehle duplicate reviews remove na kiye jayein, toh evaluation metrics galat kyu aate hain?
2. $50,000$ reviews me se $418$ duplicate drop karne ke baad dataset size kya bachega? Kya isse class balance par koi asar padta hai?

---

### Problem 2: Lowercasing ka Importance
1. Text processing me sabhi words ko lowercase me convert karna sabse pehla step kyu hota hai?
2. Agar `"Good"`, `"GOOD"`, aur `"good"` ko lowercase na kiya jaye, toh vocabulary size aur term frequency par kya asar padega?

---

### Problem 3: Regex se URLs Remove Karna
Code:
```python
re.sub(r"http\S+", "", text)
```
1. `http`, `\S`, aur `+` ka exact meaning explain karo.
2. Yahan `\S+` ki jagah `.*` kyu nahi use kar sakte? Agar `.*` use karein toh kya blunder hoga?

---

### Problem 4: Regex Greedy vs Non-Greedy HTML Tag Stripping
Review text:
```text
"<br />This was an incredible movie!<br />Loved the plot."
```
1. Non-greedy regex `re.sub(r"<.*?>", "", text)` ka output kya hoga?
2. Greedy regex `re.sub(r"<.*>", "", text)` ka output kya hoga aur kyu pura text delete ho jata hai?

---

### Problem 5: Caret Negation se Punctuations Hatana
Code:
```python
re.sub(r"[^A-Za-z0-9\s]", "", text)
```
1. Square brackets `[...]` ke andar caret `^` ka kya role hota hai?
2. Sentence `"Wow!! The actor's performance was 10/10 #CinematicMasterpiece :)"` par yeh regex apply karne par output string kya banegi?

---

### Problem 6: NLTK word_tokenize vs Python .split()
1. Python ka `text.split(" ")` natural language ke liye fail kyu ho jata hai?
2. NLTK ka `word_tokenize()` contraction words jaise `"didn't"` aur punctuation jaise `"movie!"` ko kaise alag karta hai?

---

### Problem 7: Stopwords Removal aur Zipf's Law
1. **Zipf's Law** ka formula kya hai aur ye kyu kehta hai ki top 100 English words corpus ka $\approx 50\%$ hissa hote hain?
2. Sentiment Analysis me stopwords ("the", "is", "at", "which") ko delete karna kyu beneficial hota hai?

---

### Problem 8: Stemming vs Lemmatization
1. **Porter Stemmer** aur **WordNet Lemmatizer** ke kaam karne ke tareeqe me kya mukhya antar hai?
2. Over-stemming aur under-stemming ke concrete examples do.
3. 50,000 reviews ke project me Lemmatization ke badle Stemming kyu chuni gayi?

---

### Problem 9: TF-IDF aur max_features=5000
1. $49,582$ reviews ke liye $60,000$ vocabulary words ka dense matrix store karne me kitne Gigabytes (GB) RAM lagegi, aur `max_features=5000` se memory kitni kam ho jati hai?
2. Scikit-Learn ke smooth IDF formula me agar koi word har review me ho ($\text{DF} = N$), toh uska IDF kya banega?

---

### Problem 10: PyTorch DataLoader aur Shuffling
$39,665$ training samples ko `DataLoader(train_set, batch_size=64, shuffle=True)` me wrap kiya gaya hai.
1. Ek epoch me total kitne batches banenge? Aakhiri batch me kitne samples honge?
2. Training ke dauran `shuffle=False` rakhne par gradient descent par kya negative impact padta hai?

---

### Problem 11: PyTorch RNN ke liye 3D Tensor Reshaping
Training loop me:
```python
Xb = Xb.unsqueeze(1)
```
1. `Xb` ka shape `(64, 5000)` se kya ban jata hai?
2. `(Batch, Seq_Len, Input_Dim)` me `Seq_Len = 1` ka kya significance hai?

---

### Problem 12: PyTorch RNN ka Exact Parameter Count
Model:
```python
self.rnn = nn.RNN(input_size=5000, hidden_size=128, batch_first=True)
self.fc = nn.Linear(128, 1)
```
1. `self.rnn` ke weights aur biases calculate karo.
2. `self.fc` ke weights aur biases calculate karo.
3. Total learnable parameters kitne hain?

---

### Problem 13: Binary Cross-Entropy Loss Math
1. Mini-batch ($B=64$) ke liye Binary Cross-Entropy Loss ka mathematical formula likho.
2. Positive review ($y=1$) ke liye agar model $\hat{p} = 0.99$ predict kare vs $\hat{p} = 0.01$ predict kare, toh loss values me kitna bada difference aayega?

---

### Problem 14: Model Evaluation Protocol
Test set ($9,917$ reviews) ke liye:
```python
model.eval()
with torch.no_grad():
```
1. `model.eval()` se layers par kya farak padta hai?
2. `torch.no_grad()` se RAM/VRAM aur speed par kya impact hota hai?
3. Agar model ka logit $z = -1.386$ aaye, toh Sigmoid probability kya hogi aur class kya predict hogi?

---

### Problem 15: CNN vs RNN on MNIST ($28 \times 28$)
Day 41 ke reference materials me MNIST digit classification dono models se compare ki gayi hai:
1. Ek 2D image ($28 \times 28$) ko RNN me sequential input kaise banaya jata hai ($T$ aur $d_x$ kya hota hai)?
2. CNN image classification me RNN se behtar accuracy ($>99.2\%$ vs $\approx 97\%$) kyu achieve karta hai? Dono ke inductive bias ko compare karo.
