# FALLACIES

## 📊 Benchmark Details

**Name**: FALLACIES

**Overview**: The FALLACIES dataset contains 4,640 reasoning steps for 232 types of logical fallacies categorized in a hierarchical taxonomy, used to evaluate the verification abilities of large language models in identifying fallacious reasoning.

**Data Type**: reasoning steps

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- None

**Resources**:
- [GitHub Repository](https://github.com/Raising-hrx/FALLACIES)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the self-verification abilities of large language models in logical reasoning by providing a comprehensive dataset of logical fallacies.

**Target Audience**:
- ML Researchers
- Natural Language Processing Practitioners
- Model Developers

**Tasks**:
- Logical Reasoning
- Fallacy Detection

**Limitations**: The dataset primarily focuses on logical reasoning and may not cover other types such as numerical reasoning.

## 💾 Data

**Source**: FALLACIES dataset created from human annotations and large language model outputs.

**Size**: 4,640 steps

**Format**: JSON

**Annotation**: Human-annotated by experts.

## 🔬 Methodology

**Methods**:
- Evaluation of LLMs on identifying logical fallacies in reasoning steps

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated as the percentage of correctly identified fallacies versus total attempts.

**Interpretation**: Accuracy rates indicate the model's ability to accurately assess logical fallacies.

**Validation**: Model performance validated through extensive experiments on varying large language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
