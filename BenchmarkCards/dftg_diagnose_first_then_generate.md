# DFTG (Diagnose First, Then Generate)

## 📊 Benchmark Details

**Name**: DFTG (Diagnose First, Then Generate)

**Overview**: The DFTG framework is proposed for generating targeted instruction data to mitigate hallucinations in large vision-language models by first diagnosing hallucinations, then producing tailored instructional data based on model-specific needs.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- LRV-Instruction

**Resources**:
- [Resource](https://arxiv.org/abs/2404.10332)

## 🎯 Purpose and Intended Users

**Goal**: To create a framework that addresses hallucination specificity in LVLMs by generating customized instruction data.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multimodal Instruction Tuning

**Limitations**: The method is limited to diagnosing object and attribute-level hallucinations and requires reliable information extraction capabilities.

## 💾 Data

**Source**: Synthetic data generated from diagnosed hallucinations in vision-language models.

**Size**: 79,000 instructions for MiniGPT-4, 58,000 instructions for mPlug-Owl

**Format**: JSON

**Annotation**: Generated based on diagnostic results from hallucination checking.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on model responses in hallucination benchmarks.

**Interpretation**: High scores indicate improved mitigation of hallucinations compared to existing datasets.

**Validation**: Evaluated through extensive experiments on POPE, MME, AMBER, and VHTest datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack, Data poisoning

**Potential Harm**: ['Increased hallucination leading to misinformation']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
