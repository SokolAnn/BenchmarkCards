# SciEvent

## 📊 Benchmark Details

**Name**: SciEvent

**Overview**: SciEvent is a novel multi-domain benchmark of scientific abstracts annotated via a unified event extraction schema designed to enable structured and context-aware understanding of scientific content. It includes 500 abstracts across five research domains.

**Data Type**: annotated scientific abstracts

**Domains**:
- Natural Language Processing
- Social Computing
- Computational Biology
- Medical Informatics
- Digital Humanities

**Languages**:
- English

**Similar Benchmarks**:
- SCIREX
- SCIERC

**Resources**:
- [GitHub Repository](https://github.com/desdai/SciEvent)

## 🎯 Purpose and Intended Users

**Goal**: To provide a challenging benchmark for multi-domain scientific event extraction and facilitate structured understanding of scientific content.

**Target Audience**:
- NLP Researchers
- Interdisciplinary Scholars

**Tasks**:
- Event Segmentation
- Trigger Identification
- Argument Extraction

**Limitations**: The dataset may suffer from potential data contamination as it is constructed from recent publications that could overlap with LLM pretraining corpora.

## 💾 Data

**Source**: 500 scientific abstracts from diverse peer-reviewed journals

**Size**: 500 abstracts

**Format**: N/A

**Annotation**: Manually annotated by graduate students specializing in NLP and scientific fields

## 🔬 Methodology

**Methods**:
- Fine-tuned EE models
- Large language models (LLMs)
- Human annotators

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on the overlap between predicted and actual event segments, triggers, and arguments.

**Interpretation**: Higher scores indicate better performance, with significant gap observed between human and model performances.

**Baseline Results**: Human annotators show significantly better performance compared to models, with a gap of approximately 20% in argument classification tasks.

**Validation**: Cohen's Kappa for event segmentation annotations = 0.83

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Fairness

**Atlas Risks**:
- **Privacy**: Exposing personal information
- **Fairness**: Data bias

**Demographic Analysis**: Assessment of argument types across different domains shows varying performance results indicating potential biases.

**Potential Harm**: Data contamination concerns due to overlap with LLM training datasets.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset is anonymized, and measures for privacy protection are in place.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
