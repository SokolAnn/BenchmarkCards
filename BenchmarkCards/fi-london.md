# FI-London

## 📊 Benchmark Details

**Name**: FI-London

**Overview**: A new dataset comprising facade images of buildings in London and their respective age epochs, developed for estimating building age using zero-shot classification algorithms.

**Data Type**: image

**Domains**:
- Computer Vision
- Geography

**Languages**:
- English

**Resources**:
- [Resource](https://zichaozeng.github.io/ba_classifier)

## 🎯 Purpose and Intended Users

**Goal**: To develop a zero-shot classifier that predicts the age epoch of buildings based on their facade images, tackling challenges of geographical data scarcity and model training.

**Target Audience**:
- Researchers in Computer Vision
- Urban Planners
- Architectural Historians

**Tasks**:
- Image Classification

**Limitations**: Due to the unbalanced sample distribution in the dataset, it can currently only be used for testing.

## 💾 Data

**Source**: Dataset of facade images collected from Brent and Camden in London.

**Size**: 131 images

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Zero-shot classification

**Metrics**:
- Accuracy
- Micro F1 Score
- Mean Absolute Error (MAE)

**Calculation**: Micro F1 Score is calculated as 2 × (Precision Micro × Recall Micro) / (Precision Micro + Recall Micro). MAE is the average absolute difference between predicted and actual mid-years of the age epochs.

**Interpretation**: A lower MAE indicates better predictive accuracy, especially for buildings near the boundary of two epochs.

**Baseline Results**: Accuracy of 39.69% and a mean absolute error of 0.85 decades.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
