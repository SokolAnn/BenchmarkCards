# MultiProSE (Multi-label Arabic Dataset for Propaganda, Sentiment, and Emotion Detection)

## 📊 Benchmark Details

**Name**: MultiProSE (Multi-label Arabic Dataset for Propaganda, Sentiment, and Emotion Detection)

**Overview**: The MultiProSE dataset is released as the first multi-label Arabic dataset for propaganda detection, sentiment analysis, and emotion recognition. The dataset is an extension of the ArPro dataset, annotated with sentiment and emotion dimensions, to facilitate research on the interaction between these opinion dimensions.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic

**Resources**:
- [GitHub Repository](https://github.com/xxx/xxx)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for the classification of propaganda, sentiment, and emotion in Arabic news texts.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Propaganda Detection
- Sentiment Analysis
- Emotion Recognition

**Limitations**: During the annotation process, the annotators faced several challenges such as time constraints, the need for clear annotation guidelines, and the complexity of emotions and sentiments in diverse topics.

## 💾 Data

**Source**: The dataset was collected from several Arabic news domains, derived from the existing ArPro dataset along with an in-house collection.

**Size**: 8,000 examples

**Format**: N/A

**Annotation**: Manually annotated by three native Arabic speakers with strict guidelines and quality control measures to ensure accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Micro-F1
- Macro-F1
- Accuracy

**Calculation**: Metrics are calculated using results from several pre-trained and large language models for the respective tasks.

**Interpretation**: Higher Micro-F1 and Macro-F1 scores indicate better model performance in each task.

**Baseline Results**: AraBERT achieved a Micro-F1 score of 0.769 for propaganda detection, while GPT-4o-Mini achieved the highest score for sentiment analysis at 0.842.

**Validation**: Inter-Annotator Agreement (IAA) was assessed using Light's Kappa and Fleiss’ Kappa measures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
