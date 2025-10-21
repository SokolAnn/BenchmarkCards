# Grounded Language Dataset (GoLD)

## 📊 Benchmark Details

**Name**: Grounded Language Dataset (GoLD)

**Overview**: GoLD is a multimodal dataset of common household objects described by people using either spoken or written language, enabling research on grounded language learning.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Robotics

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/iral-lab/UMBC_GLD)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that can be used for training models in grounded language acquisition and understanding natural language in robot-assisted tasks.

**Target Audience**:
- ML Researchers
- Robotics Researchers
- AI Developers

**Tasks**:
- Grounded Language Learning
- Natural Language Processing

**Limitations**: N/A

## 💾 Data

**Source**: Images and audio descriptions collected using Amazon Mechanical Turk and Microsoft Azure Kinect.

**Size**: 8250 text descriptions and 4059 speech descriptions with 207 object instances across 47 classes.

**Format**: JSON, audio

**Annotation**: Manually annotated text descriptions and automatically generated speech transcriptions.

## 🔬 Methodology

**Methods**:
- Manifold Alignment
- Triplet Loss for model training

**Metrics**:
- Mean Reciprocal Rank (MRR)
- Word Error Rate (WER)
- BLEU Score

**Calculation**: Mean Reciprocal Rank is calculated by ranking the distance of a test embedding to all embeddings of the corresponding domain.

**Interpretation**: Higher MRR indicates better performance in aligning language and visual input.

**Validation**: Evaluated using MRR over a holdout set.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
