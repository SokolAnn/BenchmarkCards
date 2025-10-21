# Benchmarking PDF Accessibility Evaluation

## 📊 Benchmark Details

**Name**: Benchmarking PDF Accessibility Evaluation

**Overview**: This paper introduces a novel benchmark dataset of scholarly PDFs with expert-validated accessibility annotations across seven criteria and a four-category evaluation framework to systematically assess accessibility evaluation approaches.

**Data Type**: PDF documents with accessibility annotations

**Domains**:
- Natural Language Processing
- Accessibility

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Anukriti12/PDF-Accessibility-Benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized methodology to evaluate PDF accessibility and explore the capabilities of large language models in accessibility assessment.

**Target Audience**:
- ML Researchers
- Accessibility Practitioners
- Document Authors

**Tasks**:
- Accessibility Evaluation
- Automated Testing

**Limitations**: N/A

## 💾 Data

**Source**: Expert-validated scholarly PDFs derived from a corpus of 20,000 scholarly articles

**Size**: 125 PDFs

**Format**: PDF

**Annotation**: Expert validations of accessibility against WCAG and PDF/UA standards

## 🔬 Methodology

**Methods**:
- Large Language Models evaluation
- Zero-shot prompting
- Expert validation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on model performance across accessibility evaluation criteria.

**Interpretation**: Models are assessed based on their capability to evaluate and categorize PDF accessibility accurately.

**Baseline Results**: GPT-4-Turbo achieved the highest overall accuracy of 0.85.

**Validation**: Expert review of the annotated dataset and model outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: This work is licensed under a Creative Commons Attribution 4.0 International License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
