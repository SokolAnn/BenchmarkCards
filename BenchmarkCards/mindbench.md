# MindBench

## 📊 Benchmark Details

**Name**: MindBench

**Overview**: MindBench is a comprehensive benchmark designed for the structural analysis and parsing of mind maps, including bilingual dataset of high-resolution images with detailed annotations and evaluation metrics, covering five structured understanding and parsing tasks.

**Data Type**: bilingual mind map images with annotations

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Chinese

**Resources**:
- [Resource](https://miasanlei.github.io/MindBench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized tool for research in structured document analysis, focusing on mind maps.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Full Parsing
- Partial Parsing
- Position-related Parsing
- Structured Visual Question Answering
- Position-related Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Data generated from mind map files and synthetic data.

**Size**: 21,527 examples in crawled dataset, 400,000 examples in synthetic dataset

**Format**: JSON

**Annotation**: Parsed from real mind map files and synthesized using automated processes.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Field-level F1 Score
- Tree Edit Distance (TED)-based accuracy

**Calculation**: Precision and recall calculated for F1 score evaluation; TED is calculated using the Zhang-Shasha algorithm.

**Interpretation**: Higher scores indicate better model performance in understanding and structuring mind maps.

**Baseline Results**: Performance benchmarks established using various visual document understanding models.

**Validation**: Models evaluated on test sets of various complexities and tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
