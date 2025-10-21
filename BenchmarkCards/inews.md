# iNews

## 📊 Benchmark Details

**Name**: iNews

**Overview**: iNews is a novel large-scale dataset specifically designed to facilitate the modeling of personalized affective responses to news content. It comprises annotations from 291 demographically diverse UK participants across 2,899 multimodal Facebook news posts, including multifaceted labels for valence, arousal, dominance, discrete emotions, content relevance judgments, sharing likelihood, and modality importance ratings.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Social Computing

**Languages**:
- English

**Similar Benchmarks**:
- GoEmotions
- Emotion Detection in NLP datasets

**Resources**:
- [Resource](https://arxiv.org/abs/2503.03335)

## 🎯 Purpose and Intended Users

**Goal**: To enable research in LLM personalization, subjectivity, affective computing, and human behavior simulation by modeling individual-level affective responses to news content.

**Target Audience**:
- Affective Computing Researchers
- ML Researchers
- Model Developers
- Social Computing Scholars

**Tasks**:
- Emotion Detection
- News Sentiment Analysis

**Limitations**: While providing substantial demographic and geographic diversity, the dataset is focused on UK-based annotators and news outlets, which may limit generalizability to other populations.

## 💾 Data

**Source**: Annotations collected from 291 demographically diverse UK participants for 2,899 Facebook news posts.

**Size**: 2,899 posts

**Format**: CSV

**Annotation**: Annotations include valence-arousal-dominance ratings, discrete emotion classifications, and modality influence assessments.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Quantitative analysis

**Metrics**:
- Valence
- Arousal
- Dominance
- Exact Accuracy
- Mean Absolute Error (MAE)

**Calculation**: Metrics are calculated based on annotator responses to news post annotations and were validated against established psychometric standards.

**Interpretation**: Higher scores in valence indicate more positive emotional responses, while higher arousal reflects greater emotional engagement.

**Validation**: Inter-annotator agreement was assessed using Krippendorff’s alpha.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: The dataset features a diverse group of annotators across various demographics.

**Potential Harm**: Risk of generating biased models based on subjective annotations and potential privacy concerns related to persona data.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personally identifiable information was collected. All participants provided informed consent.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent was obtained from all annotators before participation.

**Compliance With Regulations**: The study was conducted with the approval of the institutional ethics review board.
