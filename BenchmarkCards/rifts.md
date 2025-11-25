# RIFTS

## 📊 Benchmark Details

**Name**: RIFTS

**Overview**: RIFTS is a benchmark designed to systematically measure human-LLM grounding, consisting of approximately 1,740 tasks that require selective use of clarification and follow-up requests for interactive grounding.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/microsoft/rifts)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve the grounding capabilities of language models in human-LLM interactions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Clarification
- Follow-Up Requests

**Limitations**: N/A

## 💾 Data

**Source**: Derived from publicly available LLM interaction data including WildChat, Bing Chat, and MultiWOZ.

**Size**: 1,740 tasks

**Format**: N/A

**Annotation**: Automatically annotated using a model based on human-LLM interaction logs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Rooted in predicting and analyzing the expected grounding acts based on past interactions.

**Interpretation**: The evaluation focuses on how well models initiate clarifications and follow-up requests during interactions.

**Baseline Results**: All evaluated models perform worse than random on RIFTS, with the best model achieving 25.26% accuracy.

**Validation**: Tasks validated through user interaction logs and predicted grounding acts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**
- **Fairness**

**Demographic Analysis**: N/A

**Potential Harm**: Potential for users to disclose sensitive information during grounding interactions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected was done so with user consent.

**Data Licensing**: RIFTS is released under the ODC-By license.

**Consent Procedures**: Users were informed of data usage for research in exchange for model access.

**Compliance With Regulations**: Not Applicable
