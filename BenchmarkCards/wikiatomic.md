# WikiAtomic

## 📊 Benchmark Details

**Name**: WikiAtomic

**Overview**: WikiAtomic is a novel dataset comprised of prompt/response pairs in which provided context is incrementally increased to study how large language models prioritize contextual and parametric knowledge in knowledge-consistent scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/PortNLP/WikiAtomic)

## 🎯 Purpose and Intended Users

**Goal**: To investigate how large language models allocate knowledge between local context and global parameters when answering open-ended questions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Wikipedia articles decomposed into atomic sentences.

**Size**: 10,000 atomic sentences

**Format**: N/A

**Annotation**: Manual extraction and verification of atomic sentences.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- FActScore

**Calculation**: Metrics are calculated based on the overlap between responses and provided contexts, using entailment scores to classify sentences.

**Interpretation**: A higher FActScore indicates fewer hallucinations and more factually accurate responses.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
