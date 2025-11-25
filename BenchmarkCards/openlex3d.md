# OpenLex3D

## 📊 Benchmark Details

**Name**: OpenLex3D

**Overview**: OpenLex3D is a dedicated benchmark to evaluate 3D open-vocabulary scene representations, providing new label annotations for 23 scenes, capturing real-world linguistic variability and introducing nuanced descriptions. It defines two evaluation tasks: open-set semantic segmentation and object retrieval.

**Data Type**: semantic segmentation and object retrieval labels

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://openlex3d.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of 3D scene representations using open-vocabulary semantics, capturing linguistic variability across object categories.

**Target Audience**:
- ML Researchers
- Computer Vision Practitioners

**Tasks**:
- Semantic Segmentation
- Object Retrieval

**Limitations**: The label set focuses on direct labels and does not account for additional object properties such as affordances, material, and color.

## 💾 Data

**Source**: Human-annotated labels for 23 scenes from the Replica, ScanNet++, and HM3D datasets.

**Size**: 23 scenes labeled with an average of 11 labels per object

**Format**: N/A

**Annotation**: Labels reviewed by four human annotators for each object.

## 🔬 Methodology

**Methods**:
- Human evaluation of segmentation and retrieval tasks
- Open-set metrics for evaluation

**Metrics**:
- Top-N IoU
- Average Precision (AP)

**Calculation**: Evaluation metrics are calculated based on predicted labels and their textual features compared to ground truth.

**Interpretation**: Top-N IoU assesses the proportion of correctly classified objects within defined categories; AP evaluates the effectiveness of retrieval tasks.

**Baseline Results**: State-of-the-art 3D open-vocabulary methods evaluated on both tasks.

**Validation**: Evaluation of performance across various existing models to identify strengths and weaknesses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
