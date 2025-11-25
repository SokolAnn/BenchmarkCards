# CLC-UKET Dataset

## 📊 Benchmark Details

**Name**: CLC-UKET Dataset

**Overview**: This paper develops a benchmark for predicting case outcomes in the UK Employment Tribunal (UKET) by creating the CLC-UKET dataset, which consists of approximately 19,000 UKET cases and extensive legal annotations to facilitate multi-class case outcome prediction.

**Data Type**: text

**Domains**:
- Legal

**Languages**:
- English

**Resources**:
- [Resource](https://www.cst.cam.ac.uk/research/srg/projects/law)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark dataset and evaluate its effectiveness in predicting case outcomes in the UK Employment Tribunal.

**Target Audience**:
- Legal Researchers
- AI Practitioners

**Tasks**:
- Case Outcome Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Cambridge Law Corpus (CLC) and UKET judgments

**Size**: 19,090 cases

**Format**: N/A

**Annotation**: Legal annotations were created using a large language model (LLM) for automatic annotation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the predictions compared to human-annotated outcomes.

**Interpretation**: A higher F1 score indicates better performance in predicting the correct case outcomes.

**Baseline Results**: BERT achieved an F1 Score of 0.421, T5 achieved an F1 Score of 0.564, and GPT-4 achieved an F1 Score of 0.549.

**Validation**: Empirical results were validated against human predictions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Sensitive personal information is anonymized when necessary.

**Data Licensing**: The dataset is licensed under the Open Government Licence, allowing public usage.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The dataset and its curation comply with relevant ethical and legal standards.
