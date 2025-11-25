# m&m’s: A Benchmark to Evaluate Tool-Use for Multi-step Multi-modal Tasks

## 📊 Benchmark Details

**Name**: m&m’s: A Benchmark to Evaluate Tool-Use for Multi-step Multi-modal Tasks

**Overview**: m&m’s benchmark contains 4K+ multi-step multi-modal tasks involving 33 tools that include multi-modal models, (free) public APIs, and image processing modules. The benchmark includes a high-quality subset of 1,565 task plans that are human-verified and executable.

**Data Type**: multi-step multi-modal tasks

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- ToolEmu
- TaskBench

**Resources**:
- [Resource](https://huggingface.co/datasets/zixianma/mms)
- [GitHub Repository](https://github.com/RAIVNLab/mms)

## 🎯 Purpose and Intended Users

**Goal**: To support comprehensive and rigorous evaluation of tool-use abilities of planning agents for multi-step multi-modal tasks.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Multi-step planning
- Tool invocation
- Task automation

**Limitations**: m&m’s only considers sequential task plans, which represent a majority of real-world user requests. Some tasks might require dynamic task plans depending on the output for one subtask.

## 💾 Data

**Source**: Generated using a tool graph with human verification.

**Size**: 4,427 examples

**Format**: JSON

**Annotation**: Human-verified by three annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- tool-F1
- argname-F1
- pass rate

**Calculation**: Metrics are calculated based on comparing predicted tool names and argument names against ground truth.

**Interpretation**: Higher tool-F1 indicates better tool selection, whereas higher argname-F1 and pass rate imply improved tool invocation.

**Baseline Results**: Not specified.

**Validation**: Human verification for plans ensures accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
