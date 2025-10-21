# Lyrics Emotion Attribution

## 📊 Benchmark Details

**Name**: Lyrics Emotion Attribution

**Overview**: This paper presents a manually labeled dataset for multi-label emotional attribution of song lyrics based on the Mean Opinion Score (MOS) methodology, predicting six emotional intensity scores for joy, sadness, anger, fear, surprise, and disgust.

**Data Type**: emotional intensity scores

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/LLM-HITCS25S/LyricsEmotionAttribution)

## 🎯 Purpose and Intended Users

**Goal**: To construct a high-quality, manually labeled dataset for lyric emotion attribution and evaluate the capabilities of various language models in predicting emotional intensity.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Emotion Classification

**Limitations**: N/A

## 💾 Data

**Source**: Constructed via manual annotation using the Mean Opinion Score (MOS) method by a committee of human annotators.

**Size**: N/A

**Format**: N/A

**Annotation**: Manual annotation by experts using the MOS methodology.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

**Calculation**: MAE and RMSE were calculated to evaluate model performance in predicting emotional intensity scores.

**Interpretation**: Lower MAE and RMSE values indicate better predictive accuracy in estimating emotional intensity.

**Baseline Results**: Fine-tuned models achieved lower MAE and RMSE values compared to zero-shot models.

**Validation**: Models were validated based on their predictive accuracy across all six emotions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
