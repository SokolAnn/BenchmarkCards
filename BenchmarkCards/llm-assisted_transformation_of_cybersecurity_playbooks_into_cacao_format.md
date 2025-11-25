# LLM-Assisted Transformation of Cybersecurity Playbooks into CACAO Format

## 📊 Benchmark Details

**Name**: LLM-Assisted Transformation of Cybersecurity Playbooks into CACAO Format

**Overview**: This paper proposes a systematic approach to automatically translate legacy incident response playbooks into the standardized, machine-readable CACAO format using Large Language Models (LLMs) and various Prompt Engineering techniques.

**Data Type**: text

**Domains**:
- Cybersecurity

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Fraunhofer-FIT-DSAI/CyberGuard)

## 🎯 Purpose and Intended Users

**Goal**: To automate the transformation of legacy unstructured cybersecurity playbooks into standardized, machine-readable formats aligned with the CACAO specification.

**Target Audience**:
- Cybersecurity practitioners
- SOAR platform developers

**Tasks**:
- Cybersecurity Playbook Transformation

**Limitations**: The dataset used is vendor-specific and may not capture the diversity of real-world playbooks.

## 💾 Data

**Source**: Custom-generated dataset of legacy playbooks paired with manually created CACAO references.

**Size**: 40 playbooks

**Format**: JSON

**Annotation**: Manual annotations from experts for CACAO translations.

## 🔬 Methodology

**Methods**:
- Prompt Engineering
- Syntactic Validation
- Semantic Evaluation

**Metrics**:
- Syntactic Error Counts
- Damerau-Levenshtein Distance
- Graph Edit Distance

**Calculation**: Errors were calculated based on the number of syntactic problems identified and measured using distance metrics.

**Interpretation**: Lower error counts indicate better performance in translating playbooks to the CACAO format.

**Baseline Results**: The method achieved a 73% reduction in syntactic errors compared to baseline models.

**Validation**: Validation was performed using a custom syntax-checking mechanism tailored to the CACAO format.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Automated transformation also raises concerns regarding the handling of sensitive information which may exist in playbooks.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
