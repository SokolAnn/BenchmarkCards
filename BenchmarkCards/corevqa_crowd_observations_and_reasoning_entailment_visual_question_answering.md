# COREVQA (Crowd Observations and Reasoning Entailment Visual Question Answering)

## 📊 Benchmark Details

**Name**: COREVQA (Crowd Observations and Reasoning Entailment Visual Question Answering)

**Overview**: COREVQA is a benchmark of 5608 image and synthetically generated true/false statement pairs, designed to evaluate Vision-Language Models' ability to perform visual entailment reasoning on complex, crowded images.

**Data Type**: image and true/false statement pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VQAv2
- SNLI-VE
- NWPU-Crowd

**Resources**:
- [Resource](https://huggingface.co/datasets/COREVQA2025/COREVQA)
- [GitHub Repository](https://github.com/corevqa/COREVQA)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of COREVQA is to rigorously evaluate Vision-Language Models in terms of their capabilities for detailed visual inspection and multi-step visual entailment across complex image scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Images sourced from the CrowdHuman dataset and statement pairs generated synthetically.

**Size**: 5,608 image-statement pairs

**Format**: N/A

**Annotation**: Hand-labeled ground truths for accuracy.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on model responses compared to hand-labeled ground truths.

**Interpretation**: Performance is assessed based on the ability of models to correctly identify the truthfulness of statements about the images.

**Baseline Results**: GPT-4.1 achieved the highest accuracy at 77.57%.

**Validation**: Models were evaluated on the entire dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
