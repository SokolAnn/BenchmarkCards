# SKA-Bench (Structured Knowledge Augmented QA Benchmark)

## 📊 Benchmark Details

**Name**: SKA-Bench (Structured Knowledge Augmented QA Benchmark)

**Overview**: SKA-Bench is a comprehensive benchmark designed to evaluate the structured knowledge understanding capabilities of large language models (LLMs) through a fine-grained approach, encompassing different types of structured knowledge such as knowledge graphs and tables.

**Data Type**: question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/zjukg/SKA-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and rigorous evaluation for LLMs in understanding structured knowledge.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering
- Information Integration
- Noise Robustness

**Limitations**: SKA-Bench is limited to English only and does not yet capture the performances of LLMs in understanding structured knowledge across multiple languages.

## 💾 Data

**Source**: A collection of structured knowledge augmented QA instances generated from various existing datasets such as WebQSP, CWQ, WTQ, and others.

**Size**: 921 instances

**Format**: JSON

**Annotation**: Manual annotation performed by domain experts to identify positive and noisy knowledge units.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Macro F1 Score
- Rejection Rate

**Calculation**: Metrics are calculated based on the agreement between predicted answers and gold answers.

**Interpretation**: A higher F1 Score indicates better performance in understanding structured knowledge.

**Validation**: Empirical evaluations conducted on multiple LLMs to assess their understanding capabilities through various testbeds.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
