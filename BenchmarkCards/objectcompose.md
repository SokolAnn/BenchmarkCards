# ObjectCompose

## 📊 Benchmark Details

**Name**: ObjectCompose

**Overview**: ObjectCompose is a method for generating diverse object-to-background compositional changes to evaluate the resilience of vision models. It quantitatively assesses the impact of background variations on deep learning model performance.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- ImageNet
- COCO

**Resources**:
- [GitHub Repository](https://github.com/Muhammad-Huzaifaa/ObjectCompose)

## 🎯 Purpose and Intended Users

**Goal**: To analyze the resilience of vision models to natural and adversarial background changes.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Object Detection
- Image Classification
- Segmentation

**Limitations**: N/A

## 💾 Data

**Source**: ImageNet and COCO datasets

**Size**: 77,070 images in ImageNet-B and 5,635 images in COCO-DC

**Format**: N/A

**Annotation**: Segmentation masks generated using SAM and captions generated using BLIP-2.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Evaluation on various vision models

**Metrics**:
- Top-1 Accuracy
- Average Precision (AP)

**Calculation**: Performance drop attributed to changes in background context.

**Interpretation**: A decrease in accuracy indicates a greater vulnerability to background changes.

**Baseline Results**: Original model performance compared against models subjected to background variations.

**Validation**: Evaluation performed on standard benchmarks using vision models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
