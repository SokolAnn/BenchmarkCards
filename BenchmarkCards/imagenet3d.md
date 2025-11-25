# ImageNet3D

## 📊 Benchmark Details

**Name**: ImageNet3D

**Overview**: ImageNet3D is a large dataset for general-purpose object-level 3D understanding that augments 200 categories from the ImageNet dataset with 2D bounding box, 3D pose, 3D location annotations, and image captions interleaved with 3D information.

**Data Type**: 2D bounding box and 3D pose annotations

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- ObjectNet3D
- PASCAL3D+

**Resources**:
- [GitHub Repository](https://github.com/user/repo)
- [Resource](https://huggingface.co/datasets/name)
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: Facilitate the evaluation and research of general-purpose object-level 3D understanding models.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- 6D Pose Estimation
- Object Classification
- Open-Vocabulary Pose Estimation

**Limitations**: N/A

## 💾 Data

**Source**: ImageNet21k dataset

**Size**: 86,000 objects across 200 categories

**Format**: JSON

**Annotation**: Annotated by a team of 30 trained annotators

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Pose Accuracy
- Classification Accuracy

**Calculation**: Pose accuracy is measured by the percentage of samples with pose errors smaller than a pre-defined threshold.

**Interpretation**: Higher accuracy indicates better performance in 3D awareness and classification.

**Baseline Results**: Results demonstrate the potential of models trained on ImageNet3D compared to existing datasets.

**Validation**: Cross-validation performed on multiple model metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
