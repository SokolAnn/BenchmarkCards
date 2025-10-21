# Do-Not-Answer

## 📊 Benchmark Details

**Name**: Do-Not-Answer

**Overview**: This work presents the first open-source dataset to evaluate safeguards in large language models (LLMs), consisting of prompts that responsible language models should not answer. The dataset includes a comprehensive risk taxonomy and aims to contribute towards the safe development and deployment of LLMs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Libr-AI/do-not-answer)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that helps evaluate the safety of large language models and identifies dangerous capabilities to mitigate risks in their deployment.

**Target Audience**:
- ML Researchers
- Safety Engineers
- Developers of LLMs

**Tasks**:
- Safety Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: The dataset consists of prompts collected from various risk categories that LLMs should not answer, and responses collected from six different LLMs.

**Size**: 939 prompts and 5,634 responses

**Format**: N/A

**Annotation**: Responses were annotated based on harmfulness and categorized into action categories.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Evaluation metrics are calculated based on the human annotations of the responses collected.

**Interpretation**: Results indicate how well models refuse to answer harmful prompts and adhere to safety guidelines.

**Baseline Results**: N/A

**Validation**: Responses were evaluated by annotators for harmfulness and categorized into predefined action categories.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: The dataset is aimed at detecting and preventing harmful responses in LLMs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
