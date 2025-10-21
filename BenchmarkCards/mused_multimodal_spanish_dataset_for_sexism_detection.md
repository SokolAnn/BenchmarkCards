# MuSeD (Multimodal Spanish Dataset for Sexism Detection)

## 📊 Benchmark Details

**Name**: MuSeD (Multimodal Spanish Dataset for Sexism Detection)

**Overview**: MuSeD is a new Multimodal Spanish dataset for Sexism Detection consisting of approximately 11 hours of videos extracted from TikTok and BitChute, with an innovative annotation framework that examines the contributions of textual, vocal, and visual modalities in identifying sexist content.

**Data Type**: multimodal (video, audio, text)

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Spanish

**Resources**:
- [GitHub Repository](https://github.com/lauradegrazia/MuSeD)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to provide a dataset for detecting sexism in social media videos by combining text, audio, and video modalities.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Sexism Detection

**Limitations**: N/A

## 💾 Data

**Source**: Videos collected from TikTok and BitChute using curated hashtags related to sexism and gender identity.

**Size**: 400 videos (≈11 hours)

**Format**: Video, audio, text

**Annotation**: Annotated at multiple levels including text, audio, and visual content by a team of trained linguists and an expert moderator.

## 🔬 Methodology

**Methods**:
- Manual annotation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Model performance is calculated based on accuracy against labels assigned by human annotators.

**Interpretation**: A model is considered effective in detecting sexism if it shows high accuracy in correctly identifying sexist vs. non-sexist content.

**Baseline Results**: N/A

**Validation**: Inter-annotator agreement was evaluated to ensure the reliability of annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes diverse demographic backgrounds in annotator expertise to minimize bias.

**Potential Harm**: The dataset aims to identify and prevent the spread of sexism and discrimination in social media content.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All collected videos were publicly available and shared by their creators.

**Data Licensing**: Not Applicable

**Consent Procedures**: Annotators provided informed consent to engage with potentially offensive material.

**Compliance With Regulations**: Not Applicable
