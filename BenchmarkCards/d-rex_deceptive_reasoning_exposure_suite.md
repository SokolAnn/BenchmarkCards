# D-REX (Deceptive Reasoning Exposure Suite)

## 📊 Benchmark Details

**Name**: D-REX (Deceptive Reasoning Exposure Suite)

**Overview**: D-REX is a benchmark designed to evaluate the discrepancy between a model's internal reasoning process and its final output, focusing on detecting deceptive reasoning in large language models.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TruthfulQA
- AILuminate
- StrongReject

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To address the critical issue of deceptive reasoning in large language models and facilitate the development of safety mechanisms.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Safety Engineers

**Tasks**:
- Deceptive Reasoning Detection

**Limitations**: N/A

## 💾 Data

**Source**: Constructed through a competitive red-teaming exercise

**Size**: 8,162 samples

**Format**: N/A

**Annotation**: Generated through human red-teaming exercises

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Detection Evasion
- Output Camouflage
- Malicious Internal Reasoning
- Secrecy
- Deceptively Harmful Output

**Calculation**: Based on the performance of models against specific deceptive reasoning criteria.

**Interpretation**: Models are judged on their ability to camouflaged malicious intent while generating benign outputs.

**Baseline Results**: Comparison against other benchmarks, but no specific baselines reported.

**Validation**: No specific validation methods mentioned.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**
- **Robustness**: Prompt injection attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
