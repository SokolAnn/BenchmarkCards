# ToolGrad-5K

## 📊 Benchmark Details

**Name**: ToolGrad-5K

**Overview**: ToolGrad-5K is a tool-use dataset generated through an agentic framework that constructs valid tool-use chains with a 100% pass rate, enabling efficient data generation for teaching LLMs tool usage capabilities.

**Data Type**: triplets of (user prompt, tool-use chains, AI responses)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://zhongyi-zhou.github.io/toolgrad/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of ToolGrad-5K is to efficiently generate synthetic tool-use datasets for large language models through a novel framework.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Tool Use Training

**Limitations**: While ToolGrad improves efficiency, it does not ensure real-world alignment of user inquiries.

## 💾 Data

**Source**: Generated through the ToolGrad framework utilizing a large-scale API database.

**Size**: 5,000 examples

**Format**: N/A

**Annotation**: Automatically generated using the ToolGrad framework.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Pass rate
- Number of ground-truth tool uses
- LLM calls
- Tool calls

**Calculation**: Metrics are derived by evaluating the success of generated triplets and the efficiency of the tool-use process.

**Interpretation**: A pass rate of 100% indicates successful generation of usable examples, while the number of tool uses reflects the complexity of generated data.

**Baseline Results**: Compared with ToolBench, ToolGrad-5K boasts a 100% pass rate compared to a 63.8% pass rate from DFS.

**Validation**: The dataset was validated by its construction process, ensuring each triplet was successfully generated.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: BY-CC license for all artifacts, including dataset and fine-tuned models.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
