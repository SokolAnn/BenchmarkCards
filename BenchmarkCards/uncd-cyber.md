# UNCD-Cyber

## 📊 Benchmark Details

**Name**: UNCD-Cyber

**Overview**: UNCD-Cyber provides a detailed assessment of the removal of dangerous capabilities in LLMs using a fine-grained evaluation framework based on Cognitive Diagnosis Modeling.

**Data Type**: question-answering pairs

**Domains**:
- Cybersecurity

**Languages**:
- English

**Similar Benchmarks**:
- MUSE

**Resources**:
- [GitHub Repository](https://github.com/lyicheng619/UNCD.git)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the evaluation of LLM unlearning methods through fine-grained diagnostic assessments of harmful knowledge retention.

**Target Audience**:
- ML Researchers
- Cybersecurity Experts
- Model Developers

**Tasks**:
- Knowledge Assessment
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Open-source Cyber Threat Intelligence reports and tailored evaluation datasets based on MITRE ATT&CK techniques.

**Size**: 4,900 forget samples and 8,300 retain samples

**Format**: JSONL

**Annotation**: Generated using GPT-4o and reviewed by experts.

## 🔬 Methodology

**Methods**:
- Cognitive Diagnosis Modeling
- Question-answering evaluation

**Metrics**:
- Accuracy
- Mean knowledge state score

**Calculation**: Metrics are calculated based on the assessment of knowledge concepts associated with the ability to perform cyberattacks.

**Interpretation**: Higher scores indicate greater effectiveness in unlearning harmful capabilities while retaining benign ones.

**Validation**: Validation from responses collected during various unlearning methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Privacy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: Residual harmful capabilities resulting from ineffective unlearning methods.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
