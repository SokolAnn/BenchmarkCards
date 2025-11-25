# DOCNLI: A Large-scale Dataset for Document-level Natural Language Inference

## 📊 Benchmark Details

**Name**: DOCNLI: A Large-scale Dataset for Document-level Natural Language Inference

**Overview**: DOCNLI is a newly-constructed large-scale dataset for document-level NLI, transformed from a range of NLP problems and covering multiple genres of text. It allows for premises that stay in the document granularity, with hypotheses varying in length.

**Data Type**: premise-hypothesis pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/salesforce/DocNLI)

## 🎯 Purpose and Intended Users

**Goal**: To address NLP challenges that require document-level reasoning such as question answering, summarization, and fact-checking.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Natural Language Inference
- Question Answering
- Document Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Transformed from existing NLP datasets including ANLI, SQuAD, and summarization datasets like DUC2001, CNN/DailyMail, and Curation.

**Size**: 942,314 pairs

**Format**: N/A

**Annotation**: Data derived and reformulated into a document-level NLI format.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: F1 is calculated based on the classification performance of models trained using DOCNLI on various NLP benchmarks and tasks.

**Interpretation**: Higher F1 scores indicate better performance in correctly classifying entailment relationships between premises and hypotheses.

**Baseline Results**: State-of-the-art models on task-specific benchmarks after fine-tuning on DOCNLI.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
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
