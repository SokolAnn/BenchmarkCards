# MMFakeBench (Mixed-Source Multimodal Misinformation Detection Benchmark)

## 📊 Benchmark Details

**Name**: MMFakeBench (Mixed-Source Multimodal Misinformation Detection Benchmark)

**Overview**: MMFakeBench is the first comprehensive benchmark for mixed-source multimodal misinformation detection, comprising 11,000 data pairs across three categories: textual veracity distortion, visual veracity distortion, and cross-modal consistency distortion.

**Data Type**: multimodal (text-image pairs)

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://liuxuannan.github.io/MMFakeBench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for mixed-source multimodal misinformation detection and evaluate existing methods.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Misinformation Detection
- Text Classification
- Multimodal Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Includes 11,000 data pairs generated using various AI tools, with diverse sources and categories as defined in the benchmark.

**Size**: 11,000 pairs

**Format**: JSON

**Annotation**: Automatically generated with verification from AI models.

## 🔬 Methodology

**Methods**:
- Evaluation of detection methods
- Automated metrics
- Model-based evaluation

**Metrics**:
- F1 Score
- Precision
- Recall
- Accuracy

**Calculation**: Metrics calculated based on multi-class classification across instances categorized into textual, visual, and cross-modal distortions.

**Interpretation**: Higher scores indicate better performance in identifying misinformation across mixed sources.

**Validation**: Comprehensive evaluation performed under a zero-shot setting with multiple large vision-language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Attribution Non-Commercial ShareAlike 4.0 International (CC BY-NC-SA 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
