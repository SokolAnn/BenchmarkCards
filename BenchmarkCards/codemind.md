# CodeMind

## 📊 Benchmark Details

**Name**: CodeMind

**Overview**: CodeMind is a framework designed to gauge the code reasoning abilities of LLMs through explicit and implicit code reasoning tasks: Independent Execution Reasoning (IER), Specification Reasoning (SR), and Dynamic Semantics Reasoning (DSR).

**Data Type**: code and test input-output pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Python

**Similar Benchmarks**:
- CRUXEval
- REVAL
- HumanEval
- ClassEval

**Resources**:
- [GitHub Repository](https://github.com/Intelligent-CAT-Lab/CodeMind)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the code reasoning abilities of LLMs on programming tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Independent Execution Reasoning
- Specification Reasoning
- Dynamic Semantics Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: A selection of Python programs from existing benchmarks including HumanEval, CRUXEval, ClassEval, and Avatar.

**Size**: 1450 programs

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- IER Rate
- Specification Reasoning Score
- Dynamic Semantics Reasoning Score

**Calculation**: Metrics are calculated based on the output correctness of LLMs in predicting program outputs or refactoring code based on specifications.

**Interpretation**: Higher scores indicate better reasoning capabilities of the LLMs in relation to the complexity of the tasks.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
