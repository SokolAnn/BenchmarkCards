# StructTest

## 📊 Benchmark Details

**Name**: StructTest

**Overview**: StructTest is a novel benchmark that evaluates LLMs on their ability to follow compositional instructions and generate structured outputs, providing an unbiased, cost-effective, and difficult-to-cheat evaluation framework.

**Data Type**: structured output generation tasks

**Domains**:
- Natural Language Processing
- Computer Vision
- Mathematics
- Programming

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- GSM8K
- BIG-Bench
- AGIEval

**Resources**:
- [GitHub Repository](https://github.com/SparkJiao/StructTest)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of StructTest is to assess LLMs' ability to follow complex instructions for generating structured outputs that are decoupled from underlying data and programmatically verifiable.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Structured Output Generation
- Text Summarization
- Code Generation
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Test cases are generated programmatically for structured output tasks.

**Size**: N/A

**Format**: Structured outputs

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Programmatic evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are computed based on structural accuracy and correctness of parsed content.

**Interpretation**: Performance is evaluated based on the correctness of structured outputs.

**Validation**: Tasks are designed to be highly unlikely to have been encountered by existing models during training.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt leaking

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
