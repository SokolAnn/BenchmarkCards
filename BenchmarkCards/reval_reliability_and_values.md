# REVAL (REliability and VALues)

## 📊 Benchmark Details

**Name**: REVAL (REliability and VALues)

**Overview**: REVAL is a comprehensive benchmark designed to evaluate the Reliability and Values of large vision-language models (LVLMs), encompassing over 144K image-text Visual Question Answering (VQA) samples.

**Data Type**: Visual Question Answering samples

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MultiTrust

**Resources**:
- [Resource](https://doi.org/10.48550/ARXIV.2403.16566)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust framework for evaluating the reliability and ethical values of large vision-language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Ethics Researchers

**Tasks**:
- Visual Question Answering
- Bias Evaluation
- Safety Assessment
- Robustness Testing

**Limitations**: N/A

## 💾 Data

**Source**: Self-constructed dataset and existing datasets like Dysca, VLBiasBench, and ToViLaG.

**Size**: 144,411 samples

**Format**: N/A

**Annotation**: Manually annotated based on various evaluation criteria.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- Rejection Rate

**Calculation**: Metrics are calculated based on normalized scores across various evaluation dimensions.

**Interpretation**: Higher values indicate better performance and ethical alignment.

**Baseline Results**: N/A

**Validation**: The benchmark's validity is tested through comparisons with existing benchmarks and assessments of multiple LVLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Exposing personal information
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
