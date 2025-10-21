# OFFICE BENCH

## 📊 Benchmark Details

**Name**: OFFICE BENCH

**Overview**: OFFICE BENCH is one of the first office automation benchmarks for evaluating current LLM agents’ capability to address the office tasks in realistic office workflows.

**Data Type**: task-based workflows involving multiple applications

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FUNSD
- CORD
- SROIE
- DocVQA

**Resources**:
- [GitHub Repository](https://github.com/zlwang-cs/OfficeBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capability of LLM agents in solving tasks across different applications in office automation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Office Automation Tasks

**Limitations**: N/A

## 💾 Data

**Source**: Synthesized data simulating realistic office environments with fictitious names and data from ChatGPT and random generators.

**Size**: 300 tasks

**Format**: N/A

**Annotation**: Tasks are annotated based on complexity involving single, two, or three applications for realism.

## 🔬 Methodology

**Methods**:
- Exact Matching
- Fuzzy Matching
- Execution-based Evaluation

**Metrics**:
- Pass Rate

**Calculation**: Measured as the percentage of tasks passed by the LLM agents.

**Interpretation**: Higher pass rates indicate better performance of LLM agents in office automation tasks.

**Baseline Results**: GPT-4 Omni achieves the highest pass rate of 47.00%.

**Validation**: Tasks are validated through various customized evaluation methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Only synthesized data is used, with no real names or sensitive information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
