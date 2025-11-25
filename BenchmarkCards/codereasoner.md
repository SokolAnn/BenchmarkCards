# CodeReasoner

## 📊 Benchmark Details

**Name**: CodeReasoner

**Overview**: CodeReasoner is a novel framework that improves the code reasoning ability of large language models (LLMs) by constructing a specialized dataset and utilizing a two-phase training approach combining instruction tuning and reinforcement learning.

**Data Type**: python code examples

**Domains**:
- Natural Language Processing

**Languages**:
- Python

**Similar Benchmarks**:
- CRUXEval
- LiveCodeBench
- REval

**Resources**:
- [GitHub Repository](https://github.com/lingxiaotang/CodeReasoner)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the code reasoning capabilities of large language models through improved dataset construction and training methodologies.

**Target Audience**:
- ML Researchers
- Model Developers
- Software Engineers

**Tasks**:
- Input/Output Prediction
- Coverage Prediction
- State Tracking
- Path Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Constructed dataset focusing on succinct test cases to enhance reasoning about code execution, generated via a novel method.

**Size**: 17,332 test cases for supervised fine-tuning, 18,796 test cases for reinforcement learning

**Format**: N/A

**Annotation**: Validation through execution of generated test cases and removal of any failing cases.

## 🔬 Methodology

**Methods**:
- Instruction tuning
- Reinforcement learning

**Metrics**:
- Accuracy
- Pass@1

**Calculation**: Metrics calculated based on the model's performance across various benchmarks including comparing outputs against expected results.

**Interpretation**: Higher accuracy indicates better performance in predicting outputs and understanding code execution.

**Baseline Results**: CodeReasoner -7B outperforms existing models like GPT-4o; detailed performance metrics provided in the paper.

**Validation**: Evaluated through extensive tests against established benchmarks like CRUXEval, LiveCodeBench, and REval.

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

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
