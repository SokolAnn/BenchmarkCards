# Multimodal ECG Classification Benchmark

## 📊 Benchmark Details

**Name**: Multimodal ECG Classification Benchmark

**Overview**: This benchmark assesses the performance of multimodal models to classify electrocardiograms (ECGs) with 98 Japanese labels, utilizing contrastive learning approaches.

**Data Type**: ECG sequence data

**Domains**:
- Healthcare

**Languages**:
- Japanese

**Resources**:
- [Resource](https://huggingface.co/EQUES/MedLLama3-JP-v2)

## 🎯 Purpose and Intended Users

**Goal**: To assist physicians in interpreting ECG data effectively using a multimodal machine learning model.

**Target Audience**:
- Healthcare Practitioners
- Machine Learning Researchers

**Tasks**:
- Multimodal Classification

**Limitations**: Further improvement in ECG interpretation capabilities is essential for labels with low accuracy.

## 💾 Data

**Source**: ECG records obtained from the University of Tokyo Hospital and Mitsui Hospital.

**Size**: 37,285 ECG records

**Format**: N/A

**Annotation**: Labels selected by cardiology specialists from ECG reports.

## 🔬 Methodology

**Methods**:
- Contrastive Learning
- Evaluation using Top-1 and Top-5 Accuracy

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated for both top-1 and top-5 predictions based on the model's classification output.

**Interpretation**: Top-1 accuracy indicates the model's primary guess, while top-5 accuracy shows the model's ability to identify the correct answer within its top five predictions.

**Baseline Results**: Comparative accuracy with previous research shows slight improvements in specific classification tasks.

**Validation**: Evaluated through performance on test datasets with both existing and new labels.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
