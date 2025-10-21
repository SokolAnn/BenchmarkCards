# LLMDetect

## 📊 Benchmark Details

**Name**: LLMDetect

**Overview**: LLMDetect is a benchmark designed to evaluate detectors’ performance on new tasks for detecting LLM-generated content, including LLM Role Recognition and LLM Involvement Measurement.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ZihaoCheng123/LLMDetect)

## 🎯 Purpose and Intended Users

**Goal**: To provide a new detection paradigm that moves beyond binary classification for detecting LLM-generated content.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- LLM Role Recognition
- LLM Involvement Measurement

**Limitations**: N/A

## 💾 Data

**Source**: Hybrid News Detection Corpus (HNDC) consisting of human-written articles curated from reputable sources.

**Size**: 64,304 articles

**Format**: N/A

**Annotation**: Annotated with LLM role and involvement ratio.

## 🔬 Methodology

**Methods**:
- Zero-shot detection
- Supervised fine-tuning
- Feature-based classifiers
- PLM-based classifiers

**Metrics**:
- F1 Score
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)

**Calculation**: Metrics are calculated based on model predictions and ground truth in various tasks.

**Interpretation**: High F1 scores indicate better performance in identifying LLM-generated content.

**Baseline Results**: Fine-tuned PLM-based models consistently outperform other baseline models across both tasks.

**Validation**: Evaluated through training and testing on the HNDC and DetectEval components.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
