# CIRCUIT (Circuit Interpretation and Reasoning Capabilities)

## 📊 Benchmark Details

**Name**: CIRCUIT (Circuit Interpretation and Reasoning Capabilities)

**Overview**: CIRCUIT is a benchmark designed to assess Large Language Models' reasoning capabilities in analog circuit design, consisting of 510 question-answer pairs across various levels of analog-circuit-related subjects.

**Data Type**: question-answering pairs

**Domains**:
- Electrical Engineering
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2502.07980v1)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate and enhance the reasoning capabilities of LLMs in understanding and interpreting analog circuits.

**Target Audience**:
- ML Researchers
- Circuit Design Engineers
- Industry Practitioners

**Tasks**:
- Circuit Interpretation
- Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from various educational and industry circuit design sources, including MIT course materials.

**Size**: 510 questions

**Format**: JSON

**Annotation**: Questions were manually curated and structured around templates for consistency.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Global Accuracy
- Template Accuracy (pass@k/n)

**Calculation**: Global accuracy is calculated as the number of correctly answered questions divided by the total number of questions. Template accuracy evaluates if various numerical setups of a template are solved correctly.

**Interpretation**: Higher global accuracy indicates better overall performance, while template accuracy provides insights into the understanding of circuit topologies.

**Validation**: The benchmark's evaluation setup is designed to allow for automatic and human evaluations, providing a comprehensive performance understanding.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: N/A - The dataset does not involve personal data.

**Data Licensing**: Not Applicable

**Consent Procedures**: N/A - No personal data collection involved.

**Compliance With Regulations**: Not Applicable
