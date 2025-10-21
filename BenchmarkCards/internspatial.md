# InternSpatial

## 📊 Benchmark Details

**Name**: InternSpatial

**Overview**: InternSpatial is the largest open-source dataset for spatial reasoning in vision-language models, comprising 12 million QA pairs over various instruction formats to enhance spatial reasoning capabilities.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- SpatialVLM
- SpatialQA
- OSD

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of InternSpatial is to enhance spatial reasoning capabilities in vision-language models by providing a comprehensive and diverse dataset.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Position Comparison
- Size Comparison
- Existence Estimation
- Object Counting
- Rotation Estimation
- Absolute Distance
- Room Size
- Object Size
- Route Planning
- Appearance Order

**Limitations**: N/A

## 💾 Data

**Source**: Sourced from diverse visual environments including in-the-wild scenes, structured indoor spaces, urban streetscapes, object-centric scenes, and embodied navigation contexts.

**Size**: 12,035,415 question-answer pairs

**Format**: JSON

**Annotation**: Automated annotation using a data generation pipeline incorporating visual language models.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Manual verification

**Metrics**:
- Accuracy

**Calculation**: Evaluation metrics are computed based on the performance of models trained on InternSpatial.

**Interpretation**: Higher accuracy indicates better spatial reasoning capabilities.

**Baseline Results**: InternVL-Spatial-8B achieved 12.1% improvement in average accuracy on InternSpatial-Bench compared to baseline models.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
