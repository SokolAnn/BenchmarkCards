# SARChat-Bench-2M: A Multi-Task Vision-Language Benchmark for SAR Image Interpretation

## 📊 Benchmark Details

**Name**: SARChat-Bench-2M: A Multi-Task Vision-Language Benchmark for SAR Image Interpretation

**Overview**: This paper innovatively proposes the first large-scale multimodal dialogue dataset for SAR images, named SARChat-2M, which contains approximately 2 million high-quality image-text pairs, encompassing diverse scenarios with detailed target annotations. This dataset supports several key tasks such as visual understanding and object detection tasks and serves as the first visual-language benchmark in the SAR domain.

**Data Type**: image-text pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/JimmyMa99/SARChat)

## 🎯 Purpose and Intended Users

**Goal**: To enable and evaluate VLMs’ capabilities in SAR image interpretation, providing a paradigmatic framework for constructing multimodal datasets across various remote sensing vertical domains.

**Target Audience**:
- Researchers in Computer Vision
- Researchers in Natural Language Processing
- Industry Practitioners

**Tasks**:
- Classification
- Fine-Grained Description
- Instance Counting
- Spatial Grounding
- Cross-Modal Identification
- Referring

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from the SARDet-100K dataset and enhanced annotations from ten established SAR detection benchmarks.

**Size**: 2,000,000 image-text pairs

**Format**: N/A

**Annotation**: Multimodal adaptations and enhanced language annotations from existing datasets.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Intersection over Union (IoU)

**Calculation**: Metrics are calculated based on predictions made by models, including precision and recall rates for different tasks.

**Interpretation**: Higher Accuracy indicates better model prediction fit, while IoU measures the overlap between predicted and ground truth bounding boxes.

**Baseline Results**: Comparison of various VLMs showed differences in performance metrics across classification and spatial grounding tasks.

**Validation**: Extensive experiments on sixteen state-of-the-art VLMs to validate the dataset's effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: In this study, all SAR datasets and methodologies are used strictly for academic research purposes, adhering to their respective licenses and data usage agreements.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
