# C-VQA (Counterfactual Visual Question Answering)

## 📊 Benchmark Details

**Name**: C-VQA (Counterfactual Visual Question Answering)

**Overview**: C-VQA is a novel dataset designed to examine the counterfactual reasoning capabilities of multi-modal large language models. It consists of original questions infused with counterfactual presuppositions to evaluate the reasoning abilities of models.

**Data Type**: image-question pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VQAv2
- CF-VQA
- VQA-CP

**Resources**:
- [Resource](https://bzhao.me/C-VQA/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate counterfactual reasoning abilities in multi-modal language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: The dataset currently includes a limited number of images, affecting the comprehensiveness of evaluation.

## 💾 Data

**Source**: Constructed using original questions from VQAv2 and generating new counterfactual questions.

**Size**: 6,144 image-question pairs (3,144 real and 3,000 synthetic)

**Format**: JSON

**Annotation**: Manually annotated by experts and verified for correctness.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on model performance on original vs. counterfactual questions.

**Interpretation**: High performance indicates better reasoning capabilities in counterfactual scenarios.

**Baseline Results**: Performance metrics varied, showing drops of up to 40% for counterfactual questions.

**Validation**: Comparative evaluation with existing state-of-the-art models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Yes, the dataset includes an analysis of biases in answering based on gender-related questions.

**Potential Harm**: ['Bias in handling gender-related counterfactual questions']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
