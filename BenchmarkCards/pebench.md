# PEBench

## 📊 Benchmark Details

**Name**: PEBench

**Overview**: PEBench is a novel benchmark designed to facilitate a thorough assessment of machine unlearning (MU) in multimodal large language models (MLLMs). It features a fictitious dataset of personal entities and corresponding event scenes to evaluate unlearning across distinct yet entangled concepts.

**Data Type**: image

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMUBench
- CLEAR

**Resources**:
- [Resource](https://pebench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of PEBench is to evaluate the efficacy of machine unlearning in multimodal large language models, focusing on personal identities and event scenes.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Machine Unlearning

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic dataset consisting of 200 fictitious personal entities across 40 event scenes.

**Size**: 8,000 images

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- ROUGE-L
- Precision

**Calculation**: Metrics are calculated based on the model's performance in retaining knowledge and forgetting designated concepts.

**Interpretation**: Higher scores indicate better performance in the evaluation of unlearning effectiveness.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
