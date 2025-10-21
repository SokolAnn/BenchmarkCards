# HI-TOM (Higher Order Theory of Mind)

## 📊 Benchmark Details

**Name**: HI-TOM (Higher Order Theory of Mind)

**Overview**: HI-TOM is a benchmark specifically designed for evaluating higher-order Theory of Mind reasoning in Large Language Models, featuring multiple-choice questions that assess reasoning about others' beliefs across orders from zeroth to fourth.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ying-hui-he/Hi-ToM_dataset)

## 🎯 Purpose and Intended Users

**Goal**: To introduce a benchmark that evaluates higher-order Theory of Mind reasoning in LLMs and to analyze the limitations of current models in this paradigm.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Theory of Mind Reasoning

**Limitations**: The dataset primarily explores reasoning capabilities and does not encompass comprehensive human-like conversation complexities found in real-world interactions.

## 💾 Data

**Source**: Constructed from a set of predetermined story components using automated generation scripts combined with manual review.

**Size**: N/A

**Format**: N/A

**Annotation**: Manually checked for logical consistency and correctness.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated using standard accuracy, considering correct responses to both the higher-order and all lower-order questions in the story.

**Interpretation**: Accuracy underlines the ability of models to reason through multiple levels of Theory of Mind.

**Baseline Results**: Models evaluated include GPT-4, GPT-3.5 Turbo, Claude, and Guanaco, with performance rates below 60% on higher-order questions.

**Validation**: Empirical testing across various LLMs with experimental analysis of failure cases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No sensitive or personal information was included in the dataset.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
