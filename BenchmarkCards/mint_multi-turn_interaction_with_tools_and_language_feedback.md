# MINT (Multi-turn Interaction with Tools and Language Feedback)

## 📊 Benchmark Details

**Name**: MINT (Multi-turn Interaction with Tools and Language Feedback)

**Overview**: MINT is a benchmark that evaluates Large Language Models' ability to solve tasks through multi-turn interactions, utilizing both external tools and user-provided natural language feedback. It aims to provide an evaluation framework that reflects real-world user-LLM interactions.

**Data Type**: multi-turn interaction scenarios

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://xingyaoww.github.io/mint-bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' performance in multi-turn interactions utilizing tools and natural language feedback, ensuring better alignment with real-world applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation
- Question Answering
- Decision Making

**Limitations**: N/A

## 💾 Data

**Source**: Repurposed datasets for evaluation including reasoning, coding, and decision-making tasks, specifically collections from HotpotQA, GSM8K, MATH, and MMLU.

**Size**: 29,307 instances initially filtered to 586 for evaluation

**Format**: N/A

**Annotation**: The dataset instances have been curated for their necessity of multi-turn interaction to solve.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Performance analysis across LLMs

**Metrics**:
- Success Rate

**Calculation**: Success Rate is calculated as the percentage of successful task completions across evaluation instances.

**Interpretation**: A higher Success Rate indicates a better performance in multi-turn task-solving capabilities.

**Baseline Results**: Comparison with 20 open- and closed-source LLMs shows varying capabilities, with metrics evaluated for performance improvements.

**Validation**: Comprehensive evaluation and analysis against established benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
