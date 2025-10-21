# SciGraphQA

## 📊 Benchmark Details

**Name**: SciGraphQA

**Overview**: SciGraphQA is a comprehensive, multi-turn question-answer dataset derived from scientific literature and graphs. It supports open vocabulary dialogues and distinguishes itself by focusing on real-world academic graphs rather than synthetic data.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ChartQA

**Resources**:
- [GitHub Repository](https://github.com/user/repo)
- [Resource](https://huggingface.co/datasets/scigraphqa)

## 🎯 Purpose and Intended Users

**Goal**: To establish a scientific question-answering benchmark for multi-modal large language models (MLLMs).

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Data generated from 290,000 Computer Science and Machine Learning ArXiv papers published between 2010 and 2020.

**Size**: 295,000 examples

**Format**: JSON

**Annotation**: Automatically generated using Palm-2

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- CIDEr
- BLEU-4
- ROUGE

**Calculation**: N/A

**Interpretation**: A CIDEr score indicates the quality of generated answers relative to reference answers.

**Baseline Results**: CIDEr score of 0.268 achieved by the fine-tuned SciGraphQA-baseline model.

**Validation**: Evaluated using a 3K test set.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
