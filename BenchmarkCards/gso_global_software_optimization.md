# GSO (Global Software Optimization)

## 📊 Benchmark Details

**Name**: GSO (Global Software Optimization)

**Overview**: GSO is a benchmark for evaluating language models’ capabilities in developing high-performance software through challenging optimization tasks extracted from real-world codebases. It leverages an automated pipeline to create performance tests that measure the ability of software engineering agents (SWE-Agents) to improve runtime efficiency.

**Data Type**: code optimization tasks

**Domains**:
- Software Engineering

**Languages**:
- Python
- C
- C++

**Similar Benchmarks**:
- SWE-Bench
- EvalPerf
- EffiBench

**Resources**:
- [Resource](https://gso-bench.github.io/)
- [GitHub Repository](https://github.com/gso-bench/gso)
- [Resource](https://huggingface.co/datasets/gso-bench/gso)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the optimization capabilities of language models and agents in the context of high-performance software development tasks.

**Target Audience**:
- Machine Learning Researchers
- Software Engineers
- AI Developers

**Tasks**:
- Software Optimization
- Code Performance Improvement

**Limitations**: The benchmark contains 102 tasks, which may introduce variance in results due to its limited size.

## 💾 Data

**Source**: Extracted from public GitHub repositories with licenses that permit software usage.

**Size**: 102 tasks

**Format**: N/A

**Annotation**: Manually curated to ensure diversity and complexity of the optimization tasks.

## 🔬 Methodology

**Methods**:
- Automated performance tests
- Code base commit analysis

**Metrics**:
- OPT@K
- Success Rate

**Calculation**: Metrics are computed by analyzing the model-generated patches against human-authored optimization commits.

**Interpretation**: Success is defined by the model's ability to generate an optimization patch that improves runtime and maintains functional correctness.

**Baseline Results**: Leading SWE-Agents achieved a success rate of less than 5%.

**Validation**: Manual curation of benchmark instances to ensure quality and diversity.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Performance optimization failures']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Collected from public repositories governed by various open-source licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
