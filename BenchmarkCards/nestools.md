# NESTOOLS

## 📊 Benchmark Details

**Name**: NESTOOLS

**Overview**: NESTOOLS is a high-quality dataset designed for comprehensive evaluations of large language models' nested tool learning abilities, constructed through a novel automatic data generation process.

**Data Type**: nested tool calling instances

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- API-Bank
- ToolBench
- T-Eval

**Resources**:
- [GitHub Repository](https://github.com/hhan1018/NesTools)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and provide insights into the nested tool learning capabilities of large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Tool Learning Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Automatically generated using LLMs with manual reviews.

**Size**: 1,000 instances

**Format**: JSON

**Annotation**: Manual review and refinement by experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are computed based on the correctness of tool selection, tool calling order, parameter filling, and nested parameter filling.

**Interpretation**: A higher score indicates better performance in correctly handling nested tool calls.

**Baseline Results**: N/A

**Validation**: Extensive validation through experiments on 22 popular LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt leaking

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
