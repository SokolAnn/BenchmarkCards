# ABSPYRAMID

## 📊 Benchmark Details

**Name**: ABSPYRAMID

**Overview**: ABSPYRAMID is a unified entailment graph to comprehensively evaluate language models’ abstraction ability, consisting of 221K textual descriptions of abstraction knowledge across diverse events.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AbstractATOMIC

**Resources**:
- [GitHub Repository](https://github.com/HKUST-KnowComp/AbsPyramid)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the abstraction ability of language models using a comprehensive graph of abstraction knowledge.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Abstraction Detection
- Abstraction Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from ASER and crowdsourced validation of abstract concepts.

**Size**: 221,000 examples

**Format**: JSON

**Annotation**: Crowdsourced and manually verified for validity.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Macro F1 Score
- AUC

**Calculation**: Metrics are calculated based on predicted vs ground-truth labels with standard classification metrics.

**Interpretation**: Higher scores in Accuracy and Macro F1 indicate better performance in abstract concept identification and generation.

**Baseline Results**: Comparative results against previous benchmarks like AbstractATOMIC show improvement in LLM performance.

**Validation**: Split datasets for training, validation, and testing with maintained sample integrity.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Misinterpretation of abstract knowledge leading to incorrect applications.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Collects data from open-source corpora with proper anonymization.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
