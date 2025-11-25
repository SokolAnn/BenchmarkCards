# SciReplicate-Bench

## 📊 Benchmark Details

**Name**: SciReplicate-Bench

**Overview**: SciReplicate-Bench is a benchmark of 100 tasks from 36 NLP papers published in 2024, designed to evaluate LLMs' capabilities in reproducing algorithms described in academic papers by generating code from algorithm descriptions.

**Data Type**: algorithm description and code tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/user/repo)
- [Resource](https://www.examplehomepage.com)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' ability to reproduce algorithms from scientific literature by generating executable code.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Code Generation
- Algorithm Comprehension

**Limitations**: N/A

## 💾 Data

**Source**: 36 peer-reviewed NLP papers selected from 2024.

**Size**: 100 tasks

**Format**: CSV or JSON

**Annotation**: Annotated by researchers followed by manual review.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Execution accuracy
- CodeBLEU
- Reasoning graph accuracy

**Calculation**: Metrics are calculated based on the accuracy of generated code against reference implementations and reasoning graphs.

**Interpretation**: Higher execution accuracy and reasoning graph accuracy indicate better understanding and implementation of algorithmic concepts.

**Baseline Results**: N/A

**Validation**: Cross-validated against reference implementations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
