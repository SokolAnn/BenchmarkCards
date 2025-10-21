# THEPALIT BENCHMARK DATASET

## 📊 Benchmark Details

**Name**: THEPALIT BENCHMARK DATASET

**Overview**: A benchmark dataset of malicious prompts created to evaluate the performance of LLM security solutions against attacks such as prompt injection and jailbreaks.

**Data Type**: malicious and benign prompts

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Deepset Prompt Injections Dataset

**Resources**:
- [Resource](https://huggingface.co/datasets/deepset/prompt-injections)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and compare the features and performance of various LLM security solutions using a benchmark dataset.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Security Evaluation
- Prompt Injection Detection

**Limitations**: N/A

## 💾 Data

**Source**: Combination of manually generated prompts, automated prompts, and augmented data from the Deepset Prompt Injections Dataset.

**Size**: 500 prompts

**Format**: N/A

**Annotation**: Manual and automated generation techniques used to create prompts.

## 🔬 Methodology

**Methods**:
- Performance Evaluation
- Comparative Analysis

**Metrics**:
- Accuracy
- Precision
- Recall
- False Positive Rate (FPR)
- F1-Score
- Latency
- Attack Success Rate (ASR)

**Calculation**: Metrics calculated based on true positives, false positives, and false negatives among the evaluated prompts.

**Interpretation**: Results indicate the effectiveness of security tools in detecting malicious prompts, with high precision and low FPR being ideal.

**Validation**: Evaluated security tools against the benchmark dataset and compared against a baseline LLM model.

## ⚠️ Targeted Risks

**Risk Categories**:
- Security
- Privacy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Data leakage through malicious prompts']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
