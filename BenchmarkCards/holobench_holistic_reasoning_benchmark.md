# HoloBench (Holistic Reasoning Benchmark)

## 📊 Benchmark Details

**Name**: HoloBench (Holistic Reasoning Benchmark)

**Overview**: HoloBench is designed to evaluate the holistic reasoning capabilities of long-context language models (LCLMs) when handling complex, multi-document queries. It systematically controls context length, information density, information positioning, and query complexity.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/megagonlabs/holobench)
- [Resource](https://hf.co/datasets/megagonlabs/holobench)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively evaluate LCLMs' ability to perform holistic reasoning over large document collections.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Adapted from text-to-SQL benchmarks using diverse datasets from the SPIDER dataset.

**Size**: 90 questions total across various complexities and types.

**Format**: N/A

**Annotation**: Automatically generated dynamic gold answers using SQL queries.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Database operations evaluation

**Metrics**:
- Accuracy

**Calculation**: The model's output is evaluated based on the proportion of correct entries in generated answers compared to the gold standard.

**Interpretation**: Higher proportions of correct entries indicate better holistic reasoning capabilities of LCLMs.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
