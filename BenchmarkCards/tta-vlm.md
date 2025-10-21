# TTA-VLM

## 📊 Benchmark Details

**Name**: TTA-VLM

**Overview**: TTA-VLM is a comprehensive benchmark for evaluating test-time adaptation (TTA) methods on vision-language models (VLMs), addressing key limitations in existing TTA research by implementing 8 episodic and 7 online TTA methods across 15 widely-used datasets.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/TomSheng21/tta-vlm)

## 🎯 Purpose and Intended Users

**Goal**: To provide fair comparisons and comprehensive evaluations of test-time adaptation methods for vision-language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Classification
- Multi-modal Retrieval

**Limitations**: The benchmark focuses on classification tasks and does not cover broader tasks of VLMs, such as image captioning, VQA, and segmentation.

## 💾 Data

**Source**: 15 datasets commonly adopted in VLM fine-tuning, including fine-grained and ImageNet-related datasets.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Robustness
- Calibration
- Out-of-Distribution Detection
- Stability

**Calculation**: Metrics are calculated based on predefined experimental setups and comparisons across all methods in the benchmark.

**Interpretation**: Higher accuracy and robust metrics indicate better performance of TTA methods.

**Baseline Results**: Performance gains of most existing TTA methods are marginal compared to the pioneering baseline TPT.

**Validation**: The benchmark has been validated through extensive experimentation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
