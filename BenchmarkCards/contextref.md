# ContextRef

## 📊 Benchmark Details

**Name**: ContextRef

**Overview**: ContextRef is a benchmark for assessing referenceless metrics for image description generation against human preferences. It includes human ratings across various quality dimensions and robust checks to evaluate metric reliability.

**Data Type**: image-description pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/elisakreiss/contextref)

## 🎯 Purpose and Intended Users

**Goal**: To assess referenceless metrics for image description generation vis-a-vis human preference judgments and provide insights into their reliability and weaknesses.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Image Captioning
- Text Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: The English language subset of the WIT dataset from Wikipedia, featuring various image and description pairs.

**Size**: 204 samples

**Format**: N/A

**Annotation**: Human ratings based on a variety of quality dimensions through a human-subjects experiment.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Correlation with human preferences

**Calculation**: Metrics are based on how well the model-assigned scores align with human quality judgments across various dimensions.

**Interpretation**: Higher correlations with human ratings indicate better alignment between model predictions and human preferences.

**Validation**: Assessments based on robustness checks against various manipulations of input data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
