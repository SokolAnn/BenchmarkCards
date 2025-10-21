# ReSeDis (Referring Search and Discovery)

## 📊 Benchmark Details

**Name**: ReSeDis (Referring Search and Discovery)

**Overview**: ReSeDis is a benchmark specifically designed to evaluate a model’s ability to perform large-scale referring object search in realistic, open-world settings, integrating large-scale image retrieval and fine-grained object localization.

**Data Type**: image with bounding boxes and segmentation masks

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/hufflepuff0596/ReSeDis)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capability of models to search and localize objects in large image datasets based on natural language descriptions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Object Localization
- Image Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: MS-COCO dataset with additional manual descriptions created for the benchmark.

**Size**: 7,088 images and 9,664 referring expressions

**Format**: N/A

**Annotation**: Manually written referring expressions with bounding boxes and segmentation masks.

## 🔬 Methodology

**Methods**:
- Object Candidate Generation
- Cross-Modal Similarity Scoring
- Intra-Image Relational Reasoning

**Metrics**:
- Recall Accuracy of Target Images
- Object Localization Accuracy

**Calculation**: Recall accuracy is calculated based on the model's ability to correctly identify relevant images, while localization accuracy uses Precision at 50% overlap threshold (Pr@50).

**Interpretation**: High recall accuracy indicates effective image searching, while high localization accuracy indicates precise object detection.

**Baseline Results**: Top-1 image recall of 21.22% with YOLOv8 proposals; Top-1 image recall of 23.33% using ground-truth boxes.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
