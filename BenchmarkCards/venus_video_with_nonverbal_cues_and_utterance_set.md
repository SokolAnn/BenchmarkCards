# VENUS (VidEo with Nonverbal cues and Utterance Set)

## 📊 Benchmark Details

**Name**: VENUS (VidEo with Nonverbal cues and Utterance Set)

**Overview**: VENUS is a large-scale multimodal dataset designed for multimodal conversations with nonverbal annotations. It comprises 10-minute clips from dialogue-rich podcasts featuring two-person interactions, along with time-aligned text, facial expressions, and body language.

**Data Type**: video with nonverbal annotations

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/winston1214/nonverbal-conversation)

## 🎯 Purpose and Intended Users

**Goal**: To advance research in understanding and generating both text and nonverbal expressions in conversations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Generation
- Nonverbal Cue Generation

**Limitations**: The VENUS dataset is primarily curated from one source, which may limit the diversity of nonverbal expression patterns.

## 💾 Data

**Source**: YouTube podcast videos

**Size**: 89,459 dialogues, 1,114,328 turns

**Format**: JSON

**Annotation**: Annotations include time-aligned text, 3D facial expression features, and body language features.

## 🔬 Methodology

**Methods**:
- Quantitative evaluation
- Qualitative analysis

**Metrics**:
- Perplexity
- BERT Score
- METEOR
- Negative Log-Likelihood (NLL)

**Calculation**: Metrics are calculated based on the model performance during evaluation.

**Interpretation**: Lower perplexity and higher BERT Score indicate better performance in generating natural language and nonverbal expressions.

**Validation**: The dataset and model were validated through extensive evaluation metrics and user studies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Bias

**Atlas Risks**:
- **Privacy**: Personal information in data

**Demographic Analysis**: The dataset does not detail demographic factors.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Privacy measures include releasing only video IDs instead of raw video frames and anonymizing 3D facial and body motions.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
