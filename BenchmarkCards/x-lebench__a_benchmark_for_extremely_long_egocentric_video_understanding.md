# X-LeBench: A Benchmark for Extremely Long Egocentric Video Understanding

## 📊 Benchmark Details

**Name**: X-LeBench: A Benchmark for Extremely Long Egocentric Video Understanding

**Overview**: X-LeBench is a versatile benchmark dataset specifically designed for evaluating tasks on extremely long egocentric video recordings, including a life-logging simulation pipeline that produces realistic daily plans aligned with real-world video data.

**Data Type**: video

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Ego4D

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating the understanding of extremely long egocentric videos.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Temporal Localization
- Summarization
- Counting
- Ordering

**Limitations**: Some contextual inconsistencies exist within the dataset.

## 💾 Data

**Source**: Ego4D dataset

**Size**: 432 simulated video life logs

**Format**: N/A

**Annotation**: Auto&Manual

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Recall
- Rouge-L
- BERT Score
- Accuracy

**Calculation**: Metrics are calculated based on the accuracy of task-specific outputs.

**Interpretation**: Higher scores indicate better performance in video understanding tasks.

**Validation**: Evaluated using various multimodal approaches.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
