# ERAS (Evaluation of Robustness to Locally Ambiguous Segmentation)

## 📊 Benchmark Details

**Name**: ERAS (Evaluation of Robustness to Locally Ambiguous Segmentation)

**Overview**: ERAS tests a model's vulnerability to morphological garden path errors by comparing its behavior on sentences with and without local segmentation ambiguities.

**Data Type**: paired sentences

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the susceptibility of Chinese NLP models to morphological garden path errors.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Word Segmentation
- Sentiment Analysis

**Limitations**: ERAS can only be used for two kinds of models: word segmentation models and sentiment analysis models.

## 💾 Data

**Source**: Synthetically generated pairs of ambiguous and unambiguous sentences.

**Size**: 203,944 pairs

**Format**: CSV

**Annotation**: Manually verified by native speakers of Mandarin Chinese.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Models evaluated based on their performance on ambiguous versus unambiguous sentences.

**Interpretation**: Lower accuracy on ambiguous sentences indicates susceptibility to garden path errors.

**Baseline Results**: Human accuracy score of 91.3%

**Validation**: Evaluation based on the null hypothesis testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
