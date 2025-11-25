# R2SM (Referring and Reasoning for Selective Masks)

## 📊 Benchmark Details

**Name**: R2SM (Referring and Reasoning for Selective Masks)

**Overview**: The R2SM dataset consists of both modal and amodal text queries, each paired with the corresponding ground-truth mask, enabling model finetuning and evaluation for the ability to segment images as per user intent.

**Data Type**: text-image segmentation pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/vllabnthu/R2SM)

## 🎯 Purpose and Intended Users

**Goal**: To provide a challenging and insightful testbed for advancing research in multimodal reasoning and intent-aware segmentation.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Image Segmentation

**Limitations**: N/A

## 💾 Data

**Source**: Constructed by augmenting annotations of COCOA-cls, D2SA, and MUV A.

**Size**: 7,276 images with 36,324 text queries

**Format**: N/A

**Annotation**: Generated using the Claude API, employing a systematic methodology for text query generation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Generalized Intersection-over-Union (gIoU)
- Cumulative Intersection-over-Union (cIoU)

**Calculation**: Metrics are calculated by comparing predicted masks to ground-truth masks.

**Interpretation**: Higher scores indicate better overlap between predicted and ground-truth masks.

**Baseline Results**: Fine-tuned models generally show improved performance on the dataset, indicating its utility in enhancing segmentation capabilities.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
