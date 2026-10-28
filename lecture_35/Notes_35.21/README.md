# Submodule 35.21: Git & GitHub Assignment Task

## 1. Official Assignment Requirements

As assigned in the lecture visual specification (`assignment_task.png`):

```text
Git & GitHub
Assignment Task:
Push all your existing projects in separate GitHub repositories using git commands:
• CreditWise Loan System
• SmartCart Segmentation System

Important Note:
1. Don't include the dataset in the repository. There are 2 ways to do that:
   • Create a new folder without the dataset & push that onto GitHub.
   • Include the dataset in a special file called .gitignore
2. Add a README describing the project.

Also push all your future projects onto GitHub.
```

---

## 2. Visual Reference to Assigned Task

![Assignment Task Specification](assignment_task.png)

---

## 3. Mastering `.gitignore` for Machine Learning Repositories

In data science and AI engineering, raw datasets (e.g. 100MB+ `.csv` files, high-resolution image archives, SQLite databases) and virtual environments should **never** be committed to Git. GitHub enforces a strict 100MB per-file limit and a 1GB recommended repository limit.

### Creating a Standard Data Science `.gitignore`:
Inside your project root, create a file named `.gitignore`:

```text
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual Environments
venv/
.env/
env/
ENV/

# Large Datasets (CRITICAL)
*.csv
*.xlsx
*.parquet
*.json
*.zip
*.tar.gz
data/raw/
data/processed/

# Model Checkpoints & Weights
*.pt
*.pth
*.onnx
*.h5
*.pkl

# Secrets and Local Configurations
.env
config.private.yaml

# OS Specific
.DS_Store
Thumbs.db
```

---

## 4. Project 1 Execution: CreditWise Loan System

### Step 1: Navigate to Project & Verify Files
```bash
cd "c:/path/to/CreditWise_Loan_System"
```

### Step 2: Initialize Git & Create `.gitignore`
```bash
git init
echo "*.csv" >> .gitignore
echo "*.xlsx" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "venv/" >> .gitignore
```

### Step 3: Create Comprehensive `README.md`
```markdown
# CreditWise Loan System

## Overview
CreditWise Loan System is an end-to-end Machine Learning classification engine that evaluates loan applicant risk profiles and predicts default probabilities.

## Architecture & Algorithms
- Supervised ML Classification (Logistic Regression, Random Forest, XGBoost)
- Automated Feature Engineering, Missing Value Imputation, and One-Hot Encoding
- Evaluation Metrics: ROC-AUC, Precision, Recall, F1-Score

## Installation & Usage
1. Clone the repository: `git clone https://github.com/username/creditwise-loan-system.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Train model: `python train.py`
```

### Step 4: Stage, Commit & Push to GitHub
```bash
git add .
git commit -m "Initial commit of CreditWise Loan System with .gitignore and documentation"
git branch -M main
git remote add origin https://github.com/your-username/creditwise-loan-system.git
git push -u origin main
```

---

## 5. Project 2 Execution: SmartCart Segmentation System

### Step 1: Navigate & Initialize
```bash
cd "c:/path/to/SmartCart_Segmentation_System"
git init
```

### Step 2: Configure `.gitignore` & `README.md`
```bash
# Configure .gitignore to exclude raw customer transaction datasets
echo "dataset/" >> .gitignore
echo "*.csv" >> .gitignore
echo "models/*.pkl" >> .gitignore
```

### Step 3: Create `README.md`
```markdown
# SmartCart Customer Segmentation System

## Overview
SmartCart is an Unsupervised Machine Learning clustering platform that segments retail customers based on annual income, spending scores, and purchasing behavior.

## Key Techniques
- K-Means Clustering with Elbow Method & Silhouette Analysis Optimization
- Hierarchical Agglomerative Clustering (Dendrogram Visualization)
- Principal Component Analysis (PCA) for 2D/3D Cluster Projection
```

### Step 4: Stage, Commit & Push
```bash
git add .
git commit -m "Initialize SmartCart Segmentation System with clustering pipelines and documentation"
git branch -M main
git remote add origin https://github.com/your-username/smartcart-segmentation-system.git
git push -u origin main
```
