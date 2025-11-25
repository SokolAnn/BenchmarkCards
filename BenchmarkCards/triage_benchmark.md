# TRIAGE Benchmark

## 📊 Benchmark Details

**Name**: TRIAGE Benchmark

**Overview**: TRIAGE is a novel machine ethics benchmark that tests LLMs’ ability to make ethical decisions during mass casualty incidents using real-world ethical dilemmas with clear solutions designed by medical professionals.

**Data Type**: patient descriptions

**Domains**:
- Medical Ethics

**Languages**:
- English

**Similar Benchmarks**:
- MACHIA VELLI Benchmark

**Resources**:
- [GitHub Repository](https://github.com/NLie2/Triage)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark ethical decision-making capabilities of large language models in medical contexts, specifically during mass casualty situations.

**Target Audience**:
- AI Researchers
- Medical Professionals

**Tasks**:
- Ethical Decision Making

**Limitations**: N/A

## 💾 Data

**Source**: Triage training materials for the START and jumpSTART models.

**Size**: 87 patient descriptions

**Format**: N/A

**Annotation**: Designed by medical professionals.

## 🔬 Methodology

**Methods**:
- Mixed logistic regression models

**Metrics**:
- Accuracy

**Calculation**: Correctness evaluated by the accuracy of triage assignments.

**Interpretation**: Models' performance compared against random guessing.

**Baseline Results**: All models except Mistral outperform random guessing.

**Validation**: Evaluated models' ability to assign patients to correct triage groups across various ethical contexts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
