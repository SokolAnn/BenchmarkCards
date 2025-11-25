# EgoTextVQA

## 📊 Benchmark Details

**Name**: EgoTextVQA

**Overview**: EgoTextVQA is a novel and rigorously constructed benchmark for egocentric QA assistance involving scene text. It contains 1.5K ego-view videos and 7K scene-text aware questions that reflect real user needs in outdoor driving and indoor house-keeping activities.

**Data Type**: video-question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- QAEgo4D
- AssistQ

**Resources**:
- [GitHub Repository](https://github.com/zhousheng97/EgoTextVQA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for research on egocentric scene-text aware QA assistance.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: EgoTextVQA dataset created from ego-view videos sourced from RoadTextVQA and EgoSchema.

**Size**: 1,507 videos, 7,064 question-answering pairs

**Format**: N/A

**Annotation**: Manually reviewed and refined by human annotators

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the percentage of correctly answered questions.

**Interpretation**: Higher accuracy indicates better performance in answering scene-text aware questions.

**Baseline Results**: Best-performing model Gemini 1.5 Pro achieves around 33% accuracy.

**Validation**: Timestamps are set for each question, and models are evaluated based on their answers derived from the video content prior to the question's timestamp.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
