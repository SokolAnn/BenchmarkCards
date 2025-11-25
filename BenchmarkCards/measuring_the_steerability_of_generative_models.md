# Measuring the Steerability of Generative Models

## 📊 Benchmark Details

**Name**: Measuring the Steerability of Generative Models

**Overview**: This paper introduces a benchmark task to evaluate the steerability of generative models, where users are tasked with prompting models to reproduce sampled outputs. The study finds that several models perform poorly on this task, indicating a need to improve generative model steerability.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/SarahBentley/Steerability)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate how well users can steer generative models towards desired outputs.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Image Generation
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Large-scale user study with generative models (text-to-image and large language models).

**Size**: 554 goal images

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- User study
- Prompting mechanisms
- Reinforcement learning

**Metrics**:
- Satisfaction rate
- Image Similarity Rating
- Improvement Rate
- Prompt-Output Misalignment

**Calculation**: Metrics are calculated using human annotations comparing generated images to goal images.

**Interpretation**: Higher ratings indicate better steerability of the models.

**Validation**: Reinforcement learning and human ratings are used for validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
