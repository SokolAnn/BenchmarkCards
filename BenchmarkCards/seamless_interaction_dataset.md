# Seamless Interaction Dataset

## 📊 Benchmark Details

**Name**: Seamless Interaction Dataset

**Overview**: The Seamless Interaction dataset is a large-scale collection of over 4,000 hours of face-to-face interaction footage from over 4,000 participants in diverse contexts, designed to advance research in social AI.

**Data Type**: video

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- AMI Meeting Corpus
- IEMOCAP
- CANDOR

**Resources**:
- [GitHub Repository](https://github.com/facebookresearch/seamless_interaction)
- [Resource](https://huggingface.co/datasets/facebook/seamless-interaction)

## 🎯 Purpose and Intended Users

**Goal**: To develop socially intelligent AI technologies through the understanding and generation of dyadic behavioral dynamics.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Gesture Generation
- Facial Motion Generation

**Limitations**: N/A

## 💾 Data

**Source**: Over 4,000 hours of dyadic footage collected from participants during face-to-face interactions.

**Size**: 4,065 hours

**Format**: video

**Annotation**: Includes metadata and extensive annotations for interaction contexts, participant relationships, and quality assessments.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Fréchet Feature Distance (FFD)
- Lip-Sync score (Sync-C)
- Fréchet Inception Distance (FID)
- Fréchet Gesture Distance (FGD)

**Calculation**: Metrics calculated based on visual behavior assessments for generated interactions and comparisons to ground truth.

**Interpretation**: Lower FFD and FID scores indicate higher quality face generation; higher Sync-C scores indicate better lip synchronization.

**Baseline Results**: Compared to standard benchmarks in the field of audiovisual interaction modeling.

**Validation**: Evaluation through both human studies and automatic metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness
- Fairness

**Atlas Risks**:
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Fairness**: Data bias

**Demographic Analysis**: Analysis of participant demographics to ensure diverse representation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Informed consent was obtained, ensuring participant privacy and data protection.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants signed consent forms before participation.

**Compliance With Regulations**: Not Applicable
