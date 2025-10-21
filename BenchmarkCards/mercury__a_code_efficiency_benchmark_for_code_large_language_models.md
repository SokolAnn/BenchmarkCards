# Mercury: A Code Efficiency Benchmark for Code Large Language Models

## 📊 Benchmark Details

**Name**: Mercury: A Code Efficiency Benchmark for Code Large Language Models

**Overview**: Mercury is the first code efficiency benchmark for Code LLMs, comprising 1,889 Python tasks to assess and improve the efficiency of code generation by evaluating both functional correctness and code efficiency through the Beyond metric.

**Data Type**: Python programming tasks

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MBPP
- APPS

**Resources**:
- [GitHub Repository](https://github.com/Elfsong/Mercury)
- [Resource](https://huggingface.co/datasets/Elfsong/Mercury)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for assessing code efficiency and functional correctness of code generation models.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: The Mercury benchmark assumes a uniform distribution of code runtime, which simplifies evaluation but may not reflect real-world scenarios accurately.

## 💾 Data

**Source**: Public programming tasks from LeetCode, filtered for quality.

**Size**: 1,889 tasks

**Format**: JSON

**Annotation**: Tasks accompanied by solutions and automatically generated test cases.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Test case generation

**Metrics**:
- Beyond
- Pass

**Calculation**: The Beyond metric is calculated using runtime percentiles from a distribution of historical solutions, reflecting both functional correctness and efficiency.

**Interpretation**: A higher Beyond score indicates better efficiency relative to historical solutions for each task.

**Validation**: The validity of tasks is assessed through automated test case generation and execution.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution Non Commercial 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: All tasks are sourced from publicly accessible domains, ensuring compliance with copyright guidelines.
