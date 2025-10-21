# MSP60K

## 📊 Benchmark Details

**Name**: MSP60K

**Overview**: MSP60K is a new large-scale, cross-domain dataset for pedestrian attribute recognition consisting of 60,122 images and 57 attribute annotations across eight scenarios. It addresses challenges in existing datasets by incorporating synthetic degradation and diverse real-world conditions.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- PETA
- PA100K
- RAPv1
- WIDER

**Resources**:
- [GitHub Repository](https://github.com/Event-AHU/OpenPAR)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for pedestrian attribute recognition models and facilitate the development of more effective PAR methods.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Pedestrian Attribute Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Dataset contains images collected using smart surveillance systems and mobile phones.

**Size**: 60,122 images

**Format**: N/A

**Annotation**: Images are labeled with 57 attributes across various scenarios.

## 🔬 Methodology

**Methods**:
- Evaluation of 17 pedestrian attribute recognition models
- Random and cross-domain split protocols

**Metrics**:
- Mean Accuracy (mA)
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on predictions against ground truth labels provided in the dataset.

**Interpretation**: Higher scores indicate better performance in recognizing pedestrian attributes under various conditions.

**Baseline Results**: N/A

**Validation**: Dataset split into random training/testing subsets and cross-domain scenarios to evaluate generalization.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
