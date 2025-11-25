# AIMS.uk and AIMS.ca

## 📊 Benchmark Details

**Name**: AIMS.uk and AIMS.ca

**Overview**: AIMS.uk and AIMS.ca are newly annotated datasets from the UK and Canada to enable cross-jurisdictional evaluation of corporate compliance statements regarding modern slavery, facilitating the development of AI tools for compliance monitoring.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/user/repo)
- [Resource](https://huggingface.co/datasets/...)

## 🎯 Purpose and Intended Users

**Goal**: To provide annotated datasets for analyzing compliance with modern slavery legislation and to advance AI-assisted compliance checking frameworks.

**Target Audience**:
- ML Researchers
- Government Agencies
- NGOs
- Businesses

**Tasks**:
- Text Classification
- Compliance Monitoring

**Limitations**: Limitations include the small size of the datasets and potential biases from manual annotations.

## 💾 Data

**Source**: Modern slavery statements from UK and Canadian government registries.

**Size**: 50 statements each for AIMS.uk and AIMS.ca with 2807 and 3658 sentences respectively.

**Format**: N/A

**Annotation**: Manually annotated by domain experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated based on predictions made by models fine-tuned on the datasets.

**Interpretation**: Higher F1 scores indicate better model performance in correctly identifying compliance criteria.

**Baseline Results**: Fine-tuned models on AIMS.au achieve better overall results than zero-shot or few-shot models.

**Validation**: Validation involves comparison of predictions against expert annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 International (CC BY 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
