# FD-Dataset

## 📊 Benchmark Details

**Name**: FD-Dataset

**Overview**: FD-Dataset is a bilingual fingerprinting benchmark comprising 90,000 text samples from 20 famous proprietary and open-source LLMs, designed to facilitate research in LLM attribution.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [Resource](https://arxiv.org/abs/2501.16029v3)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset that enhances research and development in the area of large language model attribution.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Model Attribution

**Limitations**: N/A

## 💾 Data

**Source**: Generated texts from 20 proprietary and open-source LLMs.

**Size**: 90,000 samples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy
- Macro F1 Score

**Calculation**: Metrics are calculated based on model performance across various attribution tasks evaluated on FD-Dataset.

**Interpretation**: Higher Macro F1 scores indicate better performance in differentiating between LLM sources.

**Baseline Results**: FDLLM achieves a Macro F1 score of 96.56% and accuracy values exceeding 95% on unseen models.

**Validation**: Extensive empirical evaluations demonstrate the effectiveness of the FDLLM model on the FD-Dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
