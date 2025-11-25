# Multimodal Instruction Dataset for Content Moderation

## 📊 Benchmark Details

**Name**: Multimodal Instruction Dataset for Content Moderation

**Overview**: This study introduces a novel dataset designed for content moderation tasks, incorporating images, videos, sounds, and text data to boost the performance of content moderation systems, particularly using large language models.

**Data Type**: multimodal instruction-response pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- ToxiGen
- NSFW dataset

**Resources**:
- [Resource](https://huggingface.co/modrwkv)

## 🎯 Purpose and Intended Users

**Goal**: To enhance content moderation practices by providing a comprehensive dataset that allows for more accurate and efficient content moderation models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Content Moderation

**Limitations**: The dataset lacks image diversity and may contain embedded biases. Limited access to computational resources poses challenges.

## 💾 Data

**Source**: Aggregated from multiple publicly available sources for text, images, audio, and video content.

**Size**: 558,958 text instruction-response pairs; 83,625 image instruction-response pairs

**Format**: N/A

**Annotation**: Generated responses using GPT-4 and GPT-4V, alongside manual classification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: The accuracy is gauged by the proportion of correct classifications of model outputs against expected outcomes.

**Interpretation**: Higher accuracy indicates better alignment of model responses with expected content moderation standards.

**Baseline Results**: Mod-RWKV achieved 66.9% accuracy in text tasks; Mod-VisualRWKV achieved 84.8% accuracy in image tasks.

**Validation**: Evaluated using the ToxiGen dataset for text and NSFW images for image assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Stringent security protocols implemented to prevent unauthorized data access.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
