# SURGE

## 📊 Benchmark Details

**Name**: SURGE

**Overview**: SURGE is a comprehensive benchmark with 1160 problems covering 8 key aspects related to multi-language programming tasks, competition-level programming problems, repository-level code analysis, high-cost scientific computing, time-complexity-intensive algorithms, buggy code analysis, programs dependent on specific compilers or execution environments, and formal mathematical proof verification.

**Data Type**: programming problems

**Domains**:
- Computer Science

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Imbernoulli/SURGE)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large language models as general-purpose surrogate code executors and provide insights into their capabilities and limitations.

**Target Audience**:
- ML Researchers
- Model Developers
- Software Engineers

**Tasks**:
- Code Execution Prediction
- Code Generation
- Bug Detection

**Limitations**: While SURGE covers diverse execution scenarios, it does not encompass all specialized environments, such as hardware-dependent simulations or real-time systems.

## 💾 Data

**Source**: Constructed using various methodologies including Iterative Refactor, Repository Sampling, and Manual Implementation from multiple sources.

**Size**: 1,160 problems

**Format**: N/A

**Annotation**: Manual verification and code generation by LLMs.

## 🔬 Methodology

**Methods**:
- Human Evaluation
- Automated Metrics

**Metrics**:
- Exact Match
- Relative Absolute Error (RAE)
- Jaccard similarity

**Calculation**: Metrics are calculated based on the performance of models executing code and matching predicted outputs with ground truths.

**Interpretation**: Accuracy of outputs compared to expected results; successful executions count for accuracy metrics.

**Baseline Results**: Evaluation conducted on 21 open-source and proprietary models.

**Validation**: Models tested through multiple prompting strategies and under various computational tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Data contamination
- **Robustness**: Prompt injection attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
