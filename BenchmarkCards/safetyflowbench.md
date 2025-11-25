# SafetyFlowBench

## 📊 Benchmark Details

**Name**: SafetyFlowBench

**Overview**: SafetyFlowBench is a comprehensive safety benchmark specifically designed for evaluating the safety of large language models (LLMs). The benchmark consists of 23,446 queries with low redundancy and strong discriminative power, constructed through a fully automated pipeline that minimizes time and resource costs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Japanese
- Korean
- French
- German
- Russian
- Arabic

**Resources**:
- [GitHub Repository](https://github.com/yangyangyang127/SafetyFlow)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of SafetyFlowBench is to automate the benchmarking of large language models' safety to mitigate risks and improve safety evaluation processes.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Safety Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from real-world texts (e.g., Reddit), generated content, and existing safety benchmarks.

**Size**: 23,446 prompts

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Harmful Rate (HR)
- Safety Rate (SR)

**Calculation**: Safety Rate is calculated as SR = 1 - HR, where HR is the percentage of harmful responses.

**Interpretation**: A higher Safety Rate indicates better model safety performance.

**Baseline Results**: N/A

**Validation**: Extensive experiments were conducted to validate the efficacy and efficiency of the SafetyFlowBench.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
