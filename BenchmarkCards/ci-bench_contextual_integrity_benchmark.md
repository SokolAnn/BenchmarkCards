# CI-Bench (Contextual Integrity Benchmark)

## 📊 Benchmark Details

**Name**: CI-Bench (Contextual Integrity Benchmark)

**Overview**: CI-Bench is a comprehensive synthetic benchmark for evaluating the ability of AI assistants to protect personal information during model inference, leveraging the Contextual Integrity framework.

**Data Type**: dialogues and emails

**Domains**:
- Healthcare
- Finance
- eCommerce
- Education
- Entertainment
- Family & Friends
- Government
- Hospitality

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2409.13903)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate AI assistants' ability to assess the appropriateness of information flow based on privacy norms defined by the Contextual Integrity framework.

**Target Audience**:
- ML Researchers
- AI Developers
- Data Privacy Experts

**Tasks**:
- Context Understanding
- Expectation Identification
- Appropriateness Judgment
- Response Generation

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic generation via a multi-step pipeline from structured data.

**Size**: 44,100 test cases

**Format**: text

**Annotation**: Annotated by human experts for appropriateness judgment.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Area Under ROC Curve (AUC)

**Calculation**: Metrics are calculated based on human-annotated ground truth labels and model responses.

**Interpretation**: Performance is interpreted based on AUC scores, where higher scores indicate better model capability in judging appropriateness.

**Validation**: Evaluated AI assistants based on prototype large language models (e.g., Gemini).

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
