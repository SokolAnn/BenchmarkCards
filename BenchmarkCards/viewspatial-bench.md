# ViewSpatial-Bench

## 📊 Benchmark Details

**Name**: ViewSpatial-Bench

**Overview**: ViewSpatial-Bench is the first comprehensive benchmark for evaluating multi-perspective spatial localization capabilities of vision-language models across five distinct task types.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- EmbSpatial-Bench
- VSI-Bench
- 3DSRBench
- SPHERE

**Resources**:
- [GitHub Repository](https://github.com/ZJU-REAL/ViewSpatial-Bench)
- [Resource](https://zju-real.github.io/ViewSpatial-Page/)

## 🎯 Purpose and Intended Users

**Goal**: To quantitatively evaluate vision-language models' spatial localization capabilities in 3D environments from multiple perspectives.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Spatial Localization
- Perspective-Taking

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from ScanNet and MS-COCO datasets using automated annotation pipelines.

**Size**: 5,712 samples

**Format**: N/A

**Annotation**: Automated annotation with manual verification.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated by comparing model predictions with ground truth answers.

**Interpretation**: Higher accuracy indicates better spatial localization performance across multiple viewpoints.

**Baseline Results**: N/A

**Validation**: Evaluated under zero-shot settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
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
