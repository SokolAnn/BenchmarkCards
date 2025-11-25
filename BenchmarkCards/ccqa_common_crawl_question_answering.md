# CCQA (Common Crawl Question Answering)

## 📊 Benchmark Details

**Name**: CCQA (Common Crawl Question Answering)

**Overview**: We propose a novel open-domain question-answering dataset based on the Common Crawl project, containing approximately 130 million multilingual question-answer pairs. This dataset is designed for in-domain pre-training of popular language models for the question-answering task.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TriviaQA
- Natural Questions
- ELI5
- GooAQ

**Resources**:
- [GitHub Repository](https://github.com/facebookresearch/CCQA)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to provide a large-scale, natural, and diverse open-domain question-answering dataset for model pre-training.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated from Common Crawl snapshots using schema.org annotations.

**Size**: 130 million question-answer pairs

**Format**: JSON

**Annotation**: Automatically annotated using schema.org definitions.

## 🔬 Methodology

**Methods**:
- Evaluation on zero-shot and fine-tuned settings

**Metrics**:
- Exact Match (EM)
- Answer-level Recall (AR)
- ROUGE-L

**Calculation**: Metrics are computed based on question-answer pairs for evaluating the performance of models.

**Interpretation**: Higher scores indicate better performance in answering questions correctly.

**Baseline Results**: N/A

**Validation**: The dataset was validated through evaluations showing effective performance across multiple benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
