# RAFT (Real-world Annotated Few-shot Tasks)

## 📊 Benchmark Details

**Name**: RAFT (Real-world Annotated Few-shot Tasks)

**Overview**: RAFT is a real-world few-shot text classification benchmark designed to measure how much recent and upcoming NLP advances benefit applications. It includes naturally occurring tasks and uses an evaluation setup that mirrors deployment, with the aim of tracking model improvements that translate into real-world benefits.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FLEX
- FewGLUE
- CrossFit
- NaturalInstructions

**Resources**:
- [Resource](https://raft.elicit.org)
- [Resource](https://raft.elicit.org/datasets)
- [Resource](https://raft.elicit.org/baselines)

## 🎯 Purpose and Intended Users

**Goal**: To measure and track few-shot performance on tasks representative of real-world text classification scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: RAFT dataset includes tasks like hate-speech detection, medical case report parsing, and literature review automation.

**Size**: 11 datasets with varying sizes

**Format**: N/A

**Annotation**: Collected through human crowdsourcing with task-specific instructions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: F1 scores are macro-averaged across multiple datasets.

**Interpretation**: Higher F1 scores indicate better model performance in classifying the provided examples.

**Baseline Results**: Human crowdsourced average F1 score is 0.735; GPT-3 average F1 score is 0.627.

**Validation**: Evaluation is run weekly to minimize information gained from frequent submissions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: Offensive content may be present due to the inclusion of a hate-speech detection dataset.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Datasets under various licenses such as Creative Commons Attribution 4.0 International.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
