# COMMON-TOM

## 📊 Benchmark Details

**Name**: COMMON-TOM

**Overview**: COMMON-TOM is a question answering benchmark based on naturally-occurring spoken dialogs in English, designed to evaluate the theory of mind capabilities of language models.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/cogstates/common-tom)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark the theory of mind capabilities of language models using natural spoken conversations.

**Target Audience**:
- ML Researchers
- Cognitive Scientists

**Tasks**:
- Question Answering

**Limitations**: The dataset is relatively small, containing only four dialogs, and does not involve tracking ToM in other languages.

## 💾 Data

**Source**: CALLHOME corpus of dyadic dialogs

**Size**: 7,374 queries

**Format**: N/A

**Annotation**: Annotated based on cognitive states and beliefs of discourse participants.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the proportion of correct answers relative to the total number of queries.

**Interpretation**: Higher accuracy indicates better performance in understanding theory of mind tasks.

**Baseline Results**: Human performance: 80% accuracy, Mistral-7B (Fine-Tune): 64% accuracy.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**
- **Accuracy**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
