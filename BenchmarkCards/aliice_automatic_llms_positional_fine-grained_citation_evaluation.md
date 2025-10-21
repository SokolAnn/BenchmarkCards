# ALiiCE (Automatic LLMs’ Positional Fine-grained Citation Evaluation)

## 📊 Benchmark Details

**Name**: ALiiCE (Automatic LLMs’ Positional Fine-grained Citation Evaluation)

**Overview**: ALiiCE is the first automatic evaluation framework for positional fine-grained citation generation, utilizing a dependency tree based approach to parse sentence-level claims into atomic claims and evaluate citation quality using three metrics: positional fine-grained citation recall, precision, and coefficient of variation of citation positions.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ylXuu/ALiiCE)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the positional fine-grained citation generation performance of large language models and demonstrate the effectiveness of the ALiiCE framework.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Long-form Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: ASQA (Ambiguous QA) and ELI5 (Explain Like I’m Five) datasets

**Size**: 948 queries for ASQA, 1,000 examples for ELI5

**Format**: Text

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Citation Recall
- Citation Precision
- Coefficient of Variation of Citation Positions (CVCP)

**Calculation**: Metrics are derived based on the performance of large language models in generating positional fine-grained citations in long-form QA responses.

**Interpretation**: Higher values of citation recall and precision indicate better citation quality, and CVCP measures the dispersion of citation positions within sentences.

**Validation**: Evaluation is validated through experiments comparing various language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
