# MedBookVQA

## 📊 Benchmark Details

**Name**: MedBookVQA

**Overview**: MedBookVQA is a systematic and comprehensive multimodal benchmark derived from open-access medical textbooks, consisting of 5,000 clinically relevant questions across various medical VQA task categories.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/slyipae1/MedBookVQA)
- [GitHub Repository](https://github.com/slyipae1/MedBookVQA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating General Medical Artificial Intelligence (GMAI) systems across diverse medical domains.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Medical Professionals
- AI Developers

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Open-access medical textbooks from DOAB (Directory of Open Access Books).

**Size**: 5,000 questions

**Format**: N/A

**Annotation**: Automated extraction of medical figures paired with narrative context.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Evaluation on a variety of models

**Metrics**:
- Accuracy

**Calculation**: Percentage of correctly answered questions across VQA tasks.

**Interpretation**: Higher accuracy indicates better performance in medical VQA tasks.

**Baseline Results**: Measured against various multimodal large language models (MLLMs).

**Validation**: Tests conducted on diverse MLLMs, revealing significant capability gaps in GMAI systems.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Societal Impact**: Impact on education: bypassing learning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No sensitive data included as information is sourced from publicly available textbooks.

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
