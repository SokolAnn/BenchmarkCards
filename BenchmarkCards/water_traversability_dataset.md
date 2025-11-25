# Water Traversability Dataset

## 📊 Benchmark Details

**Name**: Water Traversability Dataset

**Overview**: This paper introduces a dataset of human-annotated water traversability ratings to evaluate foundation models for zero-shot terrain traversability estimation.

**Data Type**: images with water traversability ratings

**Domains**:
- Robotics

**Languages**:
- N/A

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To explore zero-shot terrain traversability estimation using vision-language models (VLMs) and to investigate human consensus on water traversability ratings.

**Target Audience**:
- ML Researchers
- Robotics Practitioners

**Tasks**:
- Multi-class Classification

**Limitations**: N/A

## 💾 Data

**Source**: Dataset comprises images from RUGD, RELLIS-3D, self-taken images, and CC-0 online images.

**Size**: 195 images with 508 annotated instances

**Format**: N/A

**Annotation**: Seven annotators rated traversability on a scale from 1 to 4, based on their estimations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: F1 scores were calculated to evaluate the performance of different VLMs in estimating traversability.

**Interpretation**: F1 scores at most 0.51 indicate limitations in model performance on the evaluated dataset.

**Baseline Results**: N/A

**Validation**: The performance of models was tested against the water traversability dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
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
