# Virology Capabilities Test (VCT)

## 📊 Benchmark Details

**Name**: Virology Capabilities Test (VCT)

**Overview**: The Virology Capabilities Test (VCT) is a large language model benchmark that measures the capability to troubleshoot complex virology laboratory protocols. It consists of 322 multimodal questions covering fundamental, tacit, and visual knowledge essential for practical work in virology laboratories.

**Data Type**: multimodal question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- GPQA

**Resources**:
- [Resource](https://arxiv.org/abs/2504.16137)

## 🎯 Purpose and Intended Users

**Goal**: To measure practical knowledge about virology with a focus on troubleshooting experiments in virology protocols, including dual-use topics.

**Target Audience**:
- ML Researchers
- Life Sciences Researchers
- AI Safety Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Questions constructed from the inputs of PhD-level expert virologists and subjected to rigorous vetting and validation processes.

**Size**: 322 questions

**Format**: N/A

**Annotation**: Validated by multiple expert reviewers

## 🔬 Methodology

**Methods**:
- Human evaluation
- Expert evaluation

**Metrics**:
- Accuracy

**Calculation**: Models must correctly select all true answer statements from a set of 4–10 true/false answer statements.

**Interpretation**: Higher scores indicate better performance in accurately answering complex virology questions.

**Baseline Results**: Expert virologists scored an average of 22.1% accuracy on tailored VCT questions.

**Validation**: Each question was peer-reviewed by multiple experts before acceptance into the benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**
- **Governance**: Lack of system transparency
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
