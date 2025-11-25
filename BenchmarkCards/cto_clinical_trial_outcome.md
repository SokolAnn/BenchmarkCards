# CTO (Clinical Trial Outcome)

## 📊 Benchmark Details

**Name**: CTO (Clinical Trial Outcome)

**Overview**: The CTO benchmark provides a large-scale repository integrating approximately 125,000 drug and biologics trials, including LLM interpretations, phase progression tracking, sentiment analysis from news sources, and other trial-related metrics, aimed at improving the quality and reliability of clinical trial outcome labels.

**Data Type**: trial outcome labels

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- TOP

**Resources**:
- [Resource](https://chufangao.github.io/CTOD/)

## 🎯 Purpose and Intended Users

**Goal**: To democratize clinical trial outcome prediction and improve predictive modeling in drug development.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Clinical Trial Researchers

**Tasks**:
- Clinical Trial Outcome Prediction

**Limitations**: N/A

## 💾 Data

**Source**: CTTI (Clinical Trial Transformation Initiative) database and various online news sources.

**Size**: 125,840 clinical trials

**Format**: N/A

**Annotation**: Manually annotated dataset of clinical trials from 2020 to 2024.

## 🔬 Methodology

**Methods**:
- Automated labeling
- Manual annotation
- Data programming aggregation

**Metrics**:
- F1 Score

**Calculation**: The F1 score is calculated based on the agreement of automated labels with human-annotated labels.

**Interpretation**: An F1 score close to 1 indicates high agreement with expert annotations.

**Baseline Results**: Achieved an F1 score of 94 for Phase 3 trials and 91 across all phases.

**Validation**: Peer-reviewed and validated against existing datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Data privacy rights alignment
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: We use publicly available data, minimizing the risk of identification.

**Data Licensing**: MIT License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
