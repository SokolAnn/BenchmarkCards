# PEFT-U Benchmark

## 📊 Benchmark Details

**Name**: PEFT-U Benchmark

**Overview**: PEFT-U consists of a series of user-centered tasks containing diverse and individualized expressions where the preferences of users can potentially differ for the same input. It aims to assess the efficacy of language models in producing personalized outputs based on user-specific information.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ChrisIsKing/Parameter-Efficient-Personalization)

## 🎯 Purpose and Intended Users

**Goal**: The PEFT-U Benchmark aims to build and evaluate NLP models for user personalization.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Sentiment Analysis
- Humor Detection
- Hate Speech Detection
- Emotion Recognition

**Limitations**: While designed to capture diverse user perspectives, the benchmark may not fully represent all real-world communication scenarios. The intricacies of individual preferences and linguistic nuances are vast and varied.

## 💾 Data

**Source**: Curated datasets across various domains focusing on user-centered tasks related to hate speech, sentiment, and humor.

**Size**: 15,000+ users across 13+ personalized tasks.

**Format**: N/A

**Annotation**: Manual annotation by experts and users with consideration for individual perspectives.

## 🔬 Methodology

**Methods**:
- Zero-shot/Few-shot Prompting
- LoRa
- Adapters
- Prompt Tuning
- Prefix Tuning
- P-Tuning
- IA^3

**Metrics**:
- Accuracy

**Calculation**: Aggregates performance metrics across tasks based on user-specific outputs.

**Interpretation**: Higher scores indicate better performance in capturing individual user preferences.

**Validation**: Validation through performance comparisons and user agreement metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
