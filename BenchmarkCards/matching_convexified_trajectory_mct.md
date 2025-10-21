# Matching Convexified Trajectory (MCT)

## 📊 Benchmark Details

**Name**: Matching Convexified Trajectory (MCT)

**Overview**: This paper introduces the Matching Convexified Trajectory (MCT) method, which improves upon traditional Dataset Distillation techniques by creating a convexified expert trajectory that enhances optimization stability, convergence speed, and reduces storage requirements.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Dataset Condensation (DC)
- Distribution Matching (DM)
- Matching Training Trajectories (MTT)

**Resources**:
- [Resource](https://arxiv.org/abs/2406.19827)

## 🎯 Purpose and Intended Users

**Goal**: To present a novel Dataset Distillation method that improves stability and speed of model training while reducing memory consumption.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Dataset Distillation

**Limitations**: The enhancement in validation accuracy is limited by the choice of starting and ending points and the simplified calculation of trajectory characteristics.

## 💾 Data

**Source**: CIFAR-10, CIFAR-100, and Tiny-ImageNet datasets

**Size**: 3 datasets

**Format**: Image

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Distillation accuracy is computed based on the average accuracy of networks trained on synthetic datasets.

**Interpretation**: The validation accuracy trends indicate how quickly and stably the model converges using the proposed method compared to traditional methods.

**Baseline Results**: Comparison against Dataset Condensation (DC), Distribution Matching (DM), and Matching Training Trajectories (MTT) showed MCT achieved superior performance across benchmarks.

**Validation**: Extensive experiments validated the method across multiple datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
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
