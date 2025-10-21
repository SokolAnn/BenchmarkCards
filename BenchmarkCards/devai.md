# DevAI

## 📊 Benchmark Details

**Name**: DevAI

**Overview**: DevAI is a benchmark consisting of 55 realistic automated AI development tasks designed to evaluate the code generation abilities of agentic systems, providing robust evaluations through a dynamic framework, Agent-as-a-Judge.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- SWE-Bench
- HumanEval
- MBPP

**Resources**:
- [Resource](https://huggingface.co/devai-benchmark)
- [GitHub Repository](https://github.com/metauto-ai/agent-as-a-judge)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for automated AI development tasks, assessing the capabilities of agentic systems to generate complex code solutions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation
- Evaluation of AI Development Tasks

**Limitations**: N/A

## 💾 Data

**Source**: Expertly crafted dataset of AI development tasks focusing on real-world applications.

**Size**: 55 tasks

**Format**: JSON

**Annotation**: Manually annotated with hierarchical user requirements and preferences.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Agent-as-a-Judge
- LLM-as-a-Judge

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on task requirement satisfaction and comparison with human evaluators.

**Interpretation**: Evaluation outcomes are interpreted relative to how well agentic systems meet the task requirements.

**Baseline Results**: Comparative evaluations were made against human evaluators and LLM-as-a-Judge.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
