# ETHICS

## 📊 Benchmark Details

**Name**: ETHICS

**Overview**: The ETHICS dataset is introduced to assess a machine learning system's ability to predict basic human ethical judgments in open-world settings, enabling the evaluation of models against moral concepts like justice, virtue ethics, deontology, utilitarianism, and commonsense morality.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/hendrycks/ethics)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate how well models understand basic shared human values and moral concepts.

**Target Audience**:
- ML Researchers
- Ethicists
- AI Developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Crowdsourced scenarios collected via Amazon Mechanical Turk and data from Reddit.

**Size**: 130,000 examples

**Format**: Text

**Annotation**: Annotated by multiple workers with majority voting to ensure quality.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on binary classification accuracy for each task.

**Interpretation**: A high classification accuracy indicates the model's ability to correctly predict moral judgments.

**Validation**: The dataset is validated through majority labeling by annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personal information was collected.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Ethics approval was obtained from an institutional review board.
