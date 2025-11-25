# MDBench (Multi-Document Reasoning Benchmark)

## 📊 Benchmark Details

**Name**: MDBench (Multi-Document Reasoning Benchmark)

**Overview**: MDBench is a new benchmark for evaluating LLMs on multi-document reasoning tasks, generated through a synthetic process that enables the creation of challenging question-answer examples based on structured knowledge.

**Data Type**: question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/launch/MDBench)
- [GitHub Repository](https://github.com/jpeper/MDBench)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the capabilities of large language models in multi-document reasoning and to provide a scalable approach to benchmark generation.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The evaluation framework is primarily focused on multi-document reasoning and may not encompass all reasoning tasks.

## 💾 Data

**Source**: The benchmark is generated from structured seed knowledge sourced from tabular data, specifically the TabFact dataset, which comprises tables from Wikipedia.

**Size**: 1,000 examples

**Format**: JSON

**Annotation**: Automatically validated with human-validated examples to ensure quality.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Exact match

**Calculation**: Metrics are calculated based on the comparison of model predictions against ground-truth answers, using a scoring mechanism for accuracy assessments.

**Interpretation**: Higher accuracy indicates better reasoning capabilities across multi-document QA tasks.

**Validation**: The benchmark examples undergo a multi-step validation process integrating automated checks for quality and internal consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning, Evasion attack
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
