# AUTO TRUST

## 📊 Benchmark Details

**Name**: AUTO TRUST

**Overview**: AutoTrust is a comprehensive benchmark for assessing the trustworthiness of large vision-language models for autonomous driving, considering dimensions such as Trustfulness, Safety, Robustness, Privacy, and Fairness.

**Data Type**: visual question-answering pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- NuScenes-QA
- NuScenes-MQA
- DriveLM-NuScenes
- LingoQA
- CoVLA

**Resources**:
- [GitHub Repository](https://github.com/taco-group/AutoTrust)
- [Resource](https://taco-group.github.io/AutoTrust/)

## 🎯 Purpose and Intended Users

**Goal**: To holistically assess the trustworthiness of large vision-language models for autonomous driving.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Regulators

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Multiple open-access autonomous driving datasets including NuScenes-QA, NuScenes-MQA, DriveLM-NuScenes, and LingoQA.

**Size**: 10,000 unique scenes and 18,000 queries

**Format**: N/A

**Annotation**: Generated via both manual and automated methods.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Demographic Accuracy Difference (DAD)
- Worst Accuracy (WA)

**Calculation**: Accuracy is calculated based on the number of correct answers divided by the total number of answers. DAD and WA are derived from model performance comparisons across demographic groups.

**Interpretation**: Higher metrics indicate better trustworthiness; lower DAD values reflect less bias across demographic groups.

**Baseline Results**: N/A

**Validation**: Robustness evaluated through performance against various adversarial and misleading scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack, Evasion attack
- **Privacy**: Personal information in data
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Includes analysis of model performance across genders, ages, and races.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Models demonstrated some vulnerabilities in preserving anonymity in sensitive data contexts.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
