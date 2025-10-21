# Spam-T5: Benchmarking Large Language Models for Few-Shot Email Spam Detection

## 📊 Benchmark Details

**Name**: Spam-T5: Benchmarking Large Language Models for Few-Shot Email Spam Detection

**Overview**: This paper develops a benchmark to evaluate traditional machine learning algorithms and large language models (LLMs) on four widely used spam detection datasets, comparing performance in both full-training and few-shot settings. The paper also introduces Spam-T5, a Flan-T5 model fine-tuned for email spam detection, and provides code and data publicly.

**Data Type**: text (email and SMS messages)

**Domains**:
- Natural Language Processing
- Cybersecurity

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/jpmorganchase/llm-email-spam-detection)
- [GitHub Repository](https://github.com/jpmorganchase/emailspamdetection)
- [Resource](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection)
- [Resource](https://spamassassin.apache.org/old/publiccorpus/)
- [Resource](https://www.cs.cmu.edu/~enron/)
- [GitHub Repository](https://github.com/huggingface/setfit)
- [Resource](http://arxiv.org/abs/1907.11692)

## 🎯 Purpose and Intended Users

**Goal**: Develop a benchmark for evaluating traditional machine learning algorithms and LLMs on four popular spam detection datasets and to evaluate models in both supervised (full training set) and few-shot settings; introduce Spam-T5, a Flan-T5 fine-tuned for spam detection.

**Target Audience**:
- Researchers
- Industry Practitioners

**Tasks**:
- Text Classification
- Binary Classification (Spam vs Ham)

**Limitations**: High computational requirements for LLMs and need for specialized hardware; the small Flan-T5 model demonstrated limited generalization and was excluded; SetFit did not achieve a meaningful result on the full Enron training set after 104 hours of training.

## 💾 Data

**Source**: Four public spam detection datasets: Ling-Spam dataset; SMS Spam Collection; SpamAssassin Public Corpus; Enron Email dataset.

**Size**: Ling-Spam: 2,893 messages; SMS Spam Collection: 5,574 messages; SpamAssassin Public Corpus: 6,047 messages; Enron Email dataset (used subset): 33,716 emails

**Format**: N/A

**Annotation**: Existing dataset labels as provided by the original datasets (each message labeled as 'spam' or 'ham').

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation
- Stratified 5-fold cross-validation (for tf-idf feature selection)
- Few-shot evaluation with varying numbers of training samples

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Metrics (F1, precision, recall) computed on test sets. Full-training experiments used an 80% train / 20% test split. Few-shot experiments report macro-averages across the four datasets for k in {4, 8, 16, 32, 64, 128, 256, Full}.

**Interpretation**: Higher F1 score indicates better spam detection performance. The paper treats the model with the highest average F1 as best-performing (Spam-T5 reported as best overall). Few-shot robustness and higher sample efficiency are interpreted as advantages of LLMs.

**Baseline Results**: Full training sets: Spam-T5 average F1 = 0.9742; RoBERTa average F1 = 0.9670; SetFit average F1 = 0.9670; SVM average F1 = 0.9560; XGBoost average F1 = 0.8842. Few-shot mean F1 across shot sizes (macro average): Spam-T5 = 0.7498; RoBERTa = 0.6253; SetFit = 0.7112. (See paper Tables 3, 4, 5 for per-dataset and per-shot details.)

**Validation**: Used 80%/20% train/test splits for experiments. Stratified 5-fold cross-validation was used to tune number of tf-idf features for baseline models. Few-shot evaluation performed by varying training sample counts and reporting macro-averages across datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Misuse
- Societal Impact
- Accuracy
- Fairness

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Misuse**: Improper usage
- **Societal Impact**: Impact on the environment
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Potential Harm**: ['Potential misuse for censorship', 'Environmental impact (energy consumption and carbon emissions)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
