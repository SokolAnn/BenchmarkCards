# HumanEval Pro and MBPP Pro

## 📊 Benchmark Details

**Name**: HumanEval Pro and MBPP Pro

**Overview**: HumanEval Pro and MBPP Pro are new benchmarks for evaluating LLMs on self-invoking code generation tasks, where models must solve base problems and leverage their solutions to tackle more complex problems.

**Data Type**: self-invoking programming problems

**Domains**:
- Computer Science

**Languages**:
- Python

**Similar Benchmarks**:
- HumanEval
- MBPP
- BigCodeBench

**Resources**:
- [GitHub Repository](https://github.com/CodeEval-Pro/CodeEval-Pro)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of large language models on the self-invoking code generation task, highlighting the differences in performance between traditional and self-invoking generation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Code Generation

**Limitations**: The programming languages of our benchmarks only include Python; the diversity of self-invoking problems is limited by the original problems.

## 💾 Data

**Source**: Derived from existing datasets: HumanEval, MBPP, and BigCodeBench

**Size**: 57 self-invoking programming problems

**Format**: Problem-solution pairs in Python

**Annotation**: Problems generated using Deepseek-V2.5 with manual review for test cases

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- pass@k

**Calculation**: Metrics are calculated based on the pass@k score for the benchmarks, evaluating model abilities to generate correct solutions.

**Interpretation**: Higher pass rates indicate better model performance in self-invoking code generation tasks.

**Baseline Results**: Frontier LLMs display a significant drop in performance on self-invoking tasks, with many models showing a 10% to 15% drop compared to traditional benchmarks.

**Validation**: Models are validated through repetitive testing and manual review of generated test cases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: Potential misuse of generated code and reinforcement of existing biases in training data.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
