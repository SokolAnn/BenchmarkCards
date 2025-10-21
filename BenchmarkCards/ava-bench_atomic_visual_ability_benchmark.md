# AVA-BENCH (Atomic Visual Ability Benchmark)

## 📊 Benchmark Details

**Name**: AVA-BENCH (Atomic Visual Ability Benchmark)

**Overview**: AVA-BENCH is introduced as the first benchmark explicitly designed to disentangle 14 Atomic Visual Abilities (AVAs) for Vision Foundation Models (VFMs), thereby enabling detailed assessments of their strengths and weaknesses across foundational visual capabilities.

**Data Type**: image-question pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2506.09082)

## 🎯 Purpose and Intended Users

**Goal**: The goal of AVA-BENCH is to provide a systematic, diagnostic, and comprehensive evaluation protocol for Vision Foundation Models (VFMs), focusing on their fundamental visual abilities.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Object Recognition
- Scene Recognition
- Emotion Recognition
- Color Detection
- Action Recognition
- Fine-Grained Recognition
- Counting
- Localization
- Absolute Depth
- Relative Depth
- Spatial Reasoning
- Orientation
- Texture

**Limitations**: N/A

## 💾 Data

**Source**: Curated from 26 diverse datasets focused on specific Atomic Visual Abilities.

**Size**: 218K image-question pairs

**Format**: image-question pairs

**Annotation**: Curated and filtered to ensure each image-question pair tests a single AVA.

## 🔬 Methodology

**Methods**:
- Automated evaluation using language models
- Standardized metrics for each AVA

**Metrics**:
- Accuracy
- Mean Absolute Error (MAE)
- Generalized Intersection-over-Union (GIoU)
- Average Normalized Levenshtein Similarity (ANLS)

**Calculation**: Metrics are calculated based on task-specific evaluation protocols outlined for each AVA.

**Interpretation**: Higher metrics indicate better performance in identifying or predicting the specific visual capability.

**Baseline Results**: N/A

**Validation**: The dataset was split into 80% train and 20% test ensuring balanced representation across classes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
