# RSVQAxBEN-MM

## 📊 Benchmark Details

**Name**: RSVQAxBEN-MM

**Overview**: This work introduces the RSVQAxBEN-MM dataset, which adds the SAR images from BEN-MM to the question/answer of RSVQAxBEN, facilitating Remote Sensing Visual Question Answering (RSVQA) using high-resolution SAR imagery.

**Data Type**: image-question-answer pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- BEN
- BEN-MM
- RSVQAxBEN

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the extraction of information from remote sensing images using a benchmark dataset for RSVQA.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Visual Question Answering

**Limitations**: The dataset is heavily unbalanced and presents challenges due to geographical generalization.

## 💾 Data

**Source**: Derived from the BigEarthNet and RSVQAxBEN datasets, integrating SAR images with optical images and associated questions/answers.

**Size**: 14,758,150 image/question/answer triplets

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- End-to-End RSVQA
- Prompt-RSVQA

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: F1 Score is computed as the harmonic mean of precision and recall.

**Interpretation**: Higher F1 and accuracy scores indicate better performance in answering the questions correctly.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Bias

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
