# Active Code Learning: Benchmarking Sample-Efficient Training of Code Models

## 📊 Benchmark Details

**Name**: Active Code Learning: Benchmarking Sample-Efficient Training of Code Models

**Overview**: We build the first benchmark to study this critical problem - active code learning. Specifically, we collect 11 acquisition functions (which are used for data selection in active learning) from existing works and adapt them for code-related tasks. Then, we conduct an empirical study to check whether these acquisition functions maintain performance for code data.

**Data Type**: text (source code snippets; code-summary pairs; code-pair classification pairs)

**Domains**:
- Software Engineering
- Machine Learning

**Similar Benchmarks**:
- CodeXGLUE
- CodeNet

**Resources**:
- [Resource](https://arxiv.org/abs/2306.01250)

## 🎯 Purpose and Intended Users

**Goal**: To build a benchmark to study how active learning can help us efficiently build code models – active code learning.

**Target Audience**:
- Developers
- Researchers

**Tasks**:
- Multi-class Classification
- Binary Classification
- Code Summarization

**Limitations**: The external threat lies in our considered acquisition functions used for active learning, code tasks and datasets, and code models. The internal threat can be the implementation of acquisition functions and code models. The construct threat can be the configuration of active learning. It is almost impossible to use the BLEU score here (the time cost is monthly) for some experiments.

## 💾 Data

**Source**: Datasets used: JAVA250 (IBM) for problem classification; BigCloneBench (subset) for clone detection; CodeSearchNet (Microsoft) datasets for JavaScript and Ruby for code summarization. Pre-trained code models: CodeBERT and GraphCodeBERT.

**Size**: JAVA250: 62,500 train / - / 12,500 test; BigCloneBench (subset): 90,102 train / 4,000 dev / 4,000 test; CodeSearchNet JavaScript: 58,025 train / 3,885 dev / 3,291 test; CodeSearchNet Ruby: 24,927 train / 1,400 dev / 1,261 test.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Empirical evaluation of acquisition functions via controlled active learning experiments
- Automated metrics for evaluation
- Repeated experiments (5 runs) and averaging
- Spearman's rank correlation analysis for exploratory study

**Metrics**:
- Accuracy
- F1 Score
- Perplexity (PPL)
- BLEU Score
- CodeBERTScore

**Calculation**: Accuracy: percentage of correctly classified examples. F1 Score: harmonic mean of precision and recall (formula provided in paper). Perplexity (PPL): exp of negative average log-likelihood over tokens (formula provided). BLEU: computed with brevity penalty and 4-gram precision as described in paper. CodeBERTScore: described as using pretrained contextual embeddings and pairwise cosine similarities.

**Interpretation**: Higher Accuracy, F1 Score, and BLEU indicate better performance. Lower Perplexity indicates better performance. The paper reports that active learning for non-classification tasks produces models with at least a 29.64% performance gap compared to models trained on the entire dataset, indicating ineffectiveness in that setting.

**Baseline Results**: Baseline (models trained on entire training data) reported in Table 2: Problem classification Accuracy — CodeBERT 98.10%, GraphCodeBERT 98.49%. Clone detection F1 — CodeBERT 97.15%, GraphCodeBERT 97.05%. Code summarization JavaScript PPL/BLEU — CodeBERT 3.85 / 14.34, GraphCodeBERT 3.79 / 14.89. Code summarization Ruby PPL/BLEU — CodeBERT 4.04 / 12.80, GraphCodeBERT 3.99 / 13.54.

**Validation**: Experiments repeated five times and averaged. Models initialized by training on randomly selected 500 samples. Labeling budgets set as percentages of training data (e.g., 1% with 10 iterative AL iterations). Total of 5,200 models trained across experiments; training consumed over 3,200 GPU hours. Exploratory correlation analyses use Spearman's rank correlation with reported p-values.

## ⚠️ Targeted Risks

**Risk Categories**:
- Governance

**Atlas Risks**:
- **Governance**: Unrepresentative risk testing, Lack of testing diversity, Incorrect risk testing

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
