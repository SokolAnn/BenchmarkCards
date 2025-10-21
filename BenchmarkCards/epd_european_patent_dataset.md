# EPD (European Patent Dataset)

## 📊 Benchmark Details

**Name**: EPD (European Patent Dataset)

**Overview**: EPD is a dataset of English-language patents granted by the European Patent Office (EPO) in 2024, designed to support various patent-related tasks, including claim generation. It provides high-quality, legally validated claims that fill a gap for cross-jurisdiction evaluation of language models on patent tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HUPD-DCG

**Resources**:
- [GitHub Repository](https://github.com/scylj1/EPDdocuments)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for training language models to generate patent claims and support various patent-related tasks using high-quality legal data.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Legal Professionals

**Tasks**:
- Claim Generation
- Patent Classification
- Patent Summarization
- Patent Retrieval

**Limitations**: The EPD dataset only includes patents published by the European Patent Office and documented in English.

## 💾 Data

**Source**: European Patent Office (EPO) Open Patent Services (OPS)

**Size**: 107,000 patents

**Format**: JSON

**Annotation**: Legally validated claims sourced directly from the EPO, ensuring high quality.

## 🔬 Methodology

**Methods**:
- Fine-tuning LLMs
- Evaluation with traditional metrics (BLEU, ROUGE, BERTScore)
- LLM-as-a-judge evaluation

**Metrics**:
- BLEU
- ROUGE-1
- ROUGE-L
- BERTScore

**Calculation**: Metrics are calculated based on the overlap between generated claims and reference claims for text generation tasks.

**Interpretation**: Higher scores indicate better performance in generating claims that align with legal standards.

**Baseline Results**: Models fine-tuned on EPD consistently outperform those trained on other datasets.

**Validation**: The effectiveness of EPD is validated through comparative performance evaluations with existing datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset is sourced from publicly accessible documents and does not include private information.

**Data Licensing**: CC-BY-NC-4.0 license is planned for the dataset.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
