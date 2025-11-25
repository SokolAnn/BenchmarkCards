# COUNTS (Common Objects UNder disTribution Shifts)

## 📊 Benchmark Details

**Name**: COUNTS (Common Objects UNder disTribution Shifts)

**Overview**: COUNTS is a large-scale dataset designed for out-of-distribution (OOD) generalization research in object detection and grounding tasks, encompassing 14 natural distributional shifts, over 222K samples, and more than 1,196K annotated bounding boxes.

**Data Type**: image

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/jiansheng-li/COUNTS_benchmark)
- [Resource](https://huggingface.co/datasets/jianshengli/COUNTS)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the training and evaluation of traditional object detectors and to assess the OOD grounding capabilities of multimodal large language models (MLLMs).

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Object Detection
- Grounding

**Limitations**: N/A

## 💾 Data

**Source**: Real-world images sourced and annotated through a combination of automated pipelines and human annotation.

**Size**: 222,234 images

**Format**: N/A

**Annotation**: Annotated through human verification for bounding boxes and domain information.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- mAP (Mean Average Precision)

**Calculation**: Metrics calculated based on object detection tasks using various domain shifts.

**Interpretation**: Higher mean average precision (mAP) indicates better generalization capabilities across diverse domains.

**Baseline Results**: Various object detectors including Faster R-CNN, YOLOv9, and DINO were evaluated.

**Validation**: Cross-validation using distinct training and testing domains to assess model performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
