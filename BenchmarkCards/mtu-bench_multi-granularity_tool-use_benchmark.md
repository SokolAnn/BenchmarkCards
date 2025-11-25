# MTU-Bench (Multi-Granularity Tool-Use Benchmark)

## 📊 Benchmark Details

**Name**: MTU-Bench (Multi-Granularity Tool-Use Benchmark)

**Overview**: MTU-Bench is a multi-granularity benchmark for evaluating large language models (LLMs) in their tool-use capabilities across diverse scenarios. It includes MTU-Instruct for training and MTU-Eval for comprehensive evaluation, covering various real-world tool-use scenes.

**Data Type**: dialogue interactions and tool usage scenarios

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MetaTool
- API-Bank
- ToolLLM

**Resources**:
- [GitHub Repository](https://github.com/MTU-Bench-Team/MTU-Bench.git)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of MTU-Bench is to provide a comprehensive evaluation framework for assessing the tool-use abilities of large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Tool Use Evaluation
- Dialogue Systems

**Limitations**: MTU-Bench may not fully capture all potential edge cases or highly complex interactions that might occur in dynamic real-world environments.

## 💾 Data

**Source**: Composed of existing task-oriented dialogue datasets such as MultiWOZ, SGD, and others, transformed to create realistic tool-use examples.

**Size**: 159,061 dialogues

**Format**: JSON

**Annotation**: Collected through automated synthesis and manual validation.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Instruction tuning

**Metrics**:
- Tool Selection Accuracy (TS)
- Parameter Selection Accuracy (PS)
- Success Rate (SR)
- Averaged Turn Success Rate (ATS)
- Soft Averaged Turn Success Rate (SATS)
- Task Process Rate (TPR)

**Calculation**: Metrics are calculated as per user defined interactions and tool usage in dialogue.

**Interpretation**: High scores indicate better performance in tool-use tasks across diverse scenarios.

**Baseline Results**: MTU-LLaMA model performances on various scenarios and metrics.

**Validation**: Data validated through a combination of automated checks and manual annotation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: None discussed explicitly.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Current practices for data privacy in accordance with applicable laws are ensured but not explicitly detailed.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
