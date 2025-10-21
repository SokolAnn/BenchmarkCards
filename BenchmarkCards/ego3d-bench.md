# Ego3D-Bench

## 📊 Benchmark Details

**Name**: Ego3D-Bench

**Overview**: Ego3D-Bench is a benchmark for spatial reasoning of Vision-Language Models (VLMs) using ego-centric, multi-view outdoor data. It comprises over 8,600 question-answering (QA) pairs created with human annotators to ensure quality and diversity.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VSI-Bench
- All-Angle Bench

**Resources**:
- [GitHub Repository](https://github.com/manycore-research/Ego3D-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the spatial reasoning abilities of Vision-Language Models in ego-centric multi-view settings.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Robotics Developers

**Tasks**:
- 3D Spatial Reasoning
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Curated from the validation sets of NuScenes, Waymo Open Dataset, and Argoverse 1.

**Size**: 8,600 QA pairs

**Format**: JSON

**Annotation**: Created with significant involvement from human annotators.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Root Mean Squared Error (RMSE)

**Calculation**: Metrics are calculated based on multi-choice questions and absolute distance estimation.

**Interpretation**: Higher accuracy indicates better performance in spatial reasoning tasks.

**Validation**: The benchmark was validated through rigorous quality review by human annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
