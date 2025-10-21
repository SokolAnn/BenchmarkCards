# MLVU (Multi-task Long Video Understanding Benchmark)

## 📊 Benchmark Details

**Name**: MLVU (Multi-task Long Video Understanding Benchmark)

**Overview**: MLVU is a benchmark proposed for the comprehensive and in-depth evaluation of Long Video Understanding (LVU) performance. It presents substantial extensions of video lengths, diverse video genres, and various tailored evaluation tasks to better assess MLLMs' capabilities in long video understanding.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2406.04264)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and in-depth analysis for MLLMs' long-video understanding performance.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Video Summarization
- Needle Question Answering
- Ego Reasoning
- Plot Question Answering
- Sub-Scene Captioning
- Action Order
- Action Count
- Anomaly Recognition
- Topic Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Universal Long Video Collection (ULVC) which includes diverse long videos from movies, documentaries, cartoons, etc.

**Size**: 1,730 videos and 3,102 question-answer pairs

**Format**: N/A

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated by matching model predictions with ground truths in the multiple-choice and generation tasks.

**Interpretation**: Higher accuracy indicates better model understanding of long videos.

**Baseline Results**: Baseline models evaluated include various MLLMs such as GPT-4o and Video-XL.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
