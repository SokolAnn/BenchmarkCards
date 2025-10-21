# HDMB ENCH (Hallucination Detection Benchmark for Enterprise Contexts and Knowledge)

## 📊 Benchmark Details

**Name**: HDMB ENCH (Hallucination Detection Benchmark for Enterprise Contexts and Knowledge)

**Overview**: HDMB ENCH is a new dataset released for evaluating context- and common-knowledge hallucinations in large language model outputs, tailored specifically for enterprise applications.

**Data Type**: contextual documents and question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TruthfulQA
- RagTruth

**Resources**:
- [GitHub Repository](https://github.com/aimonlabs/hallucination-detection-model)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset that enables the evaluation of hallucination detection models, specifically in enterprise settings where accuracy is crucial.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Hallucination Detection
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from diverse textual contexts, including support tickets, passages from various datasets, and synthesized examples.

**Size**: 50,000 contextual documents

**Format**: JSON

**Annotation**: Annotations included sentence-level and phrase-level labels indicating factual support.

## 🔬 Methodology

**Methods**:
- Hallucination detection using contextual and common knowledge verification.

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the model's performance against human-validated labels.

**Interpretation**: Higher scores indicate better performance in detecting hallucinated content.

**Validation**: Model trained on various datasets and validated through rigorous testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
