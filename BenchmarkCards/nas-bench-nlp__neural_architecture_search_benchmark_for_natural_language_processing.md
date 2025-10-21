# NAS-Bench-NLP: Neural Architecture Search Benchmark for Natural Language Processing

## 📊 Benchmark Details

**Name**: NAS-Bench-NLP: Neural Architecture Search Benchmark for Natural Language Processing

**Overview**: We provide the first RNN-derived NAS benchmark designed for NLP tasks: we defined a search space of recurrent neural network cells (including LSTM and GRU variants), trained over 14k architectures on language modeling datasets, conducted intrinsic and extrinsic evaluations (word similarity tests and GLUE downstream tasks), and tested several NAS algorithms within a benchmarking framework. The source code and precomputed results are released.

**Data Type**: text (language modeling token sequences; static and contextual word embeddings)

**Domains**:
- Natural Language Processing
- Machine Learning

**Languages**:
- English

**Similar Benchmarks**:
- NAS-Bench-101
- NAS-HPO-Bench
- NAS-Bench-201
- NAS-Bench-1shot1

**Resources**:
- [GitHub Repository](https://github.com/fmsnew/nas-bench-nlp-release)
- [Resource](https://arxiv.org/abs/2006.07116)
- [GitHub Repository](https://github.com/salesforce/awd-lstm-lm)

## 🎯 Purpose and Intended Users

**Goal**: Introduce the first RNN-derived NAS benchmark designed for NLP tasks, providing a recurrent-cell search space, precomputed training results for 14k+ architectures on language modeling datasets, and a framework to evaluate NAS algorithms and downstream performance.

**Target Audience**:
- Neural Architecture Search researchers
- Natural Language Processing researchers

**Tasks**:
- Language Modeling
- Word Similarity (Intrinsic Evaluation)
- Natural Language Understanding (GLUE downstream tasks)

**Limitations**: The benchmark is a very sparse sample from the extremely large search space; the distribution of performance metrics (perplexity) is not skewed toward the optimum and hand-crafted architectures (LSTM, GRU) are difficult to match; architectures do not achieve the same performance as recent Transformer-based models such as BERT, T5, or ELECTRA; vocabulary size limitations affect downstream evaluation (GLUE).

## 💾 Data

**Source**: Penn Tree Bank (PTB) and WikiText-2 datasets for training; generated search space of recurrent cell architectures (RNN, LSTM, GRU and variations); precomputed training and evaluation metrics for generated architectures.

**Size**: PTB: 1.086M tokens, vocabulary size 10,000. WikiText-2: 2.552M tokens, vocabulary size 33,278. Generated architectures: 14,322 architectures (4,114 trained three times with different seeds; 289 trained on WikiText-2).

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated precomputation of architecture training (simulated NAS environment with checkpointing and wall-time simulation)
- Intrinsic evaluation (WordSimilarity-353, SimLex-999 via cosine similarity and correlation)
- Extrinsic evaluation (GLUE pipeline via Jiant toolkit)
- Evaluation of NAS algorithms (Random Search, Hyperband, Bayesian Optimization, Regularized Evolution, Hyperopt TPE, SMAC)
- Feature extraction for architectures using graph2vec and supervised prediction experiments (XGBoost)

**Metrics**:
- Test Log Perplexity
- Validation Log Perplexity
- Train Log Perplexity
- Wall Time (simulated/training)
- Number of trainable parameters
- GLUE score (mean of task metrics * 100)
- Pearson correlation (intrinsic evaluation)
- Spearman correlation (intrinsic evaluation)
- ROC AUC (classification of flawed architectures)
- R2 Score (regression predicting final log perplexity)
- Regret (difference between current best testing log perplexity and global best testing log perplexity)

**Calculation**: Log perplexity logged per epoch: log_PPL(p) = - sum_x p(x) log p(x). GLUE score computed as average of performance measures across ten tasks multiplied by 100. Regret defined as r(t) = L(t) - L*, where L(t) is the final testing log perplexity of the best architecture according to validation perplexity found so far at time t, and L* is the lowest testing log perplexity in the whole dataset (reported L* = 4.36).

**Interpretation**: Lower (log) perplexity indicates better language modeling performance. Higher GLUE score indicates better downstream natural language understanding performance. Lower regret (closer to zero) indicates better NAS algorithm performance. Higher Pearson/Spearman correlation indicates better intrinsic semantic evaluation. Higher ROC AUC and R2 indicate better predictive performance for the respective tasks.

**Baseline Results**: Language modeling baselines on PTB (Table 2): LSTM: 10.9M parameters, Test perplexity 78.5; Top-2: 9.2M, 84.7; GRU: 9.2M, 86.1; RNN: 5.73M, 135.1. GLUE baselines (Table 3): baseline from [41] reported overall 69.1; evaluated architectures (150 random trained on WikiText-2) achieved mean GLUE score 38.1 (std 1.8), min 34.7, max 43.6.

**Validation**: Validation perplexity used for early ranking and selection; experiments include grid search for dropout hyperparameters on subsets; 4,114 architectures trained three times with different seeds for stability analysis; NAS algorithm performance reported as average regret over 30 trials.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Governance

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Governance**: Lack of testing diversity

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
