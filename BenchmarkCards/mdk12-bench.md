# MDK12-Bench

## 📊 Benchmark Details

**Name**: MDK12-Bench

**Overview**: MDK12-Bench is a multi-disciplinary benchmark assessing the reasoning capabilities of Multimodal Large Language Models (MLLMs) via real-world K-12 examinations, comprising 140K reasoning instances across diverse difficulty levels from primary school to 12th grade.

**Data Type**: reasoning instances

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/LanceZPF/MDK12)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the reasoning abilities of MLLMs across diverse real-world K-12 tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multimodal Reasoning
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collected from online open-source exam paper repositories and refined through automated review and human inspection.

**Size**: 141,320 instances

**Format**: JSON

**Annotation**: Annotated instance-level knowledge points with difficulty levels and detailed answer explanations.

## 🔬 Methodology

**Methods**:
- Evaluated via dynamic evaluation framework with bootstrapped text and images.

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on model responses compared to the ground truth answers.

**Interpretation**: A score of 1.0 is given for an exact match, with partial credits for correct elements.

**Validation**: Through extensive experiments on various models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
