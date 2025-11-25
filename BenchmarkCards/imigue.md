# iMiGUE

## 📊 Benchmark Details

**Name**: iMiGUE

**Overview**: The iMiGUE dataset consists of video footage of tennis players during post-match interviews, with detailed frame-level annotations of various micro-gestures. The dataset contains 72 subjects and a total of 33 gesture classes.

**Data Type**: video

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- MiGA challenge datasets

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the iMiGUE dataset is to facilitate understanding of micro-gestures and their relationship to emotional states.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Micro-Gesture Recognition

**Limitations**: The class distribution is highly imbalanced, with 28 of the 33 classes being tail classes with relatively few samples.

## 💾 Data

**Source**: iMiGUE dataset collected from videos of tennis players

**Size**: N/A

**Format**: N/A

**Annotation**: Detailed frame-level annotations

## 🔬 Methodology

**Methods**:
- Evaluation of model performance using Top-1 accuracy
- Model training and validation procedures

**Metrics**:
- Top-1 accuracy

**Calculation**: Top-1 accuracy is calculated as the percentage of correctly classified gestures over total classifications.

**Interpretation**: High accuracy indicates good performance in recognizing micro-gestures.

**Baseline Results**: Top-1 accuracy of CLIP-MG model is 61.82%.

**Validation**: Local validation set was created by setting aside 20% of the training data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: No explicit demographic analysis provided.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
