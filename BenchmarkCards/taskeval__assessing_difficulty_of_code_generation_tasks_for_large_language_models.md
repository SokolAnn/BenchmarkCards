# TaskEval: Assessing Difficulty of Code Generation Tasks for Large Language Models

## 📊 Benchmark Details

**Name**: TaskEval: Assessing Difficulty of Code Generation Tasks for Large Language Models

**Overview**: This paper introduces TaskEval, a framework for evaluating the characteristics of code generation tasks for large language models (LLMs) using diverse prompts and Item Response Theory (IRT). It highlights the limitations of traditional single-prompt evaluations and provides a more granular assessment of task difficulty and discriminant across multiple benchmarks.

**Data Type**: code generation tasks

**Domains**:
- Software Engineering

**Languages**:
- Python

**Similar Benchmarks**:
- HumanEval
- ClassEval

**Resources**:
- [GitHub Repository](https://github.com/FlowSs/TaskEval)
- [Resource](https://sdk-codex.github.io/human-eval/)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the assessment of large language models in code generation tasks by introducing a framework that evaluates task characteristics based on difficulty and discriminant metrics.

**Target Audience**:
- ML Researchers
- Model Developers
- Software Engineers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: HumanEval+ and ClassEval benchmarks

**Size**: 200 tasks across benchmarks

**Format**: N/A

**Annotation**: Collected human difficulty ratings

## 🔬 Methodology

**Methods**:
- Human evaluation
- IRT modeling

**Metrics**:
- Difficulty
- Discriminant

**Calculation**: IRT models are used to evaluate the difficulty of tasks and the discriminant power of those tasks with respect to model capabilities.

**Interpretation**: Tasks with higher difficulty scores are expected to yield lower success rates among LLMs, while tasks with higher discriminants are better at differentiating between LLM performances.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
