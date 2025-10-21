# Seal-Tools: Self-Instruct Tool Learning Dataset for Agent Tuning and Detailed Benchmark

## 📊 Benchmark Details

**Name**: Seal-Tools: Self-Instruct Tool Learning Dataset for Agent Tuning and Detailed Benchmark

**Overview**: Seal-Tools is a new tool learning dataset for evaluating the tool-calling ability of LLMs, featuring a variety of tools and instances, including hard instances with nested tool callings. It utilizes a self-instruct method for data generation.

**Data Type**: API tool instances

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ToolBench
- API-Bank
- ToolAlpaca

**Resources**:
- [GitHub Repository](https://github.com/fairyshine/Seal-Tools)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive tool learning dataset that enables the evaluation and finetuning of LLMs for tool-calling tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Tool Calling
- Task Completion

**Limitations**: N/A

## 💾 Data

**Source**: Self-instruct method using LLMs to generate tools and instances.

**Size**: 14,076 instances, 4,076 tools

**Format**: JSON

**Annotation**: Automatically generated with quality control measures

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Format Accuracy
- Tool Selection Precision/Recall/F1
- Parameter Filling Precision/Recall/F1

**Calculation**: Metrics are calculated based on comparing model outputs with gold standards.

**Interpretation**: Higher scores indicate better performance in tool selection and parameter filling tasks.

**Baseline Results**: Results show significant performance improvements compared to existing models.

**Validation**: Evaluated with multiple LLMs, comparing performance on single-tool and multiple-tool instances.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Methods to reduce errors caused by LLMs are employed, but potential privacy leaks exist.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
